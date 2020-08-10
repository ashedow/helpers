# Databases

## Types

### Centralised database.

### Distributed database.

### Personal database.

### End-user database.

### Commercial database.

### NoSQL database.
key walue
document
column db

### Operational database.

### Relational database.

### Cloud database.

### Object-oriented database.

# Graph database.

## Normalization vs Denormalization

| BASIS FOR COMPARISON | NORMALIZATION                                                                                                              | DENORMALIZATION                                                                          |
|----------------------|----------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| Basic                | Normalization is the process of creating a set schema to store non-redundant and consistent data.                          | Denormalization is the process of combining the data so that it can be queried speedily. |
| Purpose              | To reduce the data redundancy and inconsistency.                                                                           | To achieve the faster execution of the queries through introducing redundancy.           |
| Used in              | OLTP system, where the emphasize is on making the insert, delete and update anomalies faster and storing the quality data. | OLAP system, where the emphasis is on making the search and analysis faster.             |
| Data integrity       | Maintained                                                                                                                 | May not retain                                                                           |
| Redundancy           | Eliminated                                                                                                                 | Added                                                                                    |
| Number of tables     | Increases                                                                                                                  | Decreases                                                                                |
| Disk space           | Optimized usage                                                                                                            | Wastage                                                                                  |

### Normalization

> Normalization is the process of efficiently organizing data in a database. 
> There are two goals of the normalization process: eliminating redundant data (for example, storing the same data in more than one table) and ensuring data dependencies make sense (only storing related data in a table). Both of these are worthy goals, as they reduce the amount of space a database consumes and ensure that data is logically stored.

#### Normal forms

The database community has developed a series of guidelines for ensuring that databases are normalized. These are referred to as normal forms and are numbered from one (the lowest form of normalization, referred to as first normal form or 1NF) through five (fifth normal form or 5NF). In practical applications, you'll often see 1NF, 2NF, and 3NF, along with the occasional 4NF. The fifth normal form is very rarely seen and won't be discussed in this article.

* FIRST NORMAL FORM (1NF)
First normal form (1NF) sets the fundamental rules for an organized database:
 - Eliminate duplicative columns from the same table.
 - Create separate tables for each group of related data and identify each row with a unique column or set of columns (the primary key).

* SECOND NORMAL FORM (2NF)
Second normal form (2NF) further addresses the concept of removing duplicative data:
 - Meet all the requirements of the first normal form.
 - Remove subsets of data that apply to multiple rows of a table and place them in separate tables.
 - Create relationships between these new tables and their predecessors through the use of foreign keys.

* THIRD NORMAL FORM (3NF)
Third normal form (3NF) goes one significant step further:
 - Meet all the requirements of the second normal form.
 - Remove columns that are not dependent upon the primary key.

* BOYCE-CODD NORMAL FORM (BCNF OR 3.5NF)
The Boyce-Codd Normal Form, also referred to as the "third and half (3.5) normal form," adds one more requirement:
 - Meet all the requirements of the third normal form.
 - Every determinant must be a candidate key.

* FOURTH NORMAL FORM (4NF)
Finally, fourth normal form (4NF) has one additional requirement:
 - Meet all the requirements of the third normal form.
 - A relation is in 4NF if it has no multi-valued dependencies.

* FIFTH NORMAL FORM5NF (Fifth Normal Form)
 - A table is in 5th Normal Form only if it is in 4NF and it cannot be decomposed into any number of smaller tables without loss of data.

* SIXTH NORMAL FORM6NF (Sixth Normal Form)
 - 6th Normal Form is not standardized, yet however, it is being discussed by database experts for some time. Hopefully, we would have a clear & standardized definition for 6th Normal Form in the near future.

### Denormalization

> Denormalization is a strategy used on a previously-normalized database to increase performance. In computing, denormalization is the process of trying to improve the read performance of a database, at the expense of losing some write performance, by adding redundant copies of data or by grouping data.[1][2] It is often motivated by performance or scalability in relational database software needing to carry out very large numbers of read operations. Denormalization differs from the unnormalized form in that denormalization benefits can only be fully realized on a data model that is otherwise normalized.

