+++
title= "Defining class"
date= 2018-09-20T17:35:05+09:00
description = ""
creatordisplayname = "Hajoon Song"
creatoremail = "hajsong@yonsei.ac.kr"
lastmodifierdisplayname = "Hajoon Song"
lastmodifieremail = "hajsong@yonsei.ac.kr"
tags = ["class","object"]
weight = 105
#pre ="<i class='fa fa-edit' ></i> "
#alwaysopen = true
+++

#### *"Classes provide a means of bundling data and functionality together."*
(from the [Python documentation](https://docs.python.org/3/tutorial/classes.html))

We can define our own type of object by creating a new class that can carry attributes and methods to maintaining and modifying its state.

When we define a new variable, we actually create a new instance of a class.
For example, typing ```a = 'hello'``` creates an instance of a predefined string class.
Likewise, we can create a new class instance that has the format of the class we defined.

#### Class definition syntax
The simplest form of class definition looks like this:
```
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
```
Class definitions start with ```class``` statement. The definition of the class follows from the next line with indentations at the beginning of the lines.
Definition of the class must be done before using it. The ```<statement-i>``` in the class definition can be method definitions as well as attribute statements.

#### Class objects
Class objects support two kinds of operations: attribute references and instantiation.

**Attribute references** are defined as ```obj.name```. For example,
```
class MyClass:
    """ A simple example class """
    i = 100

    def f(self):
        return 'hello'
```
In this example, the class ```MyClass``` has attributes, ```i``` that returns an integer, and ```f()``` that is a function object. These attributes are referred to ```MyClass.i``` and ```MyClass.f```, respectively.
There is another attribute: ```__doc__``` returns the docstring enclosed with three double quotation marks.

Class **instantiation** uses function notation. To create an instance ```x``` in the class ```MyClass```, you can simply type as the following:
```
x = MyClass()
```

When you create an instance of your own object, you may want to customize the initialization of the instance.
This method is called whenever you create an instance of the class, and so you usually put code that handles the arguments present when you create (or instantiate) an instance of a class and conducts any kind of initialization for the object instance.
```
class MyClass:
    """ A simple example class """
    def __init__(self)
        self.data =[]

    i = 100

    def f(self):
        return 'hello'
```

Within the definition, you refer to the instance of the class as ```self```.
So, you can refer to the attribute defined earlier as ```self.<attribute name>```, and the method (or function) as ```self.<method name>``` (e.g. ```self.data``` or ```self.calculate```).

Methods are defined using the ```def``` statement.
The first argument in any method is ```self```; this syntax is how Python tells a method "make use of all the previously defined attributes and methods in this instance."
**However, you never type self when you call the method.**

#### Example
This class provides a template for holding and manipulating information about a book.
The class definition provides a single method (besides the initialization method) that returns a formatted bibliographic reference for the book.
The code below gives the class definition and then creates two instances of the class (note line continuations are added to fit the code on the page):

```
class Book:
    def __init__(self, authorlast, authorfirst, \
        title, place, publisher, year):
        self.authorlast = authorlast
        self.authorfirst = authorfirst
        self.title = title
        self.place = place
        self.publisher = publisher
        self.year = year

    def write_bib_entry(self):
        return self.authorlast \
            + ', ' + self.authorfirst \
            + ', ' + self.title \
            + ', ' + self.place \
            + ': ' + self.publisher + ', ' \
            + self.year + '.'
```
The arguments list of ```__init__``` is the list of arguments passed in to the constructor of the class, which is called when you use the class name with calling syntax.

```
beauty = Book( "Dubay", "Thomas" \
             , "The Evidential Power of Beauty" \
             , "San Francisco" \
             , "Ignatius Press", "1999" )
pynut = Book( "Martelli", "Alex" \
            , "Python in a Nutshell" \
            , "Sebastopol, CA" \
            , "O'Reilly Media, Inc.", "2003" )
```
In defining the class, you need to be consistent with indentation.
Try the following example.
```
class Book(object):
    def __init__(self, authorlast, authorfirst, \
        title, place, publisher, year):
        self.authorlast = authorlast
        self.authorfirst = authorfirst
        self.title = title
        self.place = place
        self.publisher = publisher
        self.year = year

def write_bib_entry(self):
    return self.authorlast \
        + ', ' + self.authorfirst \
        + ', ' + self.title \
        + ', ' + self.place \
        + ': ' + self.publisher + ', ' \
        + self.year + '.'
```
Does the ```Book``` class have the method ```write_bib_entry```?
What is the role of ```self``` in ```write_bib_entry```?
