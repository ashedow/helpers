# Pandas memory usage

How to reduce the memory your DataFrame

Check memory usage:
```python
df.info(verbose=False, memory_usage="deep")
```

## Dropping columns

**Don’t load all the columns**

load just needed columns:
```python
df = pd.read_csv("voters.csv", usecols=["First Name ", "Last Name "])
```

## Lower-range numerical dtypes

**Shrink numerical columns with smaller dtypes**

Each column in a Pandas DataFrame is a particular data type (dtype). For example, for integers there is the int64 dtype, int32, int16, and more.

int8 can store integers from -128 to 127.
int16 can store integers from -32768 to 32767.
int64 can store integers from -9223372036854775808 to 9223372036854775807.

By default when Pandas loads a CSV, it guesses at the dtypes. If it decides a column volumes are all integers, by default it assigns that column int64 as the dtype.

As a result, if you know that the numbers in a particular column will never be higher than 32767, you can use an int16 and reduce the memory usage of that column by 75%. And if the values will never be higher than 127, you can use an int8, using even less memory.

```python
df = pd.read_csv("voters.csv", dtype={"Ward Number ": "int8"})
```

## Categoricals

**Shrink categorical data using Categorical dtypes**

Even though the values are limited to a specific set, they are still stored as arbitrary strings, which have overhead in memory. Imagine a gender column that only says "FEMALE", "MALE", and "NON-BINARY" over and over again—that’s a lot of memory being used to store the same three strings.

A more compact representation for data with only a limited number of values is a custom [dtype called Categorical](https://pandas.pydata.org/pandas-docs/stable/user_guide/categorical.html), whose memory usage is tied to the number of different values.

When we load the CSV, we can specify that a particular column uses this dtype, and the resulting memory usage is much smaller, 69KB instead of 550KB:

```python
df = pd.read_csv("voters.csv", dtype={"Party Affiliation ": "category"})
```

## Sparse columns

**Sparse series**

If you have a column with lots of empty values, usually represented as NaNs, you can save memory by using a [sparse column representation](https://pandas.pydata.org/pandas-docs/stable/user_guide/sparse.html). It won’t waste memory storing all those empty values.

Example:
```python
df = pd.read_csv("voters.csv")
>>> series = df["Mailing Address - Apartment Number "]
>>> series.memory_usage(index=False, deep=True)
2623975
>>> len(series)
68836
>>> len(series.dropna())
13721
>>> sparse_series = series.astype("Sparse[str]")
>>> len(sparse_series)
68836
>>> sparse_series.memory_usage(index=False, deep=True)
2237939
```

## Changing numeric column representation

For example, instead of representing the values as floating numbers, we can represent them as percentages between 0 and 100. We’ll be down to two-digit (or some more) accuracy, but again for many use cases that’s sufficient. Plus, if this is output from a model, those last few digits of “accuracy” are likely to be noise, they won’t actually tell us anything useful.

```python
df = pd.read_csv("voting_smaller.csv", dtype={"likelihood": "int8"})
```

## Sampling

Let’s say you want to do a phone survey of voters in your city. You aren’t going to call all one million people, you’re going to call a sample, let’s say 1000. This can be considered a form of lossy compression, since you only want to use a subset of the rows.

When you load your data, you can specify a [skiprows function](https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#general-parsing-configuration) that will randomly decide whether to load that row or not:
```python
>>> from random import random
>>> def sample(row_number):
...     if row_number == 0:
...         # Never drop the row with column names:
...         return False
...     # random() returns uniform numbers between 0 and 1:
...     return random() > 0.001
... 
>>> sampled = pd.read_csv("/tmp/voting.csv", skiprows=sample)
>>> len(sampled)
973
```

## Reading in chunks

We’ll start with a program that just loads a full CSV into memory. In particular, we’re going to write a little program that loads a voter registration database, and measures how many voters live on every street in the city:
```python
voters_street = pandas.read_csv("voters.csv")["Residential Address Street Name "]
print(voters_street.value_counts())
```

And the bulk of memory usage is allocated by loading the CSV into memory.

In the following graph of peak memory usage, the width of the bar indicates what percentage of the memory is used:
* The section on the left is the CSV read.
* The narrower section on the right is memory used importing all the various Python modules, in particular Pandas; unavoidable overhead, basically.

As an alternative to reading everything into memory, Pandas allows you to read data in chunks. In the case of CSV, we can load only some of the lines into memory at any given time.

In particular, if we use the chunksize argument to pandas.read_csv, we get back an iterator over DataFrames, rather than one single DataFrame. Each DataFrame is the next 1000 lines of the CSV:
```python
result = None
for chunk in pandas.read_csv("voters.csv", chunksize=1000):
    voters_street = chunk[
        "Residential Address Street Name "]
    chunk_result = voters_street.value_counts()
    if result is None:
        result = chunk_result
    else:
        result = result.add(chunk_result, fill_value=0)

result.sort_values(ascending=False, inplace=True)
```

### The MapReduce idiom

Taking a step back, what we have here is an highly simplified instance of the MapReduce programming model. While typically used in distributed systems, where chunks are processed in parallel and therefore handed out to worker processes or even worker machines, you can still see it at work in this example.

In the simple form we’re using, MapReduce chunk-based processing has just two steps:
* For each chunk you load, you map or apply a processing function.
* Then, as you accumulate results, you “reduce” them by combining partial results into the final result.

We can re-structure our code to make this simplified MapReduce model more explicit:
```python
def get_counts(chunk):
    voters_street = chunk[
        "Residential Address Street Name "]
    return voters_street.value_counts()

def add(previous_result, new_result):
    return previous_result.add(new_result, fill_value=0)

# MapReduce structure:
chunks = pandas.read_csv("voters.csv", chunksize=1000)
processed_chunks = map(get_counts, chunks)
result = reduce(add, processed_chunks)

result.sort_values(ascending=False, inplace=True)
print(result)
```
Both reading chunks and map() are lazy, only doing work when they’re iterated over. As a result, chunks are only loaded in to memory on-demand when reduce() starts iterating over processed_chunks.

### From full reads to chunked reads

You’ll notice in the code above that get_counts() could just as easily have been used in the original version, which read the whole CSV into memory:
```python
def get_counts(chunk):
    voters_street = chunk[
        "Residential Address Street Name "]
    return voters_street.value_counts()
result = get_counts(pandas.read_csv("voters.csv"))
```
That’s because reading everything at once is a simplified version of reading in chunks: you only have one chunk, and therefore don’t need a reducer function.

So here’s how you can go from code that reads everything at once to code that reads in chunks:
1. Separate the code that reads the data from the code that processes the data.
2. Use the new processing function, by mapping it across the results of reading the file chunk-by-chunk.
3. Figure out a reducer function that can combine the processed chunks into a final result.

# Fast subsets of large datasets with Pandas and SQLite

1. Load the data into SQLite, and create an index
2. Rewrite our query function
3. Use Dask

## Links
https://pythonspeed.com
