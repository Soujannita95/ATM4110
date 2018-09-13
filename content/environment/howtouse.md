+++
title= "Start Python / Jupyter Notebook"
date= 2018-09-13T07:57:43+09:00
description = ""
creatordisplayname = "Hajoon Song"
creatoremail = "hajsong@yonsei.ac.kr"
lastmodifierdisplayname = "Hajoon Song"
lastmodifieremail = "hajsong@yonsei.ac.kr"
tags = ["python","jupyter notebook"]
weight = 105
#pre ="<i class='fa fa-edit' ></i> "
#alwaysopen = true
+++

This page guides you how to use Python and Jupyter Notebook using the example, Celsius and Fahrenheit converter.

When you want to convert the unit from Fahrenheit to Celsius, the formula is:

<a href="https://www.codecogs.com/eqnedit.php?latex=T[^{\circ}C]&space;=&space;(T[^{\circ}F]&space;-&space;32)&space;\times&space;5/9" target="_blank"><img src="https://latex.codecogs.com/gif.latex?T[^{\circ}C]&space;=&space;(T[^{\circ}F]&space;-&space;32)&space;\times&space;5/9" title="T[^{\circ}C] = (T[^{\circ}F] - 32) \times 5/9" /></a>

From Celsius to Fahrenheit, the formula is:

<a href="https://www.codecogs.com/eqnedit.php?latex=T(^{\circ}F)&space;=&space;(T[^{\circ}C]&space;\times&space;9/5)&space;&plus;&space;32" target="_blank"><img src="https://latex.codecogs.com/gif.latex?T(^{\circ}F)&space;=&space;(T[^{\circ}C]&space;\times&space;9/5)&space;&plus;&space;32" title="T(^{\circ}F) = (T[^{\circ}C] \times 9/5) + 32" /></a>

#### Python
To start Python, you can type ```python``` in the terminal.
```
$ python
```
Then you may see that the prompt has been changed as
```
Python 3.6.3 |Anaconda, Inc.| (default, Oct  6 2017, 12:04:38)
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Ask for the input in Celsius:
```
>>> TinC = int(input("Enter a temperature in Celsius: "))
```
Then you can see the next line asking a temperature in Celsius.
```
Enter a temperature in Celsius:
```
We can say 30, although you can give any number. Then ```TinC``` carries ```30```.
Next is to convert temperature from Celsius to Fahrenheit using the formula.
```
>>> TinF = 9.0/5.0 * TinC + 32
```
It is time to print out the answer.
```
>>> print("Temperature:", TinC, "degC = ", TinF, "degF")
```
This should give you
```
Temperature: 30 degC =  86.0 degF
```
Once you are done, you can exit Python by typing ```quit()```
```
>>> quit()
```

{{% panel %}} Make the unit converter from Fahrenheit to Celsius by yourself. {{% /panel %}}

#### IPython
Interactive Python (IPython) gives you more functionality by providing a wider range of commands than python.
To launch IPython, simply type
```
$ ipython
```
This will give you
```
Python 3.6.3 |Anaconda, Inc.| (default, Oct  6 2017, 12:04:38)
Type 'copyright', 'credits' or 'license' for more information
IPython 6.1.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]:
```
Here, you can follow the same procedure as in python to have the program of the unit converter.
```
In [1]: TinC = int(input("Enter a temperature in Celsius: "))
Enter a temperature in Celsius: 30

In [2]: TinF = 9.0/5.0 * TinC + 32

In [3]: print("Temperature:", TinC, "degC = ", TinF, "degF")
Temperature: 30 degC =  86.0 degF
```
As already mentioned above, IPython provides useful functions.
For example, if you want to know about the command ```input```, you can type
```
In [4]: input?
```
If you want to know what variables are defined, type
```
In [5]: whos
Variable   Type     Data/Info
-----------------------------
TinC       int      30
TinF       float    86.0
```
IPython also provides many magic functions. The built-in magics include:

+ Functions that work with code: %run, %edit, %save, %macro, %recall, etc.
+ Functions which affect the shell: %colors, %xmode, %autoindent, %automagic, etc.
+ Other functions such as %reset, %timeit, %%writefile, %load, or %paste.

You can always call them using the ```%``` prefix, and if you’re calling a line magic on a line by itself, you can omit ```%```.
For more information about built-in magic commands, please refer to [IPython webpage](https://ipython.readthedocs.io/en/stable/interactive/magics.html?highlight=magic)

To exit IPython, you can do either ```quit``` or ```exit```.

#### Python script
If the job requires more than a few lines of python codes, then typing commands can be overwhelming. Also, it is likely that you make mistakes. In this case, writing all python commands in a python script and running this script to get the result is the way to go.

The first thing to do is create a python script file using text editors.
If you use ```vim```, you can easily create a file by typing ```vim filename.py```.
```
$ vim ctof.py
```
Then write all python codes there.
```
# This script converts temperature in Celsius to temperature in Fahrenheit.
#
# 2018.9.13

