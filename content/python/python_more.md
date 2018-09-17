+++
title= "Functions, logical constructs and loops "
date= 2018-09-17T13:34:26+09:00
description = ""
creatordisplayname = "Hajoon Song"
creatoremail = "hajsong@yonsei.ac.kr"
lastmodifierdisplayname = "Hajoon Song"
lastmodifieremail = "hajsong@yonsei.ac.kr"
tags = ["functions","modules","Loop"]
weight = 100
#pre ="<i class='fa fa-edit' ></i> "
#alwaysopen = true
+++

#### 1. Functions
Functions in Python, in theory, work both like functions and subroutines in Fortran, in that (1) input comes via arguments and (2) output occurs through: a return variable (like Fortran functions) and/or arguments (like Fortran subroutines).
In practice, functions in Python are written to act like Fortran functions, with a single output returned. (The return value is specified by the return statement.) If you want multiple returns, it’s easier to put them into a list or use objects.

Function definitions begin with a ```def``` statement, followed by the name of the function and the argument list in parenthesis. At the end of this line comes colon. The contents of the function are written with indents (usually 4 spaces). When there is no indentation, Python assumes that the definition of the function is finished.

For example, the function to compute the area of the circle can be written as
```
def area(radius):
    area = 3.14 * (radius**2)
    return area
```
If you define this function without indentation, Python gives you an error as this.
```
>>> def area(radius):
... area = 3.14 * (radius**2)
  File "<stdin>", line 2
    area = 3.14*(radius**2)
       ^
IndentationError: expected an indented block
```
Once you define the function, you can use it with the syntax in the definition.
```
>>> a = area(3)
>>> print(a)
28.26
```

Python accepts both **positional** and **keyword** arguments in the argument list of a function.
Positional arguments are usually for *required* input while keyword arguments are usually for *optional* input.
Typically, keyword arguments are set to some default value. If you do not want to have a default value set for the keyword, a safe practice is to just set the keyword to ```None```.

We may tweak the previous ```area``` function by placing a keyword argument.
```
def area(radius, pi=None):
    area = pi * (radius**2)
    return area
```
What would you expect to see with ```a = area(3)```? How about ```a = area(3, pi=3.14)```?

A list and dictionary variable can be useful when passing positional and keyword arguments.
```
args = [3,]
kwds = {'pi':3.14}
a = area(*args, **kwds)
```
As you can see above, a list ```args``` and ```kwds``` can be passed to the function ```area```.
This is particularly useful when the function needs many positional and keyword arguments.

There are some rules for passing in function arguments by lists and dictionaries:

+ In the function call, put an asterisk (*) before the list that contains the
positional arguments and put two asterisks (**) before the dictionary that
contains the keyword arguments.
+ The list of positional arguments is a list where each element in the list
is a positional argument to be passed in, and the list is ordered in the
same order as the positional arguments.
+ The dictionary of keyword arguments uses string keys corresponding
to the name of the keyword and the value of the key:value pairs as the
value set to the keyword parameter.

#### 2. Logical constructs
You may be already familiar with logical constructs. In Python, the syntax for if-statements is
```
if <condition>:
```
followed by the block of code to execute if <condition> is true.
{{% alert theme="warning" %}}There is no need for an "endif" line because **indentation** defines the contents of the ```if``` block.{{% /alert %}}
```
a = 3
if a == 3:
    print('I am a ', a)
elif a == 2:
    print('I am a 2')
else:
    print('I am not a 3 or 2')
```
{{% alert theme="warning" %}}Don’t forget the colon at the end of ```if```, ```elif```, and ```else``` statements{{% /alert %}}

#### 3. Looping
The loop is also popular part of the programming. In Python, the loop begins with ```for```.
```
for <index> in <list>:
```
Do not forget the colon at the end of the syntax.

As the ```if``` statement, the contents of the loop is defines with indentation. That means that the loop does not require the line with ```enddo``` or something like that.

The ```for``` loop is little different compared to the Fortran do loops.
In Fortran, you specify a beginning value and an ending value (often 1 and an integer n) for an index, and the loop runs through all integers from that beginning value to that ending value, setting the index to that value.
In Python, the loop index runs through a list of items, and the index is assigned to each item in that list, one after the other, until the list of items is exhausted. For example,
```
for i in [2, -3.3, 'hello', 1, -12]:
    print(i)
```
prints out
```
2
-3.3
hello
1
-12
```
As mentioned in the previous page, list variables can have any variable types as elements.

If the iteration through numbers is desirable like Fortran, you can use a function ```range```.
```
for i in range(5):
    print(i)
```
In Python2, ```range``` creates a list. But in Python3, it creates a ```range``` type variable.
```
>>> a = range(3)
>>> a
range(0, 3)
>>> list(a)
[0, 1, 2]
```
The advantage of the ```range``` type in Python3 over the ```list``` type in Python2 is the reduced usage of the memory. In Python3, you do not need to secure memories for, for example, ```range(100000000)```.

{{% panel %}}The ```range``` function takes the form of ```range(stop)``` or ```range(start, stop[, step])```.{{% /panel %}}

Another useful function is ```enumerate```. Here is an example.
```
a = [2, -3.3, 'hello', 1, -12]
for i, v in enumerate(a):
    print(i, ': ', v)
```
results in
```
0 :  2
1 :  -3.3
2 :  hello
3 :  1
4 :  -12
```
You may figure out how ```enumerate``` works already. While iterating the list, ```enumerate``` assigns the index and the value to ```i``` and ```v```, respectively.

The following block of the code does the same thing as above.
```
a = [2, -3.3, 'hello', 1, -12]
for i in range(len(a)):
    print(i, ': ', a[i])
```

Python also has a ```while``` loop. It's like any other while loop and begins with the syntax:
```
while <condition>:
```
The code block (indented) that follows the ```while``` line is executed while *<condition>* evaluates as ```True```.
