
*DDL - Data Definition Language*
CREATE - Creates a new table, a view of a table, or other object in the database.
ALTER - Modifies an existing database object, such as a table.
DROP - Deletes an entire table, a view of a table or other objects in the database.

*DML - Data Manipulation Language*
SELECT - Retrieves certain records from one or more tables.
INSERT - Creates a record.
UPDATE - Modifies records.
DELETE - Deletes records.

*DCL - Data Control Language*
GRANT - Gives a privilege to user.
REVOKE - Takes back privileges granted from user.


*DBMS - Database Management System*
* a collection of computer program that is dedicated for the management (i.e. organization, storage and retrieval) of all databases that are installed in a system. Ex: Oracle, DB2 and Microsoft Access
* DBMS is the overall system which manages a certain database

*DataBase*
* Is designed to record	
* The database uses the Online Transactional Processing ([OLTP](/../olap/olap_and_oltp.md))
* Is an application-oriented collection of data	
* Generally limited to a single application
* Data is available real-time
* Capture data	
* Flat Relational Approach method is used for data storage.	

*Data Warehouse*
* a place that stores data for the purpose of archiving, reporting and analyzing. It can contain many different databases of an organization
* can be treated as a type of a database or a special kind of database, which provides special facilities for analysis, and reporting
* mainly store data for the purpose of reporting and analysis that would help an organization in the process making decisions
* needs to use a DBMS to make data organization and retrieval more efficient.
* Is designed to analyze
* Data warehouse uses Online Analytical Processing ([OLAP](/../olap/olap_and_oltp.md)).
* Table and joins are simple in a data warehouse because they are denormalized.
* It is a subject-oriented collection of data
* Stores data from any number of applications
* Data is refreshed from source systems as and when needed
* Analyze data
* Data Ware House uses dimensional and normalized approach for the data structure. Example: Star and snowflake schema.



COUNT - The SQL COUNT aggregate function is used to count the number of rows in a database table.
MAX- The SQL MAX aggregate function allows us to select the highest (maximum) value for a certain column.
MIN - The SQL MIN aggregate function allows us to select the lowest (minimum) value for a certain column.
AVG - The SQL AVG aggregate function selects the average value for certain table column.
SUM - The SQL SUM aggregate function allows selecting the total for a numeric column.
SQRT - This is used to generate a square root of a given number.
RAND - This is used to generate a random number using SQL command.
CONCAT - This is used to concatenate any string inside any SQL command.
Numeric - Complete list of SQL functions required to manipulate numbers in SQL.
String - Complete list of SQL functions required to manipulate strings in SQL.

function OVER widow
Окно — это некоторое выражение, описывающее набор строк, которые будет обрабатывать функция и порядок этой обработки.
истинные оконные функции из мануала — это row_number(), rank(), lead() и т.д., а можно использовать функции-агрегаты, такие как: sum(), count() и т.д. Так вот, это важно, агрегатные функции работают слегка по-другому: если не задан ORDER BY в окне, идет подсчет по всей партиции один раз, и результат пишется во все строки (одинаков для всех строк партиции). Если же ORDER BY задан, то подсчет в каждой строке идет от начала партиции до этой строки. Если же мы для агрегатной фунции sum не будем использовать ORDER BY в окне, тогда мы просто посчитаем общую сумму и покажем её во всех строках. Т.е. фреймом для каждой из строк будет весь набор строк


PARTITION BY позволяет сгруппировать строки по значению определённого столбца. Это полезно, если данные логически делятся на какие-то категории и нужно что-то сделать с данной строкой с учётом других строк той же группы (скажем, сравнить теннисиста с остальными теннисистами, но не с бегунами или пловцами). Этот оператор работает только с оконными функциями типа LAG, LEAD, RANK и т. д.
* ROW_NUMBER можно объединить с ORDER BY, чтобы определить, в каком порядке строки будут нумероваться. Выберем с помощью DISTINCT все имеющиеся виды спорта и пронумеруем их в алфавитном порядке.
* LAG - Функция LAG берёт строку и возвращает ту, которая шла перед ней.
* LEAD - Функция LEAD похожа на LAG, но вместо предыдущей строки возвращает следующую.
* RANK - Оператор RANK похож на ROW_NUMBER, но присваивает одинаковые номера строкам с одинаковыми значениями, а «лишние» номера пропускает. Есть также DENSE_RANK, который не пропускает номеров.



