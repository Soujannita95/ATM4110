+++
title= "Module"
date= 2018-09-18T08:45:40+09:00
description = ""
creatordisplayname = "Hajoon Song"
creatoremail = "hajsong@yonsei.ac.kr"
lastmodifierdisplayname = "Hajoon Song"
lastmodifieremail = "hajsong@yonsei.ac.kr"
tags = ["module"]
weight = 103
#pre ="<i class='fa fa-edit' ></i> "
+++

When you write a script, the moment may come when you think there must be functions that can do what you want to do.
Python calls "modules", and "packages" which is the collection of modules to assist users to do their job easily and quickly. (They are used interchangeably from time to time.)
Unlike compiled languages like Fortran, these modules are not collections of object files but rather regular Python source code files.
A module is a single source code file and a package is a directory containing
source code files (and possibly subdirectories of source code files).

To use a module, users can call it with ```import``` command.
```
import <module name>
```
For example, you can call NumPy module for the computation regarding arrays.
```
>>> import numpy
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'numpy']
```
or in IPython,
```
In [1]: import numpy

In [2]: whos
Variable   Type      Data/Info
------------------------------
numpy      module    <module 'numpy' from '/Us<...>kages/numpy/__init__.py'>
```
To use functions in the NumPy module, you can first write the module name, followed by dot and the function name. For example,
```
a = numpy.sin(4)
```
assign ```sin(4)``` to ```a```.

Calling ```<module name>``` with ```import``` is essentially the same as running the python file ```<module name>.py```. As an example, let's suppose that ```ctof.py``` has
```
TinC = int(input("Enter a temperature in Celsius: "))

TinF = 9.0/5.0 * TinC + 32
print("Temperature:", TinC, "degC = ", TinF, "degF")
```
In Python, we can run this script with the command of ```exec(open('ctof.py').read())```.

Now, let's try
```
>>> import ctof
```
What do you get?

For ```import numpy```, however, Python loads many functions that NumPy has because it is technically a package of many files, not a module of a single file.
If all the module file does is define functions, variables, etc., then nothing will be output.
But you have access to everything that is defined by typing the module name, a period, then the name of the module function, variable, etc. you want (hence, ```numpy.sin```, etc.).
Just as in a regular Python session you have access to all the variables, functions, etc. you define in that regular session, with an imported module, all the variables, functions, etc. that the module
created and used are also sitting inside the module's namespace, ready for you to access, using the syntax just mentioned.

Submodules (which are subdirectories inside the package directory) are also specified with the periods.
For instance, NumPy has a submodule called ```ma```, which in turn has special functions defined in it.
The submodule then is referred to as ```numpy.ma``` and the array function in the submodule as ```numpy.ma.array```.

When importing modules, shorter name can be assigned. For example,
```
import numpy as np
```
Once you assign the shorter name, you can call the function with it, e.g. ```np.sin```.

If you are interested only one function in the module, you can call it as the following.
```
from numpy import sin
```

Finally, remember, modules can contain data in addition to functions.
The syntax to refer to those module data variables is exactly the same as for functions. Thus, ```numpy.pi``` gives the value of the mathematical constant. 

You can create your own module and it will be explained later.
