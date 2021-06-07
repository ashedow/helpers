# Warehouse

The data warehouse
> A data warehouse is a copy of transaction data specifically structured for query and analysis. — Ralph Kimball

> A data warehouse is a subject-oriented, integrated, time-variant and non-volatile collection of data in support of management’s decision making process. — Bill Inmon


The data warehouse is just as relevant as it ever was, and data engineers are in charge of many aspects of its construction and operation.

Generally a data warehouses adopts three-tier architecture. Following are the three tiers of the data warehouse architecture.

* Bottom Tier - The bottom tier of the architecture is the data warehouse database server. It is the relational database system. We use the back end tools and utilities to feed data into the bottom tier. These back end tools and utilities perform the Extract, Clean, Load, and refresh functions.
* Middle Tier - In the middle tier, we have the OLAP Server that can be implemented in either of the following ways.
    * By Relational OLAP (ROLAP), which is an extended relational database management system. The ROLAP maps the operations on multidimensional data to standard relational operations.
    * By Multidimensional OLAP (MOLAP) model, which directly implements the multidimensional data and operations.
* Top-Tier - This tier is the front-end client layer. This layer holds the query tools and reporting tools, analysis tools and data mining tools.

![](download.png)

## Data Warehouse Design Techniques – Conformed Dimensions


## Data Warehouse Design Techniques – Slowly Changing Dimensions

> **Slowly Changing Dimensions (SCD)** are the most commonly used advanced dimensional technique used in dimensional data warehouses. 

Slowly changing dimensions are **used** when you wish to **capture the changing data** within the **dimension over time**. There are three methodologies for slowly changing dimensions.

* **Type 0** - The passive method
* **Type 1** - Overwriting the old value
* **Type 2** - Creating a new additional record
* **Type 3** - Adding a new column
* **Type 4** - Using historical table
* **Type 6** - Combine approaches of types 1,2,3 (1+2+3=6)
* **Type 0** - The passive method. In this method no special action is performed upon dimensional changes. Some dimension data can remain the same as it was first time inserted, others may be overwritten.

### Type 1

**Overwriting the old value.**

In this method no history of dimension changes is kept in the database. The old dimension value is simply overwritten be the new one. This type is easy to maintain and is often use for data which changes are caused by processing corrections(e.g. removal special characters, correcting spelling errors).

### Type 2

**Creating a new additional record.**

In this methodology all history of dimension changes is kept in the database. You capture attribute change by adding a new row with a new surrogate key to the dimension table. Both the prior and new rows contain as attributes the natural key(or other durable identifier). Also 'effective date' and 'current indicator' columns are used in this method. There could be only one record with current indicator set to 'Y'. For 'effective date' columns, i.e. `start_date` and `end_date`, the `end_date` for current record usually is set to value 9999-12-31. Introducing changes to the dimensional model in type 2 could be very expensive database operation so it is not recommended to use it in dimensions where a new attribute could be added in the future.

### Type 3

**Adding a new column.**

In this type usually only the current and previous value of dimension is kept in the database. The new value is loaded into 'current/new' column and the old one into 'old/previous' column. Generally speaking the history is limited to the number of column created for storing historical data. This is the least commonly needed technique.

### Type 4

**Using historical table.**

In this method a separate historical table is used to track all dimension's attribute historical changes for each of the dimension. The 'main' dimension table keeps only the current data e.g. customer and customer_history tables.

**Type 6**

Combine approaches of types 1,2,3 (1+2+3=6). In this type we have in dimension table such additional columns as:

* `current_type` - for keeping current value of the attribute. All history records for given item of attribute have the same current value.
* `historical_type` - for keeping historical value of the attribute. All history records for given item of attribute could have different values.
* `start_date` - for keeping start date of 'effective date' of attribute's history.
* `end_date` - for keeping end date of 'effective date' of attribute's history.
* `current_flag` - for keeping information about the most recent record.

In this method to capture attribute change we add a new record as in type 2. The `current_type` information is overwritten with the new one as in type 1. We store the history in a `historical_column` as in type 3.

## Data Warehouse Design Techniques – Rapidly Changing Dimensions



## Links

> nuwavesolutions.com