SQL подзапросы — или внутренние запросы, или вложенные запросы — это запрос внутри другого запроса SQL.
SELECT SUM(Quantity) AS Qty_Canada FROM Sumproduct WHERE City IN (SELECT City FROM Sellers WHERE Country = 'Canada')

***

Clustered and Nonclustered Index

> [Indexes](./indexes.md)

| A clustered index is a type of index where the table records are physically re-ordered to match the index. | A nonclustered index is a type of index that contains the references to the actual data. |

 Number of Indexes

| There can be one clustered index per table.                                                                | There can be many non-clustered indexes per table.                                       |

Speed

| The clustered index is faster than the Nonclustered Index.                                                 | The nonclustered index is slower than the clustered index.                               |

 Required Space

| The clustered index does not require an additional space.                                                  | The nonclustered index required an additional space.                                     |

**Clustered**
In a clustered index, the index organizes the actual data. It is similar to a phone directory.
The primary key is used to specify each entry in the table.


**Nonclustered**

***

Primary Key and Candidate Key

• A table without candidate keys does not represent any relation.
• There can be many candidate keys for a table in a database, but there should be only one primary key for a table.
• Although the primary key is one of the candidate keys, sometimes it is the only candidate key.
• Once a primary key was selected the other candidate keys become unique keys.
• Practically a candidate key can contain NULL values although it presently does not contain any value. Therefore, the candidate key is not qualified for a primary key because the primary key should not contain any NULL values.
• It may also be possible that candidate keys, which are unique at the moment,may contain duplicate values that disqualify a candidate key from becoming a primary key.


**Candidate key** 
Candidate key is a single column or set of columns in a table of a database that can be used to uniquely identify any database record without referring to any other data. Each table of a database can have one or more than one candidate keys. A set of candidate keys can be created by using functional dependencies. There are some important features in a candidate key. They are;

• candidate keys should be unique within the domain and they should not contain any NULL values.
• the candidate key should never change, and it must hold the same value for a specific occurrence of an entity.
• main purpose of a candidate key is to help to identify one single row out of millions of rows in a big table. Each candidate key is qualified to become a primary key.
• A candidate key is the column that qualifies as unique whereas primary key is the column that uniquely identifies a record.


**Primary Key**
* A primary key is the best candidate key of a table that is used to uniquely identify records that are stored in a table. 
* A primary key uniquely defines tuples in a relation
* Primary key value can never be NULL.
* No two tuples in a relation carry duplicate values for a primary key attribute.	
* There can be only one primary key of a relation.	
* Primary key constraint can be defined on the temporary tables.	
* By default, a primary key is clustered indexed.	
* We can insert a value to a primary key attribute, even if the referencing foreign key does not have that value in its column.	
* Before you delete a primary key value, make sure that value is not still present in the referencing foreign key column of referencing table.	

**FOREIGN KEY**
* Foreign key in a table refers to the primary key of other table.
* Foreign key accepts NULL value.
* Tuples can carry duplicate value for a foreign key attribute.
* There can be multiple foreign keys in a relation.
* Foreign Key constraint can not be defined on the temporary tables.
* Foreign key is not clustered indexed automatically; it has to be done manually.
* We can not insert a value to a foreign key, if that value is not present in the referenced primary key column.
* You can delete a value from foreign key column without bothering, whether that value is present in referenced primary key column of referenced relation.


***

SQL ALIASES can be used to create a temporary name for columns or tables.

COLUMN ALIASES are used to make column headings in your result set easier to read.
TABLE ALIASES are used to shorten your SQL to make it easier to read or when you are performing a self join (ie: listing the same table more than once in the FROM clause).


If the alias_name contains spaces, you must enclose the alias_name in quotes.
It is acceptable to use spaces when you are aliasing a column name. However, it is not generally good practice to use spaces when you are aliasing a table name.
The alias_name is only valid within the scope of the SQL statement.

***

SELECT department, SUM(sales) AS "Total sales"
FROM order_details
GROUP BY department
HAVING SUM(sales) > 1000;

***

-- CAST Syntax:  
CAST ( expression AS data_type [ ( length ) ] )  
  
-- CONVERT Syntax:  
CONVERT ( data_type [ ( length ) ] , expression [ , style ] )  

***