Pros of Denormalization:
 + Retrieving data is faster since we do fewer joins
 + Queries to retrieve can be simpler(and therefore less likely to have bugs),
 + since we need to look at fewer tables.

Cons of Denormalization:
 - Updates and inserts are more expensive.
 - Denormalization can make update and insert code harder to write.
 - Data may be inconsistent . Which is the “correct” value for a piece of data?
 - Data redundancy necessitates more storage.

## Indexes

Indexing is a way to optimize the performance of a database by minimizing the number of disk accesses required when a query is processed. It is a data structure technique which is used to quickly locate and access the data in a database.

The indexing has various attributes:

 * Access Types: This refers to the type of access such as value based search, range access, etc.
 * Access Time: It refers to the time needed to find particular data element or set of elements.
 * Insertion Time: It refers to the time taken to find the appropriate space and insert a new data.
 * Deletion Time: Time taken to find an item and delete it as well as update the index structure.
 * Space Overhead: It refers to the additional space required by the index.

In general, there are two types of file organization mechanism which are followed by the indexing methods to store the data:

1. Sequential File Organization or Ordered Index File: In this, the indices are based on a sorted ordering of the values. These are generally fast and a more traditional type of storing mechanism. These Ordered or Sequential file organization might store the data in a dense or sparse format:
    * Dense Index:
        - For every search key value in the data file, there is an index record.
        - This record contains the search key and also a reference to the first data record with that search key value.
    * Sparse Index:
        - The index record appears only for a few items in the data file. Each item points to a block as shown.
        - To locate a record, we find the index record with the largest search key value less than or equal to the search key value we are looking for.
        - We start at that record pointed to by the index record, and proceed along with the pointers in the file (that is, sequentially) until we find the desired record.
    * Hash File organization: Indices are based on the values being distributed uniformly across a range of buckets. The buckets to which a value is assigned is determined by a function called a hash function.

There are primarily three methods of indexing:
    * Clustered Indexing
    * Non-Clustered or Secondary Indexing
    * Multilevel Indexing

1. Clustered Indexing
When more than two records are stored in the same file these types of storing known as cluster indexing. By using the cluster indexing we can reduce the cost of searching reason being multiple records related to the same thing are stored at one place and it also gives the frequent joing of more than two tables(records).

Clustering index is defined on an ordered data file. The data file is ordered on a non-key field. In some cases, the index is created on non-primary key columns which may not be unique for each record. In such cases, in order to identify the records faster, we will group two or more columns together to get the unique values and create index out of them. This method is known as the clustering index. Basically, records with similar characteristics are grouped together and indexes are created for these groups.
For example, students studying in each semester are grouped together. i.e. 1st Semester students, 2nd semester students, 3rd semester students etc are grouped.
cluster_index
Clustered index sorted according to first name (Search key)

    * Primary Indexing:
    This is a type of Clustered Indexing wherein the data is sorted according to the search key and the primary key of the database table is used to create the index. It is a default format of indexing where it induces sequential file organization. As primary keys are unique and are stored in a sorted manner, the performance of the searching operation is quite efficient.

2. Non-clustered or Secondary Indexing
A non clustered index just tells us where the data lies, i.e. it gives us a list of virtual pointers or references to the location where the data is actually stored. Data is not physically stored in the order of the index. Instead, data is present in leaf nodes. For eg. the contents page of a book. Each entry gives us the page number or location of the information stored. The actual data here(information on each page of the book) is not organized but we have an ordered reference(contents page) to where the data points actually lie. We can have only dense ordering in the non-clustered index as sparse ordering is not possible because data is not physically organized accordingly.
It requires more time as compared to the clustered index because some amount of extra work is done in order to extract the data by further following the pointer. In the case of a clustered index, data is directly present in front of the index.
indexing3

3. Multilevel Indexing
With the growth of the size of the database, indices also grow. As the index is stored in the main memory, a single-level index might become too large a size to store with multiple disk accesses. The multilevel indexing segregates the main block into various smaller blocks so that the same can stored in a single block. The outer blocks are divided into inner blocks which in turn are pointed to the data blocks. This can be easily stored in the main memory with fewer overheads.

