# Spark

## Recap
Spark is built around the concepts of Resilient Distributed Datasets and Direct Acyclic Graph representing transformations and dependencies between them.

![](Spark-Overview--1-.png)

Spark Application (often referred to as Driver Program or Application Master) at high level consists of SparkContext and user code which interacts with it creating RDDs and performing series of transformations to achieve final result. These transformations of RDDs are then translated into DAG and submitted to Scheduler to be executed on set of worker nodes.

## RDD: Resilient Distributed Dataset

- **Resilient** means that we must be able to withstand failures and complete an ongoing computation. 
- **Distributed** means that we must account for multiple machines having a subset of data. 
- Formally, RDD is a read-only, partitioned collection of records. 

From a developer's point of view RDD represents distributed immutable data (partitioned data + iterator) and lazily evaluated operations (transformations). As an interface RDD defines five main properties:
```Scala
//a list of partitions (e.g. splits in Hadoop)
def getPartitions: Array[Partition]

//a list of dependencies on other RDDs
def getDependencies: Seq[Dependency[_]]

//a function for computing each split
def compute(split: Partition, context: TaskContext): Iterator[T]

//(optional) a list of preferred locations to compute each split on
def getPreferredLocations(split: Partition): Seq[String] = Nil

//(optional) a partitioner for key-value RDDs
val partitioner: Option[Partitioner] = None  
```

Here's an example of RDDs created during a call of method sparkContext.textFile("hdfs://...") which first loads HDFS blocks in memory and then applies map() function to filter out keys creating two RDDs:

![](DAG-logical-vs-partitions-view--3-.png)

HadoopRDD:
    * getPartitions = HDFS blocks
    * getDependencies = None
    * compute = load block in memory
    * getPrefferedLocations = HDFS block locations
    * partitioner = None
MapPartitionsRDD
    * getPartitions = same as parent
    * getDependencies = parent RDD
    * compute = compute parent and apply map()
    * getPrefferedLocations = same as parent
    * partitioner = None

Datasets must be typed
You can not modify data in-place in Spark. Datasets are immutable


**Partitions**
**Dependencies** (that models the relationships a RDD and its partitions and the partition which it was derived from)
**Function:** for comping the dataset based on its parent RDD
**Metadata** about its partitioning scheme and data placement


**a binary file in HDFS**

**partitions() -> Array[Partition]**
• lookup blocks information from the NameNode
• make a partition for every block
› return an array of the partitions
**iterator(p: Partition, parents: Array[Iterator[_]]) -> Iterator[Byte]**
• parents are not used
• return a reader for the block of the given partition
**dependencies() -> Array[Dependency]**

**Example: an sliced* in-memory array**
*can be used to parallelize in-memory computations

**partitions() -> Array[Partition]**
› slice array in chunks of size N
›make a partition for every chunk
› return an array of a single partition with the source array of the
partitions
**iterator(p: Partition, parents: Array[Iterator[_]]) -> Iterator[T]**
›parents are not used
›return an iterator over the source array chunk in the given partition
**dependencies() -> Array[Dependency]**
›return an empty array (no dependencies)


### RDD Operations
Operations on RDDs are divided into several groups:

#### Transformations
    * apply user function to every element in a partition (or to the whole partition)
    * apply aggregation function to the whole dataset (groupBy, sortBy)
    * introduce dependencies between RDDs to form DAG
    * provide functionality for repartitioning (repartition, partitionBy)
    * filter records and group them by a key
    * create new RDDs from existing RDDs by specifying how to obtain new items from the existing items
    * all transformtions are lazy
    Transformation is the primary way to “modify” data (given that RDDs are immutable)
    * There are transformations with narrow(local) and wide dependencies(require data shuffling). The transformation creates a new RDD every time, so you can't produce a cyclic dependency graph by applying Spark transformations to RDDs
    * MapReduce can be expressed with a couple of transformations
    * Complex transformations (like joins, cogroup) are available

it's possible to check if each keyA exists in B dataset, B in the memory on Map phase
each mapper doesn't store all the keys from A dataset. So you can't check if keyB exists in A