The CAST() function converts a value (of any type) into a specified datatype.

***

Difference between JOIN and UNION in SQL

**JOIN**
JOIN combines data from many tables based on a matched condition between them.
It combines data into new columns
Number of columns selected from each table may not be same.
Datatypes of corresponding columns selected from each table can be different.
It may not return distinct columns.

**UNION**
SQL combines the result-set of two or more SELECT statements.
It combines data into new rows
Number of columns selected from each table should be same.
Datatypes of corresponding columns selected from each table should be same.
It returns distinct rows.

***

UNION removes duplicate rows.
UNION ALL does not remove duplicate rows.

***

- SQL INNER JOIN (sometimes called simple join) The SQL INNER JOIN would return the records where table1 and table2 intersect.
FROM customers INNER JOIN orders My be replased with FROM customers, orders

- SQL EQUI JOIN
Syntax:
SELECT column_list  FROM table1, table2.... WHERE table1.column_name = table2.column_name; 
or
SELECT * FROM table1 JOIN table2 [ON (join_condition)]

An equijoin is a join with a join condition containing an equality operator. An equijoin returns only the rows that have equivalent values for the specified columns.

An inner join is a join of two or more tables that returns only those rows (compared using a comparison operator) that satisfy the join condition.

- SQL NON EQUI JOIN uses comparison operator instead of the equal sign like >, <, >=, <= along with conditions.

- SQL NATURAL JOIN is a type of EQUI JOIN and is structured in such a way that, columns with the same name of associated tables will appear once only.

Natural Join: 
    * The associated tables have one or more pairs of identically named columns.
    * The columns must be the same data type.
    * Don’t use ON clause in a natural join.

Syntax:
`SELECT * FROM table1 NATURAL JOIN table2;`
To get all the unique columns from foods and company tables, the following SQL statement can be used: `SELECT * FROM foods NATURAL JOIN company;` INNER JOIN will return all columns from foods and company tables

- SQL CROSS JOIN produces a result set which is the number of rows in the first table multiplied by the number of rows in the second table if no WHERE clause is used along with CROSS JOIN.This kind of result is called as Cartesian Product.

If WHERE clause is used with CROSS JOIN, it functions like an INNER JOIN.

![](cross-join-example.png)

- SQL OUTER JOIN returns all rows from both the participating tables which satisfy the join condition along with rows which do not satisfy the join condition. The SQL OUTER JOIN operator (+) is used only on one side of the join condition only.

The subtypes of SQL OUTER JOIN
    * LEFT OUTER JOIN or LEFT JOIN
    * RIGHT OUTER JOIN or RIGHT JOIN
    * FULL OUTER JOIN

Syntax: `Select * FROM table1, table2 WHERE conditions [+];`

This SQL statement would return all rows from the company table and only those rows from the foods table where the joined fields are equal.

The (+) after the foods.company_id field indicates that, if a company_id value in the company table does not exist in the foods table, all fields in the foods table will be displayed as NULL in the result set.

- SQL LEFT OUTER JOIN (sometimes called LEFT JOIN)

- SQL RIGHT OUTER JOIN (sometimes called RIGHT JOIN)

- SQL FULL OUTER JOIN (sometimes called FULL JOIN)

- SQL SELF JOIN is a join in which a table is joined with itself (which is also called Unary relationships), especially when the table has a FOREIGN KEY which references its own PRIMARY KEY. To join a table itself means that each row of the table is combined with itself and with every other row of the table.

The self join can be viewed as a join of two copies of the same table. The table is not actually copied, but SQL performs the command as though it were.

The syntax of the command for joining a table to itself is almost same as that for joining two different tables. To distinguish the column names from one another, aliases for the actual the table name are used, since both the tables have the same name. Table name aliases are defined in the FROM clause of the SELECT statement. See the syntax :
`SELECT a.column_name, b.column_name... FROM table1 a, table1 b WHERE a.common_filed = b common_field;`

***

CROSS APPLY
CROSS APPLY is similar to INNER JOIN, but can also be used to join table-evaluated functions with SQL Tables. CROSS APPLY’s final output consists of records matching between the output of a table-evaluated function and an SQL Table.

OUTER APPLY
OUTER APPLY resembles LEFT JOIN, but has an ability to join table-evaluated functions with SQL Tables. OUTER APPLY’s final output contains all records from the left-side table or table-evaluated function, even if they don’t match with the records in the right-side table or table-valued function.

