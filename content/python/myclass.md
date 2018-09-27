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

Within the definition, you refer to the instance of the class as ```self```.
So, you can refer to the attribute defined earlier as ```self.<attribute name>```, and the method (or function) as ```self.<method name>``` (e.g. ```self.data``` or ```self.calculate```).

In this example, the class ```MyClass``` has attributes, ```i``` that returns an integer, and ```f()``` that is a function object. These attributes are referred to ```MyClass.i``` and ```MyClass.f```, respectively.
There is another attribute: ```__doc__``` returns the docstring enclosed with three double quotation marks.

Class **instantiation** uses function notation. To create an instance ```x``` in the class ```MyClass```, you can simply type as the following:
```
x = MyClass()
```
Then, you can access the attributes as the following:
```
x.i
x.f()
```
Or you can also get attributes with
```
MyClass.i
MyClass.f(x)
```
The expression is consistent with the ```f()``` definition.

When you create an instance of your own object, you may want to customize the initialization of the instance.
This method is called whenever you create an instance of the class, and so you usually put code that handles the arguments present when you create (or instantiate) an instance of a class and conducts any kind of initialization for the object instance.
```
class MyClass:
    """ A simple example class """
    def __init__(self):
        self.data = []

    i = 100

    def f(self):
        return 'hello'
```
If you create a variable with this class, you can see additional attribute, ```data```.
```
x = MyClass()
print(x.data)
```
The example above does not take any inputs and the initialization of ```x``` doesn't do anything but creating a space called ```data```.
The following example now takes an input to initialize the instant ```x```.
```
class MyClass:
    """ A simple example class """
    def __init__(self, data):
        self.data = data

    i = 100

    def f(self):
        return 'hello'
```
If you try to create a new variable ```x``` as above, you will get an error.
```
>>> x = MyClass()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: __init__() missing 1 required positional argument: 'data'
```
Instead, you can create ```x``` by providing the initial value.
```
>>> x = MyClass(10)
>>> print(x.data)
10
```

#### A Practical Example
This class provides a template for holding and manipulating information about a book.
The class definition provides a single method (besides the initialization method) that returns a formatted bibliographic reference for the book.
The code below gives the class definition and then creates two instances of the class (note line continuations are added to fit the code on the page):

```
class Book(object):
    """
    Objective : This class organizes the information of books
    """
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
Line 1 begins the class definition.
By convention, class names follow the CapWords convention (capitalize the first letter of every word).
The argument in the class statement is a special object called ```object```.
This has to do with the objective-oriented project idea, which is a topic beyond the scope of this class. In Python3, you can skip ```object``` as in the ```MyClass``` example, but please read [this page](https://stackoverflow.com/questions/4015417/python-class-inherits-object) for more information.

Line 2-4 contains docstring. In IPython, after defining ```Book``` class, you can check the docstring with
```
In [2]: Book?
Init signature: Book(authorlast, authorfirst, title, place, publisher, year)
Docstring:      Objective : This class organizes the information of books
Type:           type
```

The arguments list of ```__init__``` is the list of arguments passed in to the constructor of the class, which is called when you use the class name with calling syntax.

You can define instances as the following.
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
Then, you can get the formatted output of the book information.
```
In [4]: pynut.write_bib_entry()
Out[4]: "Martelli, Alex, Python in a Nutshell, Sebastopol, CA: O'Reilly Media, Inc., 2003."
```

It is noted that the ```write_bib_entry``` method is called with no input parameters, but in the class definition, I still need to provide it with ```self``` as an input.
That way, the method definition is able to make use of all the attributes and methods attached to ```self```.


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

In the example above, we defined a function, ```write_bib_entry```. It is not a part of ```Book```, so that when you try
```
In [5]: pynut.write_bib_entry()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-10-de7a795a67da> in <module>()
----> 1 pynut.write_bib_entry()

AttributeError: 'Book' object has no attribute 'write_bib_entry'
```
But,
```
In [6]: write_bib_entry(pynut)
Out[6]: "Martelli, Alex, Python in a Nutshell, Sebastopol, CA: O'Reilly Media, Inc., 2003."
```
Why does this work?
What is the role of ```self``` in ```write_bib_entry```?

##### exercise
1. How would you print out the author attribute of the ```pynut``` instance (at the interpreter, after running the file)?
2. If you type print ```beauty.write_bib_entry()``` at the interpreter (after running the file), what will happen?
3. How would you change the publication year for the beauty book to ```"2010"```?

#### Remarks on class
+ It is not necessary that the function definition is textually enclosed in the class definition: assigning a function object to a local variable in the class is also ok. For example:

```
# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g
```
Then ```C``` has three attributes, ```f```, ```g```, and ```h```. ```f``` requires two inputs to determine the minimum number, but ```g``` and ```h``` need no input (and they are identical).

+ Methods may call other methods by using method attributes of the ```self``` argument:

```
class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)
```
In the method ```addtwice```, the method ```add``` was called.
```
In [12]: y = Bag()

In [13]: y.add(3)

In [14]: y.data
Out[14]: [3]

In [15]: y.addtwice(4)

In [16]: y.data
Out[16]: [3, 4, 4]
```

+ Defining empty class can be done.

```
class Employee:
    pass

john = Employee()  # Create an empty employee record

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000
```

#### Object-Oriented programming
We are using the example script that can be downloaded from [here](/images/bibliog.py)
