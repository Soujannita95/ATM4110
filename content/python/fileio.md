+++
title= "Dealing with real data"
date= 2018-10-15T20:02:05+09:00
description = ""
creatordisplayname = "Hajoon Song"
creatoremail = "hajsong@yonsei.ac.kr"
lastmodifierdisplayname = "Hajoon Song"
lastmodifieremail = "hajsong@yonsei.ac.kr"
tags = ["python","File IO"]
weight = 109
#pre ="<i class='fa fa-edit' ></i> "
#alwaysopen = true
+++

The atmospheric and oceanic sciences (AOS) are "data" intensive fields, whether data refers to observations or model output.
Most of the analysis we do involve datasets, and so facilities for file input/output (i/o) are critical.
Fortunately, Python has very robust facilities for file i/o, and we will be dealing with realistic datasets using Python.

#### Data in the text file
Some data is not too big and stored in the text file. A good example is the [CO$_2$ concentration in the atmosphere](/ATM4110/images/co2_mm_mlo.txt).
In fact this is the famous "KEELING CURVE"
Reading the text file is possible using the built-in function, ```open``` statement:
```
f = open('co2_mm_mlo.txt','r')
contents = f.readlines()
f.close()
```
As you might guess, ```f``` is an object that many methods are attached. Do you remember how to list all available methods and attributes?
```
dir(f)
```

You can see that ```close``` we used above is one of the methods. It is to flush and close the IO object. Once the file IO is closed, you can grab a handle on it. (You can not do anything with ```f``` unless you ```open``` the text file again.)

The method ```readlines``` goes through each line and save it as an element of the list, ```contents```.
```
In [4]: contents[:10]
Out[4]:
['# --------------------------------------------------------------------\n',
 '# USE OF NOAA ESRL DATA\n',
 '# \n',
 '# These data are made freely available to the public and the\n',
 '# scientific community in the belief that their wide dissemination\n',
 '# will lead to greater understanding and new scientific insights.\n',
 '# The availability of these data does not constitute publication\n',
 '# of the data.  NOAA relies on the ethics and integrity of the user to\n',
 '# ensure that ESRL receives fair credit for their work.  If the data \n',
 '# are obtained for potential use in a publication or presentation, \n']
 .
 .
 .
 '# NOTE: In general, the data presented for the last year are subject to change, \n',
 '# depending on recalibration of the reference gas mixtures used, and other quality\n',
 '# control procedures. Occasionally, earlier years may also be changed for the same\n',
 '# reasons.  Usually these changes are minor.\n',
 '#\n',
 '# CO2 expressed as a mole fraction in dry air, micromol/mol, abbreviated as ppm\n',

 '#  (-99.99 missing data;  -1 no data for #daily means in month)\n',
 '#\n',
 '#            decimal     average   interpolated    trend    #days\n',
 '#             date                             (season corr)\n',
 '1958   3    1958.208      315.71      315.71      314.62     -1\n',
 '1958   4    1958.292      317.45      317.45      315.29     -1\n',
 .
 .
 .
 ```

Well, this dataset has quite a few numbers of lines that are not values, and we want to exclude this header. Good news is that lines in the header start a special characters "#". So we can determine whether the line is in the header or not by evaluating the first letter.

The string object has a method for this. It is called ```startswith```.
```
CO2 = []
for line in contents:
    if line.startswith('#') is False:
        print(line)
```

We can see that ```line``` is a string variable containing all the characters of each line.
(Try ```type(line)``` to see the type of ```line```.)

We are interested in the CO$_2$ concentration that is in the middle of the string ```line```.
So we need to somehow break this long string into pieces to extract the CO$_2$ concentration.

Python has a host of string manipulation methods, built-in to string variables (a.k.a., objects), which are ideal for dealing with contents from text files.
We will mention only a few of these methods.
The ```split``` method of a string object takes a string and breaks it into a list using a separator. For instance:
```
In [9]: print(line)
2018   9    2018.708      405.51      405.51      409.02     29

In [10]: type(line)
Out[10]: str

In [11]: print(line.split())
['2018', '9', '2018.708', '405.51', '405.51', '409.02', '29']
```

Finally, once we have the strings we desire, we can convert them to numerical types in order to make calculations.

If you loop through a list of strings, you can use the ```float``` and ```int``` functions on the string to get a number. For instance

```
CO2 = []
for line in contents:
    if line.startswith('#') is False:
        values = line.split()
        CO2.append(float(values[3]))
```

For future purpose, we may want to save this array as another text file.
To write a string to the file that is defined by the file object ```f```, use the ```write``` method attached to the file object:
```
f.write(astr)
```
Here, ```astr``` is the string you want to write to the file. Note that a newline character is not automatically written to the file after the string is written.