Now, let me explain both variations with examples.



***

MINUS for Oracle EXCEPT for others

***

SELECT TOP statement for SQL Server and MSAccess. For other SQL databases, try the SELECT LIMIT statement.

***

The SQL INTERSECT operator is used to return the results of 2 or more SELECT statements. However, it only returns the rows selected by all queries or data sets. If a record exists in one query and not in the other, it will be omitted from the INTERSECT results.

SELECT expression1, expression2, ... expression_n
FROM tables
[WHERE conditions]
INTERSECT
SELECT expression1, expression2, ... expression_n
FROM tables
[WHERE conditions];

return like INNER JOIN

***

DELETE FROM table_name can be roll back, TRUNCATE TABLE table_name or DROP - not

DELETE Statement: This command deletes only the rows from the table based on the condition given in the where clause or deletes all the rows from the table if no condition is specified. But it does not free the space containing the table.

TRUNCATE statement: This command is used to delete all the rows from the table and free the space containing the table.

Difference between DROP and TRUNCATE Statement:
If a table is dropped, all the relationships with other tables will no longer be valid, the integrity constraints will be dropped, grant or access privileges on the table will also be dropped, if you want use the table again it has to be recreated with the integrity constraints, access privileges and the relationships with other tables should be established again. But, if a table is truncated, the table structure remains the same, therefore any of the above problems will not exist.

***

LIKE  _ wilcard matches only on a single character.

***

WHERE test_value LIKE '%!%%' escape '!'; - ! is shielding symbol

***

If we wanted to find all records containing the word "test", regardless of whether it was stored as TEST, Test, or test, we could run either of the following SQL SELECT statements:

SELECT *
FROM suppliers
WHERE UPPER(supplier_name) LIKE ('TEST%');
OR

SELECT *
FROM suppliers
WHERE UPPER(supplier_name) LIKE UPPER('test%')
These SQL SELECT statements use a combination of the Oracle UPPER function and the SQL LIKE condition to return all of the records where the supplier_name field contains the word "test", regardless of whether it was stored as TEST, Test, or test.

***

The SQL MINUS operator is used to return all rows in the first SELECT statement that are not returned by the second SELECT statement. Each SELECT statement will define a dataset. The MINUS operator will retrieve all records from the first dataset and then remove from the results all records from the second dataset.

***

UPDATE table1, table2, ...
SET column1 = expression1,
    column2 = expression2,
    ...
WHERE table1.column = table2.column
[AND conditions];

***

The SQL WHERE clause is used to filter the results and apply conditions in a SELECT, INSERT, UPDATE, or DELETE statement.

***

SELECT dept_id, SUM(salary) AS total_salaries
FROM employees
GROUP BY dept_id;

SELECT category_id, COUNT(*) AS total_products
FROM products
WHERE category_id IS NOT NULL
GROUP BY category_id
ORDER BY category_id;

return sums

category_id	total_products
25	1
50	4
75	1

In this example, we've used the COUNT function to calculate the number of products for each category_id and we've aliased the results of the COUNT function as total_products. We've excluded any category_id values that are NULL by filtering them out in the WHERE clause. Because the category_id is not encapsulated in the COUNT function, it must be listed in the GROUP BY clause.

***

The SQL ALTER TABLE statement is used to add, modify, or drop/delete columns in a table. The SQL ALTER TABLE statement is also used to rename a table.


For SQL Server:

ALTER TABLE supplier
  ALTER COLUMN supplier_name VARCHAR(100) NOT NULL;
For PostgreSQL:

ALTER TABLE supplier
  ALTER COLUMN supplier_name TYPE CHAR(100),
  ALTER COLUMN supplier_name SET NOT NULL;


For MySQL and MariaDB:

ALTER TABLE table_name
  MODIFY column_1 column_definition
    [ FIRST | AFTER column_name ],
  MODIFY column_2 column_definition
    [ FIRST | AFTER column_name ],
  ...
;
For PostgreSQL:

ALTER TABLE table_name
  ALTER COLUMN column_name TYPE column_definition,
  ALTER COLUMN column_name TYPE column_definition,
  ...
;

ALTER TABLE table_name
  DROP COLUMN column_name;

ALTER TABLE table_name
  RENAME COLUMN old_name TO new_name;
