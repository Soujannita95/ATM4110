+++
title= "Homework 5"
date= 2018-10-16T08:39:05+09:00
description = ""
creatordisplayname = "Hajoon Song"
creatoremail = "hajsong@yonsei.ac.kr"
lastmodifierdisplayname = "Hajoon Song"
lastmodifieremail = "hajsong@yonsei.ac.kr"
tags = ["linear algebra","file io"]
weight = 100
#pre ="<i class='fa fa-edit' ></i> "
alwaysopen = true
+++

#### A close look at the Keeling Curve

Accurately measuring CO$_2$ in the atmosphere requires lots of effort and support. It is unfortunate that there were years without financial support in the early period of this program and David Keeling couldn't make measurements.

This is shown in the dataset! You can see that some of the entries of CO$_2$ concentration are $-99.99$. Considering that this dataset contains concentration values, the negative entry doesn't make sense. So $-99.99$ is not the CO$_2$ concentration but tells us that no measurements were made in those times.

Now, let's try to use linear algebra to fill those gaps.