To write a list of strings to the file, use the ```writelines``` method:
```
f.writelines(contents)
```
Here, ```contents``` is a list of strings.

In this example, we want to write CO$_2$ concentration to a new file, ```co2_keeling.txt```.
```
fileout = open('co2_keeling.txt', 'w')    # open the text file to write
fileout.writelines(str(CO2))
fileout.close()
```
If you view the text file, the values are stored in one line.
We can save one value in each line as the following.
```
outputstr = ['\n'] * len(CO2)
for i in range(len(CO2)):
    outputstr[i] = str(CO2[i]) + outputstr[i]

fileout = open('co2_keeling.txt', 'w')    # open the text file to write
fileout.writelines(outputstr)
fileout.close()
```

#### Data in the csv (comma-separated values) file
You often find data in csv format. It is not very different from text files, but data values are separated with comma as the name infers. You can read csv format data as above, but slightly different.

As an example, I extracted the car accident statistics in 2017 where the incidents are sorted by the age of the drivers who caused the accident. Get the data from [here](/ATM4110/images/caraccident_data.csv).

Let's follow the steps in the previous example.
```
f = open('caraccident_data.csv','r')
contents = f.readlines()
f.close()
```
The list variable ```contents``` has each line as its element. The first line that is saved in  ```contents[0]``` contains the name of each column, but it is not the data values. So, I would do the following to read the total number of accident that is in the second column.
```
tot = []
for line in contents[1:]:
    val = line.split(',')
    tot.append(float(val[1]))
```
When using the ```split``` method, we specified that the line could be separated by the comma.

Python carries the module called ```csv``` to read and write csv files. That allows us to avoid doing tedious work of counting columns and rows.

Let's use the ```csv``` module.
```
import csv

with open('caraccident_data.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    cnt = 0
    for row in csv_reader:
        if cnt == 0:
            print(f'Column names are {", ".join(row)}')
        else:
            print(f'Values are {", ".join(row)}')
        cnt += 1
```

Rather than deal with a list of individual String elements, you can read CSV data directly into a dictionary. The ```csv``` module provides a method ```DictReader``` for us to organize the data as a dictionary variable.
```
import csv

# Option 1
f = open('caraccident_data.csv', 'r')
csv_reader = csv.DictReader(f)
print(csv_reader.fieldnames)
for row in csv_reader:
    print(f'Total number of {row["type"]} is {row["total"]}')
f.close()

# Option 2
with open('caraccident_data.csv', 'r') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        print(f'Total number of {row["type"]} is {row["total"]}')
```

#### Reading the CSV-type data using Pandas
[*pandas*](https://pandas.pydata.org) is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.
This package makes it even easier to handle cvs-type data files.
```
import pandas as pd
data = pd.read_csv('caraccident_data.csv')
print(data)
```
In IPython,
```
In [4]: whos
Variable   Type         Data/Info
---------------------------------
data       DataFrame                 type    tota<...>\n\n[6 rows x 10 columns]
pd         module       <module 'pandas' from '/U<...>ages/pandas/__init__.py'>

In [5]: print(data)
             type    total  less than 20   ...     61-64  greater than 65  unknown
0        accident  1143175         44501   ...     62373           115674    75485
1      death toll     4185           125   ...       313              838        2
2   casualty toll  1803325         65622   ...     93589           172330   148784
3  major casualty    96810          3605   ...      7353            14565     1687
4  minor casualty   581589         19729   ...     35310            55037    50046
5  other casualty  1124926         42288   ...     50926           102728    97051

[6 rows x 10 columns]
```
To see the name of columns, you can try
```
data.columns
```

There are two different ways to print out a column.
```
data.type
data["type"]
```
This is how you can grab the rows.
```
data.head(2)        # prints the first 2 rows
data.tail(1)        # prints the last low
```

If you access the element, you can combine the name of the column and the number of the row.
```
print(data.type[3], data.total[3])
```

Using the indexing, we can get more than one rows.
```
print(data.total[1:3])
```

Selecting elements in a specific location is very similar to extracting elements from the array.
There are two ways of doing it.
When using ```loc``` method, you can specify the name of the columns.
```
data.loc[:2, ['61-64','greater than 65']]
```
Or you can use ```iloc``` for the location of the columns.
```
data.iloc[:1, 7:]
```

If you want to switch columns and rows,
```
data.T
```

```pandas``` package provides a simple statistical tools attached to the variable.
```
data.describe()
```

##### Exercise: Extract statistical information from the dataset.
One of the current issues is whether we regulate the permit for the senior drivers for the safety reasons.
Let's evaluate the data of the car accident in 2017 and see whether there is a statistical background for the regulation.
Possible questions to be evaluated are.

1. Are there more car accident caused by the drivers older than 60 than those with the age between 20-40?
2. Do the accidents tend to be major by the drivers older than 60?
