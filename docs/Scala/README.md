# Scala

## Tips

* Null is evil
> https://scalac.io/null-pointer-exception-npe/
Don't need to check if null, except java object
do not return null

* Всегда инициализируйте значения.
* Оборачивайте Nullable, которые могут прийти извне в Option.
* Не возвращайте null: используйте Option, Either, Try и др.
* Видите предпосылки для появления null — быстрее исправляйте, пока ваши коллеги на радостях не завезли в проект специально предназначенный для борьбы с NPE язык.


* Option, в первую очередь, нужен, чтобы концептуально показать вероятно отсутствующую сущность, а не убегать от NPE.

> https://habr.com/ru/post/323706/
Неправильно:
```Scala
if (option.isEmpty)
  default
else
  // может взорватся c NoSuchElementException (без проверки)
  option.get
```
Правильно и короче
```Scala
option getOrElse default
```

Don’t use the get method with Option


https://alvinalexander.com/scala/best-practice-option-some-none-pattern-scala-idioms/
https://alvinalexander.com/scala/scala-option-some-none-syntax-examples/

* Using Option in method and constructor parameters
* Using Option to initialize class fields (instead of using null)
* Converting null results from other code (such as Java code) into an Option

This recipe adds these additional solutions:
* Returning an Option from a method
* Getting the value from an Option
* Using Option with collections
* Using Option with frameworks
* Using Try/Success/Failure when you need the error message (Scala 2.10 and newer)
* Using Either/Left/Right when you need the error message (pre-Scala 2.10)

similar to Try was available with the Either[Left, Right] classes. With these classes, Either is analogous to Try, Right is similar to Success, and Left is similar to Failure.


* Списки

У Option есть get, у списка есть head, а еще у него есть init и tail. Вот что мы можете получить, вызывая вышеописанные методы у пустого списка:
```Scal
// Для пустого списка:
init: java.lang.UnsupportedOperationException
head: java.lang.NoSuchElementException
last: java.lang.NoSuchElementException
tail: java.lang.UnsupportedOperationException
```
Конечно, с вами этого никогда не случится, если вы проверяете лист на пустоту.

> Извивайтесь гремучей змеей, делайте все возможное чтобы не использовать list.head и его друзей.

Вместо head неплохим вариантом будет использование метода headOption. Метод lastOption ведет себя аналогично. Если вы каким-либо образом привязаны к индексам, можете воспользоваться методом isDefinedAt, который принимает целочисленный аргумент (индекс) в качестве параметра. 

Все описанное выше по-прежнему подразумевает проверки, о которых можно забыть. Найдется еще тысяча и одна причина чтобы вы их опустили сознательно. Правильной и идиоматичной альтернативой будет использование сопоставления с образцом. Тот факт, что список является алгебраическим типом, не даст вам забыть о Nil, вы сможете спокойно избежать вызовов head и tail, сэкономив несколько строчек кода:

```Scala
def printRec(list: List[String]): Unit = list match {
  // вы также можете сопоставить одноэлеметный список, как и список из
  // n, и k элементов, если захотите. That's the power!
  case Nil  => ()
  case x::xs => println(x)
    printRec(xs)
}
```
> С точки зрения производительности для односвязного списка, коим является скаловский List (он же scala.collection.immutable.List), наиболее дешевой операцией будет запись в начало списка, нежели в конец. Для записи в конец списка требуется пройти весь список до конца. Сложность записи в начало списка O(1), в конец O(n). Не забывайте об этом.

def process (item: Option[Item]): Option[UpdatedItem] = ???

> индексы списков в Scala начинаются с нуля, а кортежей — с единицы Just historical reason


> https://habr.com/ru/post/330816/

postfix notation

Перегрузка операторов

О геттерах и сеттерах

> Для того чтобы получить имя вида isProperty для переменных булева типа, следует добавить scala.beans.BooleanBeanProperty в вашу область видимости.


Большие case-классы это плохо. Это очень плохо.
Линзы

Enum нету естьenumerate. В Scala есть идиоматичный способ создания перечислений, именуется он ADT (Algebraic Data Types), по-русски алгебраические типы данных.

Избегайте булевых аргументов в сигнатурах функций


Об итерации

Рекурсия лучше

Хвостовая рекурсия работает быстрее, чем большинство циклов. Если она, конечно, хвостовая. Для уверенности используйте аннотацию @tailrec. Ситуации бывают разными, не всегда рекурсивное решение оказывается простым доступным и понятным, тогда используйте while. В этом нет ничего зазорного. Более того, вся библиотека коллекций написана на простых циклах с предусловиями.


For comprehensions не для итерации (по индексам)

Главное, что вам следует знать про генераторы списков, или, как их еще Называют, «for comprehensions», — это то, что основное их предназначение — не в реализации циклов.


Более того, использование этой конструкции для итерации по индексам будет достаточно дорогостоящей процедурой. Цикл while или использование хвостовой рекурсии — намного дешевле. И нагляднее.

Не используйте return

Не используйте метки

Не используйте Структурные типы


* Init privat variables if you need to initialie them often

* Do not use `var`
“val” is used to define Immutable data. It’s evaluated only once at the time of definition.
“var” is used to define Mutable data. It’s evaluated only once at the time of definition.
Both val and var are evaluated Eagerly.
“lazy val” is used to define Immutable data. It is evaluated only once when we access it for first time. That means it is evaluated Lazily.
“def” is used to define Methods or Functions. It is evaluated only when we access it and evaluated every-time we access it. That means it is evaluated Lazily.


* Do not use mutable.Map if it is not nessesary 
* Do not use regexp if it is not nessesary 
* Use collection carefully and effectiveely

Лучше не привыкать к парадигме интерфейc -> реализация

The Java volatile keyword guarantees visibility of changes to variables across threads. This may sound a bit abstract, so let me elaborate. Многопоточность, гонка пямять 
http://tutorials.jenkov.com/java-concurrency/volatile.html
http://tutorials.jenkov.com/java-concurrency/synchronized.html