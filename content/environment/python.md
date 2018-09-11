+++
title= "Python"
date= 2018-09-07T12:36:51+09:00
description = ""
creatordisplayname = "Hajoon Song"
creatoremail = "hajsong@yonsei.ac.kr"
lastmodifierdisplayname = "Hajoon Song"
lastmodifieremail = "hajsong@yonsei.ac.kr"
tags = ["python"]
weight = 101
#pre ="<i class='fa fa-edit' ></i> "
#alwaysopen = true
+++

{{% panel %}}I refer to [Unidata online python training page](https://unidata.github.io/online-python-training/introduction.html) for this page.{{% /panel %}}

{{% alert %}}I recommend you to visit [Unidata Online Python Training](https://unidata.github.io/online-python-training/) page.{{% /alert %}}


The main program language we will use in this course to handle atmospheric data is python.
Before getting into "What is Python?", here is one of the statements that shows why we want to learn it

{{<icon name="fa-quote-left" >}}
I have used a combination of Perl, Fortran, NCL, Matlab, R and others for routine research, but found out this general- purpose language, Python, can handle almost all in an efficient way from requesting data from remote online sites to statistics, and graphics.
{{<icon name="fa-quote-right" >}}

#### What Is Python?
{{<revealjs theme="night" transition="fade" >}}
## What is Python?
---
#### Python is a “batteries included” computer programming language.
More concretely, Python is a programming language that, in contrast to other programming languages such as C, Fortran, or Java, allows users to more readily focus and solve domain problems instead of dealing with the complexity of how a computer operates. Python achieves this goal by having the following attributes:
---
#### Python is a **high-level** language.
It abstracts underlying computer-related technical details. For example, Python does not make its users think too much about computer memory management or proper declaration of variables and uses safe assumptions about what the programmer is trying to convey. In addition, a high-level language can be expressed in a manner closer to English prose or mathematical equations.
---
#### Python is a **general-purpose** language.
It can be used for all problems that a computer is capable of rather than specializing in a specific area such as statistical analysis. For example, Python can be used for both artificial intelligence and statistical analysis. Python can be used for a variety of heterogeneous tasks within a given work-flow.
---
#### Python is an **interpreted** language.
Evaluation of code to obtain results can happen immediately rather than having to go through a time-consuming, compile and run cycle, which thereby speeds up the thinking and experimentation processes. IPython is an interactive form of the Python language also invented by Fernando Pérez. These environments excel for rapid-prototype of code or quick and simple experimentation with new ideas.
---
#### Python has a strong tools for solving problems.
A standard library and numerous third-party libraries (e.g. numpy, matplotlib,...) yield a vast array of existing codebases and examples for solving problems.
---
#### Python has many, many users
It allows users to quickly find solutions and example code to problems with the help of Google and Stackoverflow.
{{</revealjs>}}

These features, perhaps, come with a minor cost of reduced language performance, but this is a trade-off the vast majority of users are willing to make in order to gain all the advantages Python has to offer.

#### what you can do with Python?
Python is not just for atmospheric sciences. It has a wide area of application, and earth science is one of them.
Largely, you may categorize applications into:

+ Web development
+ Data science

##### 1. Web development
Python can be used to create the webpage.
We all know that webpage is basically html files (not Python).
Although you can edit html files for the webpage, you can also use python to create html files for you.
This is what I did to create the [ATM2106 class webpage](https://hajsong.github.io/ATM2106/).

Some sites wait for the input from the users and process the job before delivering the results back to users (Like Amazon).
Python can play an important role in these dynamic websites. For example, one of my friends build the website called [Trevii](https://www.trevii.com/D/1/NYC) which helps you organize the trip after gathering informations online. The backbone of this website is also python!

##### 2. Data science
In some sense, the purpose of using Python in this course is to do data science.
Python is efficient when handling a large dataset. It does not necessarily faster than other programming languages like Fortran or C, as mentioned above. This is because Python has to figure out the data type while users specify it for Fortran or C. If you tell Python the data type, then it can process the data with much higher speed (approaching the speed of Fortran or C).

Here, *Data science* includes machine learning! Here is an example from [Towards Data Science](https://towardsdatascience.com/simple-machine-learning-model-in-python-in-5-lines-of-code-fe03d72e78c6).

The goal of this machine learning is to find out how to combine three numbers we provide.
The first task is to generate training set.
```
from random import randint
TRAIN_SET_LIMIT = 1000
TRAIN_SET_COUNT = 100

TRAIN_INPUT = list()
TRAIN_OUTPUT = list()
for i in range(TRAIN_SET_COUNT):
    a = randint(0, TRAIN_SET_LIMIT)
    b = randint(0, TRAIN_SET_LIMIT)
    c = randint(0, TRAIN_SET_LIMIT)
    op = a + (2*b) + (3*c)
    TRAIN_INPUT.append([a, b, c])
    TRAIN_OUTPUT.append(op)
```
The training set consists of 100 sets of three numbers, ```a```, ```b```, and ```c```, and ```op = a + 2*b + 3*c```.
You can adjust the size of the training set by modifying ```TRAIN_SET_COUNT```.

Now, we will train the machine with this dataset. The package ```scikit-learn``` allows us to do machine learning easily.
```
from sklearn.linear_model import LinearRegression

predictor = LinearRegression()
predictor.fit(X=TRAIN_INPUT, y=TRAIN_OUTPUT)
```
The machine learning is done, and ```predictor``` will compute ```op``` with three inputs.
```
X_TEST = [[10, 20, 30]]
outcome = predictor.predict(X=X_TEST)
coefficients = predictor.coef_

print('Outcome : {}\nCoefficients : {}'.format(outcome, coefficients))
```
We see that the coefficients from machine learning are exactly same as the one used in the training set.
There are online courses from [Stanford](https://www.coursera.org/learn/machine-learning) and [Caltech](https://work.caltech.edu/telecourse.html) if you are interested in learning it more.
