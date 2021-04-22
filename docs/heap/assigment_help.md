# Assessment

Help information/crib for assessment

Abbreviations:

Basic - ★
Advanced - ★★
Expert - ★★★

# General CS

* Какая сортировка требует O(n) памяти? 
Никакая, потому что если мы используем сортировку слиянием, то используем рекурсию, а рекурсия использует блоки памяти.

## Types

* Hash table and hash function

## Object-Oriented Design

* Назовите основные постулаты ООП.
    * Абстракция - абстракция. Общее от частного. Разделение. Выявление характеристик.
    * Инкапсуляция - создание интерфейса для черного ящика. Приватные и публичные методы. 
    * Полиморфизм - один интерфейс, множество методов. Использование одного имени для задания общих для класса действий. Стандартизация интерфейса.
    * Наследование - процесс, посредством которого один объект может приобретать свойства другого. Объект может наследовать основные свойства другого объекта и добавлять к ним свои методы. Классы. 
            * Множественное наследование - более одного предка. Наследует все методы предков. 
    Links:
        * [SOLID, GRASP, and Other Basic Principles of Object-Oriented Design](https://dzone.com/articles/solid-grasp-and-other-basic-principles-of-object-o)

* SOLID
    Single responsibility, Open-closed, Liskov substitution, Interface segregation и Dependency inversion. Используются вместе. 
    * SRP Принцип единственной ответственности (The Single Responsibility Principle) Существует лишь одна причина, приводящая к изменению класса. Если больше одной, то следует разбить данный класс. 
    * OCP Принцип открытости/закрытости (The Open Closed Principle) «программные сущности … должны быть открыты для расширения, но закрыты для модификации.»
    * LSP Принцип подстановки Барбары Лисков (The Liskov Substitution Principle). 
        * Наследующий класс должен дополнять, а не замещать поведение базового класса.
        * Исполнение контрактов
            * Предусловия (то, что обязано быть истинным для выполнения подпрограммы) не могут быть усилены в подклассе.
            * Постусловия (условия, которые гарантируются самой подпрограммой. Кроме того, наличие постусловия в подпрограмме гарантирует ее завершение) не могут быть ослаблены в подклассе.
    * ISP Принцип разделения интерфейса (The Interface Segregation Principle)
        * Много специализированных интерфейсов лучше, чем один универсальный.
    * DIP Принцип инверсии зависимостей (The Dependency Inversion Principle)
        * Модули верхних уровней не должны зависеть от модулей нижних уровней. Оба типа модулей должны зависеть от абстракций. Модуль - логически взаимосвязанная совокупность функциональных элементов
        * Абстракции не должны зависеть от деталей. Детали должны зависеть от абстракций.

* GRASP
General Responsibility Assignment Software Patterns
    * Controller - The controller pattern assigns the responsibility of dealing with system events to a non-UI class that represents the overall system or a use case scenario. A controller object is a non-user interface object responsible for receiving or handling a system event.
    * Creator - Creation of objects is one of the most common activities in an object-oriented system. Which class is responsible for creating objects is a fundamental property of the relationship between objects of particular classes.
    * Indirection - The indirection pattern supports low coupling and reuse potential between two elements by assigning the responsibility of mediation between them to an intermediate object. An example of this is the introduction of a controller component for mediation between data (model) and its representation (view) in the model-view control pattern. This ensures that coupling between them remains low.
    * Information expert - Information expert (also expert or the expert principle) is a principle used to determine where to delegate responsibilities such as methods, computed fields, and so on. Using the principle of information expert, a general approach to assigning responsibilities is to look at a given responsibility, determine the information needed to fulfill it, and then determine where that information is stored.
    * High cohesion - High cohesion is an evaluative pattern that attempts to keep objects appropriately focused, manageable and understandable. High cohesion is generally used in support of low coupling. 
    * Low coupling - Coupling is a measure of how strongly one element is connected to, has knowledge of, or relies on other elements. Low coupling is an evaluative pattern that dictates how to assign responsibilities to support
    * Polymorphism - According to the polymorphism principle, responsibility for defining the variation of behaviors based on type is assigned to the type for which this variation happens. This is achieved using polymorphic operations. The user of the type should use polymorphic operations instead of explicit branching based on type.
    * Protected variations - The protected variations pattern protects elements from the variations on other elements (objects, systems, subsystems) by wrapping the focus of instability with an interface and using polymorphism to create various implementations of this interface.
    * Pure fabrication - A pure fabrication is a class that does not represent a concept in the problem domain, specially made up to achieve low coupling, high cohesion, and the reuse potential thereof derived (when a solution presented by the information expert pattern does not). 

* KISS
*Keep it simple, stupid*

* What is Dependency injection
    Концепция Inversion of Control Container IoC 
    * Inversion of Control (инверсия управления) это принцип объектно-ориентированного программирования, при котором объекты программы не зависят от конкретных реализаций других объектов, но могут иметь знание об их абстракциях (интерфейсах) для последующего взаимодействия.
    * Dependency Injection (внедрение зависимостей) - процесс предоставления внешней зависимости. Композиция структурных шаблонов проектирования, при которой за каждую функцию приложения отвечает один, условно независимый объект (сервис), который может иметь необходимость использовать другие объекты (зависимости), известные ему интерфейсами. Зависимости передаются (внедряются) сервису в момент его создания.
    
* Design Patterns
    Паттерны или шаблоны - архитектурная конструкция. 23 классических от банды 4 ( Эрих Гамма, Ричард Хелм, Ральф Джонсон, Джон Влиссидес). Состоит из:
        * проблемы, которую решает паттерн;
        * мотивации к решению проблемы способом, который предлагает паттерн;
        * структуры классов, составляющих решение;
        * описания особенностей реализации в различных контекстах;
        * связи с другими паттернами.
    Отношения между классами: 
    * агрегация (aggregation) — описывает связь «часть»–«целое», в котором «часть» может существовать отдельно от «целого».
    * композиция (composition) — подвид агрегации, в которой «части» не могут существовать отдельно от «целого».
    * зависимость (dependency) — изменение в одной сущности (независимой) может влиять на состояние или поведение другой сущности (зависимой).
    * обобщение (generalization) — отношение наследования или реализации интерфейса.
    Типы и виды паттернов:
        * Creational Пораждающие. Отвечают за удобное и безопасное создание новых объектов или даже целых семейств объектов.
            * Factory Method Фабричный метод — определяет общий интерфейс для создания объектов в суперклассе, позволяя подклассам изменять тип создаваемых объектов.
            * Abstract Factory - позволяет создавать семейства связанных объектов, не привязываясь к конкретным классам создаваемых объектов. общие интерфейсы.
            * Builder — позволяет создавать сложные объекты пошагово. Строитель даёт возможность использовать один и тот же код строительства для получения разных представлений объектов. Вынести конструирование объекта за пределы его собственного класса, поручив это дело отдельным объектам, называемым строителями. Выделить вызовы методов строителя в отдельный класс, называемый «Директором».
            * Prototype - позволяет копировать объекты, не вдаваясь в подробности их реализации (не привязываясь к их конкретным классам)
            * Singleton - гарантирует, что у класса есть только один экземпляр, и предоставляет к нему глобальную точку доступа. (нарушает SRP)
        * Structural Структурные. Отвечают за построение удобных в поддержке иерархий классов.
            * Adapter - позволяет объектам с несовместимыми интерфейсами работать вместе. Адаптер следует интерфейсу, который один объект ожидает от другого. Когда первый объект вызывает методы адаптера, адаптер передаёт выполнение второму объекту, вызывая в нём те или иные методы в том порядке, который важен для второго объекта.
            * Bridge - разделяет один или несколько классов на две отдельные иерархии — абстракцию и реализацию, позволяя изменять их независимо друг от друга. Заменить наследование делегированием. Для этого нужно выделить одну из таких «плоскостей» в отдельную иерархию и ссылаться на объект этой иерархии, вместо хранения его состояния и поведения внутри одного класса.«Абстракция» (или «интерфейс») — это образный слой управления чем-либо. Он не делает работу самостоятельно, а делегирует её слою «реализации» (иногда называемому «платформой»).
            * Composite - позволяет сгруппировать объекты в древовидную структуру, а затем работать с ними так, если бы это был единичный объект. 
            * Decorator - позволяет динамически добавлять объектам новую функциональность, оборачивая их в полезные «обёртки». один объект содержит другой, вместо того, чтобы наследовать его. Оба объекта имеют общий интерфейс, поэтому для пользователя нет никакой разницы с чем работать — с чистым объектом или обёрнутым
            * Facade - предоставляет простой интерфейс к сложной системе классов, библиотеке или фреймворку. 
            * Flyweight - позволяет вместить бóльшее количество объектов в отведённую оперативной память за счёт экономного разделения общего состояния объектов между собой, вместо хранения одинаковых данных в каждом объекте. предлагает не хранить в классе внешнее состояние, а передавать его в те или иные методы через параметры.
            * Proxy - позволяет подставлять вместо реальных объектов специальные объекты-заменители. Эти объекты перехватывают вызовы к оригинальному объекту, позволяя сделать что-то до или после передачи вызова оригиналу. предлагает создать новый класс-дублёр, имеющий тот же интерфейс, что и оригинальный служебный объект. При получении запроса от клиента, объект-заместитель сам бы создавал экземпляр служебного объекта и переадресовывал бы ему всю реальную работу.
        * Behavioral Поведенческие. Решают задачи эффективного и безопасного взаимодействия между объектами программы.
            * CoR, Chain of Command, Chain of Responsibility - позволяет передавать запросы последовательно по цепочке обработчиков. Каждый последующий обработчик решает, может ли он обработать запрос сам и стоит ли передавать запрос дальше по цепи.
            * Command - превращает запросы в объекты, позволяя передавать их как аргументы при вызове методов, ставить запросы в очередь, логировать их, а также поддерживать отмену операций. Поддержка отмены
            * Iterator - даёт возможность последовательно обходить элементы составных объектов, не раскрывая их внутреннего представления.
            * Intermediary, Controller, Mediator - позволяет уменьшить связанность множества классов между собой, благодаря перемещению этих связей в один класс-посредник.
            * Memento - позволяет делать снимки состояния объектов, не раскрывая подробностей их реализации. Затем снимки можно использовать, чтобы восстановить прошлое состояние объектов.
            * Observer - создаёт механизм подписки, позволяющий одним объектам следить и реагировать на события, происходящие в других объектах.
            * State - позволяет объектам менять поведение в зависимости от своего состояния. Извне создаётся впечатление, что изменился класс объекта.предлагает создать отдельные классы для каждого состояния, в котором может пребывать контекстный объект, а затем вынести туда поведения, соответствующие этим состоянию. Вместо того чтобы хранить код всех состояний, первоначальный объект (называемый «контекстом») будет содержать ссылку на один из объектов-состояний и делегировать ему работу, зависящую от состояния
            * Strategy - определяет семейство схожих алгоритмов и помещает каждый из них в собственный класс. После чего, алгоритмы можно взаимозаменять прямо во время исполнения программы. Вместо того чтобы изначальный класс сам выполнял тот или иной алгоритм, он будет отыгрывать роль контекста, ссылаясь на одну из стратегий и делегируя ей выполнение работы. А для смены алгоритма будет достаточно подставить в контекст другой объект-стратегию.Общий интерфейс
            * Template Method - определяет скелет алгоритма, перекладывая ответственность за некоторые его шаги на подклассы. Паттерн позволяет подклассам переопределять шаги алгоритма, не меняя его общей структуры.
            * Visitor - позволяет создавать новые операции, не меняя классы объектов, над которыми эти операции могут выполняться.предлагает разместить новое поведение в отдельном классе, вместо того, чтобы множить его сразу в нескольких классах

* Architectural system patterns:
    * Model-View-Controller
        Используется в ситуации, когда связь между представление и другими частями приложения невозможна (и Вы не можете использовать MVVM или MVP);
        Частым примером использования может служить ASP.NET MVC.
    * Model-View-Presenter
        Используется в ситуации, когда невозможно связывание данных (нельзя использовать Binding)
        Частым примером может быть использование Windows Forms.
    * Model-View-View Model
        Используется в ситуации, когда возможно связывание данных без необходимости ввода специальных интерфейсов представления (т.е. отсутствует необходимость реализовывать IView);
        Частым примером является технология WPF.
    * Presentation-Abstraction-Control
    * Naked objects
    * Hierarchical Model-View-Controller
    * View-Interactor-Presenter-Entity-Routing VIPER
> Model - Model means data that is required to display in the view. Model represents a collection of classes that describes the business logic (business model and the data model). It also defines the business rules for data means as how the data can be changed and manipulated.
> View - The View represents UI components like XML, HTML etc. View displays the data that is received from the controller as the outcome. In MVC pattern View monitors the model for any state change and displays updated model. Model and View interact with each other using the Observer pattern.
> Controller - The Controller is responsible to process incoming requests. It processes the user’s data through the Model and passing back the results to View. It normally acts as a mediator between the View and the Model.
> Presenter - The Presenter receives the input from users via View, then process the user’s data with the help of Model and passing the results back to the View. Presenter communicates with view through interface. Interface is defined in presenter class, to which it pass the required data. Activity/fragment or any other view component implement this interface and renders the data in a way they want.
> View-Model - It is responsible for exposing methods, commands, and other properties that help to maintain the state of the view, manipulate the model as the result of actions on the view, and trigger events in the view itself. View has a reference to View-Model but View-Model has no information about the View. There is many-to-one relationship between View and View-Model means many Views can be mapped to one View-Model. It is completely independent of Views.

## DataBase

* Базы данных. Виды. Структура.
    Модели баз данных:
        * Иерархическая - древовидный граф. 
            + Позволяет описать как на логическом, так и физическом.
            - жесткая фиксированность взаимосвязи между элементами. Любые изменения связей - изменение структуры.
            Быстрота доступа за счет потери гибкости
        * Сетевая - диаграмма связей. 
            Допустимы любые виды связей между записями
            Отсутствуют ограничения на число обратных связей. 
            Используется принцип многие ко многим.
            + большая информационная гибкость по сравнению с иерархической моделью
            – жесткость структуры
        * Реляционная - отсутствуют отличия между объектами и взаимосвязями. 
            Связь один к одному. Связи между объектами представлены в виде двумерных таблиц – отношений.
            * Каждая строка - ключ
        * NoSQL - убирает ограничения реляционной модели (недостаточная производительность, трудоёмкое горизонтальное масштабирование, недостаточная производительность в кластере) и облегчает средства хранения и доступа к данным. Используют неструктурированный подход (создание структуры на лету), тем самым снимая ограничения жестких связей и предлагая различные типы доступа к специфическим данным.
            * Не используют общий формат запроса, такой как SQL в реляционных базах данных. Каждое NoSQL решение использует собственную систему запросов.
            * хранят данные как одно целое в базе. Такие данные могут представлять собой одиночный объект как JSON и вместе с тем корректно отвечать на запросы к полям.
    * Свойства отношений:
        * каждый элемент – один элемент данных;
        * повторяющиеся группы отсутствуют;
        * элементы столбца имеют одинаковую природу;
        * в таблице не повторяются строки;
        * строки и столбцы можно просматривать в любом порядке.
    * Взаимосвязи:
        * Один к одному - любому экземпляру сущности А соответствует только один экземпляр сущности В, и наоборот.
        * Один ко многим - любому экземпляру сущности А соответствует 0, 1 или несколько экземпляров сущности В, но любому экземпляру сущности В соответствует только один экземпляр сущности А.
        * Многие к одному - любому экземпляру сущности А соответствует только один экземпляр сущности В, но любому экземпляру сущности В соответствует 0, 1 или несколько экземпляров сущности А.
        * Многие ко многим - любому экземпляру сущности А соответствует 0, 1 или несколько экземпляров сущности В, и любому экземпляру сущности В соответствует 0, 1 или несколько экземпляров сущности А.
    * Сущность - нечто, что заслуживает отдельной таблицы
    * Нормальные формы – это рекомендации по проектированию баз данных
        1. (1NF) Перая нормальная форма. Таблица базы данных – это представление сущности вашей системы, которую вы создаете. 
            * Первичный ключ - каждая таблица имеет первичный ключ, состоящий из наименьшего возможного количества полей.
            * Атомарность - поля не имеют дубликатов в каждой записи и каждое поле содержит только одно значение.
            * порядок записей таблицы не должен иметь значения.
        2. (2NF) Вторая нормальная форма. Для того, чтобы база данных была нормализована согласно второй нормальной форме, она должна быть нормализована согласно первой нормальной форме. Вторая нормальная форма связана с избыточностью данных.
            * Избыточность данных - поля с не первичным ключом не должны быть зависимы от первичного ключа.
        3. (3NF) Третья нормальная форма. Транзитивные зависимости между полями базы данных существует тогда, когда значения не ключевых полей зависят от значений других не ключевых полей. Чтобы база данных была в третьей нормальной форме, она должна быть во второй нормальной форме.
        > Транзитивность — свойство бинарного отношения. Бинарное отношение R на множестве X называется транзитивным, если для любых трёх элементов множества a,b,c выполнение отношений aRb и bRc влечёт выполнение отношения aRc.
            * Транзитивные зависимости - не может быть транзитивных зависимостей между полями в таблице. Поля зависят от первичного ключа, а не от других полей. 
        4. Нормальная форма Бойса — Кодда (BCNF)
            * Переменная отношения находится в нормальной форме Бойса — Кодда (иначе — в усиленной третьей нормальной форме) тогда и только тогда, когда каждая её нетривиальная и неприводимая слева функциональная зависимость имеет в качестве своего детерминанта некоторый потенциальный ключ.
        5. (4NF) Четвертая нормальная форма 
            * Переменная отношения находится в четвёртой нормальной форме, если она находится в нормальной форме Бойса — Кодда и не содержит нетривиальных многозначных зависимостей.
        6. (5NF) Пятая номальная форма
            * Переменная отношения находится в пятой нормальной форме (иначе — в проекционно-соединительной нормальной форме) тогда и только тогда, когда каждая нетривиальная зависимость соединения в ней определяется потенциальным ключом (ключами) этого отношения.
        7. (DKNF) Доменно-ключевая нормальная форма
            * Переменная отношения находится в ДКНФ тогда и только тогда, когда каждое наложенное на неё ограничение является логическим следствием ограничений доменов и ограничений ключей, наложенных на данную переменную отношения.
        8. (6NF) Шестая нормальная форма
            * Переменная отношения находится в шестой нормальной форме тогда и только тогда, когда она удовлетворяет всем нетривиальным зависимостям соединения. Из определения следует, что переменная находится в 6НФ тогда и только тогда, когда она неприводима, то есть не может быть подвергнута дальнейшей декомпозиции без потерь. Каждая переменная отношения, которая находится в 6НФ, также находится и в 5НФ.
    * Удаление данных. Не нарушать ссылочную целостность.
    Может нарушиться:
        * обновляется внешний ключ
        * добавляется новая строка-потомок
        * удаление строки-предка, а потомки остались
        * обновление первичного ключа в строке-предке. поменяли идентификатор категории, а на прежний идентификатор у нас ссылаются определенные вещи. Итог: часть вещей опять в подвешенном состоянии.
    Решение:
        * При обновлении в таблице-потомке проверяется новое значение внешнего ключа. Если указываемого значения нет среди первичных ключей таблицы-предка, то возвращается ошибка.
        * При добавлении новой строки-потомка. Если указываемое значение внешнего ключа не существует среди первичных ключей таблицы-предка, то возвращается ошибка. 
    Методы:
        ON DELETE
        * CASCADE - при удалении или обновлении записи в таблице-предке, которая содержит первичный ключ, автоматически удаляются или обновляются записи со ссылками на это значение в таблице-потомке. 
        * SET NULL – при удалении или обновлении записи в таблице-предке, которая содержит первичный ключ, значения внешнего ключа в таблице-потомке устанавливаются в NULL. 
        * NO ACTION — при удалении или обновлении записи в таблице-предке, которая содержит первичный ключ, в таблице-потомке никаких действий предприниматься не будет. 
        * RESTRICT – если в таблице-потомке есть записи, которые ссылаются на существующий первичный ключ в таблице-потомке, то при удалении или обновлении записи с первичным ключом в таблице-предке возвратится ошибка. 
        * SET DEFAULT – тут понятно из названия, что при удалении или обновлении записи в таблице-предке, которая содержит первичный ключ, в таблице-потомке соответствующим записям будет выставлено значение по умолчанию.

• Что такое SQL транзакция? Зачем нужны индексы? Журнализация?
    * Транзакция - атомарное (неделимое) действие, последовательность операторов манипулирования данными (чтения, удаления, вставки, модификации) 
    Для обеспечения контроля целостности каждая транзакция должна начинаться при целостном состоянии БД и должна сохранить это состояние целостным после своего завершения. Если операторы, объединенные в транзакцию, выполняются, то происходит нормальное завершение транзакции, и БД переходит в обновленное (целостное) состояние. Если же происходит сбой при выполнении транзакции, то происходит так называемый откат к исходному состоянию БД.
    Модели:
        * Автоматическое
        * Управляемое
    * Индекс – это системная структура данных, в которой размещается обязательно упорядоченный перечень значений какого-либо ключа со ссылками на те кортежи отношения, в которых эти значения встречаются. Индексы строятся на тех столбцах таблицы, которые часто используются в запросах. Для одной таблицы может быть создано несколько индексов. Однако увеличение числа индексов замедляет операции добавления, обновления, удаления строк таблицы, поскольку при этом приходится обновлять сами индексы. 
    Хранит только ссылки на записи таблицы. Когда происходит работа с индексом, определяется только список записей (точнее список их первичных ключей), подходящих под запрос. После этого происходит еще один запрос — для получения данных каждой записи из этого списка.
    EXPLAIN - для анализа индексов `EXPLAIN SELECT * FROM users WHERE email = test@test.com`
        * Уникальные индексы - для колонок, значения в которых должны быть уникальными по всей таблице. 
        * Составные индексы - так как можно использовать только один индекс для запроса, то в запросах, где используется несколько колонок необходимо использовать составные индексы. Работет так же как простой, но для значений используются значения всех входящих колонок сразу (очередность будет иметь значение)
        * Primary Key (Первичный ключ) - особый тип индекса, который является идентификатором записей в таблице. Он обязательно уникальный и указывается при создании таблиц 
        * Кластерный индекс - сохраняют данные записей целиком, а не ссылки на них. При работе с таким индексом не требуется дополнительной операции чтения данных.
    Создание индексов только при необходимости. 
        * См slow_log tckb > 1сек, нужен. 
        * Самые частые запросы
        * Индекс на таблицах < N*1000 не нужен
        * Удалять неиспользуемые
    * Журнализация - ведение журнала изменений для сохранения состояний и возможности восстановления. Журнал - часть БД, недоступная пользователям СУБД и поддерживаемая с особой тщательностью, в которую поступают записи обо всех изменениях основной части БД.

• Что такое шардинг? Какой бывает и чем отличается? Репликация?
    Репликация и шардинг - архитектурное решение. Часто используют вместе. 
    * Репликация - создание полного дубликата БД. Позволяет использовать два или больше одинаковых серверов вместо одного. Операций чтения (SELECT) данных часто намного больше, чем операций изменения данных (INSERT/UPDATE). Поэтому, репликация позволяет разгрузить основной сервер за счет переноса операций чтения на слейв.
        master - основной сервер, куда поступают все данные. Все изменения(добавление, обновление, удаление) должны происходить на нем
        slave - вспомогательный, который копирует все данные с мастера. С этого сервера следует читать данные. Таких серверов может быть несколько.
    Подходы:
        * master-slave - для резервирования. Один основной, на котором выполняются все операции. slave - читает и копирует данные. Может быть N(но лучше не более 20 на 1 master) slave.
            + переклчение при выходе из строя
            - задержка репликации
        * master-master - любой из серверов как для чтения, так и для записи. Подключение к случайному мастеру. 
            - Выход из строя приводит к потере каких-либо данных
            - задержка репликации
            - проблема обедающих философов
    Режимы репликации:
        * Встроенный - никто не знает когда произойдет репликация.
        * Синхронный - позволит гарантировать копирование данных на Слейв. Уменьшает скорость работы.
        * Ручной - 
    * Шардинг - техника масштабирования работы с данными. Суть в партиционировании бд на отдельные части так, чтобы каждую из них можно было вынести на отдельный сервер. Процесс зависит от структуры базы данных и выполняется прямо в приложении в отличие от репликации.
        * Вертикальный шардинг - выделение таблицы или группы таблиц на отдельный сервер.В этом случае несколько таблиц (обычно самых крупных) будут находится на одном сервере, а остальные на другом. Тогда запросы к разным таблицам будут обрабатываться разными серверами базы данных. key-value базы (например Memcache) часто поддерживают из коробки. 
        * Горизонтальный шардинг - это разделение одной таблицы на разные сервера. Это необходимо использовать для огромных таблиц, которые не умещаются на одном сервере. Разделение таблицы на куски делается по такому принципу:
            * На нескольких серверах создается одна и та же таблица (только структура, без данных).
            * В приложении выбирается условие, по которому будет определяться нужное соединение (например, четные на один сервер, а нечетные — на другой или же удобно делать разделение по остатку от деления на N шардов).
            * Перед каждым обращением к таблице происходит выбор нужного соединения.
        Поиск и фильтрация, например при помощи Elastic Search. 
        Перебалансировка
        Резервирование с помощью Master-Slave репликации. 
        Партиционирование - возможность разделить таблицу на разные логические группы в рамках одного сервера. Позволяет улучшить эффективность работы с большими таблицами, когда большинство операций производится только со свежими данными

# Python

## Core

* Pickle Bomb
https://intoli.com/blog/dangerous-pickles/


* Descriptors
In general, a descriptor is an object attribute with “binding behavior”, one whose attribute access has been overridden by methods in the descriptor protocol. Those methods are `__get__()`, `__set__()`, and `__delete__()`. If any of those methods are defined for an object, it is said to be a descriptor.
Descriptors are Python objects that implement a method of the descriptor protocol, which gives you the ability to create objects that have special behavior when they’re accessed as attributes of other objects.


### Datatypes in python

* **Numeric data types**: int, float, complex
* **String data types**: str
* **Sequence types**: list, tuple, range
* **Binary types**: bytes, bytearray, memoryview
* **Mapping data type**: dict
* **Boolean type**: bool
* **Set data types**: set, frozenset


* What the difference is between a Numpy array and a normal list?
You can append elements to a list, but you can't change the size of a ´numpy.ndarray´ without making a full copy.
Lists can containt about everything, in numpy arrays all the elements must have the same type.
In practice, numpy arrays are faster for vectorial functions than mapping functions to lists.
I think than modification times is not an issue, but iteration over the elements is.
Numpy arrays have many array related methods (´argmin´, ´min´, ´sort´, etc).
Numpy arrays is a typed array, the array in memory stores a homogenous, densely packed numbers.
Python list is a heterogeneous list, the list in memory stores references to objects rather than the number themselves.

* Difference Between a List and an Array in Python?
array elements are of the same data type, vs. list elements can have different data types.
Yoy can for example divide Arrays `array([3, 6, 9, 12])/3` but if you tried to do the same with a list, the code would throw an error.

* list/set/tuple ★
https://docs.python.org/3.2/tutorial/datastructures.html
list - ordered array of items. Mutable. Implication of iterations is Time-consuming. The list is better for performing operations, such as insertion and deletion. Lists consume more memory. Lists have several built-in methods. The unexpected changes and errors are more likely to occur.
typle - array of items. Immutable. Implication of iterations is comparatively Faster. Tuple data type is appropriate for accessing the elements. Tuple consume less memory as compared to the list. Tuple does no have must built-in methods. In tuple, it is hard to take place.
set - mutable, unordered collection with no duplicate elements. Items in set cannot be changed or replaced. sort data but not garanted (good for int)

    * operation cost ★★
    Стоимость сортировки отсортированного массива - 
    Стоимость сортировки reverse массива - 
    `list.sort(reverse=True|False, key=myFunc)`

    * Memory cost ★★
        Your list of tuples adds an extra layer. You have 3 layers of items:

        The outer list of length 1 million, so 1 million pointers
        1 million 2-slot tuples, so 2 million pointers
        2 million references to 1 million integer values
        while your dict only holds:

        The dict (including 1 million cached hashes) with 2 million pointers + extra space to grow the table
        2 million references to 1 million integer values
        It's those 1 million tuples plus the list to hold the references to them that take up more memory than the 1 million cached hashes. There are some 50% more pointers involved here, easily accounting for the 50% more memory use you see.

        There is another downside to your list of tuples: lookup time. To find a matching key in the dict, there is a O(1) complexity cost. To do the same in the list of tuples, you have to potentially scan the whole list for a O(n) cost. Don't use a list of tuples if you need to map keys to values.
    * Internal structure of list/set/tuple ★★★

* Most generic form of list comprehensions ★
```
*result* = [*transform* *iteration* *filter*]
```

* Time complexity
https://wiki.python.org/moin/TimeComplexity

* Dict comprehensions ★★

* How to dict ★★
> https://eng.lyft.com/hashing-and-equality-in-python-2ea8c738fb9d
Hash map. Need `__hash__` and `__eq__`
Don’t override __hash__ and __eq__ to force objects to hashable. Use immutable objects instead.

Dict and Sets are some of the most common data structures, used heavily for their O(1) lookup times. This O(1) look is enabled by hash functions which have the following properties:
* If a == b then hash(a) == hash(b)
* If hash(a) == hash(b), then a might equal b
* If hash(a) != hash(b), then a != b

*Storing an object*:
    * Call __hash__ on the key to compute the hash of the key. If the key is not hashable raise a TypeError
    * Store (hash_value, key, value) in an array at location hash_value % len(array).
    * If the array requires resizing, re-use the previously computed hash_values to re-insert all previously stored values.

*Retrieving an object by key*
    * Call __hash__ on the key to compute the hash of the key. If the key is not hashable raise a TypeError
    * Look in hash(key) % len(array)for an entry with a matching hash_value. If one exists — check for equality, first by identity, then by calling __eq__.

    * Таблицы Hash должны допускать коллизии hash, то есть даже если два различных ключа имеют одно и то же значение hash, реализация таблицы должна иметь стратегию однозначной вставки и извлечения пар ключей и значений.
    * Python dict использует открытую адресацию для разрешения коллизий hash (объяснено ниже) (см. dictobject.c:296-297 ).
    *Таблица Python hash-это просто непрерывный блок памяти (что-то вроде массива, поэтому вы можете выполнить поиск O(1) по индексу).
    * Каждый слот в таблице может хранить одну и только одну запись. Это очень важно.
    * Каждая запись в таблице фактически представляет собой комбинацию трех значений: < hash, ключ, значение > . Это реализовано как структура C (см. dictobject.h:51-56 ).
    Когда новый дикт инициализируется, он начинается с 8 слотов . (см. dictobject.h:49 )
    * При добавлении записей в таблицу мы начинаем с некоторого слота i, который основан на hash ключа. CPython изначально использует i = hash(key) & mask (где mask = PyDictMINSIZE - 1, но это не очень важно). Просто обратите внимание, что начальный слот , i, который проверяется, зависит от hash ключа.
    * Если этот слот пуст, запись добавляется в слот (под записью я имею в виду <hash|key|value> )., но что делать, если этот слот занят!? Скорее всего, потому что другая запись имеет тот же самый hash (hash столкновение!)
    * Если слот занят, то CPython (и даже PyPy) сравнивает hash AND ключ (под сравнением я подразумеваю сравнение == , а не сравнение is ) записи в слоте с hash и ключом текущей записи, подлежащей вставке ( dictobject.c:337,344-345 ) соответственно. Если оба совпадают, то он думает, что запись уже существует, сдается и переходит к следующей записи, которую нужно вставить. Если либо hash, либо ключ не совпадают, он начинает зондирование .
    * Зондирование просто означает, что он ищет слоты по слотам, чтобы найти пустой слот. Технически мы могли бы просто пойти один за другим, i+1, i+2, ... и использовать первый доступный (это линейное зондирование). Но по причинам, прекрасно объясненным в комментариях (см. dictobject.c:33-126), CPython использует случайное зондирование . При случайном зондировании следующий слот выбирается в псевдослучайном порядке. Запись добавляется в первый пустой слот. Для этого обсуждения фактический алгоритм, используемый для выбора следующего слота, на самом деле не важен (см. dictobject.c:33-126 для алгоритма зондирования). Что важно, так это то, что слоты исследуются до тех пор, пока не будет найден первый пустой слот.
    * То же самое происходит и для поиска, просто начинается с начального слота i (где i зависит от hash ключа). Если hash и ключ не совпадают с записью в слоте, он начинает зондировать, пока не найдет слот с совпадением. Если все слоты исчерпаны, он сообщает о сбое.
    * BTW, размер dict будет изменен, если он заполнен на две трети. Это позволяет избежать замедления поиска. (см. dictobject.h:64-65 )


* What data types are returned if we change braces in list comprehensions to ()/{} ★★
() - returns generator

* Special collections from "collections" module ★★★
namedtuple() - factory function for creating tuple subclasses with named fields
deque - list-like container with fast appends and pops on either end
Counter - dict subclass for counting hashable objects
OrderedDict - dict subclass that remembers the order entries were added
defaultdict - dict subclass that calls a factory function to supply missing values

* 2-tier comprehensions behavior (with 2 statements) ★★★

### Generators

* Looping throgh generators ★
`__iter__` - itriable, `__next__` iterator
yeld
example:
```python
def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]


# For loop to reverse the string
for char in rev_str("hello"):
    print(char)
```

* Defining generators and iterators ★★

**Итераторы** — объекты, которые позволяют обходить коллекции. 
Итерируемый — объект, в котором есть метод __iter__. В свою очередь, итератор — объект, в котором есть два метода: __iter__ и __next__. почти всегда iterator возвращает себя из метода __iter__, так как они выступают итераторами для самих себя, но есть исключения.
Некоторые итерируемые (iterable) не являются итераторами, но используют другие объекты как итераторы. Например, объект list относится к итерируемым, но не является итератором. В нём реализован метод __iter__, но отсутствует метод __next__. Итераторы объектов list относятся к типу listiterator. Обратите внимание, у объектов list есть определённая длина, а у listiterator нету.
Важная поправка к сказанному выше: если у объекта нет метода __iter__, его можно обойти, если определить метод __getitem__. В этом случае встроенная функция iter возвращает итератор с типом iterator, который использует __getitem__ для обхода элементов списка. Этот метод возвращает StopIteration или IndexError, когда обход завершается. 
В модуле itertools есть набор итераторов, которые упрощают работу с перестановками, комбинациями, декартовыми произведениями и другими комбинаторными структурами

**generator** expressions don’t construct list-objects, they generate values “just in time” as a generator function or class-based iterator would. 
A generator function returns a generator object that can be iterated to get the values.
В целом стоит избегать прямого вызова __iter__ и __next__. При использовании for или генераторов списков Python вызывает эти методы сам. Если всё-таки необходимо вызвать методы напрямую, используйте встроенные функции iter и next и в параметрах передавайте итератор или контейнер. Например, если c — итерируемый, используйте конструкцию iter(c) вместо c.__iter__(). Если a — итератор, используйте next(a), а не a.__next__(). Это похоже на использование len.
A generator is simply a function which returns an object on which you can call next, such that for every call it returns some value, until it raises a StopIteration exception, signaling that all values have been generated. Such an object is called an iterator.
It is as easy as defining a normal function, but with a yield statement instead of a return statement.
 - Generator function contains one or more yield statements.
 - When called, it returns an object (iterator) but does not start execution immediately.
 - Methods like `__iter__()` and `__next__()` are implemented automatically. So we can iterate through the items using next().
 - Once the function yields, the function is paused and the control is transferred to the caller.
 - Local variables and their states are remembered between successive calls.
 - Finally, when the function terminates, StopIteration is raised automatically on further calls.

List comprehension uses 87724 bytes of memory while the generator function uses only 125 bytes of memory. By using generators we save memory when compared to list comprehension where a lot of memory is used.

The getsizeof() object returns the amount of memory that holds the nums_squared_list list compared to len() object that would return the total number of items with the nums_sqaured_list list.

* Lazy evaluations
Lazy Evaluation will not immediately evaluate the expression but only does it when the outcome is needed.
map() - lazy
property isn’t really creating a lazy attribute itself. Instead, it’s just a matter of providing an interface to ease data handling.

* Positive and negative sides ★★

* Difference between range and xrange in python2.x ★★
In Python 2.x:
range creates(return) a list, so if you do range(1, 10000000) it creates a list in memory with 9999999 elements.
xrange is a sequence object generator that evaluates lazily.
In Python 3, range does the equivalent of python's xrange, and to get the list, you have to use list(range(...)).

* Difference between python2.x python3.x ★★

|                               | python3                                                                             | python2                                                                      |
|-------------------------------|-------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| Function print                | print ("hello")                                                                     | print "hello"                                                                |
| Division of Integers          | Whenever two integers are divided, you get a float value                            | In Python 2, integer division returns an integer.  7/ 2 gives 3. To get the exact answer, the programmer should use 7.0 / 2. 0.	             |
| Unicode                       | In Python 3, default storing of strings is Unicode.                                 | To store Unicode string value, you require to define them with "u".          |
| Rules of ordering Comparisons | In this version, Rules of ordering comparisons have been simplified.                |                                                                              |
| Iteration                     | The new Range() function introduced to perform iterations.                          | In Python 2, the xrange() is used for iterations.                            |
| Exceptions                    | It should be enclosed in parenthesis.                                               | It should be enclosed in notations.                                          |
| Leak of variables             | The value of variables never changes.                                               | The value of the global variable will change while using it inside for-loop. |
| Backward compatibility        | Not difficult to port python 2 to python 3 but it is never reliable.                | Python version 3 is not backwardly compatible with Python 2.                 |
| Library                       | Many recent developers are creating libraries which you can only use with Python 3. | Many older libraries created for Python 2 is not forward-compatible.         |
| input |   In Python 3, input() function reads the input as a string. raw_input() function is not available.   |   In Python 2, input() function can be used to read as strings if they are inside quotes else read as numbers. In Python 2, raw_input() function is used to get input from the user. This function reads a string.		|


* Usage of generators to provide function input ★★★


* Two way of defenition generators ★★★
comprehensions def with yeld
generator expression and generator function. generator expression is similar with list comprehension, except we use ().

* contextlib - module provides utilities for common tasks involving the with statement. 
Needs `__enter__` and `__exit__`
Example:
```python
class ResourceForWith:
    def __init__(self, name):
        self.__resource = Resource(name)
    def __enter__(self):
        return self.__resource
    def __exit__(self, type, value, traceback):
        self.__resource.post_work()
```

* getattr() -build-in function.
Return the value of the named attribute of object. name must be a string
`getattr(x, 'foobar')` is equivalent to `x.foobar` If the named attribute does not exist, default is returned if provided, otherwise AttributeError is raised.

Unlike the __getattr__ method, which doesn’t get called when a particular attribute is in the instance dictionary, the __getattribute__ method gets called every time an attribute is retrieved.

* diff between yeld and return

`yeld`
    * Yield is generally used to convert a regular Python function into a generator.
    * It replace the return of a function to suspend its execution without destroying local variables.	
    * It is used when the generator returns an intermediate result to the caller.	
    * Code written after yield statement execute in next function call.	
    * It can run multiple times.	
    * Yield statement function is executed from the last state from where the function get paused.

`return`
    * Return is generally used for the end of the execution and “returns” the result to the caller statement.
    * Return statement does not retain any state. Every time you call function, it executed independently.
    * It exits from a function and handing back a value to its caller.
    * It is used when a function is ready to send a value.
    * while, code written after return statement wont execute.
    * It only runs single time.
    * Every function calls run the function from the start.

### Objects

* Purpose of `__str__` and `__repr__` in Python?
Implement `__repr__` for every class you implement. There should be no excuse.
Implement `__str__` for classes which you think readability is more important of non-ambiguity.

* Difference of "new" and "old" obj in python2.x ★
`__new__` accepts cls as it's first parameter and `__init__` accepts self, because when calling `__new__` you actually don't have an instance yet, therefore no self exists at that moment, whereas `__init__` is called after `__new__` and the instance is in place, so you can use self with it.
Old-style classes don't actually have a `__new__` method because for them `__init__` is the constructor. The body of `__new__` will never be executed in this case because it is not the purpose for old-style classes.
The new-style classes let the developer override both `__new__` and `__init__` and they have distinct purposes, `__new__` (the constructor) is solely for creating the object and `__init__` (the initializer) for initializing it.

* Что происходит при создании объекта (какие вызовы) что при создании инстанса etc

* Inheritance type ★
1. Multiple Inheritance
Multiple Inheritance means that you're inheriting the property of multiple classes into one. In case you have two classes, say A and B, and you want to create a new class which inherits the properties of both A and B, then
```python
class A:
    # variable of class A
    # functions of class A
class B:
    # variable of class A
    # functions of class A
class C(A, B):
    # class C inheriting property of both class A and B
    # add more properties to class C
```
2. Multilevel Inheritance
In multilevel inheritance, we inherit the classes at multiple separate levels. We have three classes A, B and C, where A is the super class, B is its sub(child) class and C is the sub class of B.
```python
class A:
    # properties of class A
class B(A):
    # class B inheriting property of class A
    # more properties of class B
class C(B):
    # class C inheriting property of class B
    # thus, class C also inherits properties of class A
    # more properties of class C
```
3. Using issubclass() method
In python, there is a function which helps us to verify whether a particular class is a sub class of another class, that built-in function is issubclass(paramOne, paramTwo), where paramOne and paramTwo can be either class names or class's object name.

* Method Resolution Order (MRO) in Python
> https://medium.com/technology-nineleaps/python-method-resolution-order-4fd41d2fcc
As its name is indicative, multiple inheritance in python is when a class inherits from multiple classes. One example of this would be that a child inherits personality traits from both parents.
The [C3 algorithm](https://www.python.org/download/releases/2.3/mro/) describes how to build a linearization of a class hierarchy, which is an ordered list of the ancestors, i.e., SubClass.__mro__.

* In the case of multiple inheritance, the attribute/method is first looked up in the current class. If the interpreter does not find the said attribute/method, then it searches for it in the next class in the MRO hierarchy. If it fails to find it in any of the classes in the hierarchy, it spits out an error message saying there is no definition of the attribute/method you are looking for.
* In case of multiple parent classes, MRO searchers in a depth-first order followed by a left-right path

* The difference between Old-style classes and New-style classes ★

Old-style classes are the ones that are prior to python 3 and defined without inheriting from base class 'object', which in turn is inherited from 'type' by default.
In python 3 there aren't new or old styles of classes and they inherit directly from 'object' so there is no need to specify it as a base anymore. 
The object base class brings methods/properties that are common to all new-style classes.

In Old-style classes, obj.__class__ and type(obj) evaluate to different things. obj.__class__ gives the class name, where as type(obj) gives . This is due to the fact that all old-style objects/instances, irrespective of their classes, are implemented with a single built-in type called instance.
In New-style classes, obj.__class__ and type(obj) both evaluate to the same thing i.e. the class name.
Apart from this significant difference, there are two additional methods that New-style classes support which Old-style classes don't: mro() and super(). We will get to these later in the chapter.

Python 3 does not support Old-style classes. In fact, there is little chance that you will find a topic in the discussion forums relating to these in Python 3 docs. In Python 2 docs, it lies here.
In Python 2, class BaseClass(object): refer to new-style classes and class BaseClass: refer to old-style classes.
In Python 3, both class BaseClass(object): and class BaseClass: refer to the new-style classes, the latter syntax inherits the object class implicitly.

* Calling methods of base classes in "new" and "old" obj ★

* Constructor ★
The name of a constructor is always the same, `__init__()`. When you create a class without a constructor, Python automatically creates a default constructor for you that doesn’t do anything. Every class must have a constructor, even if it simply relies on the default constructor. 
default constructor :The default constructor is simple constructor which doesn’t accept any arguments.It’s definition has only one argument which is a reference to the instance being constructed.
parameterized constructor :constructor with parameters is known as parameterized constructor.The parameterized constructor take its first argument as a reference to the instance being constructed known as self and the rest of the arguments are provided by the programmer.

* ABC ★
Abstract Cass Method. Abstract class - class with one or more abstract methods. Абстрактные классы не могут быть инстанциированы, от них нужно унаследовать, реализовать все их абстрактные методы и только тогда можно создать экземпляр такого класса. В Python отсутствует встроенная поддержка абстрактных классов, для этой цели используется модуль abc (Abstract Base Class)
Abstract method - defined, but not declareted method. This methot should be define 


* builtins
`__builtins__` objects.
You should use __builtin__ in your programs (in the rare cases that you need it), because __builtins__ is an implementation detail of CPython. It may either be identical to __builtin__, or to __builtin__.__dict__, depending on the context.


* super()
Главная задача метода super() это давать возможность использовать и исполнять в классе потомке, методы класса-родителя.
методом super() мы явно вызываем родительский конструктор.

```python
class C(B, A):
    def __init__(self):
        super(C,self).__init__()
```

* Public, protected and private fields ★★
Incapsulation in python:
public - default. 
self._salary=sal # protected attribute
self.__name=name  # private attribute 

+ magic methods

* Underscore
Single underscore:
    Single underscore is used for saving the value of last executed expression in Python interactive command prompt.We can also save the value to another variable.
    Ignoring values in looping
    Ignoring values in tuple unpacking
    Used in numeric literals: 1_000_000
    _single_leading_underscore: weak “internal use” indicator. E.g. from M import * does not import objects whose names start with an underscore..
    _single_trailing_underscore_: used by convention to avoid conflicts with Python keyword like `var_`

Double:
    __double_leading_underscore: when naming a class attribute, invokes name mangling (inside class FooBar, __boo becomes _FooBar__boo)
    __double_leading_and_trailing_underscore__: “magic” objects or attributes that live in user-controlled namespaces. E.g. __init__, __import__ or __file__. Never invent such names; only use them as documented.

* "Magic" methods. Why, for what and samples ★★
Built-in classes in Python define many magic methods. Use the dir() function to see the number of magic methods inherited by a class. All the attributes and methods defined in the int class. The int class includes various magic methods surrounded by double underscores. For example, the `__add__` method is a magic method which gets called when we add two numbers using the + operator. 

* Presence of class-field and object-field with same name/ How to access ★★

* Way to access private fields in python ★★★
Python's convention to make an instance variable protected is to add a prefix _ (single underscore) to it. This effectively prevents it to be accessed, unless it is from within a sub-class.
A double underscore __ prefixed to a variable makes it private. It gives a strong suggestion not to touch it from outside the class. Any attempt to do so will result in an AttributeError.

* MRO of new and old style obj ★★★
2.7 near left by depth
3 more horisontal

### Decorators

* What is decorator and how it's applied ★
A decorator is a higher order function that accepts a function and returns a function.[0]
Sometimes you want to modify a bunch of functions the same way. In calculus, derivatives and integrals are common higher order functions.

* Common form of simple decorator ★
A decorator is a function, that creates a wrapper function around another function.
```python
def my_decor(f):
    def wrapper():
        return f()
    return wrapper
def hello():
    ''' Helllo function, says hello'''
    print("Hello There!")
```

* Замыкание
Замыкание — это комбинация функции и множества ссылок на переменные в области видимости функции. Последнее иногда называют ссылочной средой. Замыкание позволяет выполнять функцию за пределами области видимости. В Python ссылочная среда хранится в виде набора ячеек. Доступ к ним можно получить с помощью атрибутов func_closure или __closure__. В Python 3 используется только __closure__.


* Downside of simple decorator and how to avoid it (functools.wraps) ★★
Если вы достаточно внимательны, то заметите, что мы заботимся, чтобы у возвращаемой функции был правильно указан __name__, но не заботимся о __doc__ или __module__. Поэтому если у функции add есть строка документации, она потеряется. Как можно этого избежать? Мы могли бы справиться с проблемой так же, как при обработке __name__. Но выполнять такие операции с каждым декоратором утомительно. Поэтому в модуле functools есть декоратор wraps, который срабатывает именно в таком сценарии. Использование декоратора внутри другого декоратора может показаться странным. Но если вы думаете о декораторах как о функциях, которые принимают функции в качестве параметров и возвращают функции, всё становится на места. Декоратор wraps используется в следующих примерах вместо ручной обработки __name__ и других подобных атрибутов.

When you use a decorator, you're replacing one function with another. In other words, if you have a decorator
```python
def logged(func):
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging
```
then when you say
```python
@logged
def f(x):
   """does some math"""
   return x + x * x
```
it's exactly the same as saying
```python
def f(x):
    """does some math"""
    return x + x * x
f = logged(f)
```
and your function f is replaced with the function with_logging. Unfortunately, this means that if you then say
```python
print(f.__name__)
```
it will print with_logging because that's the name of your new function. In fact, if you look at the docstring for f, it will be blank because with_logging has no docstring, and so the docstring you wrote won't be there anymore. Also, if you look at the pydoc result for that function, it won't be listed as taking one argument  x; instead it'll be listed as taking *args and **kwargs because that's what with_logging takes.
If using a decorator always meant losing this information about a function, it would be a serious problem. That's why we have functools.wraps. This takes a function used in a decorator and adds the functionality of copying over the function name, docstring, arguments list, etc. 
```python
from functools import wraps
def logged(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging
@logged
def f(x):
   """does some math"""
   return x + x * x
print(f.__name__)  # prints 'f'
print(f.__doc__)   # prints 'does some math'
```

* Decorator which takes parameters ★★
```python
def decorator_fun(func):  
  print("Inside decorator")  
  def inner(*args, **kwargs):  
    print("Inside inner function")  
    print("Decorated the function")  
    func()
  return inner
  
def func_to():  
    print("Inside actual function")  
# another way of using decorators 
decorator_fun(func_to)() 
```
```Output
Inside decorator
Inside inner function
I like geeksforgeeks
Inside actual function
```

```python
def decorator_func(x, y):
    def Inner(func):
        def wrapper(*args, **kwargs): 
            print("I like Geeksforgeeks") 
            print("Summation of values - {}".format(x+y) )
            func(*args, **kwargs)
        return wrapper 
    return Inner
# Not using decorator  
def my_fun(*args): 
    for ele in args: 
        print(ele)
# another way of using dacorators 
decorator_func(12, 15)(my_fun)('Geeks', 'for', 'Geeks') 
```
```
Output:
I like Geeksforgeeks
Summation of values - 27
Geeks
for
Geeks
```

* Downside of functools.wraps and how to avoid it ★★★

* Nesting decorators ★★★

### Multithreading & Multiprocessing

* Basic skills of using multithreading ★
The threading module uses threads, the multiprocessing module uses processes. The difference is that threads run in the same memory space, while processes have separate memory. This makes it a bit harder to share objects between processes with multiprocessing. Since threads use the same memory, precautions have to be taken or two threads will write to the same memory at the same time. This is what the global interpreter lock is for.
Spawning processes is a bit slower than spawning threads. Once they are running, there is not much difference.
Processes spawn threads
- Also in python 3.2 added concurrent.futures package.  concurrent.futures.ThreadPoolExecutor makes the Python threading example code almost identical to the multiprocessing module.
By default, the ProcessPoolExecutor creates one subprocess per CPU.
-  Async/Await (Python 3.5+ only) Concurrency Cooperative 1 Processors The tasks decide when to give up control.
The async def syntax marks a function as a coroutine. Internally, coroutines are based on Python generators, but aren’t exactly the same thing. Coroutines return a coroutine object similar to how generators return a generator object. Once you have a coroutine, you obtain its results with the await expression. When a coroutine calls await, execution of the coroutine is suspended until the awaitable completes. 

* Async
Потоки — наиболее распространённый инструмент. Думаю, вы слышали о нём и ранее, однако asyncio оперирует несколько другими понятиями:
* **цикл событий (event loop)** по большей части всего лишь управляет выполнением различных задач: регистрирует поступление и запускает в подходящий момент
* **корутины** — специальные функции, похожие на генераторы python, от которых ожидают (await), что они будут отдавать управление обратно в цикл событий. Необходимо, чтобы они были запущены именно через цикл событий
* **футуры** — объекты, в которых хранится текущий результат выполнения какой-либо задачи. Это может быть информация о том, что задача ещё не обработана или уже полученный результат; а может быть вообще исключение


* Async gather
`acync.gather` lets you fire off a bunch of coroutines simultaneously, and the current context will resume once all of the coroutines have completed. The return value is a list of responses from each coroutine.

* Basic understanding of GIL ★
https://callhub.io/understanding-python-gil/
GIL позволяет одновременно выполнять только один поток, даже в многопоточной архитектуре с более чем одним ядром процессора, GIL приобрел репутацию «печально известной» функции Python.
Python использует подсчет ссылок для управления памятью. Это означает, что объекты, созданные в Python, имеют переменную подсчета ссылок, которая отслеживает количество ссылок, которые указывают на объект. Когда этот счет достигает нуля, память, занятая объектом, освобождается.
Python uses reference counting for memory management. It means that objects created in Python have a reference count variable that keeps track of the number of references that point to the object. When this count reaches zero, the memory occupied by the object is released.
```python
import sys
a = []
b = a
sys.getrefcount(a)
OUT: 3
```
GIL - это одиночная блокировка самого интерпретатора, которая добавляет правило, согласно которому выполнение любого байт-кода Python требует получения блокировки интерпретатора. Это предотвращает взаимные блокировки (так как существует только одна блокировка) и не приводит к значительному снижению производительности. Но это эффективно делает любую связанную с процессором программу Python однопоточной.

The problem was that this reference count variable needed protection from race conditions where two threads increase or decrease its value simultaneously. If this happens, it can cause either leaked memory that is never released or, even worse, incorrectly release the memory while a reference to that object still exists. This can can cause crashes or other “weird” bugs in your Python programs.

The GIL is a single lock on the interpreter itself which adds a rule that execution of any Python bytecode requires acquiring the interpreter lock. This prevents deadlocks (as there is only one lock) and doesn’t introduce much performance overhead. But it effectively makes any CPU-bound Python program single-threaded.

* Garbaje collector
Модуль gc включает функции для изменения порогового значения, ручного запуска процесса сбора мусора, отключения процесса сбора мусора и т. д. Мы можем проверить пороговые значения разных поколений сборщика мусора с помощью метода get_threshold():


* Difference between process and thread ★★
Multiprocessing many Processors The processes all run at the same time on different processors.
    + Separate memory space
    + Code is usually straightforward
    + Takes advantage of multiple CPUs & cores
    + Avoids GIL limitations for cPython
    + Eliminates most needs for synchronization primitives unless if you use shared memory (instead, it's more of a communication model for IPC)
    + Child processes are interruptible/killable
    + Python multiprocessing module includes useful abstractions with an interface much like threading.Thread
    + A must with cPython for CPU-bound processing
    - IPC a little more complicated with more overhead (communication model vs. shared memory/objects)
    - Larger memory footprint
Threading 1 Processors The operating system decides when to switch tasks external to Python.
    + Lightweight - low memory footprint
    + Shared memory - makes access to state from another context easier (run in the same memory space)
    + Allows you to easily make responsive UIs
    + cPython C extension modules that properly release the GIL will run in parallel
    + Great option for I/O-bound applications
    - cPython - subject to the GIL
    - Not interruptible/killable
    - If not following a command queue/message pump model (using the Queue module), then manual use of synchronization primitives become a necessity (decisions are needed for the granularity of locking)
    - Code is usually harder to understand and to get right - the potential for race conditions increases dramatically

* Event loop vs Treading



* Create a process in python ★★

* Creating a thread in python ★★
https://pymotw.com/2/threading/

Other ways:
https://www.parallelpython.com/examples.php
For example https://stackabuse.com/parallel-processing-in-python/
    * Using the subprocess module
    * Using the os.system() Method
pp module

* What types of thread may improve execution speed of program (CPU or IO and why) ★★★
https://realpython.com/python-concurrency/
- I/O-Bound Process
Your program spends most of its time talking to a slow device, like a network connection, a hard drive, or a printer.
Speeding it up involves overlapping the times spent waiting for these devices.
Юзать treading ибо iowait небольшой и предсказуем
- CPU-Bound Process
You program spends most of its time doing CPU operations.
Speeding it up involves finding ways to do more computations in the same amount of time.

* Primitives used to sync threads and processes ★★★
AsyncIO
- Lock:
- Event:
- Condition:
- Semaphore:
- BoundedSemaphore:

multiprocessing
 - Semaphore:
 - Array:

threading
 - Rblock: This class implements reentrant lock objects. A reentrant lock must be released by the thread that acquired it. Once a thread has acquired a reentrant lock, the same thread may acquire it again without blocking; the thread must release it once for each time it has acquired it.
 - Semaphore:

iowait - переключение потока

* When we need to use threads and when processes and why (non based  python) ★★★

### Metaclasses

* Basic understanding of metaclasses (what is it, how to applay it on class) ★
Principially, metaclasses are defined like any other Python class, but they are classes that inherit from "type". Another difference is, that a metaclass is called automatically, when the class statement using a metaclass ends. In other words: If no "metaclass" keyword is passed after the base classes (there may be no base classes either) of the class header, type() (i.e. __call__ of type) will be called. If a metaclass keyword is used, on the other hand, the class assigned to it will be called instead of type.
В принципе, метаклассы определяются как любой другой класс Python, но они являются классами, которые наследуются от «типа». Другое отличие состоит в том, что метакласс вызывается автоматически, когда оператор класса, использующий метакласс, заканчивается. Другими словами: если ключевое слово «metaclass» не передано после базовых классов (возможно, не существует и базовых классов) заголовка класса, будет вызван `type()` - мметакласс (то есть __call__ типа). Если используется ключевое слово metaclass, с другой стороны, назначенный ему класс будет вызываться вместо type.

There is a contract between a class and its callers. The class promises to do certain things and have certain properties.
There are different levels to the contract.

An ABC is an ordinary class (meaning, its instances are arbitrary objects), it's an instance of type. A metaclass has other classes for instances, and it inherits from type (in addition to being an instance of type).

* Defining a metaclasses ★★

* Use cases ★★

* How metaclasses could be defined ★★★
```python
  MyClass = type('MyClass', (), {})

class Foo(object):
  __metaclass__ = something...
  [...]
```

* Base clase for metaclasses if we define it as class ★★★

### Modules and packages

* What is module ★
A module is a single file (or files) that are imported under one import and used.
There are actually three different ways to define a module in Python:
* A module can be written in Python itself.
* A module can be written in C and loaded dynamically at run-time, like the re (regular expression) module.
* A built-in module is intrinsically contained in the interpreter, like the itertools module.
* A module’s contents are accessed the same way in all three cases: with the import statement.

* File module and dir module ★

* Ways to import something from module ★★

* Sys.modules ★★

* Dynamic imports (`__import__`) ★★★

* Cycling imports and how to avoid ★★★

* Module name collision (base module name from req. and local submodules name)/ How works import in this cse and how to avoid this behavor ★★★

* Packages
The Python Package Index (PyPI) is a repository of software for the Python programming language.
Packages allow for a hierarchical structuring of the module namespace using dot notation. In the same way that modules help avoid collisions between global variable names, packages help avoid collisions between module names.

If a file named __init__.py is present in a package directory, it is invoked when the package or a module in the package is imported. This can be used for execution of package initialization code, such as initialization of package-level data.





### Testing

* Basic understanding unit testing? continuius integration ★

* Best practices writing unit tessts ★

* Coverage reports ★★

* Mocking, request factory (for Django) ★★

* Pytest fixtures ★★★

* Writing custom Tesst Runner? use cases (for Django) ★★★


## Django

> https://www.knowledgehut.com/interview-questions/django

* Django design pattern?
Django follows MVC pattern (Model-View-Controller), also referred to as MTV (Model-Template-View). 
    Model – describes database schema 
    Views – Controls what user can view. It retrieves data from the table and passes it to the template which is rendered to Browser eventually.
    Template – Determines how the user sees it. 
    Controller – controls the entire flow of models and data.

* How Django process a request?
When a user requests a page, Django determines whether the request URL pattern is mentioned in URLs.py. Once the regex matches, Django calls the corresponding view. HttpRequest is passed as an argument to that view function and the implementation part is executed further.

We know that all web application uses HTTP/HTTPS protocol. The basic principle of the HTTP protocol is Client sends a request to the server and the data server sends a response back to the client based on request data. We need a web server and WSGIserver while setting up a Django application on the server. Without a web server, WSGI server will result in a more number of requests resulting in gradually slow down the application performance. The web server will help in balancing the requests load on the server. 

The client is a piece of software which sends a request by following HTTP/HTTPS protocol and mostly we consider Web Browser as a client. "Nginx, uWSGI and Django" or "Nginx, gunicorn and Django" or "Apache, mod_wsgi and Nginx" are the three types of combinations in Django application deployment on the server and we can use any one of the combinations. Now let us discuss on how a request is processed and response is created and sent to the client.

When a client sends request it first passed to a web server. The request contains configuration rules to be dispatch to the WSGI server. WSGI server sends the request to the Django application.

For dealing with request-response lifecycle, Django application has the following layers -
    * Request middlewares
    * URL Router
    * Views
    * Context processors
    * Template Renderers
    * Response middleware
Any request that comes in is *handled by Request middleware*. There can be multiple middlewares and can find it in `settings.py` (project settings). While processing the request Django Request middlewares follow the order. Django has some default middlewares and we can also write or customize middleware. Middleware process the request and submits it to the *URL Router* or *URL dispatcher*.

*URL Router* receives a request from the middleware and from the request it collects the URL path. From the URL path, the URL router tries to match the request path with available URL patterns. These patterns are in the regular expression form. Once the URL path is matched with URL patterns the request is submitted to the View associated with URL.

*Views* are the business logic layer, which processes the business logic using request and request data. A request is processed in the view, it is sent to Context processor. Context processor adds context data that helps Template Renders to deliver the template to generate HTTP response and again this request will be sent back to Response middleware to process. Request middleware adds or modifies header information or body information before sending it to the client again.

* What are the disadvantages of Django?

Django is an amazing framework, still, there are a few cons. The URL specifying with regular expressions is not an easy task.  Template errors fail silently by default, to know that, you may waste a lot of time to figure out what’s wrong, or you might not even know that your application has a problem. Along with the advantages, there are many disadvantages to Django mentioned below.

Template Mistakes Flop Discreetly itself - System developers do not pay attention to mistakes when they undertake a class-based viewpoint and they are extended through inheritance.

Does Not Have The Capacity To Manage Different Requests At The Same Time:

Django does not support individual procedures to deal with many requests at the same time. Developers need to investigate approaches and make singular procedures to control various requests proficiently and rapidly at once.

Django is Excessively Monolithic: Django framework directs you into a given specific pattern.

Regex To Indicate Its URL: Django uses regex to determine its URL routing models, which makes the code bigger and makes convoluted syntaxes. 

While Managing Backwards Compatibility, It’s Moving Extremely Gradually: Django has a tendency to get greater and heavier after some time. Django stresses more on dev profitability and backward compatibility than the speed.

Django uses routing patterns to specify its URL.
Everything is based on Django ORM and the ORM system lacks features.
Components are tightly coupled and get deployed together
To work with Django, knowledge of the full system is required.
There are many pros and cons of Django, still, when a project with a deadline is considered, using Django for the project provides the ultimate solution.

* What is CRUD?

The most common task in web application development is to write create, read, update and delete functionality (CRUD) for each table. It refers to the set of common operations that are used in web applications to interact with data from the database. It provides a CRUD interface that allows users to create, read, update or delete data in the application database.

Django helps us with its simplified implementation for CRUD operations using Function-Based views and class-based Views.

* **Function-based views** are simple to implement and easy to read but they are hard to customize or extend the functionality. Code reuse is not allowed and so there is repetitiveness.
* **Class-based views** - In no time CRUD operations can be implemented using CBVs. As the model evolves changes would be reflected automatically in CBVs. CBVs are easily extendable and allow code reuse. Django has built-in generic CBVs which makes it easy to use

## Flask 
* What is the default host port and port of Flask?
Flask default host is a localhost (127.0.0.1), and the default port is 5000.

* How to change default host and port in Flask?
Flask default host and port can be changed by passing the values to host and port parameters while calling run method on the app.
```python
from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def index():
    return "Hello, World!"
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
```
* Which Flask extension can be used to create an Ajax application?
We can use Flask-Sijax to create an Ajax application. Flask-Sijax is an extension that uses Python/JQuery. It is available on PyPI and can be installed using pip.

Sijax stands for Simple Ajax. Once configured and initialized, it enables the use of @flask_sijax decorator, which we can use for making Ajax aware of the views in a Flask Application.
## Lib & Frameworks


## Random Python facts

1. list в Python — это вовсе не связный список, а динамический массив. 
2. Проверка на включение in — это такая же операция как >, < или ==. Помните двойные неравенства вроде 1 < x < 5? Выражение 1 < x in [1, 2, 3] работает так же. Это (1 < x) and (x in [1, 2, 3]).
3. Да для Python есть компиляторы. И не только JIT как Numba (классная штука, кстати!), но и обычные. Например, Nuitka. Разговор о их целесообразности оставим за скобками.
4. Если на объект нет ссылок, то он уничтожается сразу, а не ждёт сборки мусора. GC нужен для сложных случаев, когда у нас есть циклические ссылки.
5. Python очень медленный, но м̶ы̶ ̶л̶ю̶б̶и̶м̶ ̶е̶г̶о̶ ̶н̶е̶ ̶з̶а̶ ̶э̶т̶о̶ обычно это не проблема. Python можно использовать для I/O bound задач или написать бинарный модуль на быстром языке программирования.
6. Язык для файлов конфигурации Starlark (он же Skylark) от Google — это Python на минималках.
7. Многие знают, что числа от -5 до 255 интернированы. То есть заранее размещены в памяти. В эту память при желании можно залезть и поменять значение так, чтоб литерал 5 имел значение 7. Весёлой отладки!
8. У интерпретатора Python есть ключи командной строки для оптимизации, но они просто удаляют assert и строки документации.
9. __ читается как dunder.
10. Формат pickle — это последовательность команд для специальной виртуальной машины. Опкод R может вызвать произвольную функцию. Например, os.system. Так что лучше не используйте pickle из ненадёжных источников. И не храните в нём ничего на диске, он не для этого.
11. В последних версиях в dict ключи упорядочены. Но это не было сделано специально. Это был побочный эффект новой реализации словарей. Однако, разработчикам понравилось, и начиная с Python 3.7 это поведение гарантируется. Так что OrderedDict не нужен.
12. Если вы скучаете по структурам, посмотрите в сторону namedtuple или датаклассов. Они удобны!
13. Python — это просто хобби-проект ван Россума на рождественские каникулы 1989 года.
14. У циклов есть блок else, который часто очень удобен.
15. У функции может быть вызвано два return. Например:
```python
def f():
    try:
        return 1
    finally:
        return 2
```
Функция вернёт 2.
16. Да, в Python есть многопоточность. Да, там честные потоки операционной системы. Да, они могут работать одновременно во многих случаях. Да, я знаю про GIL.
17. bool — это подкласс int. Гарантируется, что у False и True числовые значения 0 и 1.
18. Хэш-таблица любого словаря содержит примерно ⅓ пустых ячеек, чтоб эффективно работать. Ничего полезного в них не хранится.  Но это ячейки для ссылок, так что память расходуется не так сильно.
20. Модули — это синглтоны, создающиеся в момент первого импорта. Часто это полезно.
21. yield в генераторах может возвращать значения, которые отправлены в него снаружи методом send (да, есть такой).
22. Благодаря send и генераторам реализовали асинхронное программирование. async и await — это просто синтаксический сахар.
23. Список может содержать сам себя. Python это обнаруживает и не зацикливается при выводе.
```python
>>> a = []
>>> a.append(a)
>>> a
[[...]]
```
24. В Python нет оптимизации хвостовой рекурсии не потому, что Гвидо не осилил, а потому, что он не хочет всё усложнять. Если очень хочется, можно реализовать Y-комбинатор с оптимизацией и использовать его. Если вам действительно нужна TCO, то вы знаете, как это сделать.
25. Для длинной арифметики Python хранит массив цифр в системе счисления с основанием 2³⁰. Кстати, может быть и 2¹⁵. Если кому интересны подробности, читайте тут — https://github.com/python/cpython/blob/master/Include/longintrepr.h


# Web

##  Network in frontend
• Что такое DNS?
        Domain Name System — система доменных имён) — компьютерная распределённая система для получения информации о доменах. Чаще всего используется для получения IP-адреса по имени хоста (компьютера или устройства), получения информации о маршрутизации почты, обслуживающих узлах для протоколов в домене (SRV-запись).
        SRV - стандарт в DNS, определяющий местоположение, то есть имя хоста и номер порта серверов для определенных служб. `_service._proto.name TTL class SRV priority weight port target` 
        * service: символьное имя сервиса.
        * proto: транспортный протокол используемый сервисом, как правило TCP или UDP.
        * name: доменное имя, для которого эта запись действует.
        * TTL: стандарт DNS, время жизни.
        * class: стандарт DNS, поле класса (это всегда IN).
        * priority: приоритет целевого хоста, более низкое значение означает более предпочтительный. 
        * weight: относительный вес для записей с одинаковым приоритетом.
        * port: Порт TCP или UDP, на котором работает сервис.
        * target: канонические имя машины, предоставляющей сервис.
    FQDN (Fully Qualifed Domain Name) - полностью определённое имя домена. 
    RDNS - обратный запрос. Для получения DNS-имени адреса 11.22.33.44 запросить у DNS-сервера запись 44.33.22.11.in-addr.arpa, и тот вернёт соответствующее символьное имя.

• HTTP протокол. Как работает. 
    HTTP (HyperText Transfer Protocol но сейчас передает что угодно) - синхронный протокол передачи данных, относящийся к TCP/IP, 7 уровнь OSI, работающий на основе технологии клиент-сервер. По умолчанию 80 порт. Использует URI (URI = URL или URI = URN или URI = URL + URN)
        При http соединении выполняется tcp-handshake (SYN,SYN-ACK,ACK)
        * Клиент отправляет запрос, который имеет Request Line вида `GET /tutorials/other/top-20-mysql-best-practices/ HTTP/1.1` и заголовки.
            Структура:
                * method
                * path
                * protocol
        * Сервер отдает ответ со строкой состояния типа `HTTP/1.x 200 OK` и заголовками
            Структура:
                * protocol
                * status code
        * Выполняется передача данных с учетом upgrade, данных заголовков и т п.
    HTTPS - расширение HTTP, использующее 443 TCP порт и являющееся связкой HTTP и SSL/TLS.
        При https используется соеинение по 443 TCP порту. добавляется этап с отправкой сертификата и его проверкой
        При http2 используется заголовок `upgrade: h2c`

• Какие заголовки есть в HTTP протоколе?
    Заголовки Http1. Имеют название (минимум один ASCII) и значение (любой ASCII включая переносы строк и тп ). Увидеть заголовки - плагины браузера (Firebug, Live HTTP Headers), curl(2), telnet, openssl ( испольовать ключ --servername при проверки с SNI(Server name indication)). 
    Типы заголовков:
        * General Headers - Основные для запросов клиент-сервер
            * `Cache-control: no-cache | no-store | max-age=3600 | max-stale=0 | min-fresh=0 | no-transform | only-if-cached | cache-extension`
            * `Connection`
            * `Date` - дата генерации отклика
            * `Upgrade: HTTP/2.0, SHTTP/1.3, IRC/6.9, RTA/x11`
            * `Transfer-Encoding: chunked` - Список способов кодирования, которые были применены к сообщению для передачи.
            * `Via: 1.0 fred, 1.1 nowhere.com (Apache/1.1)` - cписок версий протокола, названий и версий прокси-серверов, через которых прошло сообщение.
        * Request Headers - заголовки только для запросов клиента
            * `host: ya.ru` - Доменное имя и порт хоста запрашиваемого ресурса
            * `From: user@example.com`
            * `User-Agent: Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1`
            * `Accept-Encoding: gzip,deflate`
            * `Accept: text/plain`
            * `Accept-Charset: utf-8`
            * `Accept-Language: ru`
            * `Authorization: Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==` - Информация для авторизации на прокси-сервере в base64
            * `If-Modified-Since | If-Unmodified-Since: Sat, 29 Oct 1994 19:43:31 GMT` - Дата. Выполнять метод если сущность изменилась | не изменилась с указанного момента.
            * `Last-Modified` - дата последней модификации
            * `Max-Forwards: 10` - Максимально допустимое количество переходов через прокси
            * `Pragma: no-cache`
            * `Proxy-Authorization: Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==` - параметры авторизации на прокси сервере. 
            * `Referer: http://en.wikipedia.org/wiki/Main_Page` - URI ресурса, после которого клиент сделал текущий запрос.
            * CORS
                * `Access-Control-Request-Method`
        * Response Headers - заголовки для ответов сервера
            * `Set-Cookie: name=newvalue; expires=date; path=/; domain=.example.org`
            * `Accept-Ranges: bytes`
            * `Age` - кол-во секунд с момента модификации ресурса
            * `Server: Apache/2.2.17 (Win32) PHP/5.3.5` - Список названий и версий веб-сервера и его компонентов с комментариями. Для прокси-серверов поле Via.
            * `ETag: "56d-9989200-1132c580"` - entity tag это закрытый идентификатор, присвоенный веб-сервером на определенную версию ресурса, найденного на URL. Если содержание ресурса для этого адреса меняется на новое, назначается и новый ETag.
            * `Location: http://example.com/about.html#contacts` - URI по которому клиенту следует перейти или URI созданного ресурса. Используется при коде ответа 301/302(307)
            * `WWW-Authenticate: Basic realm="Restricted Area"` - для аутентификации пользователя через HTTP. Когда браузер увидит этот header, он откроет диалоговое окно входа в систему.
            * `Access-Control-Allow-Origin` - регулирует, с какого домена разрешено запрашивать данные
        * Entity Headers - заголовки сущностей. 
            * `Allow` - код ответа и доступные options `Allow: GET, HEAD, OPTIONS` 
            * `Content-Language`
            * `Content-Encoding: gzip` Способ кодирования содержимого сущности при передаче. 
            * `Content-Type: text/html;charset=utf-82`
            * `Accept-Encoding: gzip,deflate`
            * `Content-Disposition: form-data; name="MessageTitle"` `Content-Disposition: form-data; name="AttachedFile1"; filename="photo-1.jpg"` - Способ распределения сущностей в сообщении при передаче нескольких фрагментов. передается с Content-Type

• Методы запроса
        * GET - получить документ
        * HEAD - аналогичен GET, но для метаданных (только код ответа и заголовки). Нет тела. 
        * POST - Применяется для передачи пользовательских данных заданному ресурсу.
        * PUT - для загрузки содержимого запроса на указанный в запросе URI 
        * PATCH - как PUT, но применяется только к фрагменту ресурса
        * DELETE - удаляет ресурс
        * CONNECT - преобразует соединение запроса в прозрачный TCP/IP-туннель, обычно чтобы содействовать установлению защищённого SSL-соединения через нешифрованный прокси.
        * TRACE	- возвращает полученный запрос так, что клиент может увидеть, что промежуточные сервера добавляют или изменяют в запросе.
        * LINK - устанавливает связь указанного ресурса с другими.
        * UNLINK - убирает связь указанного ресурса с другими.
    Коды статуса:
        * 100 - информационный
        * 200 используются для успешных запросов.
        * 300 для перенаправления.
        * 400 используются, если возникла проблема с запросом.
        * 500 используются, если возникла проблема с сервером.
    Прокси - промежуточный сервер можду клиентом и конечным сервером.
    MIME (Multipurpose Internet Mail Extension, Многоцелевые расширения почты Интернета) — спецификация для передачи по сети файлов различного типа: изображений, музыки, текстов, видео, архивов и др. Указание MIME-типа используется в HTML обычно при передаче данных форм и вставки на страницу различных объектов. 

• CORS - Cross-Origin Resource Sharing
    Различает простые и сложные. 
    * Простые. 
        1. Посылается ajax запрос, где браузер добавляет заголовок `Origin` с адресом страницы, откуда инициирован запрос. 
        2. Сервер читает заголовок, и решает как его обрабатывать. Заголовок ответа `Access-Control-Allow-Origin` регулирует, с какого домена разрешено запрашивать данные. Это может быть как веб-адрес, так и знак астерикса (звездочки), если разрешено всем. Несколько разных адресов через запятую, к сожалению, не поддерживаются.
        Методы:
            * `POST`
            * `GET`
            * `HEAD`
        Заголовки:
            * `Accept`
            * `Accept-Language`
            * `Content-Language`
            * `Last-Event-ID`
            * `Content-Type`, но только со значениями `application/x-www-form-urlencoded`, `multipart/form-data`, `text/plain`
    * Сложные - использование API. Почти всегда JSON. Проходит в 2 этапа.
        1. Preflight request. Браузер делает запрос по тому же урлу методом `OPTIONS`. Клиент посылает хочет отправить ajax `PUT` на `api.bob.com` с сайта `api.bob.com`. 
            `OPTIONS /cors HTTP/1.1`
            `Origin: http://api.bob.com`
            `Access-Control-Request-Method: PUT`
            `Access-Control-Request-Headers: X-Custom-Header` - запрос разрешения. 
            `Host: api.alice.com`
            `Connection: keep-alive`
        2. Сервер может ответить
            `200 OK HTTP/1.1`
            `Access-Control-Allow-Origin: http://api.bob.com`
            `Access-Control-Allow-Methods: GET, POST, PUT` - какими методами можно ходить вмместе с заголовком `X-Custom-Header`
            `Access-Control-Allow-Headers: X-Custom-Header`
            `Content-Type: text/html; charset=utf-8`
        3. Так как ответ сервера разрешает выполнить запрос, то 2 запрос браузер уже делает по назначению. 
        Заголовки:
            * `Content-Type: application/json`
    Заголовок ответа Access-Control-Allow-Origin регулирует, с какого домена разрешено запрашивать данные
    Для сокращения preflight-запросов `OPTIONS` либо кешировать `Cache-Control`, либо объявить в заголовках сервера, например Nginx
    Даже если возвращаете ответ с не-положительным статусом, например, не прошла валидация или нет прав, заголовок Access-Control-Allow-Origin обязан присутствовать. Если заголовка нет, браузер решит, что CORS-запрос запрещен и не прочитает ответ.

• Отличие сокет соединения (WebSockets) от HTTP запросов
    HTTP - синхронный и симметричный с фиксированными ролями клиент-сервер. 
    WebSockets - ассинхронный, ассиметричный, равноправный. Расширение HTTP. Предназначен для решения задач и снятия ограничений обмена данными между браузером и сервером. 
    Описания заголовков:
        * GET, Host - Стандартные HTTP-заголовки из URL запроса
        * Upgrade, Connection - Указывают, что браузер хочет перейти на websocket.
        * Origin - Протокол, домен и порт, откуда отправлен запрос.
        * Sec-WebSocket-Key - Случайный ключ, который генерируется браузером: 16 байт в кодировке Base64.
        * Sec-WebSocket-Version - Версия протокола. Текущая версия: 13.
        * Все заголовки, кроме GET и Host, браузер генерирует сам, без возможности вмешательства JavaScript.
        * Sec-WebSocket-Extensions: deflate-frame означает, что браузер поддерживает модификацию протокола, обеспечивающую сжатие данных. Это говорит не о самих данных, а об улучшении способа их передачи. Браузер сам формирует этот заголовок.
        * Sec-WebSocket-Protocol: soap, wamp говорит о том, что по WebSocket браузер собирается передавать не просто какие-то данные, а данные в протоколах SOAP или WAMP («The WebSocket Application Messaging Protocol»). Стандартные подпротоколы регистрируются в специальном каталоге IANA.
    WSS - ws над https
    Установка соединения.
        Работает над TCP и по http GET отравяет заголовок `Upgrade: WebSocket`, `Connection: Upgrade`, `Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==` с вопросом, о том, поддерживается ли WebSockets. 
        Если сервер поддерживает, то отвечает `HTTP/1.1 101 Web Socket Protocol Handshake`, `Upgrade: websocket` , `Connection: Upgrade` , `Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=`. Причем любой код ответа отличный от 101 бкдет означать, что handshake не завершен.
    Используется, например в webRTC (Ну или  XMLHttpRequest или Loong pooling). Есть проблема преодоление nat и межсетевых экранов. P2P 3 ситуации - 2 за nat, 1 за nat, 2 без nat (например оба в локальной сети):
        * ICE (Interactive Connectivity Establishment) - протокол, процесс нахождения соединения между двумя клиентами. STUN и TURN - ICE сервера. Сначала логическое соединение, потом физическое.
        * STUN (Session Traversal Utilities for NAT) - сервер позволяет получить инфу о nat, межсетевых экранов, получить публичный IP, IP:NNNN, позволяет создавать необходимые записи в таблице NAT, а также возвращает внешний адрес узла. Публичный. Возвращает обратный адрес, то есть адрес узла отправителя. Узел, находящий за роутером, обращается к STUN серверу, чтобы пройти через NAT. Пакет, пришедший к STUN серверу, содержит адрес источника – адрес роутера, то есть внешний адрес нашего узла. Этот адрес STUN сервер и отправляет обратно. Таким образом, узел получает свой внешний IP адрес и порт, через который он доступен из сети. Далее, WebRTC с помощью этого адреса создает дополнительного кандидата (внешний адрес роутера и порт). Теперь в таблице NAT роутера есть запись, которая пропускает к нашему узлу пакеты, отправленные на роутер по нужному порту.
        * TURN (Traversal Using Relays around NAT) - улучшенный STUN сервер. Может работать как STUN. Позволяет решить проблему когда оба собеседника находятся за симметричным NAT (каждый за своим). Поднять приватный, использовать чьи-то услуги, так как работает как релей, который проксирует трафик. Однако, есть и преимущества. Если p2p коммуникация невозможна (как например, в 3g сетях), то сервер переходит в режим ретранслятора (relay), то есть работает как посредник. Разумеется, ни о каком p2p тогда речь не идет, но за рамками механизма ICE узлы думают, что общаются напрямую. 

• В чем разница между векторной и растровой графикой?
    Вектор - фигуры
    Растр - точки

## Optimisation frontend
    Понять как происходит отрисовка в браузере и предпринять соответствующие шаги.
        1. На основании полученного HTML строится DOM-дерево (Document Object Model).
        2. На основании полученного CSS строится CSSOM-дерево (CSS Object Model).
        3. Применительно к построенным DOM и CSSOM выполняются скрипты.
        4. На основе DOM и CSSOM формируется дерево рендеринга.
        5. На основании дерева рендеринга генерируется макет страницы с указанием размеров и координат всех элементов.
        6. Страница рендерится – выводится на экран.
    * HTML
        * Стили — в первую очередь, скрипты — в последнюю.
        * Повышение доступности. Использование `alt`, ARIA (семантическая разметка) и role атрибуты. Использовать wave.
    * CSS 
        * @media атрибуты
        * Отложенная загрузка CSS, если есть
        * Снижение специфичности `a.navItem` вместо `.header .nav .menu .link a.navItem`
        * Доставка только необходимого. Использовать UnCSS
        * Избегайте CSS-выражений (expressions)
    * JS
        * Асинхронная загрузка скриптов. async
        * Отложенная загрузка скриптов. defer
        * Клонирование узлов перед последующими манипуляциями. Использовать если внесение в DOM многочисленных изменений приводит к нежелательным результатам
        * Использование атрибутов Preload/ Prefetch/ Prerender/ Preconnect.

• Какие методы применяются для оптимизации трафика?
    * Блокировка нежелательного контента (например, рекламы или дополнительного «тяжёлого» оформления)
    * Избегать редиректов 3хх
    * Уменьшать кол-во DNS запросов
    * Кэширование информации (Заголовки `add_header Cache-Control "max-age=31536000, immutable";` например) HTTP-заголовок Expires. Кэш запросов к базе. DNS кэш
    * Приоритизируйте загрузку содержимого
    * Сжатие загружаемых веб-страниц
        * gzip
        * http2
    * Уменьшение качества изображений, CSS-спрайты, минимизация файлов, избавление от лишних css, js
    * Css в начале (Размещение внутренних стилей для контента начального экрана (above the fold) в разделе header). 
        * Critical css. Отдавать сначала критичные стили, затем остальное, наприер при помощи `onload` js или же [loadCSS](https://github.com/filamentgroup/loadCSS) (создает <link rel="stylesheet"> с атрибутом media="only x"). Иметь запасной вариант <noscript>
        * Progressive css. Отдельный css для каждой части страницы, и ссылка на стиль непосредственно перед блоком. Соответственно - последовательная загрузка. __Скорее концепт__
        * Использовать Gulp с разным priority
    * Размещение js в конце.
    * Откладывание загрузки изображений до завершения загрузки страницы. inline img. Загрузка картинки без применения масштабирования (не менять размер тегами, а отдавать сразу в нужном)
    * Оптимизация загрузки шрифтов.
    * Поддомены для параллельного скачивания, в случае http1 (не более 2 компонентов с 1 хоста) или же использование htp/2
    * CDN (Content Delivery Network) для популярных js библиотек и, в ряде случаев, шрифтов.
    * Оптимизация со стороны сервера/бд и т п.

• В чем различие между SVG и Canvas?
    * Scalable Vector Graphics - может быть статическим, динамическим, интерактивным и анимированным. Использует DOM. Медленнее чем Canvas. Гуд для интерфейсов. 
    * Canvas - спека, опеределяющая js API для отрисовки объектов. Работает быстрее. Из пикселей и не использует DOM узлы. Нет специальных функций для анимации. Операции над пикселями. Неиже доступность. Подходит для игр. Может быть:
        * 2D - лучше внедрен. 
        * 3D(WebGL)

• Разница между layout, painting and compositing. 
    Layout: Браузер определит, сколько места занимает каждый элемент и куда его поместить.
    Painting: Это процесс заполнения пикселей. Это связано с извлечением элементов.
    Compositing: Браузер рисует элемент на экране в правильном порядке, чтобы страница отображалась правильно.

• Доступность сайта. 
    Виды доступности:
        * А - низший, доступен людям без отклонений или с легкими отклонениями
        * АА - средний
        * ААА - наивысший, доступен для всех, за редким исключением. 
    Принципы:
        * воспринимаемость - Информация и элементы интерфейса должны быть доступны для восприятия любого пользователя.
        * управляемость - Все элементы интерфейса и навигации доступны для взаимодействия.
        * понятность - Контент и интерфейс в целом должны быть понятны пользователю. Ничего на сайте не должно находится за пределами его понимания.
        * надежность - Контент на сайте должен быть одинаковым для любого пользователя. В том числе для тех, кто работает с вашим сайтом при помощи вспомогательных технологий.

## HTML/CSS and so on

* Разница между progressive enhancement и graceful degradation. feature detection.
    Понятия говорящие о способности системы продолжать своё функционирование в случае отказа некоторых её компонентов. И чем серьёзней отказ, тем ниже качество работы системы и работы с системой.
    * Graceful Degradation - может выражаться в возможности работы при отключённом JavaScript
        Использование noscript.css
    * Progressive Enhancement - строгая и последовательная идеалогия создания веб интерфейсов. Интерфейсы должны создаваться поэтапно, от простого к сложному. На каждом из этапов должен получаться законченный веб-интерфейс, который будет лучше, красивее и удобнее предыдущего.
        * html - логическая разметка
        * css - внешний вид
        * css3 - законченный внешний вид
        * js - интерактивностьы
    * Responsive Design - подход, когда с помощью медиавыражений, резиновых сеток и т. п. достигается адекватное отображение страницы на всех устройствах. mobile first
    * Feature Detection - определение возможностей браузера
        * распарсить юзер-агент, определить версию браузера и писать в коде свитчи по версии браузера;
        * пытаться определять поддержку фич путём проверки нужных полей / вызовов нужных методов
    * Feature inference - предположение возможностей. Суть - обнаружение возможностей вместо обнаружения браузера.
    * Парсинг `user-agent` - определить браузер.

* Ajax и JSONP
    * AJAX (Asynchronous Javascript And Xml) - технология обращения (любое, не обязательно xml) к серверу без перезагрузки страницы.
    Форматы:
        * JSON – для отправки и получения структурированных данных, объектов.
        * XML – если сервер почему-то работает в формате XML, то можно использовать и его, есть средства.
        * HTML/текст – можно и просто загрузить с сервера код HTML или текст для показа на странице.
        * Бинарные данные, файлы – гораздо реже, в современных браузерах есть удобные средства для них.
    * JSONP (JSON with padding) - дополнение json. Проблема состоит в том что политикой безопасности браузера не разрешается делать кросдоменные XHR запросы (тобиш AJAX в простонародьи). Учитывая что приложения должны получать данные с REST API, которое может находиться на другом сервере, то вполне логично что нужно придумать какой-то способ получать  данные и что бы это можно было делать не взирая на ограничения браузера. JSONP предоставляет междоменный доступ к существующему JSON API путём оборачивания начинки JSON в вызов функции.
    * JSONPP (англ. parameterized JSON with padding — «параметризованный JSON с подкладкой») — развитие идеи JSONP. JSONPP включает в себя URL источника, имя функции, которая будет обрабатывать JSON данные, строка для eval после получения данных и строка для eval после окончания обработки данных
    * COMET - любая модель работы веб-приложения, при которой постоянное HTTP-соединение позволяет веб-серверу отправлять (push) данные браузеру без дополнительного запроса со стороны браузера. Чат, аукцион, редактирование.
    * Server side events (поддерживают все кроме IE). По дизайну может меньше чем websocket. При создании объекта `new EventSource(src)` браузер автоматически подключается к адресу `src` и начинает получать с него события. Чтобы соединение успешно открылось, сервер должен ответить с заголовком `Content-Type: text/event-stream`, а затем оставить соединение висящим и писать в него сообщения в специальном формате:
        * Каждое сообщение пишется после `data:`. Если после двоеточия есть пробел, то он игнорируется.
        * Сообщения разделяются двумя строками `\n\n`.
        * Если нужно переслать перевод строки, то сообщение разделяется. Каждая следующая строка пересылается отдельным `data:`.
        * При разрыве соединения пытается его восстановить сам. Прекратить это:
            * Ответить статусом не 200
            * Ответить с `Content-Type` не `text/event-stream`
            * `eventSource.close();`
    * Ajax Long-Polling:
        * Клиент запрашивает веб-страницу с сервера с использованием обычного HTTP (см. HTTP выше)
        * Клиент получает запрошенную веб-страницу и выполняет JavaScript на странице, которая запрашивает файл с сервера.
        * Сервер не сразу отвечает запрошенной информацией, но ждет, пока не появится новая информация.
        * Когда появится новая информация, сервер отвечает новой информацией.
        * Клиент получает новую информацию и немедленно отправляет другой запрос на сервер, повторно запуская процесс.
    * WebSocket - предназначен для решения любых задач и снятия ограничений обмена данными между браузером и сервером. Позволяет пересылать любые данные, на любой домен, безопасно и почти без лишнего сетевого трафика. `var socket = new WebSocket("ws://javascript.ru/ws");`

* Что такое FOUC (Flash Of Unstyled Content)? Как его избежать?
    FOUS - кратковременное появление неоформленных HTML-элементов в некоторых версиях браузеров – сразу же после создания визуальных элементов и до полного применения стилей. Для предотвращения использовать: загрузку стилей в <head> normalize.css; осуществлять проверку аддонами. 

* Чем отличается блочный элемент от строчного?
    Блочные (p div form header nav ul li h1) и строчные (a span b em i cite mark code)
    * Блочные обладают свойствами:
        * Без указанного значения ширины он растягивается на весь родительский контейнер
        * Может быть оформлен полями (margin) или отступами (padding)
        * Без указанного значения высоты он естественным образом растягивается до размера, нужного для размещения внутри него дочерних элементов (предположим, что они не выравнены по какому-либо краю или у них не указано позиционирование)
        * По умолчанию данный элемент будет расположен ниже предыдущего в разметке элемента (предположим, что окружающие элементы не выравнены по какому-либо краю или у них не указано позиционирование)
        * Игнорирует параметр vertical-align
    * Строчные обладают свойствами:
        * Простирается вместе с текстовым контентом
        * Не будет очищать предыдущий контент для того, чтобы перейти на следующую строку (как блочные элементы)
        * Подвержен параметру white-space в CSS
        * Игнорирует параметры верхнего и нижнего поля (margin), но принимает поля по левой и правой сторонам, а также отступы (padding)
        * Игнорирует значения высоты и ширины
        * Если выравнен по левому или правому краю, автоматически станет блочным элементом, обладающим всеми характеристиками блочных элементов
        * Подвержен параметру vertical-align  
    vertical-align (baseline|bottom|middle|sub|super|text-bottom|text-top|top|inherit | значение | проценты) - выравнивает элемент по вертикали относительно своего родителя, окружающего текста или ячейки таблицы. По умолчанию - baseline  

* В чем разница расположения тэга script в body и head?
    В случае полключения внешнего скрипта в body, то браузер не продолжит выполнение, пока не выполнит скрипт.
    В случае с head - скрипт фактически выносится за пределы документа. 
    Если указан async или defer
        * async - Загружает скрипт асинхронно.
        * defer - Откладывает выполнение скрипта до тех пор, пока вся страница не будет загружена полностью.

* Для чего нужен doctype и сколько разновидностей?
    doctype - указание типа документа, инструкция (правила) для браузера как производить анализ, какой режим использовать. 
        * HTML (5, 4.01 Strict, 4.01 Transitional, 4.01 Frameset) - гипертекстовый язык разметки на основе SGML (Standard Generalized Markup Language — стандартный обобщённый язык разметки)
        * XHTML (1.0 Strict, 1.0 Transitional, 1.0 Frameset, 1.1) - расширяемый язык разметки на базе XML. Более строгие правила. Соответственно, если application/xhtml+xml, то любая ошибка сломает
            * Все теги закрыты. Одиночные тоже <img />
            * Вложенность не должна нарушаться
            * Имена атрибутов в нижнем регистре
            * Все спецсимволы “<” и “&” везде, даже в URL, должны заменяться на сущности "&lt;" и "&amp;" соответственно.
            * Все значения атрибутов в " " или ' '
    Strict - строгий. Запрещается использовать устаревшие теги и атрибуты
    Transitional - переходный. 
    Frameset - для работы с фреймами. 
    Режимы:
        * standards mode - соответствует стандартам. При Standards Mode современные браузеры должны одинаково правильно представлять соответствующую стандартам страницу.
        * quirks mode - неопределенное состояние. Режим, в котором имитируются особенности старых стандартов для корректного отображения страниц, написанных для старых браузеров. Если doctype объявлен некорректно или не объявлен то всегда используется. 

* Как следует оформлять страницу, в которой контент может быть на разных языках? Многоязычные сайты?
    Необхоимо учитывать:
        * Кодировка. Использование одной кодировки везде. Unicode, например UTF-8
        * Перевод контента и всех сообщений, плагинов и т. п. с учетом языковых особенностей. 
    Варианты решений:
        * Сайты на поддоменах или отдельных доменах
        * Подкаталоги `sitename.com/ru/` `sitename.com/en/` и т п. Считается лучшим вариантом для seo
        * Использование <q lang="fr">
    Варианты решений со стороны БД:
        * Поля для каждого языка. Для каждого поля для каждого языка в таблице создается отдельная колонка. Проблема - неизвестно сколько таких понадобится. Требуется изменение бд каждый раз при добавлении нового языка
        * Таблица локализации. Для каждой сущности требующей локализации создается две таблицы. Основная таблица, содержащая поля, которые не зависят от конкретного языка и таблица содержащая поля требующие перевода. Также в БД создается таблица со списком доступных языков. Гибко. Структура немного сложнее и предполагает создание таблицы-саттелита для каждой таблицы содержащей локализуемые поля.
        *  Использование сериализованных данных сложной структуры. В каждое поле требующее перевода пишется информация в сериализованном виде, например в JSON, XML, binary, etc. Объект при этом может быть например словарем, в котором ключ — язык, значение — текст. Или любой другой структуры. Целостоность данных зависит уже не только от бд, но и от механизма сериализации. Очень сильно снижается нормализация базы данных.
        * Отдельная запись в таблице для каждого языка. В каждой таблице, которая описывает сущность требующую локализации поле с указанием языка, к которому относится запись. Также в БД создается таблица со списком доступных языков. По сути одному объекту предметной области может соответствовать несколько объектов в БД и несколько связей. ЧТо может достаточно сильно усложнить бизнес-логику.
        * Использование внешних средств локализации. Использование внешних модулей. В случае если необходимо предоставить дотуп к сайту как можно большему числу пользователей.
        * Создание таблицы перевода для каждого языка. Для каждого языка в БД создается отдельная таблица, содержащая поля требующие перевода. При добавлении нового языка необходимо вносить изменения в базу. При большом количестве поддерживаемых языков количество таблиц может быть очень велико.
    Варианты решений для статической информации:
        * Текст хранится в базе и кэшируется при запуске веб-приложения — вариант позволяет потенциально расширять количество поддерживаемых языков. По сути текст становится не статическим, а вполне динамическим контентом.
        * Текст хранится в ресурсных файлах — вариант по быстродействия быстрее предыдущего варианта, но для добавления языка необходима правка файлов веб-приложения
        * Для каждого языкового варианта создается отдельный шаблон, содержащий статический текст — на мой взгляд излишне избыточный вариант. Имеет те же недостатки, что и предыдущий.

* Чем полезны data- атрибуты?
    можно привязать к элементу данные, которые будут доступны в JavaScript.

* В чем отличие атрибутов от свойств?
    Атрибуты – это то, что написано в HTML. (about, data- или dataset, value, class)
        * Строка
        * Не чувствитеьны к регистру
        * Видны в innerHTML
        * Изменение некоторых свойств обновляет атрибут. Но это скорее исключение, чем правило. Чаще синхронизация – односторонняя: свойство зависит от атрибута, но не наоборот. Например, при изменении свойства `input.value` атрибут `input.getAttribute('value')` не меняется
        * Атрибуты можно добавлять, удалять и изменять. Для этого есть специальные методы:
            * setAttribute(name, value) - Устанавливает значение атрибута
            * getAttribute(name) - Получить значение атрибута
            * hasAttribute(name) - Проверить, есть ли такой атрибут
            * removeAttribute(name) - Удалить атрибут
    Свойство – это то, что находится внутри DOM-объекта (name, href, src, alt)
        * Любое значение
        * Регистрозависимы
        * Не видны в innerHTML
    Синхронизация - браузер синхронизирует значение ряда свойств с атрибутами. Если меняется атрибут, то меняется и свойство с этим именем. И наоборот.

* В чем отличие тэгов article, footer, header от div?
    article, footer, header - семантические теги (микроразметка), помогающие корректно определить значимость области поисковикам, скринридерам и т. п. 
    Еще семантические теги: nav, hgroup(удален), section, aside, figure

* Зачем нужен атрибут <srcset>?
    Появился в html5 для <img>. Может использоваться вместо `src` и задавать URL изображений. Значение - одна или несколько строк, разделенных запятой. В состав каждой входят:
        * URL файла с изображением, optionally, whitespace followed by one of:
        * Значение ширины viewport (им должно быть положительное целое число, за которым следует символ «w»). The width descriptor is divided by the source size given in the sizes attribute to calculate the effective pixel density.
        * Значение плотности пикселей (положительное число, за которым следует символ «x»), по умолчанию равно 1x.
    Нельзя смешивать в одном атрибуте srcset width descriptors и pixel density descriptors. Duplicate descriptors (for instance, two sources in the same srcset which are both described with '2x') are invalid, too.
    User agent'ы могут выбирать любой из указанных источников, что даёт им относительную свободу выбора на основании, к примеру, пользовательских настроек и скорости соединения.

* Какие есть селекторы в CSS?
    Селекторы позволяют очень точно указывать к каким элементам применять CSS-свойства.
    Селектор тега, class, id, универсальный селектор *, селекторы атрибутов a[]

* Как браузер определяет приоритет стилей по селекторам?
    Изначально стили браузера -> автора -> пользователя -> автора !important -> пользователя 
    Каскадность. Специфичность селекторов (selector's specificity) определяет их приоритетность в таблице стилей. Чем специфичнее селектор, тем выше его приоритет.
    Спецефичность - условная величина вычисляемая и выражаемая в N. Чем больше N, тем выше приоритет. Вычисление - каскадно, справа налево, без +
    * Селектор тега - 1
    * Селектор класса (class, псевдоклас (pseudo-classes (checked, visited, active, last-child, nth-child, hover)) - 10 
    * Селектор id и псевдоэлементами (pseudo-elements (after, before, selection, first-line, first-letter)) - 100 
    * inline-style - 1000
    * inline-style перекрывает все селекторы описанные в стилях. !important перекрывает в том числе и встроенные стили.
    Псевдоклассы (стиль для состояния, : ) и псевдоэлементы (ключевые слова к селекторам, ::, выделить часть )
    Селектор - последовательность простых селекторов, разделенных пробелами либо символами ">" и "+"

* Какие единицы измерения есть в CSS?
    * px = 1 точка
    * em = значению font-size родителя
    * rem = значению font-size <html> (корневого элемента документа)
    * % относительно родительского элемента
    * vw = 1% от ширины окна
    * vh = 1% от высоты окна
    * vmin = меньший от 1vw или 1vh
    * vmax = больший от 1vw или 1vh
    * ex = размер символа "x"
    * ch = размер символа "0" , размеры присутствуют в шрифте всегда, даже если по коду этих символов в шрифте находятся другие значения, а не именно буква "x" и ноль "0". В этом случае они носят более условный характер.
    Умерли, но были:
        * 1mm (мм) = 3.8px
        * 1cm (см) = 38px
        * 1pt (типографский пункт) = 4/3 px 
        * 1pc (типографская пика) = 16px

* Что такое Flexbox?
    Flexible Box Layout Module — модуль макета гибкого контейнера — представляет собой способ компоновки элементов.
    CSS раскладки:
        * Table (html и css таблицы). Достаточно объявления `display:table` или `display: table-cell` 
        * Css layout
        <!-- * inline-block layout - зависят от свойства vertical-align  -->
        * Position 
        * Float - передвижение(извлечение) блоков внутри потока (обтекаемые блоки). Меняет не только элемент, но и его предков, родственников, потомков и следующие за ним элементы. Часто испольуется с clean - очистка. Если элемент содержит только float - схлопывается.
            * Если значение left или right:
                * Элемент отображается как блочный, так словно ему установлено свойство display: block;
                * Элемент по ширине сжимается до размеров содержимого, если для элемента явно не установлена ширина width;
                * Элемент прилипает к левому (left) или правому краю (right);
                * Все остальное содержимое страницы, идущее в HTML коде после элемента с float, обтекает его;
        * Template Layout Module - альтернатива float. Grid - сетка. Если flexbox - одно измерение, то grid - два

* Свойства block
    Для расположения элементов есть три типа отображения, о которых вам стоит знать. Вот основные различия между тем, как эти три типа отображения влияют на раскладку:
        * block — Моя ширина ограничена моим родителем. На меня влияют свойства width и height. Моя высота зависит от моего контента.
        * inline — Моя ширина и высота определяются моим контентом и значения свойств width и height не влияют на меня. Думайте обо мне как о слове в параграфе.
        * inline-block — Я такой же как block, но моя ширина зависит от моего контента

* Свойства position 
    * static — Значение по умолчанию. Свойства позиционирования top, bottom, right и left игнорируются.
    * absolute — Элемент будет сдвинут со своей естественной позиции в раскладке и спозиционирован относительно своего ближайшего спозиционированного родителя при помощи свойств позиционирования.
    * fixed — Элемент будет сдвинут со своей естественной позиции в раскладке и его позиция будет высчитываться от края окна. На мобильных устройствах с зумом поведение может быть непредсказуемым.
    * relative — В отличие от absolute или fixed, элемент остается на своем естественном месте в раскладке и свойства top, right, bottom и left только выталкивают его с его естественной позиции

* Свойства box-sizing
    * content-box — значение по умолчанию. При вычислении размеров блока размеры padding и border не принимаются в расчет. Свойства width и height задают ширину и высоту контента и не включают в себя значения отступов, полей и границ.
    * border-box — При вычислении размеры padding и border включаются в общие размерам блока.


## JS ans so on
• Какие типы данных есть в JavaScript?
    * bool, function(), Null, string, number, undefined, object. NaN
    Причем любой объет - хэш-таблица, а каждое свойство объекта, включая имя метода это ключ хеш-таблицы. 
    Если же нужны массивы, то у них есть splice(). Не удалять из массива delte, иначе на пустом месте остается undefined 
    typeof() возвращает не тип, а строку, которая зависит от аргумента и не является именем типа. Поэтому Null - object, object {key:value} - object, а object (function) - function. Массив тоже object (Array.isArray(myVar))
    При создании function() создается похожий на массив объект (т. к. обладает length) arguments, содержащий все передаваемые в функцию аргументы. Объявление переменной arguments внутри функции приводит к замене/переопределению исходного объекта arguments. Свойства arguments:
        * callee (ссылка на функцию, выполняющуюся в данный момент), 
        * length 
        * caller (ссылка на функцию, которая вызвала данную). 
        свойства callee и caller являются устаревшими и не работают в строгом режиме
        Создать из arguments полноценный массив `var args = Array.prototype.slice.call(arguments);

* Что такое memoization?
    Мемоизация — сохранение результатов выполнения функций для предотвращения повторных вычислений, ускорения работы. Функция с мемоизацией - чистая. 

* В чем отличие == от ===?
    * == не строгое сравнение. перед сравнением преобразование типов.
    * === строгое сравнение. Например `[1, 2, 3] === [1, 2, 3]; // false` так как это разные массивы, по случайности имеющие одинаковыые данны. С объектами будет то же самое.

* Undeclared, Undefined, null
    Undefined - неопределенное свойство
    Undeclared - необъявленное. При обращении выдает ошибку типа 
        `console.log(obj.test)` // свойство не определено в объекте
        // undeclared
        `console.log(test)`
        //ReferenceError: test is not defined
    null - существующая переменная со значением null

* Hosting 
    hosting - эффект поднятия переменной

* this
    this в js ссылка на тот объект, в котором в данный момент исполняется код, а не на тот, в котором вы напишите это ключевое слово. Например, если используются this в callback’e/обработчике событий(onclick, onload и т.д.) переданном в метод объекта, то он будет указывать на тот объект, которому принадлежит метод/элемент DOM где произошло событие, а не на тот где вы определили callback
    Для решения используется:
        * сохранить this в переменную
        * .bind(). Возвращает обертку над ней для вызова в контексте объекта, а не изменяет функцию.

* Strict Mode
    Strict Mode - строгий режим. 
        * делает невозможным случайное создание глобальных переменных. 
        * Вызывает исключения/ошибки (TypeError) при работе с переменными, значение которых равно undefined
        * заставляет присваивания, которые всё равно завершились бы неудачей, выбрасывать исключения
        * В строгом режиме попытки удалить неудаляемые свойства будут вызывать исключения (в то время как прежде такая попытка просто не имела бы эффекта)
        * свойства, перечисленные в сериализованном объекте, встречались только один раз. 
        * имена аргументов в объявлении функций встречались только один раз. 
        * Запрещает синтаксис восьмеричной системы счисления. Восьмеричный синтаксис не является частью ECMAScript, но поддерживается во всех браузерах с помощью дописывания нуля спереди к восьмеричному числу: 0644 === 420 и "\045" === "%". 
        * Запрещает использование with. Проблема с with в том, что во время выполнения любое имя внутри блока может ссылаться как на свойство обрабатываемого объекта, так и на переменную в окружающем (или даже в глобальном) контексте -- невозможно знать об этом заранее. Строгий режим считает with синтаксической ошибкой
        * оля объекта arguments не связаны с проименованными аргументами функции, а являются их продублированными копиями значений. 

* Разница между событиями document load и document ready?
    `$(document).ready` - возникает в момент готовности дерева DOM, то есть не ожидает загрузки изображений. То же самое `$(function() { code });`
    `$(window).load` - начнёт работу когда будет готов весь DOM включая элеманты, обладающие поляи URL (объект window, картинки, скрипты, фреймы). Такой вызов подойдёт если мы хотим работать с изображениями (расчёт размеров изображения). Данный вызов, как и предыдущий является jQuery событием.
    `onload` - стандартное событие DOM, не зависит от Jquery. Имеет такую же функциональность как `$(window).load`. Выполняется когда будет загружен объект. 

* Расширять или не расширять нативные js объекты?
    NOE - нативный объект это 
    + monkey patching
    + В случае полифиллов. (Полифилл» (англ. polyfill) – это библиотека, которая добавляет в старые браузеры поддержку возможностей, которые в современных браузерах являются встроенными.  библиотека ES5 shim.)
    +/- допустимо при тщательном документировании
    - Поддерживаемость. Может вызвать конфликт. Не всегда понятно откуда мог взяться метод. Может нарушить чужой код
    - Возможность затереть уже существующий метод
    Решение проблем SugarJS (но не в библиотеках)

* Что такое method chaining? В чем суть этого приема?
    Method chaining нужен для сокращения кода, в сдучаях, когда при использовании или написании больших классов возникает необходимость вызвать подряд несколько методов объекта этого класса. Подводные камни - порядок вычисления аргументов и вызовов функций.
        * определен с помощью значения, возвращаемого методом;
        *наследуется (в качестве нового контекста используется предыдущий);
        * прекращается возвращением ничего не значащего значения (void).
    В js Method chaining - текучий интерфейс.
        // Обычная реализация
        myCar2 = Car();
        myCar2.setSpeed(100);
        myCar2.setColor('blue');
        myCar2.setDoors(5);
            
        // Текучий интерфейс
        myCar = Car();
        myCar.setSpeed(100).setColor('blue').setDoors(5);
• event delegation
    Всплытие. Заключается в том, что если у нас есть много элементов, события на которых нужно обрабатывать похожим образом, то вместо того, чтобы назначать обработчик каждому – мы ставим один обработчик на их общего предка. Из него можно получить целевой элемент event.target, понять на каком именно потомке произошло событие и обработать его.
    Упрощает инициализацию и экономит память: не нужно вешать много обработчиков. 
    Меньше кода: при добавлении и удалении элементов не нужно ставить или снимать обработчики.
    Удобство изменений: можно массово добавлять или удалять элементы путём изменения innerHTML.
    Событие должно всплывать. Нельзя, чтобы какой-то промежуточный обработчик вызвал event.stopPropagation() до того, как событие доплывёт до нужного элемента.
    Делегирование создает дополнительную нагрузку на браузер, ведь обработчик запускается, когда событие происходит в любом месте контейнера, не обязательно на элементах, которые нам интересны. Но обычно эта нагрузка настолько пустяковая, что её даже не стоит принимать во внимание.
    Алгоритм:
        * Вешаем обработчик на контейнер.
        * В обработчике: получаем event.target.
        * В обработчике: если event.target или один из его родителей в контейнере (this) – интересующий нас элемент – обработать его.

* immutable
    Неизменяемые объекты. Объект, состояние которого не может быть изменено после создания. Результатом любой модификации такого объекта всегда будет новый объект, при этом старый объект не изменится. Immutable.js, Mori, Seamless-Immutable. Использование .freze()

* bubbling Всплытие и перехват.
    bubbling (всплытие) - При наступлении события обработчики сначала срабатывают на самом вложенном элементе, затем на его родителе, затем выше и так далее, вверх по цепочке вложенности.
    Самый глубокий элемент, который вызывает событие, называется «целевым» или «исходным» элементом и доступен как event.target.
        * event.target – это исходный элемент, на котором произошло событие, в процессе всплытия он неизменен.
        * this – это текущий элемент, до которого дошло всплытие, на нём сейчас выполняется обработчик.
    Для остановки всплытия нужно вызвать метод event.stopPropagation().

* closure/замыкание
    Функция и ее лексическая область видимости. «замыкание функции», подразумевают не саму эту функцию, а именно внешние переменные.
    * Все переменные и параметры функций являются свойствами объекта переменных LexicalEnvironment. Каждый запуск функции создает новый такой объект. На верхнем уровне им является «глобальный объект», в браузере – window.
    * При создании функция получает системное свойство [[Scope]], которое ссылается на LexicalEnvironment, в котором она была создана.
    * При вызове функции, куда бы её ни передали в коде – она будет искать переменные сначала у себя, а затем во внешних LexicalEnvironment с места своего «рождения».
        обычно используется для обеспечения конфиденциальности данных объектов.
    * Каждая функция при создании получает ссылку [[Scope]] на объект с переменными, в контексте которого была создана.
    * При создании функции с использованием new Function, её свойство [[Scope]] ссылается не на текущий LexicalEnvironment, а на window.
    * Модуль при помощи замыканий – это оборачивание пакета функционала в единую внешнюю функцию, которая тут же выполняется.

* Отличия .map и .forEach
    .map - создает новый массив с результатами выхова
    .forEach - ничего не возвращает. Просто более элегантный for

* Отличия Split vs. Splice
    * split - позволяет превратить строку в массив, разбив ее по разделителю s. необязательный второй аргумент – ограничение на количество элементов в массиве. Если их больше, чем указано – остаток массива будет отброшен. не изменяет переданную строку.
    * join(str) - делает в точности противоположное split. Он берет массив и склеивает его в строку, используя str как разделитель.
    * delete - удаляет пару ключ-значение и оставляет дыру
    * shift - удаление элемента из начала массива
    * pop - удаление элемента с конца
    * Splice - универсальный раскладной нож для работы с массивами. Умеет все: удалять элементы, вставлять элементы, заменять элементы – по очереди и одновременно.
    `arr.splice(index[, deleteCount, elem1, ..., elemN])` - Удалить deleteCount элементов, начиная с номера index, а затем вставить elem1, ..., elemN на их место. Возвращает массив из удалённых элементов.
    * slice(begin, end) копирует участок массива от begin до end, не включая end. Исходный массив при этом не меняется.
    * sort - сортировка по unicode. arr.sort(fn) - своя сортировка
    * reverse() меняет порядок элементов в массиве на обратный.
    * concat(value1, value2, … valueN) создаёт новый массив, в который копируются элементы из arr, а также value1, value2, ... valueN.
    * indexOf(searchElement[, fromIndex])» возвращает номер элемента searchElement в массиве arr или -1, если его нет.
    * lastIndexOf(searchElement[, fromIndex])» ищет справа-налево: с конца массива или с номера fromIndex, если он указан.
    * Object.keys(obj) - возвращает массив свойств объекта.
    
* Экспорт и импорт.
    * Export можно ставить:
        * перед объявлением переменных, функций и классов.
        * отдельно, при этом в фигурных скобках указывается, что именно экспортируется.
    * Import `import {one, two} from "./nums";`
        * "./nums" – модуль, как правило это путь к файлу модуля.
        * one, two – импортируемые переменные, которые должны быть обозначены в nums словом export.
        * В фигурных скобках указываются значения, а затем – модуль, откуда их брать: import {a, b, c as d} from "module".
        * Можно импортировать все значения в виде объекта при помощи import * as obj from "module".
        * Без фигурных скобок будет импортировано «значение по умолчанию»: import User from "user".
    * export default - один модуль экспортирует одно значение
    Библиотеки:
        * AMD – одна из самых древних систем организации модулей, требует лишь наличия клиентской библиотеки, к примеру, require.js, но поддерживается и серверными средствами.
        * CommonJS – система модулей, встроенная в сервер Node.JS. Требует поддержки на клиентской и серверной стороне.
        * UMD – система модулей, которая предложена в качестве универсальной. UMD-модули будут работать и в системе AMD и в CommonJS.

* advantages/disadvantages of writing JavaScript code in a language that compiles to JavaScript?
    + Классы
    + Типы
    + Features
    -  transpiling and bundling.
    - The number of developers familiar with what you are doing is smaller.
    - Can’t think of another one offhand.

* JavaScript module pattern
    Module pattern - прием проектирования, цель которого скрыть внутренние детали реализации скрипта. В том числе: временные переменные, константы, вспомогательные мини-функции и т.п. Возвращает только публичную часть API, оставляя всё остальное доступным только внутри замыканий.
    Важно:
        * Обращать внимание на области видимости. Создавать модулю(скрипту) свою область видимости, например `(function() {var n = "hello"; alert(n)}());` вместо `function() {var n = "hello"; alert(n)}();`. Дело в том, что «на месте» разрешено вызывать только Function Expression. Правило:
            * Если браузер видит function в основном потоке кода – он считает, что это Function Declaration.
            * Если же function идёт в составе более сложного выражения, то он считает, что это Function Expression.
        Скобки показывают, что у нас Function Expression, который по правилам JavaScript можно вызвать «на месте».
        Второй способ - поставить перед функцией оператор `+` или `!`

* Типы объектов. Что такое host объект?
    * Встроенные объекты: String, Math, RegExp, Object, Function и т.д. - основные предопределенные объекты, всегда доступные в JavaScript.
    * Host objects (Объекты хоста): объекты типа window, Event, HTMLElement, XMLHttpRequest, узлы DOM и т.д., которые предоставляются средой браузера. Они отличаются от встроенных объектов, потому что не все окружения будут иметь одни и те же объекты хоста. Если JavaScript работает за пределами браузера, например, на языке сценариев на стороне сервера, например, в Node.js, будут доступны разные объекты хоста.
    * Объекты пользователя: объекты, определенные в JavaScript-коде.

* В чем разница между .call и .apply?
    .call и .apply обе выполняют вызов функции (метода объекта) с подменой контекста. В отличии от `.` .call и .apply принимают в качестве первого аргумента this. Но 
    * call - вызов функции с подменой контекста - this внутри функции. Принимает явный список аргументов.
    * apply - вызов функции с переменным количеством аргументов и с подменой контекста. Принимает массив со списком аргументов.
    * bind (Function.prototype.bind) - создает обертку, которая подменяет контекст этой функции. Поведение похоже на call и apply, но, в отличие от них, bind не вызывает функцию, а лишь возвращает "обёртку", которую можно вызвать позже. Кроме того, bind умеет подменять не только контекст, но и аргументы функции, осуществляя каррирование.
    * map - изменение каждого элемента в массиве.
    * filter - похож на map, но возвращаемый массив содержит только те элементы, которые удовлетворяют заданному условию, передаваемому функции в качестве параметра. Данная функция должна возвращать логическое значение – если она вернет true, то элемент добавляется в результирующий массив.
    Каррирование - преобразование функции от многих аргументов в набор функций, каждая из которых является функцией от одного аргумента.

* Что такое дескрипторы?
    Дескриптор - основной метод для управления свойствами – Object.defineProperty ( `Object.defineProperty(obj, prop, descriptor)` ). Позволяет объявить св-ва объекта и изменить аспекты. запрещено одновременно указывать значение value и функции get/set. 
    obj - Объект, в котором объявляется свойство.
    prop - Имя свойства, которое нужно объявить или модифицировать.
    descriptor - Дескриптор – объект, который описывает поведение свойства.
        value – значение свойства, по умолчанию undefined
        writable – значение свойства можно менять, если true. По умолчанию false.
        configurable – если true, то свойство можно удалять, а также менять его в дальнейшем при помощи новых вызовов defineProperty. По умолчанию false.
        enumerable – если true, то свойство просматривается в цикле for..in и методе Object.keys(). По умолчанию false.
        get – функция, которая возвращает значение свойства. По умолчанию undefined.
        set – функция, которая записывает значение свойства. По умолчанию undefined.
    * Дескрипторы данных. По умолчанию false
    * Дескрипторы доступа - определяют доступ к конкретному значению через getter-ы и setter-ы функций. Если не установлены, то по умолчанию равны undefined.
    Вместо дескрипторов можно использовать скобочную нотацию `<bracket-access> ::= <identifier> "[" <expression> "]"`
        * identifier — это переменная, которая хранит объект, содержащий свойство, значение которого мы хотим установить.
        * expression — любое валидное JavaScript-выражение, определяющее имя свойства.

* классическое и прототипное наследование.
    * Классическое - не поддерживается js в его полном представлении. 
    Имеет два типа абстракций. Класс и объект. 
        * Класс - абстракция объекта или другого класса.
        * Объект - абстракция объекта реального мира. Объекты в классических объектно-ориентированных языках программирования могут быть созданы только посредством
        Классические объекты определяются абстрактно как часть некоторой концептуальной группы и наследуют характеристики других классов или групп объектов.
    * Прототипное наследование
    Все есть объект. Объекты определяются конкретно как специальные объекты и наследуют поведение других специальных объектов.
    Шаблоны:
        * Прототипная схема прототипного наследования
        * Шаблон конструктора прототипного наследования (js, так как хотели под java, у которого классическое наследование)
    Прототипное (делегирующее) - почти js. Объекты наследуют свойства от других объектов путем создания нового или клонирования существующего + спец. свойства.
    В прототипальных объектах наследования наследуются от других объектов. Конструкторы никогда не попадают в картину. 
    Конструкторы выглядят как классы, они не ведут себя как классы
    Шаблон конструктора в JavaScript - это прототипный шаблон, инвертированный. Вместо создания объекта вы создаете конструктор. Ключевое слово new связывает указатель this внутри конструктора с клоном prototype конструктора.
        * Прототип - готовый к использованию объект, не нуждающийся в инстанцировании. Он может иметь собственное состояние (state). Можно сказать что прототип является классом и экземпляром объединенными в одну сущность, грубо говоря, Singleton'ом.
        * Вызов конструктора при создании объекта (клонировании прототипа) не обязателен.
        * Один объект может ссылаться на другой, что делает его прототипом. Если при обращении к свойству/методу оно не будет найдено в самом объекте, поиск продолжится в прототипе, а далее в прототипе прототипа и т.д.
    * Функциональное наследование
        - прототипной и псевдоклассической моделей является то, что они не обеспечивают конфиденциальности элементов

* Наследование в javascript
    В js нет привычного наследования. Прототипное наследование.
    1. Шаблон конструктор класса
    Особый тип функции называемых конструкторами, которые действуют так же, как и конструкторы в других языках. Функции-конструкторы вызываются только с помощью ключевого слова new и связывают создаваемый объект с контекстом функции-конструктора через ключевое слово this. 
        `function Class(){/*тут инициализируем поля *}`
        А потом, через прототип, добавить методы, константы и статические переменные, которые будут одни на все экземпляры.
        `Class.prototype = {/*Методы*/}`
    Или
        function Animal(type){
            this.type = type;
        }
        Animal.isAnimal = function(obj, type){
            if(!Animal.prototype.isPrototypeOf(obj)){
                return false;}
            return type ? obj.type === type : true;};

            function Dog(name, breed){
            Animal.call(this, "dog");
            this.name = name;
            this.breed = breed;}
        Object.setPrototypeOf(Dog.prototype, Animal.prototype);
        Dog.prototype.bark = function(){
            console.log("ruff, ruff");};
        Dog.prototype.print = function(){
            console.log("The dog " + this.name + " is a " + this.breed);};

        Dog.isDog = function(obj){
            return Animal.isAnimal(obj, "dog");};
    2. Определение класса
        class Animal {
            constructor(type){
                this.type = type;
            }
            static isAnimal(obj, type){
                if(!Animal.prototype.isPrototypeOf(obj)){
                return false;
                }
                return type ? obj.type === type : true;
            }
        }
        class Dog extends Animal {
            constructor(name, breed){
                super("dog");
                this.name = name;
                this.breed = breed;
            }
            bark(){
                console.log("ruff, ruff");
            }
            print(){
                console.log("The dog " + this.name + " is a " + this.breed);
            }
            static isDog(obj){
                return Animal.isAnimal(obj, "dog");
            }
        }
    3. Явное объявление прототипа, Object.create, фабричный метод
    Прототип объявляется явно. Понятно что определено в прототипе, а что определено в самом объекте. Метод Object.create удобен, потому что он позволяет создать объект от указанного прототипа.
    var Animal = {
        create(type){
            var animal = Object.create(Animal.prototype);
            animal.type = type;
            return animal;
        },
        isAnimal(obj, type){
            if(!Animal.prototype.isPrototypeOf(obj)){
            return false;
            }
            return type ? obj.type === type : true;
        },
        prototype: {}
        };
        var Dog = {
        create(name, breed){
            var proto = Object.assign(Animal.create("dog"), Dog.prototype);
            var dog = Object.create(proto);
            dog.name = name;
            dog.breed = breed;
            return dog;},
        isDog(obj){
            return Animal.isAnimal(obj, "dog");},
        prototype: {
            bark(){
            console.log("ruff, ruff");},
            print(){
            console.log("The dog " + this.name + " is a " + this.breed);}
            }
        };
    4. Object.create, фабрика верхнего уровня, отложенный прототип
    небольшим изменение способа 3, где сам класс является фабрикой, в отличии от случая когда класс является объектом с фабричным методом. Похоже, на пример конструктора (способ 1), но использует фабричный метод и Object.create.

    Когда много родительских классов `this.super.super.super.someMethod.apply(this)`

* В чем различие между асинхронным и синхронным кодом?
    * Синхронный - последовательно
    * Асинхронный - event-loop. При возникновении некоторого события оно помещается в конец очереди. Поток, который обрабатывает эту очередь, берет событие с начала очереди, и выполняет связанный с этим событием код. Не использовать блокирующих операций, использовать события вместо циклов. Сравним по производительности с многопоточным.
    * Многопоточный - создается пул потоков, каждому из которых передается задача для выполнения.

* Какие есть паттерны для работы с асинхронным кодом?
    * Основными функциями асинхронного кода JavaScript являются setTimeout и setInterval
    * Ajax - асинхронный js с jquery. Самое кроссбраузерное решение. 
    * async/await - используются в промисах
    * callback - функция высшего порядка. 
    * Promises - прокси объект, который представляет еще не известное, до выполнения функции, значение. Промисы тоже используют коллбеки, так как then и catch регистрируют коллбеки. Можем выполнять ajax запрос, возвращающий promise. удобный способ организации асинхронного кода.
        * pending - ожидание
        * fulfilled - успех
        * rejected - ошибка
    * Генераторы yield - могут приостанавливать своё выполнение, возвращать промежуточный результат и далее возобновлять его позже, в произвольный момент времени.
        `function* generateSequence() {
            yield 1;
            yield 2;
            return 3;
        }`
        Функция высшего порядка — это функция, которая может принимать другую функцию в качестве аргумента или возвращать другую функцию в качестве результата.

* Джаваскрипт однопоточный или многопоточный?
    * Однопоточный, но асинхронный

* В чем различие между описанием функций и функциональными выражениями?
    Function Declaration – функция, объявленная в основном потоке кода.
    Function Expression – объявление функции в контексте какого-либо выражения, например присваивания.
    Функции, объявленные как Function Declaration, создаются интерпретатором до выполнения кода.
    * Объявление. 
        * Функция Function Declaration
        `function name([param[, param[, ... param]]]) { statements }`
            * Имя доступно в той области видимости, где функция была определена.
            * Создаются интерпретатором до выполнения кода, соответственно могут быть вызваны до объявления.
        * Функция-выражение Function Expression
        `function [name]([param] [, param] [..., param]) { statements }`
            * Наследует текущую область видимости, то есть создаёт замыкание.
            * Её имя доступно только внутри самой функции.
            * Функция-выражение похожа на определение функции и имеет такой же синтаксис
            * Функциональное выражение, которое не записывается в переменную, называют анонимной функцией.
        * Стрелочная 
        `([param] [, param]) => { statements }`
        param => expression
            * Отличаются более кратким синтаксисом 
            * Лексически связывают значение своего this
        * Конструктор. Не рекомендуется.
        `new Function (arg1, arg2, ... argN, functionBody)`
            * Нет имени
            * Функции, определённые через функцию-выражение и объявление функции парсятся только один раз, в отличиии от функций, созданных с помощью конструктора. 
        Имя функции и переменная, к которой функция приравнена — это не одно и то же. Имя функции нельзя менять, а вот переменной, к которой приравнена функция, можно дать другое значение. 

* Что нового появилось в ES2015?
    ES6 == ES2015. Транспайлеры.
    * Spread Operator `(...args)`
        * Отменяет необходимость apply (call, bind, apply)
        * упрощенная конкатенация: `[1, 2, ...[3, 4, 5], 6, 7];`
        * Spread используется для разделения коллекций на отдельные элементы rest, наоборот, для соединения отдельных значений в массив.
    * Rest parameters – это как arguments, только лучше.
        * Cигнатура метода объявляется как function foo (...everything) {};
        * everything – это массив со всеми параметрами, переданными в foo;
        * Можно присвоить имя нескольким параметрам перед ...everything, например: function foo (bar, ...rest) {}; эти параметры будут исключены из ...rest;  ...rest должен быть последним параметром в списке.
        * rest для соединения отдельных значений в массив.
    * Assignment Destructuring - синтаксис присваивания, при котором можно присвоить массив или объект сразу нескольким переменным, разбив его на части. `let [firstName, lastName] = ["Илья", "Кантор"];`
    Или
        var f = function() {
            return ['this', 'is', 'array'];
        };
        // ES6 destructuring для массивов
        var [ first, second, third ] = f();
        console.log(first, second, third); // this is array
    * Template Literals (Шаблонные строки)
        * Можно объявлять при помощи обратных кавычек (`) в дополнение к одинарным и двойным.
        * Могут быть многострочными
        * Позволяют производить промежуточные вычисления `ponyfoo.com is ${rating}`, где rating – это переменная.
        * Можно вычислять любое валидное js-выражение, например: `${2 * 3}` или `${foo()}`.
        * Можно использовать помеченные шаблоны, чтобы изменить логику вычисления промежуточных значений
    * Object Literal (Литералы объектов)
        * Вместо `{ foo: foo }`, можно писать просто `{ foo }` – сокращенная форма записи пары свойство–значение.
        * Вычисляемые имена свойств: { [prefix + 'Foo']: 'bar' }, где prefix: 'moz' возвращает { mozFoo: 'bar' }.
        * Нельзя одновременно писать сокращенно и вычислять имя свойств.
        * Определения методов можно сделать более лаконичными при помощи следующего синтаксиса: { foo () {} }.
    * Стрелочные функции
        * Укороченая запись.
        * Функциональщина
        * Несколько способов использования. 
        * Привязаны к лексическому окружению (this это тот же контекст this, что и в родительском лексическом окружении; this нельзя изменить при помощи .call, .apply)
    * Class 
        * Синтаксический сахар для наследования прототипов (От нормальных классов отличается прототипным наследованием )
        * Синтаксис похож на объявление объектов class Foo {}.
        * Методы экземпляра new Foo().bar объявляются при помощи упрощенного синтаксиса литералов объекта class Foo { bar () {} }.
        * Статические методы – Foo.isPonyFoo() – нуждаются в префиксе, ключевом слове static class Foo { staticisPonyFoo () {} }.
        * Метод конструктора class Foo { constructor () { /* initialize instance */ }.
        * Прототипное наследование с упрощенным синтаксисом class PonyFoo extends Foo {}.
    * Let и Const
        * Let 
            * Блочная область видимости. Соответственно поднятие (hoisting) в рамках блока
        * Const
            * Блочная область видимости. 
            * Делает неизменяемой только примитивные типы (number, string ...). В случае объектов:
                * const foo = { bar: 'baz' } значит, что foo всегда будет ссылаться на объект в правой части выражения; Свойства, методы и т. п. Можно изменять.
        * Определение с таким же именем в пределах области видимости - ошибка

* Что нового появилось в ES2017?
    * Оф. Асинхронные функции
        * Оператор asynk
        * Оператор await
    * Object.values и Object.entries - облегчат работу с объектами
        * Object.entries() Данная функция возвращает массив собственных перечисляемых свойств объекта в формате [ключ, значение]. свойство, ключом которого является символ, будет проигнорировано. итерации по свойствам объекта с помощью цикла for-of
        * Object.values() похожа на Object.entries(). На выходе мы получим массив, состоящий только из значений собственных свойств, без ключей. Что, в принципе, можно понять из названия.
    * «Висячие» запятые в параметрах функций. Теперь законно оставлять запятые в конце списка аргументов функций. При вызове функции запятая в конце тоже вне криминала.
    *  два новых метода для работы со строками: padStart() и padEnd().
        * padStart() подставляет дополнительные символы перед началом строки, слева. 
        * padEnd(), в свою очередь, справа, после конца строки.
    * Функция Object.getOwnPropertyDescriptors() Функция возвращает массив с дескрипторами всех собственных свойств объекта.
        * Для копирования свойств объекта, в том числе геттеров, сеттеров, неперезаписываемых свойств.
        * Копирование объекта. .getOwnPropertyDescriptor можно использовать в качестве второго параметра в Object.create().
        * Создание кроссплатформенных литералов объектов с определенным прототипом.
        * Методы с super не могут быть скопированы, поскольку тесно связаны с изначальным объектом.
    * Разделение памяти и объект Atomics не может использоваться как конструктор, но имеет ряд собственных методов, которые призваны решить проблему безопасности при выполнении различных операций с типизированными массивами SharedArrayBuffer. Конструкция SharedArrayBuffer и уже существовавшие ранее TypedArray and DataView помогают распределять доступную память. Это обеспечивает необходимый порядок выполнения операций при одновременном использовании общей памяти несколькими потоками.
    Объект SharedArrayBuffer является примитивным строительным блоком для высокоуровневых абстракций. Буфер может использоваться для перераспределения байтов между несколькими рабочими потоками. У этого есть два явных преимущества:
        * Повышается скорость обмена данными между воркерами.
        * Координация между воркерами становится быстрее и проще (по сравнению с postMessage()).

* static method зачем?
    static, определяет статический метод для класса. Статические методы вызываются без инстанцирования их класса, и не могут быть вызваны у экземпляров (instance) класса.          * Статические методы, часто используются для создания служебных функций для приложения.
    * Статические методы недоступны напрямую, используя ключевое слово this из нестатических методов. Вам нужно вызвать их с помощью имени класса: CLASSNAME.STATIC_METHOD_NAME() или вызовом метода как свойства конструктора: this.constructor.STATIC_METHOD_NAME().

* Event loop
    Модель событийного цикла (event loop) называется так потому, что отслеживает новые события в цикле:
    0. закрытие цикла (остановка всех наблюдателей за событиями, наблюдателей сигналов, освобождение памяти выделенной под наблюдатели) и освобождение памяти зарезервированной самим циклом. uv_run
    1. loop_alive - проверяет наличие активных обработчиков или запросов. От результата выполнения этой функции будет зависеть запустится ли цикл “while” или нет. В случае отсутствия запросов или обработчиков, функция-запуска просто обновит время выполнения событийного цикла и тут же завершится. Если же есть что обрабатывать (r != 0) и флаг остановки не установлен (stop_flag == 0), то цикл запустится. И первым действием в итерации цикла будет тоже обновление времени выполнения (uv__update_time).
    2. Запуск таймеров. uv_timer_t
    3. pending callbacks внутренние подготовительные действия, которые было бы неплохо совершить перед тем, как начинать выполнение внешних операций
    4. операции I/O Вычисление времени выполнения внешней операции I/O по реализации схоже с функцией запуска таймеров, так как значение этого времени вычисляется на основе ближайшего таймера. Этим, кстати, и достигается неблокирующая модель (non-blocking poll).
    5. uv__run_check. идентична функциям uv__run_idle и uv__run_prepare, т.е. это запуск обратных вызовов, регистрирующихся по тому же принципу, и вызывающих после внешних операций. Однако, в этом случае, у нас есть возможность регистрации подобных обработчиков из Node.js. Это функция setImmediate (т.е. немедленное выполнение после внешней операции I/O)
    6. запуск закрывающихся обработчиков.
    7. uv__loop_alive.

## Tools & Frameworks

* Как отлаживать код
    * debug;
    * Отладка js в developer tools браузера
    * logs
    * try catch, catch(e) throw e, new Error(message), try catch(e) finally
    * window.onerror, если в него записать функцию, то она выполнится и получит в аргументах сообщение ошибки, текущий URL и номер строки, откуда «выпала» ошибка.
    * app для фреймворков в браузере
    * Отладка в ide (debug, linter, run)
    * node-inspector
    * spy-js
    
* Что такое NPM?
    Пакетный менеджер входящий в состав Node.js.
    * npm scripts - . Все зависимости, инструкции и скрипты (объект `scripts`) в `package.json`(манифест зависимостей). Инструменты инсталлируются и помещаются в объект `devDependencies`. В `scripts` указываются инструкции как в командной строке, как например линтер `"lint": "eslint src/js"`. Объединение задач css `"build:css": "npm run scss && npm run autoprefixer"`, js `"build:js": "npm run lint && npm run uglify"`, all `"build:images": "npm run imagemin && npm run icons",  "build:all": "npm run build:css && npm run build:js && npm run build:images",`. Отслеживание изменений например `"watch:css": "onchange 'src/scss/*.scss' -- npm run build:css",`. И вишенка `"watch:all": "parallelshell 'npm run serve' 'npm run watch:css' 'npm run watch:js'"` `"postinstall": "npm run watch:all"` . parallelshell позволяет нам одновременно выполнять несколько задач watch. Подобным функционалом обладает также npm-run-all и в отличии от `&&` не дожидается успешного выполнения предыдущей команды (в примере с `watch` `&&` застрянет) postinstall запускается сразу после выполнения npm install в командной строке.

* Что такое профилирование кода?
    Сбор характеристик работы программы/подпрограммы в целях оптимизации.
    В js с 
        * использование DevTools
        * Написание тестов/профайлера (ручное профилирование)
        * spy-js
        * jsperf - JavaScript performance playground
        * dromaeo - Mozilla JavaScript performance test suite.

* Angular 2 

* React
    Lifecycle methods:
        1.constructor(props): конструктор, в котором происходит начальная инициализация компонента
        2. componentWillMount(): вызывается непосредственно перед рендерингом компонента
        3. render(): рендеринг компонента
        4. componentDidMount(): вызывается после рендеринга компонента. Здесь можно выполнять запросы к удаленным ресурсам
        5. componentWillUnmount(): вызывается перед удалением компонента из DOM
    При обновлении:
        1. shouldComponentUpdate(nextProps, nextState): вызывается каждый раз при обновлении объекта props или state. В качестве параметра передаются новый объект props и state. Эта функция должна возвращать true (надо делать обновление) или false (игнорировать обновление). По умолчанию возвращается true. Но если функция будет возвращать false, то тем самым мы отключим обновление компонента, а последующие функции не будут срабатывать.
        2. componentWillUpdate(nextProps, nextState): вызывается перед обновлением компонента (если shouldComponentUpdate возвращает true)
        3. render(): рендеринг компонента (если shouldComponentUpdate возвращает true)
        4. componentDidUpdate(prevProps, prevState): вызывается сразу после обновления компонента (если shouldComponentUpdate возвращает true). В качестве параметров передаются старые значения объектов props и state.
        5. componentWillReceiveProps(nextProps), которая вызывается при обновлении объекта props. Новые значения этого объекта передаются в функции в качестве параметра. Как правило, в этой функции устанавливаются те свойства компонента, в том числе из this.state, которые зависят от значений из props.

# DevOps

# Data processing

# Git and version control

## Git tips
    * Коммиты с одинаковым хешем - одинаковые, с разными хешами - разные.
    * git commit –amend - команда перезаписывает текущий коммит и даже если ничего не изменилось, хеш все равно станет новым.
    * branch - указатель на коммит
    * Коммит (кроме начального) имеет родительский коммит, который для него аналог “предыдущего”. Из одного коммита может выходить несколько дочерних коммитов. Это делается с помощью ветвления. А так как ветки могут соединяться в одну, то у коммита может быть и несколько родительских коммитов. Обычно их два, но есть возможность сделать merge трех и более коммитов одновременно.
    * git branch backup - резервная копия коммитов перед rebase
    * git rebase [BRANCH or SHA1] - изменяет текущую ветку. Переданный параметр - указатель на новое начало коммитов. Пересоздаются (копируются) коммиты из диапазона [BRANCH or SHA1]..HEAD . То есть все предки текущего коммита (включая его самого) без предков коммита (включая его самого) [BRANCH or SHA1]. Это то, что интуитивно можно назвать как “новые” коммиты.
    * При ребейзинге текущая ветка - ветка с задачей, а ребейзятся относительно главной ветки.
    * При слиянии текущей задачи - переключаются на главную ветку и сливают ветку с задачей.
    * изменению подвержена всегда текущая ветка. Почти все команды в git следуют этому правилу.
    * При ребейзинге главная ветка не трогается, изменяется ветка с задачей - она пересоздается в другом месте.
    * При слиянии главная ветка изменяется - в ней создается мерж-коммит. Ветка с задачей наоборот остается в прежнем виде.
    * Ребейзинг позволяет также переписывать историю своих коммитов.
    * git rebase [FROM] [TO] --onto [START] FROM, TO, START – хеши коммитов или названия веток/тегов. Команда копирует коммиты из диапазона FROM..TO в START. Если TO - хеш, а не ветка, то результат работы увидеть сложно. Обычно это изменяемая ветка. По сути новый параметр здесь только FROM, который обрезает ветку.
