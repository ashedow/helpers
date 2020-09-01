# Elasticsearch

Elasticsearch is made of
* Cluster
A cluster is a collection of one or more nodes that, together, holds the entire data. It provides federated indexing and search capabilities across all nodes and is identified by an unique name (by default it is ‘/ elasticsearch’/)

* Node
A node is a single server which is a part of cluster, stores data and participates in the cluster’s indexing and search capabilities.

* Index
An index is a collection of documents with similar characteristics and is identified by a name. This name is used to refer the index while performing indexing, search, update, and delete operations against the documents in it. In a single cluster, you can define as many indexes as you want.

* Document
A document is a basic unit of information which can be indexed. It is expressed in JSON which is an ubiquitous internet data interchange format.

* Shards
Elasticsearch provides the ability to subdivide the index into multiple pieces called shards. Each shard is in itself a fully-functional and independent “index” that can be hosted on any node within the cluster. This is useful for the case when an index putted in a single node would take more disk space than available. The index then is subdivided between different nodes. Besides, shards allow you to distribute and parallelise operations across shards, increasing the performance.

* Replicas
Elasticsearch allows you to make one or more copies of your index’s shards which are called replica shards or replica. It provides high availability in case a node fails, and it allows you to scale out your search volume since searches can be executed on all replicas in parallel.