# document-oriented database

A document database is a NoSQL data stores that is designed to store and query data as JSON-like documents. The data in document databases is stored as documents with their metadata. The document stored is in key/value pair where the key is the unique identifier of the document. Unlike relational databases, document databases are faster to load, access, and parse.
 
Document database are also referred as document database management systems, document-oriented databases, or document store database.
 
Here are the key characteristics of document databases:
* Document DBMSs are NoSQL databases.
* Document DBMSs use key/value to store and access documents data.
* Document DBMSs have a flexible schema that can be different for each document. For example, one document can be an Author profile, while other document can be a blog.
* Common examples of document DBMS include JSON, XML docs, Catalogs, serialized PDFs and Excel docs, Profile data, and serialized objects.

## When to use document databases
 
Traditional relational DBMSs are not designed to provide efficient access to large documents or unstructured data. In case of catalogs, or profiles, or document storages, we don’t need structured design. For example, storing a document in a CMS does not require a structured format.
 
Document databases are designed to store large documents in a key/value store that are easy to search and access. The entire document is read into a memory object that is easy to read and present.
 
User profiles, content management systems, and catalogs are some common use case of document DBMS. One of the perfect example of use of a document database is storing C# Corner articles in a document DB, rather than a DRBMS.
 