## B-Tree

B-Tree is a self-balancing search tree. In most of the other self-balancing search trees (like AVL and Red-Black Trees), it is assumed that everything is in main memory. 
To understand the use of B-Trees, we must think of the huge amount of data that cannot fit in main memory. When the number of keys is high, the data is read from disk in the form of blocks. Disk access time is very high compared to the main memory access time. 
The main idea of using B-Trees is to reduce the number of disk accesses. Most of the tree operations (search, insert, delete, max, min, ..etc ) require O(h) disk accesses where h is the height of the tree. 
B-tree is a fat tree. The height of B-Trees is kept low by putting maximum possible keys in a B-Tree node. Generally, the B-Tree node size is kept equal to the disk block size. Since the height of the B-tree is low so total disk accesses for most of the operations are reduced significantly compared to balanced Binary Search Trees like AVL Tree, Red-Black Tree, ..etc.

Search, Insert, Delete - `O(log n)` , where “n” is the total number of elements in the B-tree.

Properties of B-Tree:
 1. All leaves are at the same level.
 2. A B-Tree is defined by the term minimum degree ‘t’. The value of t depends upon disk block size.
 3. Every node except root must contain at least t-1 keys. The root may contain minimum 1 key.
 4. All nodes (including root) may contain at most 2t – 1 keys.
 5. Number of children of a node is equal to the number of keys in it plus 1.
 6. All keys of a node are sorted in increasing order. The child between two keys k1 and k2 contains all keys in the range from k1 and k2.
 7. B-Tree grows and shrinks from the root which is unlike Binary Search Tree. Binary Search Trees grow downward and also shrink from downward.
 8. Like other balanced Binary Search Trees, time complexity to search, insert and delete is O(log n).


## Explain and Explain analyze

# Concurrency Control

# Race condition

# ACID

> (Atomicity, Consistency, Isolation, Durability) refers to a standard set of properties that guarantee database transactions are processed reliably.

## Atomicity
Atomicity means that you guarantee that either all of the transaction succeeds or none of it does. You don’t get part of it succeeding and part of it not. If one part of the transaction fails, the whole transaction fails. With atomicity, it’s either “all or nothing”.

## Consistency
This ensures that you guarantee that all data will be consistent. All data will be valid according to all defined rules, including any constraints, cascades, and triggers that have been applied on the database.

## Isolation
Guarantees that all transactions will occur in isolation. No transaction will be affected by any other transaction. So a transaction cannot read data from any other transaction that has not yet completed.

## Durability
Durability means that, once a transaction is committed, it will remain in the system – even if there’s a system crash immediately following the transaction. Any changes from the transaction must be stored permanently. If the system tells the user that the transaction has succeeded, the transaction must have, in fact, succeeded.

## Types of Failure

### Transaction Failure
A transaction failure could occur due to bad input or some other violation of consistency. It could also be due to a timeout or deadlock in the DBMS.

### System Failure
A system failure can be caused by a bug in the DBMS code, an operating system fault, or a hardware failure.

### Media Failure
Media failure refers to the condition of not being able to read from or write to a storage device (such as the hard disc). This could be caused by the media itself, or it could be due to bugs in the operating system.

Media failure is usually quite rare when compared to the other two types of failure.

## ACID Compliance
All of the major relational DBMSs adhere to the ACID principles. They all include features that ensure that the data maintains consistent throughout software and hardware crashes, as well as any failed transactions.

NoSQL databases are a bit different. NoSQL databases are often designed to ensure high availability across a cluster, which usually means that consistency and/or durability is sacrificed to some degree. However, most NoSQL DBMSs can provide atomicity to some degree.

# CRUD

> (Create, Read, Update, Delete) - four basic functions of persistent storage.

* create or add new entries;
* read, retrieve, search, or view existing entries;
* update or edit existing entries;
* delete, deactivate, or remove existing entries.

# master-slave

# zookiper

# Shard
