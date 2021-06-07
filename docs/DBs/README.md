# Databases types

## Centralised vs Distributed database
- As their names imply, a centralized database has only one database file, kept at a single location on a given network; a distributed database is composed of multiple database files stored in multiple physical locations, all controlled by a central DBMS.
- Distributed databases are more complex, and require additional work to keep the data stored up-to-date and to avoid redundancy. However, they provide parallelization (which balances the load between several servers), preventing bottlenecking when a large number of requests come through.
- Centralized databases make data integrity easier to maintain; once data is stored, outdated or inaccurate data (stale data) is no longer available in other places. However, it may be more difficult to retrieve lost or overwritten data in a centralized database, since it lacks easily accessible copies by nature.

## Personal database.

## End-user database.

## Cloud database.

## Commercial database.

## Operational database.

## Relational database
- In a relational database, each relation is a set of tuples. Each tuple is a list of attributes, which represents a single item in the database. Each tuple (“row”) in a relation (“table”) shares the same attributes (“columns”). Each attribute has a well-defined data type (int, string, etc), defined ahead of time — schema in a relational database is static.
- Examples include: Oracle, MySQL, SQLite, PostgreSQL

## Non relational DBs

At it’s simplest, a non-relational database is one that doesn’t use the relational model; no relations (tables) with tuples (rows) and attributes (columns). This title covers a pretty wide range of models, typically grouped into four categories: key-value stores, graph stores, column stores, and document stores.

## NoSQL database.

“NoSQL” originally referred to “non-SQL” or “non-relational” when describing a database. Sometimes “NoSQL” is also meant to mean “Not only SQL”, to emphasize that they don’t prohibit SQL or SQL-like query languages; they just avoid functionality like relation/table schemas and JOIN operations.
key walue
document
column db

## Key-value
- Key-value stores don’t use the pre-defined structure of relational databases, but instead treat all of their data as a single collection of items. For example, a screwdriver in our toolbox might have attributes like “drive_type”, “length”, and “size”, but a hammer may only have one attribute: “size”. Instead of storing (often empty) “drive_type” and “length” fields for every item in your toolbox, a “hammer_01” key will return only the information relevant to it.
- Success with this model lies in its simplicity. Like a map or a dictionary, each key-value pair defines a link between some unique “key” (like a name, ID, or URL) and its “value” (an image, a file, a string, int, list, etc). There are no fields, so the entire value must be updated if changes are made. Key-value stores are generally fast, scalable, and flexible.
- Examples include: Dynamo, MemcacheDB, Redis

## Column store
- Row-oriented databases describe single items as rows, and store all the data in a particular table’s rows together: ‘hammer_01’, ‘medium’, ‘blue’; ‘hammer_02’, ‘large’, ‘yellow’. A column store, on the other hand, generally stores all the values of a particular column together: ‘hammer_01’, ‘hammer_02’; ‘medium’, ‘large’; ‘blue’, ‘yellow’.
- This can definitely get confusing, but the two map data very differently. In a row-oriented system, the primary key is the row ID, mapped to its data. In the column-oriented system, the primary key is the data, mapping back to row IDs. This allows for some very quick aggregations like totals and averages.
- Examples include: Accumulo, Cassandra, HBase

## Object-oriented database
Not as common as other non-relational databases, an object or object-oriented database is ones in which data is represented in the form of “objects” (with attributes and methods) as used in object-oriented programming. This type might be used in place of a relational database and ORM, and may make sense when the data is complex or there are complex many-to-many relationships involved. Beware its language dependence and difficulty with ad-hoc queries though.

## Graph database
- Graph stores are a little more complicated.Using graph structures, this type of database is made for dealing with interconnected data — think social media connections, a family tree, or a food chain. Items in the database are represented by “nodes”, and “edges” directly represent the relationships between them. Both nodes and edges can store additional “properties”: id, name, type, etc.
- The strength of a graph database is in traversing the connections between items, but their scalability is limited.
- Examples include: Allegro, OrientDB, Virtuoso

## Document store
- Document stores treat all information for a given item in the database as a single instance in the database (each of which can have its own structure and attributes, like other non-relational databases). These “documents” can generally be thought of as sets of key-value pairs: {ToolName: “hammer_01”, Size: “medium”, Color: “blue”}
- Documents can be independent units, which makes performance and horizontal scalability better, and unstructured data can be stored easily.
- Examples include: Apache CouchDB, MongoDB, Azure DocumentDB.

# Databases 

## CAP theorem