TinC = int(input("Enter a temperature in Celsius: "))

TinF = 9.0/5.0 * TinC + 32
print("Temperature:", TinC, "degC = ", TinF, "degF")
```
In this example, the first three lines start with ```#```.
Whenever a line starts with ```#```, python just skips it. So it is useful to add an explanation of your code in the script file.


You can execute this script in a few different ways.

##### 1. In Python
After launching python, you can execute your python script as follows.
```
>>> exec(open('ctof.py').read())
```
If you input temperature in Celsius when it asks temperature, you can get the result.
```
Enter a temperature in Celsius: 30
Temperature: 30 degC =  86.0 degF
```
If you think that this is not a really convenient way to run the program, there are alternative ways.

##### 2. In IPython
Running a python script in IPython is much easier than in Python.
After launching IPython with ```ipython```, you can just type
```
In [1]: %run ctof.py
```
to get the same result as in python.
You can even drop the file extension.
```
In [2]: %run ctof
```
even just ```run ctof.py``` or ```run ctof``` will do the job!

Another way to run the script, copy whole lines and paste them in IPython.
To paste copied lines in IPython, you can use a magic function ```%paste```.
```
In [3]: %paste
```
Then IPython shows the copied lines below. This is particularly useful if you need to run a few lines of your python script.

IPython allows you to open the text file with an exclamation mark (!) while you are in IPython.
```
In [5]: !vim ctof.py
```
This makes ```%paste``` really useful because you can open your script and get the necessary lines without leaving IPython.

##### 3. Using Python in the terminal
You do not launch python to execute python scripts. In the terminal, you can run your script by
```
$ python ctof.py
```

##### 4. As stand-alone in the terminal
If your script starts with
```
#!/usr/bin/env python3
```
you can run this script without typing ```python``` in the terminal.
When you save the script, make sure to change file modes to be executable.
```
$ chmod 755 ctof.py
```

To run this executable file,
```
$ ./ctof.py
```


#### Jupyter Notebook
You can use Jupyter Notebook for running python commands or a script.
First, launch Jupyter Notebook.
```
$ jupyter notebook
```
Then you get to have a new window in your web browser showing the file system in the working directory.
To start python, click ```new``` in the upper right corner and select ```Python 3```.
This will open a new tab that just looks like IPython.

Jupyter Notebook consists of cells. It is your choice how to compose the cell with your commands.
You can add all the lines in one cell, or a simple line for each cell.

Let's first copy all the lines in a single cell.
Jupyter Notebook provides a help page, and it says that you can hit ```control``` key and ```enter``` key together to run the cell.
When you run the cell, you are asked to give temperature in Celsius as before.

If we decide to use cells for each line, you will be asked to give temperature after run the cell with ```TinC = int(input("Enter a temperature in Celsius: "))```.

Once you are done, you can save the Jupyter Notebook file in the web browser.

To finish Jupyter Notebook, you can come back to the terminal where you typed ```jupyter notebook``` and hit ```^C``` TWICE!

In the class, we can explore what Jupyter Notebook offers extensively.

##### Launch Jupyter Notebook remotely
In some cases, you need to use a remote server for Jupyter Notebook.
In the remote server,
```
$ jupyter notebook --no-browser --port=8889
```
This launches Jupyter Notebook without opening web browser.
Then on your local machine,
```
$ ssh -N -f -L localhost:8899:localhost:8889 [accountname]@[servername]
```
and open the browser and go to http://localhost:8899
The web browser ask for the key, and you can find it in the terminal where you launch Jupyter Notebook.
