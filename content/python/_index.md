+++
title= "Python"
date= 2018-09-07T12:36:51+09:00
description = ""
creatordisplayname = "Hajoon Song"
creatoremail = "hajsong@yonsei.ac.kr"
lastmodifierdisplayname = "Hajoon Song"
lastmodifieremail = "hajsong@yonsei.ac.kr"
tags = ["python","jupyter notebook"]
weight = 4
#pre ="<i class='fa fa-edit' ></i> "
#alwaysopen = true
+++

{{% panel %}}The material here is based on the Chapter 3-5 in "A Hands-On Introduction to Using Python in the Atmospheric and Oceanic Sciences" by Johnny Wei-Bing Lin.{{% /panel %}}


Python, like any other programming language, has variables and all the standard
control structures. We will go though Python’s basic data and
control structures that support procedural programming.
Then we will explore how to use arrays, followed by file input and output.

*A few list of changes in Python 3.x that differs from Python 2.x*

+ The ```print``` function syntax now looks like any other function, e.g., ```print("Hello")```.
+ The division operator uses floating point division, even when both the numerator and denominator are integers.
+ Using ```raise``` to raise an exception has a new syntax.
+ Dictionary methods ```keys``` and ```values``` no longer return lists. Neither does range. To make lists out of the return values, use the ```list``` function.
+ Dictionaries no longer have the ```has_key``` method. Test instead for ```key``` in ```dict``` (where ```key``` is the key of interest and ```dict``` is your dictionary object). Note that if a value in your dictionary is the same as ```key```, the membership testing will not return ```True```.
+ Relative imports (i.e., importing a module in the current directory) require the use of . in front of the module name.
+ The version of NumPy generally installed with Python 3.x has a function ```ndim``` that gives the number of dimensions of an array, rather than ```rank```.
