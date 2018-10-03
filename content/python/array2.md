+++
title= "Array operation 2"
date= 2018-10-02T17:51:32+09:00
description = ""
creatordisplayname = "Hajoon Song"
creatoremail = "hajsong@yonsei.ac.kr"
lastmodifierdisplayname = "Hajoon Song"
lastmodifieremail = "hajsong@yonsei.ac.kr"
tags = ["array","numpy"]
weight = 107
#pre ="<i class='fa fa-edit' ></i> "
+++

So far we've learned how to make arrays, ask arrays to tell us about themselves, and manipulate arrays.
But what scientists really want to do with arrays is make calculations with them.
As a start, we discuss two ways to do exactly that.
Method 1 uses ```for``` loops, in analogue to the use of loops in traditional Fortran programming, to do element-wise array calculations.
Method 2 uses array syntax, where looping over array elements happens implicitly (this syntax is also found in Fortran 90 and later versions, IDL, etc.).

#### General array operation method 1: loops
It may be straightforward to use iteration for the array operation looping through each element.
Let's look at the following example.
```
import numpy as np
a = np.array([[2, 3.2, 5.5, -6.4],
              [3, 1, 2.1, 21]])
b = np.array([[4, 1.2, -4, 9.1],
              [6, 21, 1.5, -27]])
shape_a = np.shape(a)
product_ab = np.zeros(shape_a, dtype='f')
for i in range(shape_a[0]):
    for j in range(shape_a[1]):
        product_ab[i,j] = a[i,j] * b[i,j]
```
The flow of idea is

1. Create an array with the same size of ```a``` or ```b```.
2. Iterate the slow varying direction
3. Iterate the fast varying direction
4. At each point, compute the multiplication

Now, let's time how long the iteration takes to be done. Timing the process is quite simple in IPython because it provides magic functions: ```%timeit``` and ```%%timeit```.

```%timeit``` takes the command in the following position. So it is useful to check how long(slow) the function is.

On the other hand, ```%%timeit``` takes multiple lines of code from the following line. So this is useful when we want to test the speed of the block of the code.

In this example, ```%%timeit``` is appropriate to measure the time.

```
In [1]: %%timeit
   ...: import numpy as np
   ...: a = np.array([[2, 3.2, 5.5, -6.4],
   ...:               [3, 1, 2.1, 21]])
   ...: b = np.array([[4, 1.2, -4, 9.1],
   ...:               [6, 21, 1.5, -27]])
   ...: shape_a = np.shape(a)
   ...: product_ab = np.zeros(shape_a, dtype='f')
   ...: for i in range(shape_a[0]):
   ...:     for j in range(shape_a[1]):
   ...:         product_ab[i,j] = a[i,j] * b[i,j]
   ...:

8.76 µs ± 47.8 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
```

Try to time the iteration when we need to compute large arrays.
```
np.random.seed(0)                 # to initialize the random number generation
a = np.random.randn(1000, 1000)
b = np.random.randn(1000, 1000)
shape_a = np.shape(a)
product_ab = np.zeros(shape_a, dtype='f')
for i in range(shape_a[0]):
    for j in range(shape_a[1]):
        product_ab[i,j] = a[i,j] * b[i,j]
```
In my machine, this takes 501 ms ± 7.83 ms per loop (mean ± std. dev. of 7 runs, 1 loop each).

#### General array operation method 2: array syntax
The basic idea behind array syntax is that, much of the time, arrays interact with each other on a corresponding element basis, and so instead of requiring the user to write out the nested ```for``` loops explicitly, the loops and elementwise operations are done implicitly in the operator.

Consider the first example. We can get ```product_ab``` using the multiplication operator.
```
a = np.array([[2, 3.2, 5.5, -6.4],
             [3, 1, 2.1, 21]])
b = np.array([[4, 1.2, -4, 9.1],
             [6, 21, 1.5, -27]])
product_ab = a * b
```
You can see that ```product_ab``` is exactly the same as above.

