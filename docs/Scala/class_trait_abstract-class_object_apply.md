Task:

> Нагуглить и прочитать про scala case class/class/trait/abstract class/object. Железно понимать чем они отличаются. Прочитать про объекты компаньоны, метод apply в них. Особое внимание уделить case class. В качестве первого упражнения написать такой class чтобы он обладал всеми фичами "кейс класса". Что получается и вопросы присылай/задавай сразу.

# apply 
apply  methods give you a nice syntactic sugar for when a class or object has one main use.
```Scala
scala> class Foo {}
defined class Foo

scala> object FooMaker {
     |   def apply() = new Foo
     | }
defined module FooMaker

scala> val newFoo = FooMaker()
newFoo: Foo = Foo@5b83f762
```
or
```Scala
scala> class Bar {
     |   def apply() = 0
     | }
defined class Bar

scala> val bar = new Bar
bar: Bar = Bar@47711479

scala> bar()
res8: Int = 0
```
Here our instance object looks like we’re calling a method. More on that later!

# Objects
Objects are used to hold single instances of a class. Often used for factories.
```Scala
object Timer {
  var count = 0

  def currentCount(): Long = {
    count += 1
    count
  }
}
```
How to use
```Scala
scala> Timer.currentCount()
res0: Long = 1
```
Classes and Objects can have the same name. The object is called a ‘Companion Object’. We commonly use Companion Objects for Factories.

Here is a trivial example that only serves to remove the need to use ‘new’ to create an instance.
```Scala
class Bar(foo: String)

object Bar {
  def apply(foo: String) = new Bar(foo)
}
```

## Packages
You can organize your code inside of packages.

```Scala
package com.twitter.example
```
at the top of a file will declare everything in the file to be in that package.

Values and functions cannot be outside of a class or object. Objects are a useful tool for organizing static functions.
```Scala
package com.twitter.example

object colorHolder {
  val BLUE = "Blue"
  val RED = "Red"
}
```
Now you can access the members directly
```Scala
println("the color is: " + com.twitter.example.colorHolder.BLUE)
```
Notice what the scala repl says when you define this object:
```Scala
scala> object colorHolder {
     |   val Blue = "Blue"
     |   val Red = "Red"
     | }
```
defined module colorHolder
This gives you a small hint that the designers of Scala designed objects to be part of Scala’s module system.

# Pattern Matching
One of the most useful parts of Scala.

Matching on values
```Scala
val times = 1

times match {
  case 1 => "one"
  case 2 => "two"
  case _ => "some other number"
}
```
Matching with guards
```Scala
times match {
  case i if i == 1 => "one"
  case i if i == 2 => "two"
  case _ => "some other number"
}
```
Notice how we captured the value in the variable ‘i’.

The `_` in the last case statement is a wildcard; it ensures that we can handle any statement. Otherwise you will suffer a runtime error if you pass in a number that doesn’t match. We discuss this more later.

See Also Effective Scala has opinions about when to use pattern matching and pattern matching formatting. A Tour of Scala describes Pattern Matching

## Matching on type

You can use `match` to handle values of different types differently.
```Scala
def bigger(o: Any): Any = {
  o match {
    case i: Int if i < 0 => i - 1
    case i: Int => i + 1
    case d: Double if d < 0.0 => d - 0.1
    case d: Double => d + 0.1
    case text: String => text + "s"
  }
}
```
Matching on class members
Remember our calculator from earlier.

Let’s classify them according to type.

Here’s the painful way first.
```Scala
def calcType(calc: Calculator) = calc match {
  case _ if calc.brand == "HP" && calc.model == "20B" => "financial"
  case _ if calc.brand == "HP" && calc.model == "48G" => "scientific"
  case _ if calc.brand == "HP" && calc.model == "30B" => "business"
  case _ => "unknown"
}
```
Wow, that’s painful. Thankfully Scala provides some nice tools specifically for this.

# Case Classes

case classes are used to conveniently store and match on the contents of a class. You can construct them without using new.
```Scala
scala> case class Calculator(brand: String, model: String)
defined class Calculator

scala> val hp20b = Calculator("HP", "20b")
hp20b: Calculator = Calculator(hp,20b)
```
case classes automatically have equality and nice toString methods based on the constructor arguments.
```Scala
scala> val hp20b = Calculator("HP", "20b")
hp20b: Calculator = Calculator(hp,20b)

scala> val hp20B = Calculator("HP", "20b")
hp20B: Calculator = Calculator(hp,20b)

scala> hp20b == hp20B
res6: Boolean = true
```
case classes can have methods just like normal classes.

