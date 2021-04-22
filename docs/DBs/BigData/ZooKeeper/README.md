# ZooKeeper

Zookeeper is a top-level software developed by Apache that acts as a centralized service and is *used to maintain naming and configuration data and to provide flexible and robust synchronization within distributed systems*. 
Zookeeper keeps track of status of the Kafka cluster nodes and it also keeps track of Kafka topics, partitions etc.

Zookeeper it self is *allowing multiple clients to perform simultaneous reads and writes and acts as a shared configuration service within the system*. The **Zookeeper atomic broadcast (ZAB) protocol** is the brains of the whole system, making it possible for Zookeeper to act as an atomic broadcast system and issue orderly updates.