Freq used
› Def: filter(p: T  Boolean): RDD[T]  RDD[T]
    ›returns a filtered RDD with items satisfying the predicate p
› Def: map(f: T  U): RDD[T]  RDD[U]
    ›returns a mapped RDD with items f(x) for every x in the source RDD
› Def: flatMap(f: T  Array[U]): RDD[T]  RDD[U]
    › same as map but flattens the result of f
    ›generalizes map and filter

**Filter**

› Y = X.filter(p) # where X : RDD[T]
    ›Y.partitions()  Array[Partition]
        › return the same partitions as X  
    ›Y.iterator(p: Partition, parents: Array[Iterator[T]])  Iterator[T]
        › take a parent iterator over the corresponding partition of X
        › wrap the parent iterator to skip items that do not satisfy the predicate
        › return the iterator over partition of Y
    ›Y.dependencies()  Array[Dependency]
        › k-th partition of Y depends on k-th partition of X

On closures
› Y = X.filter(lambda x: x % 2 == 0)
    ›predicate closure is captured within the Y (it is a part of the definition of Y)
    ›predicate is not guaranteed to execute locally (closure may be sent over the network to the executor)

**Partition dependency graph**

 Z = X.filter(lambda x: x % 2 == 0).filter(lambda y: y < 3)
![](0_kAw8hogu1oZPy9QU.png)

Something that is not that obvious in the MapReduce paradigm is the **cogroup transformation**. Unlike the previous transformations, cogroup operates on two keyed inputs. The result is the keyed output with the value being a pair of arrays holding the values collected for the given key from the first and the second input.
Joins, GroupBy - shuffle



#### Actions
    * trigger job execution. So Actions, together with a transformation code, are executed elsewhere, not in your driver program. Your driver program receives only the outcome.
    * used to materialize computation results - collect, print, save, and fold data.
    
    * When running locally, the executors are collocated within the same process as the driver program.
    * When running in a cluster mode, the executors are located on the cluster machines, thus allowing you to use the cluster for a computation.

Freq used ations: 
* collect()
    › collects items and passes them to the driver
    › for small datasets! all data is loaded to the driver memory
* take(n: Int)
    › collects only n items and passes them to the driver
    ›tries to decrease amount of computation by peeking on partitions
* top(n: Int)
    › collects n largest items and passes them to the driver
* reduce(f: (T, T)  T)
    › reduces all elements of the dataset with the given associate, commutative binary function and passes the result back to the driver
* saveAsTextFile(path: String)
    › each executor saves its partition to a file under the given path with every item converted to a string and confirms to the driver
* saveAsHadoopFile(path: String, outputFormatClass: String)
    ›each executor saves its partition to a file under the given path using the given Hadoop file format and confirms to the driver
* foreach(f: T  ())
    ›each executor invokes f over every item and confirms to the driver
* foreachPartition(f: Iterator[T]  ())
    ›each executor invokes f over its partition and confirms to the driver

#### Extra: persistence
    * explicitly store RDDs in memory, on disk or off-heap (cache, persist)
    * checkpointing for truncating RDD lineage

### Resiliency

#### Fault-tolerance in MapReduce
› Two key aspects
    ›reliable storage for input and output data
    ›deterministic and side-effect free execution of mappers and reducers

#### Fault-tolerance in Spark

› Same two key aspects
    ›reliable storage for input and output data
    ›deterministic and side-effect free execution of transformations(including closures)

› Determinism — every invocation of the function results in the same
returned value
    ›e. g. do not use random numbers, do not depend on a hash value order

› Freedom of side-effects — an invocation of the function does not change anything in the external world
    ›e. g. do not commit to a database, do not rely on global variables

#### Fault-tolerance & transformations
› Lineage — a dependency graph for all partitions of all RDDs involved in a computation up to the data source

if the dependencies of a failed partition fails as well then Computation is restarted to recompute the dependencies first, and the partition afterwards.



#### Fault-tolerance & actions
› Actions are side-effects in Spark
› Actions have to be idempotent that is safe to be re-executed multiple times given the same input

## Jobs, stages, tasks

› The SparkContext is the core of your application
› The driver communicates directly with the executors
› Execution goes as follows: Action -> Job -> Job Stages -> Tasks
› Transformations with narrow dependencies allow pipelining


