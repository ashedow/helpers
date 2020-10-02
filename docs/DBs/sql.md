
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
ROW_NUMBER можно объединить с ORDER BY, чтобы определить, в каком порядке строки будут нумероваться. Выберем с помощью DISTINCT все имеющиеся виды спорта и пронумеруем их в алфавитном порядке.
LAG - Функция LAG берёт строку и возвращает ту, которая шла перед ней.
LEAD - Функция LEAD похожа на LAG, но вместо предыдущей строки возвращает следующую.
RANK - Оператор RANK похож на ROW_NUMBER, но присваивает одинаковые номера строкам с одинаковыми значениями, а «лишние» номера пропускает. Есть также DENSE_RANK, который не пропускает номеров.