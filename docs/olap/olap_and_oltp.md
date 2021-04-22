# OLAP

> [olap.com](olap.com)

OLAP (Online Analytical Processing) is the technology behind many Business Intelligence (BI) applications. OLAP is a technology for data discovery, including capabilities for limitless report viewing, complex analytical calculations, and predictive “what if” scenario (budget, forecast) planning.

## About

Unlike relational databases, OLAP tools do not store individual transaction records in two-dimensional, row-by-column format, like a worksheet, but instead use multidimensional database structures—known as Cubes in OLAP terminology—to store arrays of consolidated information. The data and formulas are stored in an optimized multidimensional database, while views of the data are created on demand.

## OLAP vs OLTP
Comparing characteristics of transaction processing versus analytic systems
| Property       | OLTP     | OLAP     |
| :------------- | :----------: | -----------: |
|  Main read pattern | Small number of records per query, fetched by key   | Aggregate over large number of records    |
| Main write pattern | Random-access, low-latency writes from user input   | Bulk import (ETL) or event stream    |
| Primarily used by  | End user/customer, via web application   | Internal analyst, for decision support    |
| What data represents  | Latest state of data (current point in time)   | History of events that happened over time   |
| Dataset size  | Gigabytes to terabytes   | Terabytes to petabytes  |

### ETL

ETL is a type of data integration process.
ETL - extract, transform, load:
 1. Data Extraction
    * Know and understand your data source — where you need to extract data
    * Audit your data source
    * Study your approach for optimal data extraction
    * Reconcile records with the source data
    * Make sure that no spam/unwanted data loaded
    * Data type check
    * Remove all types of duplicate/fragmented data
    * Check whether all the keys are in place or not
 2. Data Cleansing
    * Choose a suitable cleansing mechanism according to the extracted data
 3. Transformation
    * Filtering – Select only certain columns to load
    * Using rules and lookup tables for Data standardization
    * Character Set Conversion and encoding handling
    * Conversion of Units of Measurements like Date Time Conversion, currency conversions, numerical conversions, etc.
    * Data threshold validation check. For example, age cannot be more than two digits.
    * Data flow validation from the staging area to the intermediate tables.
    * Required fields should not be left blank.
    * Cleaning ( for example, mapping NULL to 0 or Gender Male to "M" and Female to "F" etc.)
    * Split a column into multiples and merging multiple columns into a single column.
    * Transposing rows and columns,
    * Use lookups to merge data
    * Using any complex data validation (e.g., if the first two columns in a row are empty then it automatically reject the row from processing)
 4. Load
    Types:
       * Initial Load — populating all the Data Warehouse tables
       * Incremental Load — applying ongoing changes as when needed periodically.
       * Full Refresh —erasing the contents of one or more tables and reloading with fresh data.

May be used between OLTP and OLAP

## ELT

## ELT vs ETL

|	параметры	|	ETL	|	ELT	|
================================================
|	Обработать	|	Данные преобразуются на промежуточном сервере и затем передаются в базу данных Datawarehouse.	|	Данные остаются в БД хранилища данных.	|
|	Использование кода	|	"Используется для
Вычислительные преобразования
Небольшое количество данных"	|	Используется для больших объемов данных	|
|	преобразование	|	Преобразования выполняются в сервере ETL / области подготовки.	|	Преобразования выполняются в целевой системе	|
|	Время-Load	|	Данные сначала загружаются в промежуточную, а затем загружаются в целевую систему. Время интенсивно.	|	Данные загружаются в целевую систему только один раз. Быстрее.	|
|	Время-трансформация	|	Процесс ETL должен ждать завершения преобразования. По мере увеличения размера данных время преобразования увеличивается.	|	В процессе ELT скорость никогда не зависит от размера данных.	|
|	Время обслуживания	|	Это требует высокого обслуживания, так как вам нужно выбрать данные для загрузки и преобразования.	|	Низкие эксплуатационные расходы, так как данные всегда доступны.	|
|	Сложность реализации	|	На ранней стадии проще реализовать.	|	Для реализации процесса ELT организация должна иметь глубокие знания инструментов и экспертных навыков.	|
|	Поддержка хранилища данных	|	Модель ETL, используемая для локальных, реляционных и структурированных данных.	|	Используется в масштабируемой облачной инфраструктуре, которая поддерживает структурированные, неструктурированные источники данных.	|
|	Поддержка озера данных	|	Не поддерживает.	|	Позволяет использовать озеро данных с неструктурированными данными.	|
|	сложность	|	Процесс ETL загружает только важные данные, определенные во время разработки.	|	Этот процесс включает в себя разработку из вывода в обратном направлении и загрузку только соответствующих данных.	|
|	Стоимость	|	Высокие затраты для малого и среднего бизнеса.	|	Низкие входные расходы при использовании онлайн-ПО в качестве сервисной платформы.	|
|	Lookups	|	В процессе ETL как факты, так и измерения должны быть доступны в области подготовки.	|	Все данные будут доступны, поскольку извлечение и загрузка выполняются одним действием.	|
|	Скопления	|	Сложность возрастает с дополнительным объемом данных в наборе данных.	|	Мощь целевой платформы позволяет быстро обрабатывать значительные объемы данных.	|
|	вычисления	|	Перезаписывает существующий столбец или Необходимо добавить набор данных и отправить на целевую платформу.	|	Легко добавить вычисляемый столбец в существующую таблицу.	|
|	зрелость	|	Процесс используется более двух десятилетий. Это хорошо документировано, и лучшие практики легко доступны.	|	Относительно новая концепция и комплекс для реализации.	|
|	аппаратные средства	|	Большинство инструментов имеют уникальные требования к оборудованию, которые стоят дорого.	|	Быть стоимостью оборудования Saas не проблема.	|
|	Поддержка неструктурированных данных	|	В основном поддерживает реляционные данные	|	Поддержка неструктурированных данных легко доступны.	|

## Types of OLAP

### HTAP

Hybrid Transaction / Analytical Processing (HTAP)

### MOLAP

Multidimensional OLAP (MOLAP) – Cube based

### ROLAP

Relational OLAP (ROLAP) –Star Schema based

### HOLAP

Hybrid OLAP (HOLAP)

### DOLAP

Desktop OLAP (DOLAP)

### WOLAP

Web OLAP (WOLAP)

### Mobile OLAP

### SOLAP

Spatial OLAP (SOLAP)