Using ```%%timeit```, let's measure the speed.
```
In [4]: %%timeit
    ...: a = np.array([[2, 3.2, 5.5, -6.4],
    ...:              [3, 1, 2.1, 21]])
    ...: b = np.array([[4, 1.2, -4, 9.1],
    ...:              [6, 21, 1.5, -27]])
    ...: product_ab = a * b
    ...:
3.75 µs ± 235 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
```
How about the elementwise multiplication for large arrays?
```
In [5]: %%timeit
    ...: np.random.seed(0)
    ...: a = np.random.randn(1000, 1000)
    ...: b = np.random.randn(1000, 1000)
    ...: product_ab = a * b
    ...:
50 ms ± 375 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)
```
Avoiding iteration makes the calculation about 10 times faster! (And you have fewer lines of the code.)

In this example, we see that arithmetic operators are automatically defined to act elementwise when operands are NumPy arrays or scalars. (Operators do have function equivalents in NumPy, e.g., product, add, etc., for the situations where you want to do the operation using function syntax.)
Additionally, the output array c is automatically created on assignment; there is no need to initialize the output array using zeros.

Here is the table of arithmetic operator implemented in NumPy.

| Operator | Equivalent function   | Description                         |
|:--------:|:---------------------:|-------------------------------------|
| +	       | ```np.add```	       | Addition (e.g., 1 + 1 = 2)          |
| -	       | ```np.subtract```     | Subtraction (e.g., 3 - 2 = 1)       |
| -	       | ```np.negative```     | Unary negation (e.g., -2)           |
| *	       | ```np.multiply```     | Multiplication (e.g., 2 * 3 = 6)    |
| /	       | ```np.divide```       | Division (e.g., 3 / 2 = 1.5)        |
| //       | ```np.floor_divide``` | Floor division (e.g., 3 // 2 = 1)   |
| **       | ```np.power```        | Exponentiation (e.g., 2 ** 3 = 8)   |
| %	       | ```np.mod```          | Modulus/remainder (e.g., 9 % 4 = 1) |

#### Exercise: Compute the potential temperature

Write a function that takes a 2-D array of pressures ($p$, in mbar) and a 2-D array of temperatures ($T$, in K) and returns the corresponding potential temperature, assuming a reference pressure ($p_0$) of 1000 mbar.
Thus, the function’s return value is an array of the same shape and type as the input arrays.
Recall that potential temperature is given by:
$$
\theta = T\left(\frac{p_0}{p}\right)^{\kappa},
$$
where $\kappa$ = $R/cp$ = 2/7 for a perfect diatomic gas like the atmosphere.

If you go with iteration, you might come up with the following.
```
def theta(p, T, p0 = 1000, kappa = 2./7.):
    ny, nx = p.shape
    output = np.zeros((ny, nx))
    for j in range(ny):
        for i in range(nx):
            output[j,i] = T[j,i] * (p0 / p[j,i])**kappa
    return output
```

Using array operation,
```
def theta(p, T, p0 = 1000, kappa = 2./7.):
    return T * (p0 / p)**kappa
```

Now, let's use the real atmospheric data which is the climatological air temperature at 500 mbar and compute the potential temperature.

After getting the data from [this link](/ATM4110/images/T_p.npz), let's read it in IPython.
```
import numpy as np
data = np.load('T_p.npz')
T = data['T']+273.15    # convert the unit from degC to K
p = data['P']
```
As the code becomes long, It is convenient to write a script to include all the functions and scripts.
```
import numpy as np
    """
    Compute the potential temperature
    using pressure (mbar) and Temperature (K)
    """
def theta1(p, T, p0 = 1000, kappa = 2./7.):
    ny, nx = p.shape
    output = np.zeros((ny, nx))
    for j in range(ny):
        for i in range(nx):
            output[j,i] = T[j,i] * (p0 / p[j,i])**kappa
    return output

def theta2(p, T, p0 = 1000, kappa = 2./7.):
    return T * (p0 / p)**kappa

data = np.load('T_p.npz')
T = data['T']+273.15    # convert the unit from degC to K
p = data['P']

potT1 = theta1(p, T)
potT2 = theta2(p, T)

print(np.array_equal(potT1, potT2))
```

The command in the ```print``` function determines whether two arrays are identical.
The output is ```True```, which is what we expect.

If you time the speed of ```theta1``` and ```theta2```, you can see that ```theta2``` is much faster.
```
In [11]: %timeit pt1 = theta1(p, T)
27.3 ms ± 91.1 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)

In [12]: %timeit pt2 = theta2(p, T)
109 µs ± 817 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)
```
Using array operator is 250 times faster!
