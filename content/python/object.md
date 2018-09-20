+++
title= "Object"
date= 2018-09-19T09:59:47+09:00
description = ""
creatordisplayname = "Hajoon Song"
creatoremail = "hajsong@yonsei.ac.kr"
lastmodifierdisplayname = "Hajoon Song"
lastmodifieremail = "hajsong@yonsei.ac.kr"
tags = ["object","class"]
weight = 104
#pre ="<i class='fa fa-edit' ></i> "
#alwaysopen = true
+++

Python is an object oriented programming language.
In fact, almost everything in Python is an object.
Then what is an object?

An object is a **variable** that has attached to it both data (attributes) and functions
designed to act on that data (methods).
So what does this mean?

The key idea of objects is that variables shouldn't be thought of as having only values (and type), but rather they should be thought of entities that can have any number of other things "attached" to them.
If the attached thing is a piece of data, it's called an attribute of the object variable.
If the attached thing is a function, it's called a method.

*The following contents are from Chapter 7 of the textbook.*
#### Procedural vs. object-oriented programming
Procedural programs look at the world in terms of two entities, "data" and "functions".
In a procedural context, the two entities are separate from each other.
A function takes data as input and returns data as output.
In the real world, however, we don't think data and functions as separate entities.
That is, real world objects instead have both "state" and "behaviors".
For instance, people have state (tall, short, etc.) and behavior (playing basketball, running, etc.), often both at the same time, and, of course, in the same person.

#### The nuts and bolts of objects
An object in programming is an entity or "variable" that has two entities attached to it: data (attributes) and things that act on that data (methods).
Importantly, you design methods to act on the attributes; they aren’t random functions
someone has attached to the object.

The key syntax idea of objects is borrowed from module syntax: Just as you describe functions attached to modules by giving the module name, a period, then the function name, you describe things attached to a Python object by giving the variable name, a period, then the attribute or method name.

The variable types (e.g. string) we covered are in fact objects.
Python includes these objects because they are used frequently.
In Python, this common pattern or template is defined by the class statement.
Using predefined classes, we create new variables and these specific realizations of that pattern are called "instances of that class."

#### Example of how objects work: Strings
Python strings (like nearly everything else in Python) are objects.
Thus, built into Python, there (implicitly) is a class definition of the string class, and every time you create a string, you are using that definition as your template.
That template defines both attributes and methods for all string objects, so whatever string you've created, you have that set of data and functions attached to your string which you can use.

Let's create a string variables.
```
a = "hello world"
```
To see all attributes and methods, you can use ```dir()``` (You can still use ```dir()``` in IPython).
```
>>> a = "hello world"
>>> dir(a)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```
The string class has many methods attached to it.
Let's try ```a.upper()```
```
>>> a.upper()
'HELLO WORLD'
```
If you try ```a.title()```
```
>>> a.title()
'Hello World'
```
These ```upper``` and ```title``` functions only works for string variables because they are defined under the string class. If you try to use them for an integer variable,
```
>>> b = 5
>>> b.title()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'int' object has no attribute 'title'
>>> b.upper()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'int' object has no attribute 'upper'
```
With ```dir(a)```, you can get the attributes starting with double underscores, e.g. ```__doc__```.
```
>>> a.__doc__
"str(object='') -> str\nstr(bytes_or_buffer[, encoding[, errors]]) -> str\n\nCreate a new string object from the given object. If encoding or\nerrors is specified, then the object must expose a data buffer\nthat will be decoded using the given encoding and error handler.\nOtherwise, returns the result of object.__str__() (if defined)\nor repr(object).\nencoding defaults to sys.getdefaultencoding().\nerrors defaults to 'strict'."
```
In IPython, ```a.__doc__``` is printed out as ```docstring``` when you do ```a?```.
```
In [1]: a = "hello world"

In [2]: a?
Type:        str
String form: hello world
Length:      11
Docstring:
str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to sys.getdefaultencoding().
errors defaults to 'strict'.
```
Other information such as ```str```, ```hello world``` and ```11``` can be obtained by ```a.__class__```, ```a.__str__()``` and ```a.__len__()```, respectively.

Attributes of the string class can also have their own attributes. For example,
```
>>> a="hello world"
>>> dir(a.upper)
['__call__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__self__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__text_signature__']
```
You can access one of the attributes of an attribute using another period followed by the name of the attribute as the following.
```
>>> a.upper.__doc__
'S.upper() -> str\n\nReturn a copy of S converted to uppercase.'
```
{{% panel theme="default" header="Exercise" %}}
In the Python interpreter, type in:
```
a = 'The rain in Seoul.'
```
Given string ```a```:

1. Create a new string ```b``` that is a but all in uppercase.
2. Is ```a``` changed when you create ```b```?
3. How would you test to see whether ```b``` is in uppercase? That is, how could you return a boolean that is ```True``` or ```False``` depending on whether ```b``` is uppercase?
4. How would you calculate the number of occurrences of the letter “n”
in ```a```?
{{% /panel %}}
