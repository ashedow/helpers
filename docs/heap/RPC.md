# API Protocols

## SOAP
SOAP - Simple Object Access Protocol.

> SOAP is an example of a Remote Procedural Call, or RPC. 
> RPC is a broad category of approaches for allowing different computers to communicate with each other.

Some developers might take issue with the notion that SOAP is “simple,” because using a SOAP protocol requires a fair bit of work. You have to create XML documents to make calls, and the XML formatting that SOAP requires isn’t exactly intuitive. This not only makes call implementation difficult, but also makes problems hard to debug, because debugging requires parsing through long strings of complex data.

SOAP relies on standard protocols, especially HTTP and SMTP. That means that you can use SOAP in virtually every type of environment, because these protocols are available on all operating systems.

## RPC
RPC - remote procedure call
RPC-based APIs are great for actions (that is, procedures or commands).

RPC. We are sending a message, and that might end up storing something in the database to keep a history, which might be another RPC call with possibly the same field names — who knows?


## REST
REST - Representational State Transfer.
REST - частный случай JSON RPC

Like SOAP, REST relies on a standard transport protocol, HTTP, to exchange information between different applications or services. 

* REST must be stateless: not persisting sessions between requests.
* Responses should declare cacheablility: helps your API scale if clients respect the rules.
* REST focuses on uniformity: if you’re using HTTP you should utilize HTTP features whenever possible, instead of inventing conventions.

REST. We are creating a message resource in the user’s messages collection. We can see a history of these easily by doing a GET on the same URL, and the message will be sent in the background.


## JSON-RPC
While REST supports RPC data structures, it’s not the only API protocol in this category. If you like JSON, you may prefer instead to use JSON-RPC, a protocol introduced in the mid-2000s.

JSON-RPC supports a small set of commands, and does not offer as much flexibility as a protocol like REST with regard to exactly how you implement it. However, if you like simplicity and have a straightforward use case that falls with JSON-RPC’s scope, it can be a better solution than REST.

## gRPC
gRPC is an open source API that also falls within the category of RPC. 

Like REST and SOAP, gRPC uses HTTP as its transport layer. Unlike these other API protocols, however, gRPC allows developers to define any kind of function calls that they want, rather than having to choose from predefined options (like GET and PUT in the case of REST).

Another important advantage of gRPC, at least for many use cases, is that when you make a call to a remote system using gRPC, the call appears to both the sender and the receiver as if it were a local call, rather than a remote one executed over the network. This simulation avoids much of the coding complexity that you’d otherwise have to contend with in order for an application to handle a remote call.

The ability of gRPC to simplify otherwise complex remote calls has helped make it popular in the context of building APIs for microservices or Docker-based applications, which entail massive numbers of remote calls.

## GraphQL
In a way, GraphQL is to Facebook what gRPC is to Google: It’s an API protocol that was developed internally by Facebook in 2013, then released publicly in 2015. As such, GraphQL, which is officially defined as a query language, also represents an effort to overcome some of the limitations or inefficiencies of REST.

One of the key differences between REST and GraphQL is that GraphQL lets clients structure data however they want when issuing calls to a server. This flexibility improves efficiency because it means that clients can optimize the data they request, rather than having to request and receive data in whichever prepackaged form the server makes available (which could require receiving more data than the client actually needs, or receiving it in a format that is difficult to use). With GraphQL, the clients can get exactly what they want, without having to worry about transforming the data locally after they receive it.

## Apache Thrift
Like GraphQL, Apache Thrift was born at Facebook (it’s now an open source project hosted by the Apache Software Foundation), and functions essentially as an RPC framework. However, the design goals and target use cases for Thrift differ significantly from those of GraphQL.

Thrift’s main selling point is the ease with which it makes it possible to modify the protocol used by a service once the service has been defined. Combined with the facts that Thrift also supports an array of different transport methods and several different server-process implementations, this means that Thrift lends itself well to situations where you expect to need to modify or update your API architecture and implementation frequently. You might say that Thrift is great for avoiding “API architecture lock in” because it ensures that you can easily change your API architecture whenever you need to, instead of being forced to keep the same architecture because of API inflexibility.

On the other hand, some developers might contend that the choice that Thrift gives you when it comes time to implementing the API is not ideal because it leads to less consistency than you get with other API protocols that offer only one way of doing things. If you like rigid consistency and predictability, Thrift may not be the best choice for you.