Consistency, Availability, Partition tolerance - Pick Two

**Consistency**
> When you read data it will give same data how many times read and server send response each and every request but systems always consistent when read data.(all node having same data)
Consistency means that all clients see the same data at the same time, no matter which node they connect to. For this to happen, whenever data is written to one node, it must be instantly forwarded or replicated to all the other nodes in the system before the write is deemed ‘successful.’

**Availability**
> It means all requests give response and no error accured in this systems.
Availability means that that any client making a request for data gets a response, even if one or more nodes are down. Another way to state this—all working nodes in the distributed system return a valid response for any request, without exception.

**Partition tolerance**
> All functions run all time when more nodes not responsive and commnication break between two nodes
A partition is a communications break within a distributed system—a lost or temporarily delayed connection between two nodes. Partition tolerance means that the cluster must continue to work despite any number of communication breakdowns between nodes in the system.

## NoSQL
NoSQL databases are classified based on the two CAP characteristics they support:

**CP database**
> It wait for response form partioned nodes and that data are timeout error. system give data and it distributed across the hadoop cluster.System return error that based on you desire.It is good for marketing because which system does not work partition data will tagged to user.

A CP database delivers consistency and partition tolerance at the expense of availability. When a partition occurs between any two nodes, the system has to shut down the non-consistent node (i.e., make it unavailable) until the partition is resolved.

**AP database**
> It returns the recent data from the systems and it allows write options that processed when partion resolved. Availability compeling the data when come external error come from system functions. Final decision is software trade off in that systems.In this process any network problem occurs control options are there in your hand only because network problem is only temporary.

An AP database delivers availability and partition tolerance at the expense of consistency. When a partition occurs, all nodes remain available but those at the wrong end of a partition might return an older version of data than others. (When the partition is resolved, the AP databases typically resync the nodes to repair all inconsistencies in the system.)

**CA database**
> All realational database are CA. In CA all nodes are always in contact. Partion occurs in system that system will be blocked.

A CA database delivers consistency and availability across all nodes. It can’t do this if there is a partition between any two nodes in the system, however, and therefore can’t deliver fault tolerance.

### Spaces Defined by CAP:

**NoSpace:**

It is called empty set because there is no any database engines. It not satisty any theorem properties

**CD Space:**

Space between consistency and availability. In CD Space distribution does not exist and find NoSql database.Relational database are postioned in this space

**CT Space:**

It don’t have any consistency and it will favor of availability. This is a relative database and cannot guarntee between nodes

**DT Space:**

It offers some consistency and leaving certain levels of availability. In this space database not response the client enquires.

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

### CBC & Gcm

`GCM` and `CBC` modes internally work quite differently; they both involve a block cipher and an exclusive-or, but they use them in different ways.

In `CBC` mode, you encrypt a block of data by taking the current plaintext block and exclusive-oring that wth the previous ciphertext block (or IV), and then sending the result of that through the block cipher; the output of the block cipher is the ciphertext block.

`GCM` mode provides both privacy (encryption) and integrity. To provide encryption, GCM maintains a counter; for each block of data, it sends the current value of the counter through the block cipher. Then, it takes the output of the block cipher, and exclusive or's that with the plaintext to form the ciphertext.

Note two key differences:

* What's being exclusive-or'ed; in CBC mode, the plaintext is exclusive-or'ed with data that the attacker knows (the IV or a previous ciphertext block); hence, that in itself does not provide any inherent security (instead, we do it to minimize the chance that we send the same block twice through the block cipher). In GCM mode, the plaintext is exclusive-or'ed with output from the block cipher; it is inherent in the security model that the attacker cannot guess that output (unless he already knows the plaintext and the ciphertext).

* What's being sent through the block cipher; in CBC mode, the plaintext is sent through the block cipher (after it's been 'randomized' with an exclusive-or); in GCM mode, what's being sent through the block cipher doesn't actually depend on the data being encrypted, but instead only on internal state.


### CTE & OBT

Common Table Expression (CTE) или обобщенное табличное выражение (OTB) – это временные результирующие наборы (т.е. результаты выполнения SQL запроса), которые не сохраняются в базе данных в виде объектов, но к ним можно обращаться.

Главной особенностью обобщенных табличных выражений является то, что с помощью них можно писать рекурсивные запросы.

