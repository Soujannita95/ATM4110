+++
title= "Homework 6"
date= 2018-11-17T23:36:23+09:00
description = ""
creatordisplayname = "Hajoon Song"
creatoremail = "hajsong@yonsei.ac.kr"
lastmodifierdisplayname = "Hajoon Song"
lastmodifieremail = "hajsong@yonsei.ac.kr"
tags = ["confidence interval","precipitation"]
weight = 100
#pre ="<i class='fa fa-edit' ></i> "
alwaysopen = true
+++

### A confidence interval of monthly mean precipitation
In the class, we learned how to compute the 95% confidence interval for a population mean.
Using this method, try to estimate the 95% confidence interval for the monthly mean precipitation.

Since we do not know the population standard deviation of the monthly mean precipitation, we have to use the sample standard deviation. In this case, the confidence interval can be estimated using t-distribution.

$$
\bar{x} - t \frac{s}{\sqrt{N}} < \mu <\bar{x} + t \frac{s}{\sqrt{N}}
$$

where $t$ is a critical value determined from the $t_{n-1}$ distribution in such a way that there is area  0.95 (95%) between t and -t.

The value $n-1$ is called *degrees of freedom* , or *df* for short ($n$ is the size of the sample), or $\nu$.
It is a parameter of the t-curve and changes the shape of the t-curve, though usually not by much.
You can use [this table](http://www.sjsu.edu/faculty/gerstman/StatPrimer/t-table.pdf) to find out an appropriate $t$ critical values for selected $1 - \alpha$ and n-1.

By the way, the example we did in the lecture has 20 samplings so that the degrees of freedom is 19. From the table, the $t$ values for $1-\alpha = 0.95$ is 2.093. So we used this value.

You do not have to turn this homework in, but you can get extra points up to 5 if you turn in by 11/23 (Friday).