**Job stage** is a pipelined computation spanning between materialization boundaries
    › not immediately executable
    › Job is spawned in response to a Spark action
    › Job is divided in smaller sets of tasks called stages
**Task** is a job stage bound to particular partitions
    › immediately executable
    › Task is a unit of work to be done
    › Tasks are created by a job scheduler for every job stage
Materialization happens when reading, shuffling or passing data to an action
    ›narrow dependencies allow pipelining
    ›wide dependencies forbid it

Example:
1. Invoking an action…
2. …spawns the job…
3. …that gets divided into
the stages by the job scheduler…
4. …and tasks are created for every job stage.

### SparkContext – other functions

› Tracks liveness of the executors
    ›required to provide fault-tolerance
› Schedules multiple concurrent jobs
    ›to control the resource allocation within the application
› Performs dynamic resource allocation
    ›to control the resource allocation between different applications

How does your application find out the executors to work with?
The SparkContext object allocates the executors by communicating with the cluster manager.

## Caching & Persistence

Performance may be improved by persisting data across operations
    ›in interactive sessions, iterative computations and hot datasets
You can control the persistence of a dataset
    ›whether to store in the memory or on the disk
    ›how many replicas to create

Cache method 

Controlling persistence level
› rdd.persist(storageLevel)
    › sets RDD’s storage to persist across operations after it is computed for the first time
› storageLevel is a set of flags controlling the persistence, typical values are
    DISK_ONLY
        – save the data to the disk,
    MEMORY_ONLY
        – keep the data in the memory
    MEMORY_AND_DISK
        – keep the data in the memory; when out of memory – save it to the disk
    DISK_ONLY_2, MEMORY_ONLY_2, MEMORY_AND_DISK_2
        – same as about, but make two replicas <- improves failure recovery times!
› rdd.cache() = rdd.persist(MEMORY_ONLY)

Best practices
› For interactive sessions
    › cache preprocessed data
› For batch computations
    › cache dictionaries
    › cache other datasets that are accessed multiple times
› For iterative computations
    › cache static data
› And do benchmarks!

## Broadcast variables

› Broadcast variable is a read-only variable that is efficiently shared among tasks
› Distribution is done by a torrent-like protocol (extremely fast!)
› Distributed efficiently compared to captured variables

› Broadcast variables are read-only shared variables with effective sharing mechanism
› Useful to share dictionaries, models

Example
```python
sc = SparkContext(conf=…)
# compute the dictionary
my_dict_rdd = sc.textFile(…).map(…).filter(…)
my_dict_data = my_dict_rdd.collect()
# distributed the dictionary via the broadcast variable
broadcast_var = sc.broadcast(my_dict_data)
# use the broadcast variable within the task
my_data_rdd = sc.textFile(…).filter(
    lambda x: x in broadcast_var.value)
```

## Accumulator variables

› Accumulator variable is a read-write variable that is shared among tasks
› Writes are restricted to increments!
    ›increments only
    ›i. e.: var += delta 
    ›addition may be replaced by any associate, commutative operation
› can use custom associative, commutative operation for the updates
› Reads are allowed only by the driver program!
› can read the total value only in the driver
› Useful for the control flow, monitoring, profiling & debugging

When the accumulator gets incremented on the particular executor, the delta is sent back to the driver program together with a task outcome. Therefore, there is just one natural aggregation point where we can compute the total value, that is the driver. 
It is also important to note that updates generated in actions are guaranteed to be applied only once to the accumulator. This is because successful actions are never re-executed and Spark can conditionally apply the update.

For updates in transformation, there are no guarantees when they accumulate updates. Transformations can be recomputed on a failure on the memory pressure or in another unspecified codes like a preemption. Spark provides no guarantees on how many times transformation code maybe re-executed.

Use cases
› Performance counters
    ›# of processed records, total elapsed time, total error and so on and so forth
› Simple control flow
› conditionals: stop on reaching a threshold for corrupted records
    ›loops: decide whether to run the next iteration of an algorithm or not
› Monitoring
    ›export values to the monitoring system
› Profiling & debugging

