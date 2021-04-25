# NoSQL

Relational databases management systems (RDBMS) store data in tabular form of rows and columns and Structured Query Language (SQL) is the language that is used to access and manipulate data in relational databases. The rapid growth of data and need of high availability, scalability, and performance in modern software applications have handicapped relational databases due to their design structure. SQL is the only way to access data from relational databases and the going through billions and trillions of records takes time.
 
This is where non-relational databases play a vital role. The database management systems (DBMS) that do not use SQL to query databases are called NoSQL databases. NoSQL databases are also called non SQL or non relational databases. NoSQL databases are not a single kind of database. NoSQL databases are various database technologies that allow data to be stored and managed in different formats without the use of SQL. Some of the databases use their own mechanism, API and some use non SQL languages.
 
Non-relational databases have been in existences for decades but the term, “NoSQL” was coined by Carlo Strozzi in 1998 to name his lightweight Strozzi NoSQL open-source relational database. The database did not use SQL to access and manipulate data.

## Advantages of NoSQL databases

With the growing amount of data and need of real-time query responses, data analytics, and semantic algorithms, noSQL databases have become a need of today. NoSQL databases are more scalable and provide higher performance when dealing with high volumes of data. NoSQL databases also provide faster traversing and better semantic solutions.
 
Relational databases have fixed schemas. The database schema must be created before data can be inserted in a relational database. Once a database is created, software applications are written, it’s not easy to change schemas. Changing schemas on relational databases may result in loss of data, broken applications, and heavy rewriting of software applications. Even changing a column type in a relational database can cause major issues to data and applications. What if the database is large with trillions of records?
 
NoSQL database do not have predefined schemas, which makes NoSQL databases a prefect candidate for rapidly changing development environments. NoSQL allows developers to make changes on the fly without affecting applications.
 
The major drawback of NoSQL database is learning curve and multiple APIs and methods to work with the databases. There is no unified single model like SQL to work with NoSQL databases. Each NoSQL DBMS offers its own API or library. NoSQL DBMS are also broken down into various types such as graph, document, column, and key-value. Each of these DBMS has a different architecture and concept to store and manage data.

## Types of NoSQL Databases

NoSQL databases can be categorized in the following five major categories,
* Column
* Document
* Graph
* Key-value
* Object databases

### 1. Column Data Store

A column data store, also known as a column-oriented DBMS or columnar database management system, stores data in columns, rather than rows. Relational database management systems (RDBMS) store data in rows and data properties as column headers. Both row-based and column-based DBMS use SQL as their query language but column-oriented DBMS may offer better performance. Imagine you need to list all names from a table based on an ID, rather than going through all rows, you could just access a single column of the table.
Here are some of the key characteristics of column data store DBMS.
* Column store DBMS use a keyspace that is like a database schema in RDBMS.
* Column store DBMS have a concept called a key family. A key family is like a table on RDBMS. * The keyspace contains all the column families in a database.
* A column family contains multiple rows. Each row has a unique key called Row Key, which is a unique identifier for that row. While each row has a single Row Key, it may have multiple columns. Each column has a Name, Value, and TimeStamp fields.
* Each row can contain a different number of columns. All rows don’t have to have the same columns.
* Each column can contain multiple rows. All rows don’t have to have the same data.
* Column-oriented DBMS are often used on OLAP data operations. 

Example: Some of the popular column-oriented DBMS include Bigtable, Apache HBase, MariaDB, Azure SQL Data Warehouse, Google BigQuery, IBM Db2, MemSQL, Microsoft SQL Server 2012 or later, and SAP HANA.

### 2. Document Databases

Document databases management systems are designed to store *full documents as one entity* with its attributes. Documents are typically in JSON and XML documents formats that are easy to read, store, and parse using APIs and libraries. Document DBMS are faster to load, access, and parse. User profiles, content management systems, and catalogs are some common use case of document DBMS.

Example: ArangoDB, Couchbase Server, CouchDB, Amazon DocumentDB, MongoDB, CouchBase, Azure DocumentDB, Cosmos DB, Elasticsearch, Informix, Lotus Notes, and SAP HANA are some of the popular document DBMS.

### 3. Graph Databases

Graph databases are developed based on graph theory. In graph databases, a graph can be used to represent data entities, their attributes, and relationships. The vertices of a graph database are called nodes and edges are called edges.
 
Popular graph databases are Neo4j, OrientDB, and AangoDB. Microsoft Azure CosmosDB also support graph model.

### 4. Key-value Store

Key value store is designed to *store dictionary type (collection of objects or records) of data structure where data is stored in a key-value pair and key is used to retrieve data*. 

Example:
Popular key-value databases are Dynamo, ArangoDB, Berkeley DB, FoundationDB, and MemcacheDB.

### 5. Object databases

The concept of object databases came from the concept of object-oriented programming. What if we have a database system that can store an entire object, read it back, and apply operations on it?
 
Object Database Management Systems (ODMS) or Object Oriented Database Management Systems (OODBMS) provide functionality to store and manipulate data in object forms.
 
There is no unified standard of OODBMSs. Some OODBMSs use Object Query Language (OQL), that is similar to SQL for OODBMSs.
