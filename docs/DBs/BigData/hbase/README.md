# HBase

**HBase** is a column-oriented non-relational database management system that runs on top of [Hadoop Distributed File System (HDFS)](../Hadoop/README.md). 
HBase provides a fault-tolerant way of storing sparse data sets, which are common in many big data use cases. It is well suited for real-time data processing or random read/write access to large volumes of data.

HBase relies on ZooKeeper for high-performance coordination. ZooKeeper is built into HBase, but if you’re running a production cluster, it’s suggested that you have a dedicated ZooKeeper cluster that’s integrated with your HBase cluster.

HBase works well with [Hive](../MapReduce.md###Hive), a query engine for batch processing of big data, to enable fault-tolerant big data applications.

## Hbase vs Hadoop

|   HDFS    |   HBase   |
| ------------- |-------------|
| HDFS is a Java-based file system utilized for storing large data sets.    |   HBase is a Java based Not Only SQL database|
| HDFS has a rigid architecture that does not allow changes. It doesn’t facilitate dynamic storage.	| HBase allows for dynamic changes and can be utilized for standalone applications.|
| HDFS is ideally suited for write-once and read-many times use cases   |   HBase is ideally suited for random write and read of data that is stored in HDFS.|


## Links 
https://java2blog.com/hadoop-hbase/