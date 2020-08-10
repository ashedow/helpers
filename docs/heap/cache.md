# Cache 

A component that remembers recently used data in order to speed up future reads of the same data. It is generally not complete: thus, if some data is missing from the cache, it has to be fetched from some underlying, slower data storage system that has a complete copy of the
data.

## Cache Algorithms

* Least Frequently Used (LFU): 
keeps track of how often an entry is accessed. The item that has the lowest count gets removed first.
This cache algorithm uses a counter to keep track of how often an entry is accessed. With the LFU cache algorithm, the entry with the lowest count is removed first. This method isn't used that often, as it does not account for an item that had an initially high access rate and then was not accessed for a long time.

* Least Recently Used (LRU): 
puts recently accessed items near the top of the cache. When the cache reaches its limit, the least recently accessed items are removed.
This cache algorithm keeps recently used items near the top of cache. Whenever a new item is accessed, the LRU places it at the top of the cache. When the cache limit has been reached, items that have been accessed less recently will be removed starting from the bottom of the cache. This can be an expensive algorithm to use, as it needs to keep "age bits" that show exactly when the item was accessed. In addition, when a LRU cache algorithm deletes an item, the "age bit" changes on all the other items.

* Adaptive Replacement Cache (ARC): 
Developed at the IBM Almaden Research Center, this cache algorithm keeps track of both LFU and LRU, as well as evicted cache entries to get the best use out of the available cache.

* Most Recently Used (MRU): 
removes the most recently accessed items first. This approach is best when older items are more likely to be used.
This cache algorithm removes the most recently used items first. A MRU algorithm is good in situations in which the older an item is, the more likely it is to be accessed.

## Cache policies

Write-around cache writes operations to storage, skipping the cache altogether. This prevents the cache from being flooded when there are large amounts of write I/O. The disadvantage to this approach is that data isn't cached unless it's read from storage. That means the read operation will be relatively slow because the data hasn't been cached.

Write-through cache writes data to cache and storage. The advantage here is that because newly written data is always cached, it can be read quickly. A drawback is that write operations aren't considered complete until the data is written to both the cache and primary storage. This can cause write-through caching to introduce latency into write operations.

Caching benefits
Write-back cache is similar to write-through caching in that all the write operations are directed to the cache. However, with write-back cache, the write operation is considered complete after the data is cached. Later on, the data is copied from the cache to storage.

With this approach, both read and write operations have low latency. The downside is that, depending on what caching mechanism is used, the data remains vulnerable to loss until it's committed to storage.

## Cache invalidation problem

Cache invalidation can be used to push new content to a client. This method functions as an alternative to other methods of displaying new content to connected clients. Invalidation is carried out by changing the application data, which in turn marks the information received by the client as out-of-date. After the cache is invalidated, if the client requests the cache, they are delivered a new version.[1]