For SQL Server (using the stored procedure called sp_rename):

sp_rename 'table_name.old_column', 'new_name', 'COLUMN';
For MySQL and MariaDB:

ALTER TABLE table_name
  CHANGE COLUMN old_name TO new_name;

***

CONSTRAINT can be specified when the table is created with the CREATE TABLE statement, or after the table is created with the ALTER TABLE statement.

The following constraints are commonly used in SQL:

NOT NULL - Ensures that a column cannot have a NULL value
UNIQUE - Ensures that all values in a column are different
PRIMARY KEY - A combination of a NOT NULL and UNIQUE. Uniquely identifies each row in a table
FOREIGN KEY - Prevents actions that would destroy links between tables
CHECK - Ensures that the values in a column satisfies a specific condition
DEFAULT - Sets a default value for a column if no value is specified
CREATE INDEX - Used to create and retrieve data from the database very quickly

***

-- comment goes here

/* comment goes here */

***

Local
- Only available to the current Db connection for current user and are cleared when connection is closed.
- Multiple users can’t share a local temporary table.

Global
- Available to any connection once created. They are cleared when the last connection is closed.
- Can be shared by multiple user sessions.

***

The syntax for the CREATE TABLE AS statement when copying all of the columns in SQL is:

CREATE TABLE new_table
  AS (SELECT * FROM old_table);

***


SQL GLOBAL TEMPORARY TABLES are tables that are created distinct within SQL sessions.

CREATE GLOBAL TEMPORARY TABLE table_name
( column1 datatype [ NULL | NOT NULL ],
  column2 datatype [ NULL | NOT NULL ],
  ...
);

***

SQL LOCAL TEMPORARY TABLES are distinct within modules and embedded SQL programs within SQL sessions.

***

The SQL VIEW is, in essence, a virtual table that does not physically exist. Rather, it is created by a SQL statement that joins one or more tables.

CREATE VIEW view_name AS
  SELECT columns
  FROM tables
  [WHERE conditions];

Once a SQL VIEW has been created, you can drop it with the SQL DROP VIEW Statement.

DROP VIEW view_name;

 A VIEW in SQL is created by joining one or more tables. When you update record(s) in a view, it updates the records in the underlying tables that make up the SQL View.

So, yes, you can update the data in a SQL VIEW providing you have the proper privileges to the underlying SQL tables.

Yes, in Oracle, the SQL VIEW continues to exist even after one of the tables (that the SQL VIEW is based on) is dropped from the database. However, if you try to query the SQL VIEW after the table has been dropped, you will receive a message indicating that the SQL VIEW has errors.

If you recreate the table (the table that you had dropped), the SQL VIEW will again be fine.

***

An index is a performance-tuning method of allowing faster retrieval of records. An index creates an entry for each value that appears in the indexed columns. Each index name must be unique in the database.

CREATE [UNIQUE] INDEX index_name
  ON table_name (column1, column2, ... column_n);

You can drop an index in SQL using the DROP INDEX index_name statement.

For Oracle and PostgreSQL:

DROP INDEX index_name;
For MySQL and MariaDB:

DROP INDEX index_name
  ON table_name;
For SQL Server:

DROP INDEX table_name.index_name;

***

In SQL, a literal is the same as a constant. We'll cover several types of literals - string, integer, decimal, and datetime literals.


***

we can use CASE in WHERE statements

***

we can print SELECT 'this string will be just printet'

***

In SQL, a primary key is a single field or combination of fields that uniquely defines a record. None of the fields that are part of the primary key can contain a NULL value. A table can have only one primary key.

You use either the CREATE TABLE statement or the ALTER TABLE statement to create a primary key in SQL.

DROP, CREATE, ALTER the same

***

WITH clause is not supported by all database system.
WITH clause was introduced by Oracle in the Oracle 9i release 2 database.
SQL WITH clause allows you to give a sub-query block a name (a process also called sub-query refactoring), which can be referenced in several places within the main SQL query. 

***
[OBT](README.md) определяется с помощью конструкции WITH, и определить его можно как в обычных запросах, так и в функциях, хранимых процедурах, триггерах и представлениях.

The `WITH` clause is, simply put, an optional prefix for `SELECT`
`WITH` is not a stand alone command like `CREATE VIEW`: it must be followed by `SELECT`. This query (and subqueries it contains) can refer to the just defined query name in their from clause.