Предназначены:
* Основной целью OTB является написание рекурсивных запросов, можно сказать для этого они, и были созданы;
* OTB можно использовать также и для замены представлений (VIEW), например, в тех случаях, когда нет необходимости сохранять в базе SQL запрос представления, т.е. его определение;
* Обобщенные табличные выражения повышают читаемость кода путем разделения запроса на логические блоки, и тем самым упрощают работу со сложными запросами;
* Также OTB предназначены и для многократных ссылок на результирующий набор из одной и той же SQL инструкции

Можно определить с помощью [WITH](sql.md)
## B-Tree

> [Indexes](.indexes.md)

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

## Transaction

A set of logically related operations is known as transaction. The main operations of a transaction are:
* Read(A): Read operations Read(A) or R(A) reads the value of A from the database and stores it in a buffer in main memory.
* Write (A): Write operation Write(A) or W(A) writes the value back to the database from buffer.
* Commit: After all instructions of a transaction are successfully executed, the changes made by transaction are made permanent in the database.
* Rollback: If a transaction is not able to execute all operations successfully, all the changes made by transaction are undone.

### Properties of a transaction

[ACID](#ACID)

* Atomicity: As a transaction is set of logically related operations, either all of them should be executed or none. A debit transaction discussed above should either execute all three operations or none.If debit transaction fails after executing operation 1 and 2 then its new value 4000 will not be updated in the database which leads to inconsistency.

* Consistency: If operations of debit and credit transactions on same account are executed concurrently, it may leave database in an inconsistent state.

* Isolation: Result of a transaction should not be visible to others before transaction is committed. For example, Let us assume that A’s balance is Rs. 5000 and T1 debits Rs. 1000 from A. A’s new balance will be 4000. If T2 credits Rs. 500 to A’s new balance, A will become 4500 and after this T1 fails. Then we have to rollback T2 as well because it is using value produced by T1. So a transaction results are not made visible to other transactions before it commits.

* Durable: Once database has committed a transaction, the changes made by the transaction should be permanent. e.g.; If a person has credited $500000 to his account, bank can’t say that the update has been lost. To avoid this problem, multiple copies of database are stored at different locations.

### Transaction isolation levels

In database systems, isolation determines how transaction integrity is visible to other users and systems. 

A lower isolation level increases the ability of many users to access the same data at the same time, but increases the number of concurrency effects (such as dirty reads or lost updates) users might encounter. 
Conversely, a *higher isolation level reduces the types of concurrency effects* that users may encounter, but requires more system resources and increases the chances that one transaction will block another.

Isolation levels are defined by the presence or absence of the following phenomena:

* **Dirty Reads** A Dirty read is the situation when a transaction reads a data that has not yet been committed. For example, Let’s say transaction 1 updates a row and leaves it uncommitted, meanwhile, Transaction 2 reads the updated row. If transaction 1 rolls back the change, transaction 2 will have read data that is considered never to have existed.

* **Nonrepeatable Reads** Non Repeatable read occurs when a transaction reads same row twice, and get a different value each time. For example, suppose transaction T1 reads data. Due to concurrency, another transaction T2 updates the same data and commit, Now if transaction T1 rereads the same data, it will retrieve a different value.

* **Phantom Reads** Phantom Read occurs when two same queries are executed, but the rows retrieved by the two, are different. For example, suppose transaction T1 retrieves a set of rows that satisfy some search criteria. Now, Transaction T2 generates some new rows that match the search criteria for transaction T1. If transaction T1 re-executes the statement that reads the rows, it gets a different set of rows this time.

| Isolation Level   |   Dirty Read  |   Serialization Anomaly |
|--------------------|--------------|-------------------------|
| Read uncommitted   |   Allowed, but not in PG   |   Possible |
| Read committed   |   Not possible   |   Possible |
| Repeatable read   |   Not possible   |   Possible |
| Serializable   |   Not possible   |   Not possible |

* **Read Uncommitted** – Read Uncommitted is the lowest isolation level. In this level, one transaction may read not yet committed changes made by other transaction, thereby allowing dirty reads. In this level, transactions are not isolated from each other.

* **Read Committed** – This isolation level guarantees that any data read is committed at the moment it is read. Thus it does not allows dirty read. The transaction holds a read or write lock on the current row, and thus prevent other transactions from reading, updating or deleting it.

* **Repeatable Read** – This is the most restrictive isolation level. The transaction holds read locks on all rows it references and writes locks on all rows it inserts, updates, or deletes. Since other transaction cannot read, update or delete these rows, consequently it avoids non-repeatable read.

SNAPSHOT for MSQL
Specifies that data read by any statement in a transaction will be the transactionally consistent version of the data that existed at the start of the transaction. The transaction can only recognize data modifications that were committed before the start of the transaction. Data modifications made by other transactions after the start of the current transaction are not visible to statements executing in the current transaction. The effect is as if the statements in a transaction get a snapshot of the committed data as it existed at the start of the transaction.

* **Serializable** – This is the Highest isolation level. A serializable execution is guaranteed to be serializable. Serializable execution is defined to be an execution of operations in which concurrently executing transactions appears to be serially executing.


## Schedule

A schedule is a series of operations from one or more transactions. A schedule can be of two types:
* Serial Schedule: When one transaction completely executes before starting another transaction, the schedule is called serial schedule. A serial schedule is always consistent. e.g.; If a schedule S has debit transaction T1 and credit transaction T2, possible serial schedules are T1 followed by T2 (T1->T2) or T2 followed by T1 ((T2->T1). A serial schedule has low throughput and less resource utilization.
* Concurrent Schedule: When operations of a transaction are interleaved with operations of other transactions of a schedule, the schedule is called Concurrent schedule. e.g.; Schedule of debit and credit transaction shown in Table 1 is concurrent in nature. But concurrency can lead to inconsistency in the database.  The above example of a concurrent schedule is also inconsistent.

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

# DBMS: database management system

Wikipedia has a great summary: “A database management system is a software application that interacts with the user, other applications, and the database itself to capture and analyze data. A general-purpose DBMS is designed to allow the definition, creation, querying, update, and administration of databases.” MySQL, PostgreSQL, Oracle — these are database management systems.

# Middleware

Database-oriented middleware is “all the software that connects some application to some database.” Some definitions include the DBMS under this category. Middleware might also facilitate access to a DBMS via a web server for example, without having to worry about database-specific characteristics.

# Scalability

Scalability is the capability of a database to handle a growing amount of data. There are two types of scalability:
- Vertical scalability is simply adding more capacity to a single machine. Virtually every database is vertically scalable.
- Horizontal scalability refers to adding capacity by adding more machines. The DBMS needs to be able to partition, manage, and maintain data across all machines.

## master-slave

## ZooKeeper

Apache ZooKeeper is an open-source server for highly reliable distributed coordination of cloud applications. It is a project of the Apache Software Foundation.

Zookeeper is a top-level software developed by Apache that acts as a centralized service and is *used to maintain naming and configuration data and to provide flexible and robust synchronization within distributed systems*. 

Zookeeper it self is *allowing multiple clients to perform simultaneous reads and writes and acts as a shared configuration service within the system*. The **Zookeeper atomic broadcast (ZAB) protocol** is the brains of the whole system, making it possible for Zookeeper to act as an atomic broadcast system and issue orderly updates.

[ZooKeeper](BigData/ZooKeeper/README.md)

## Shard


# myisam vs innodb

in myisam vs innodb, The frequently & default used storage engine in MySQL are MyISAM (default storage engine) and InnoDB (storage engine for MySQL).

The main differences between myisam vs innodb are allow for “referential integrity” as well as “transactions”.

convert myisam to innodb
```sql
ALTER TABLE wp_posts ENGINE=InnoDB;
```

**MYISAM: (default storage engine)**
* It’s Help to Table-level Locking
* It’s designed for need of speed
* It’s does not allow foreign keys hence we call MySQL with MYISAM is DBMS
* It’s stores its tables, data as well as indexes in diskspace using separate three different files. (Database tablename.FRM, tablename.MYD, tablename.MYI)
* MYISAM not Help to transaction. You cannot commit statement as well as rollback statement with
* MYISAM. Once you issue a command it’s done.
* MYISAM Help to fulltext search
* You can use MyISAM storage engine, if the table is additional static with lots of select and less update as well as delete.

**MYISAM: (default storage engine)**
* It’s Help to Table-level Locking
* It’s designed for need of speed
* It’s does not allow foreign keys hence we call MySQL with MYISAM is DBMS
* It’s stores its tables, data as well as indexes in diskspace using separate three different files. (Database tablename.FRM, tablename.MYD, tablename.MYI)
* MYISAM not Help to transaction. You cannot commit statement as well as rollback statement with
* MYISAM. Once you issue a command it’s done.
* MYISAM Help to fulltext search
* You can use MyISAM storage engine, if the table is additional static with lots of select and less update as well as delete.


# Links

https://medium.com/@rwilliams_bv/intro-to-databases-for-people-who-dont-know-a-whole-lot-about-them-a64ae9af712
https://www.geeksforgeeks.org/
Yandex