## > CASE CLASSES WITH PATTERN MATCHING
case classes are designed to be used with pattern matching. Let’s simplify our calculator classifier example from earlier.
```Scala
val hp20b = Calculator("HP", "20B")
val hp30b = Calculator("HP", "30B")

def calcType(calc: Calculator) = calc match {
  case Calculator("HP", "20B") => "financial"
  case Calculator("HP", "48G") => "scientific"
  case Calculator("HP", "30B") => "business"
  case Calculator(ourBrand, ourModel) => "Calculator: %s %s is of unknown type".format(ourBrand, ourModel)
}
Other alternatives for that last match

  case Calculator(_, _) => "Calculator of unknown type"
OR we could simply not specify that it’s a Calculator at all.
  case _ => "Calculator of unknown type"
OR we could re-bind the matched value with another name
  case c@Calculator(_, _) => "Calculator: %s of unknown type".format(c)
```

## Case class features

* unapply method
An unapply method is generated, which makes it easy to use case classes in match expressions. This is huge for Scala/FP.

* Class Parameters are Promoted to Fields
(You won’t use var fields in this book, but if you did, mutator methods would also be generated for constructor parameters declared as var.)

* Sensible toString method
A default toString method is generated, which is helpful for debugging.

* Equals and Hashcode are implemented out of the box
equals and hashCode methods are generated, which lets you compare objects and easily use them as keys in maps (and sets).

* Copy method
As you’ll see in the next lesson, a copy method is generated. I never use this in Scala/OOP code, you’ll use it all the time in Scala/FP.

* Companion Objects

* Serializable & Extractor Patterns

An apply method is generated, so you don’t need to use the new keyword to create a new instance of the class.
Accessor methods are generated for each constructor parameter, because case class constructor parameters are public val fields by default.

## Object

Scala Singleton Objects - is a class with exactly one instance. Creates lazily when we reference it. It is a value, and as a top-level value, it is a Scala singleton. To define an object, we use the keyword ‘object’




# Exceptions
Exceptions are available in Scala via a try-catch-finally syntax that uses pattern matching.
```Scala
try {
  remoteCalculatorService.add(1, 2)
} catch {
  case e: ServerIsDownException => log.error(e, "the remote calculator service is unavailable. should have kept your trusty HP.")
} finally {
  remoteCalculatorService.close()
}
```
trys are also expression-oriented
```Scala
val result: Int = try {
  remoteCalculatorService.add(1, 2)
} catch {
  case e: ServerIsDownException => {
    log.error(e, "the remote calculator service is unavailable. should have kept your trusty HP.")
    0
  }
} finally {
  remoteCalculatorService.close()
}
```
This is not an example of excellent programming style, just an example of try-catch-finally resulting in expressions like most everything else in Scala.

Finally will be called after an exception has been handled and is not part of the expression.


# class

# Traits
traits are collections of fields and behaviors that you can extend or mixin to your classes.

Traits are used to share interfaces and fields between classes. They are similar to Java 8’s interfaces. Classes and objects can extend traits, but traits cannot be instantiated and therefore have no parameters.

## To trait, or not to trait?
Whenever you implement a reusable collection of behavior, you will have to decide whether you want to use a trait or an abstract class. There is no firm rule, but this section contains a few guidelines to consider.

If the behavior will not be reused, then make it a concrete class. It is not reusable behavior after all.

If it might be reused in multiple, unrelated classes, make it a trait. Only traits can be mixed into different parts of the class hierarchy.

If you want to inherit from it in Java code, use an abstract class. Since traits with code do not have a close Java analog, it tends to be awkward to inherit from a trait in a Java class. Inheriting from a Scala class, meanwhile, is exactly like inheriting from a Java class. As one exception, a Scala trait with only abstract members translates directly to a Java interface, so you should feel free to define such traits even if you expect Java code to inherit from it. See Chapter 29 for more information on working with Java and Scala together.

If you plan to distribute it in compiled form, and you expect outside groups to write classes inheriting from it, you might lean towards using an abstract class. The issue is that when a trait gains or loses a member, any classes that inherit from it must be recompiled, even if they have not changed. If outside clients will only call into the behavior, instead of inheriting from it, then using a trait is fine.

If efficiency is very important, lean towards using a class. Most Java runtimes make a virtual method invocation of a class member a faster operation than an interface method invocation. Traits get compiled to interfaces and therefore may pay a slight performance overhead. However, you should make this choice only if you know that the trait in question constitutes a performance bottleneck and have evidence that using a class instead actually solves the problem.

If you still do not know, after considering the above, then start by making it as a trait. You can always change it later, and in general using a trait keeps more options open.



# abstract class

Abstract classes can have constructor parameters as well as type parameters. Traits can have only type parameters. There was some discussion that in future even traits can have constructor parameters

Abstract classes are fully interoperable with Java. You can call them from Java code without any wrappers. Traits are fully interoperable only if they do not contain any implementation code


# Class with case class feature