Most databases process `WITH`-queries in the same way that they process `VIEW`: they replace the reference to the query by its definition and optimize the overall query.

The PostgreSQL database was different until version 12: it optimized each `WITH` query and the main statement independent of each other.

If a `WITH` query is referred to multiple times, some databases cache (i.e. “materialize”) its result to prevent double execution.

```sql
 WITH  [ ( column_name [ ,...n ] ) ]
    AS
     ( CTE_query_definition )

<...>

 WITH TestCTE (UserID, Post, ManagerID)
        AS
        (
                SELECT UserID, Post, ManagerID FROM TestTable 
        )
   SELECT * FROM TestCTE
```
* `common_table_expression_name` – это псевдоним или можно сказать идентификатор обобщенного табличного выражения. Обращаться к OTB мы будем, как раз используя этот псевдоним;
* `column_name` – имя столбца, который будет определен в обобщенном табличном выражении. Использование повторяющихся имен нельзя, а также их количество должно совпадать с количеством столбцов возвращаемых запросом `CTE_query_definition`. Указывать имена столбцов необязательно, но только в том случае, если всем столбцам в запросе `CTE_query_definition` присвоены уникальные псевдонимы;
* `CTE_query_definition` — запрос `SELECT`, к результирующему набору которого, мы и будем обращаться через обобщенное табличное выражение, т.е. `common_table_expression_name`.

После обобщенного табличного выражения, т.е. сразу за ним должен идти одиночный запрос `SELECT`, `INSERT`, `UPDATE`, `MERGE` или `DELETE`.

***

A transaction is NOT automatically created when you run an executable SQL statement in SQL Server.

Manually create a new transaction using the BEGIN TRAN or BEGIN TRANSACTION statement (TRAN eq to TRANSACTION)

[Transactions](README.md#Concurrency Control ##Transaction)

```sql
SET TRANSACTION ISOLATION LEVEL
    { READ UNCOMMITTED
    | READ COMMITTED
    | REPEATABLE READ
    | SNAPSHOT # For MSQL server
    | SERIALIZABLE
    }
```

Set transaction name
```sql
BEGIN TRANSACTION update_balance;
UPDATE account SET balance = balance - 100 WHERE account_id = 1;
UPDATE account SET balance = balance + 100 WHERE account_id = 2;
```

To commit a transaction in SQL Server, simply run the COMMIT command:
```sql
BEGIN TRANSACTION;
UPDATE account SET balance = balance - 100 WHERE account_id = 1;
UPDATE account SET balance = balance + 100 WHERE account_id = 2;
COMMIT;
```
The changes made as part of the transaction are permanently saved to the database.


To roll back a transaction in SQL Server, simply run the ROLLBACK command:
```sql
BEGIN TRANSACTION;
UPDATE account SET balance = balance - 100 WHERE account_id = 1;
UPDATE account SET balance = balance + 100 WHERE account_id = 2;
ROLLBACK;
```
The changes from these statements are not saved to the database after the ROLLBACK command is run.

A savepoint can be created with the SAVE TRANSACTION command:
```sql
BEGIN TRANSACTION;
UPDATE account SET balance = balance - 100 WHERE account_id = 1;
UPDATE account SET balance = balance + 100 WHERE account_id = 2;
SAVE TRANSACTION after_bal_transfer;
```
SQL commands can be run after the SAVE TRANSACTION command. The transaction can then be rolled back to the savepoint if needed, and the statements before the savepoint are not lost.
```sql
ROLLBACK TO SAVEPOINT after_bal_transfer;
```


***

## Optimizer Hints Oracle

### Type of Hints
Hints falls into the following general classifications:

**Single-table**

Single-table hints are specified on one table or view. INDEX and USE_NL are examples of single-table hints.

**Multi-table**

Multi-table hints are like single-table hints, except that the hint can specify one or more tables or views. LEADING is an example of a multi-table hint. Note that USE_NL(table1 table2) is not considered a multi-table hint because it is actually a shortcut for USE_NL(table1) and USE_NL(table2).

**Query block**

Query block hints operate on single query blocks. STAR_TRANSFORMATION and UNNEST are examples of query block hints.

**Statement**

Statement hints apply to the entire SQL statement. ALL_ROWS is an example of a statement hint.



***