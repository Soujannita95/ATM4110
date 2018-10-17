+++
title= "Basic Data and Control Structures"
date= 2018-09-17T10:08:38+09:00
description = ""
creatordisplayname = "Hajoon Song"
creatoremail = "hajsong@yonsei.ac.kr"
lastmodifierdisplayname = "Hajoon Song"
lastmodifieremail = "hajsong@yonsei.ac.kr"
tags = ["python","data type"]
weight = 101
#pre ="<i class='fa fa-edit' ></i> "
#alwaysopen = true
+++

#### 1. Overview of basic variables and operators
Unlike languages like Fortran, Python is **dynamically typed**, variables take on the type of whatever they are set to when they are assigned.
Thus, ```a=5``` makes the variable a an integer, but ```a=5.0``` makes the variable a floating point number.
Additionally, because assignment can happen anytime during the program, this means you can change the type of the variable without changing the variable name.

The built-in variable types include:

+ integer and floating point
+ strings
+ booleans : ```True``` and ```False```
+ nonetype : ```None```
+ lists and tuples : variable v.s. fixed
+ dictionaries : consists of keys and values

{{% alert theme="info" %}}Python is case-sensitive, so "N" and "n" are different.{{% /alert %}}

#### 2. Integer and Float
The easiest way to get the idea of integer and float is probably with an example.
If we define variables as the following:
```
a = 3.5
b = -2.1
c = 3
d = 4
```
Then arithmetic operations below
```
a*b
b+c
a/c
c/d
```
give us
```
# a*b
-7.3500000000000005
# b+c
0.8999999999999999
# a/c
1.1666666666666667
# c/d (in Python2)
0
# c/d (in Python3)
0.75
```
We did not specify the data type, but Python automatically decides what type a variable based on the value/operation. For example, ```c/d``` returns integer because ```c``` and ```d``` are integers.
Python will generally make the output type the type that retains the most information, so ```a/c``` returns float.

Here’s a question: Why is the answer to ```a*b``` not exactly -7.35?
Remember that floating point numbers on any binary computer are, in general, not represented exactly.
The default formatting setting for the print command, will sometimes print out enough of the
portion after the decimal point to show that.

#### 3. Strings
String variables are created by setting text in either paired single or double quotes. For example,
```
a = 'hello'
b = "hello"
```
both work as long as they are consistently paired.

Some "special" strings include:

+ ```\n```: newline character
+ ```\t```: tab character
+ ```\\```: backslash

```
>>> a="Hello \nHello"
>>> print(a)
Hello
Hello
>>> a="Hello \tHello"
>>> print(a)
Hello 	Hello
>>> a="Hello \\Hello"
>>> print(a)
Hello \Hello
```
Python uses the addition operator to join strings together.
```
>>> a="Hello"
>>> b=" world"
>>> print(a+b+'!')
Hello world!
>>> a+b
'Hello world'
```
#### 4. Booleans
Boolean variables are variables that can have only one of two values: ```True``` and ```False```.
In some languages, the integer value zero is considered false and the integer value one is considered true, which was the case in older versions of Python.
Although this still seems to work in recent versions of Python, using ```True``` and ```False``` reduces ambiguity.

{{% alert theme="info" %}}Note the capitalization matters.{{% /alert %}}
```
>>> a=true
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined
>>> a=True
```
Try this in a Python interpreter:
```
a = True
b = False
print(a and b)
print(a or b)
print(4 > 5)
```
What did you get?

#### 5. NoneType
A variable of NoneType can have only a single value, the value ```None``` (```N``` has to be capitalized).
Try this in a Python interpreter:
```
a = None
print(a is None)
print(a == 4)
```
The first ```print``` statement will return ```True```, while the second ```print``` statement will return ```False```.
The ```is``` operator compares "equality" not in the sense of value but in the sense of memory location.
Although "```a == None```" also works, the better syntax for comparing to ```None``` is "```a is None```".

This NoneType variables can be useful to safely initialize a parameter. After initialize a parameter with ```None```, you need to assign a value before doing an operation. Otherwise, Python will give an error. This is a simple way to make sure that the variable is set to a real value.

#### 6. Lists and tuples
Lists are ordered sequences. The items in the list do not have to be of the same type. You can define a list with both numbers and strings, and even another list.

To define a list, you use square brackets and commas.
```
a = [2, 3.2, 'hello', [-1.2, 'there', 5.5]]
```
To access elements, you use addresses that starts with zero. For example, the first element of ```a``` is ```a[0]```, the second is ```a[1]```.
If the element of the list is also a list, you can access the element with, for example, ```a[3][1]```.
In Python, list elements can also be addressed starting from the end; thus, ```a[-1]``` is the last element in list ```a```, ```a[-2]``` is the next to last element, etc.
```
>>> a[3][1]
'there'
>>> a[-1]
[-1.2, 'there', 5.5]
>>> a[-2]
'hello'
```
You can create new lists by slicing an existing list.

{{% alert theme="warning" %}} The lower limit of the range is *inclusive*, and the upper limit of the
range is *exclusive*. {{% /alert %}}
```
>>> a[0:3]
[2, 3.2, 'hello']
>>> a[1:3]
[3.2, 'hello']
>>> a[2:3]
['hello']
>>> a[3:3]
[]
```
The length of a list can be obtained using the ```len``` function.
```
>>> len(a)
4
>>> len(a[0])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: object of type 'int' has no len()
>>> len(a[3])
3
```

The element can be replaced with other types of item without any issues.
```
>>> a[2] = 0.0
>>> a
[2, 3.2, 0.0, [-1.2, 'there', 5.5]]
```
Python allows you to modify the list by providing build-in functions. When ```a = [2, 3.2, 'hello', [-1.2, 'there', 5.5]]```,
```
>>> a.insert(2,'everyone')
>>> print(a)
[2, 3.2, 'everyone', 'hello', [-1.2, 'there', 5.5]]
>>> a.remove(2)
>>> print(a)
[3.2, 'everyone', 'hello', [-1.2, 'there', 5.5]]
>>> a.append(4.5)
>>> print(a)
[3.2, 'everyone', 'hello', [-1.2, 'there', 5.5], 4.5]
```

Tuples are nearly identical to lists with the exception that tuples cannot be changed!
To define tuples, you use parenthesis instead of square brackets.
```
>>> b = (3.2, 'hello')
>>> b[0]
3.2
>>> b[0]=1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```
{{% panel %}}You can, to an extent, treat strings as lists. Thus, if a = "hello", then a[1:3] will return the substring "el".{{% /panel %}}

{{% panel %}}If the list contains lots of elements, you can break the list after the completion of an element and continue the list on the next line. Or you can put a backslash ("\") at the end of a line{{% /panel %}}

#### 7. Dictionaries
Dictionaries are unordered lists whose elements are referenced by *keys*, not by position.
*Keys* refer to *Values* that can be anything.

When defining a dictionary, you use curly braces ("{}"). The elements of a dictionary are "Key:Value" pairs, separated by a colon. For example,
```
a = {'a':2, 'b':3.2, 'c':[-1.2, 'there', 5.5]}
```
It is similar to *lists* to access the elements, except you use the keys.
```
>>> a['a']
2
>>> a['c']
[-1.2, 'there', 5.5]
```
There are a few built-in functions for dictionaries.

+ a.keys() : show all the keys
+ a.values() : show all the values
