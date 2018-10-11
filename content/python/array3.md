+++
title= "Array operation 3"
date= 2018-10-10T09:39:11+09:00
description = ""
creatordisplayname = "Hajoon Song"
creatoremail = "hajsong@yonsei.ac.kr"
lastmodifierdisplayname = "Hajoon Song"
lastmodifieremail = "hajsong@yonsei.ac.kr"
tags = ["Numpy","array"]
weight = 108
#pre ="<i class='fa fa-edit' ></i> "
#alwaysopen = true
+++

We are going to look at more array operations using Numpy before diving into the linear algebra.

#### Fancy indexing
NumPy offers more indexing facilities than regular Python sequences. In addition to indexing by integers and slices, as we saw before, arrays can be indexed by arrays of integers and arrays of booleans.
```
>>> a = np.arange(12)**2                       # the first 12 square numbers
>>> i = np.array( [ 1,1,3,8,5 ] )              # an array of indices
>>> a[i]                                       # the elements of a at the positions i
array([ 1,  1,  9, 64, 25])
>>>
>>> j = np.array( [ [ 3, 4], [ 9, 7 ] ] )      # a bidimensional array of indices
>>> a[j]                                       # the same shape as j
array([[ 9, 16],
       [81, 49]])
```
The second example shows that Numpy returns the result in the same format of the input.

When the indexed array a is multidimensional, a single array of indices refers to the first dimension of a. The following example shows this behavior by converting an image of labels into a color image using a palette.

```
>>> palette = np.array( [ [0,0,0],                # black
...                       [255,0,0],              # red
...                       [0,255,0],              # green
...                       [0,0,255],              # blue
...                       [255,255,255] ] )       # white
>>> image = np.array( [ [ 0, 1, 2, 0 ],           # each value corresponds to a color in the palette
...                     [ 0, 3, 4, 0 ]  ] )
>>> palette[image]                            # the (2,4,3) color image
array([[[  0,   0,   0],
        [255,   0,   0],
        [  0, 255,   0],
        [  0,   0,   0]],
       [[  0,   0,   0],
        [  0,   0, 255],
        [255, 255, 255],
        [  0,   0,   0]]])
```
We can also give indexes for more than one dimension. The arrays of indices for each dimension must have the same shape.
```
>>> a = np.arange(12).reshape(3,4)
>>> a
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
>>> i = np.array( [ [0,1],                        # indices for the first dim of a
...                 [1,2] ] )
>>> j = np.array( [ [2,1],                        # indices for the second dim
...                 [3,3] ] )
>>>
>>> a[i,j]                                     # i and j must have equal shape
array([[ 2,  5],
       [ 7, 11]])
>>>
>>> a[i,2]
array([[ 2,  6],
       [ 6, 10]])
>>>
>>> a[:,j]                                     # i.e., a[ : , j]
array([[[ 2,  1],
        [ 3,  3]],
       [[ 6,  5],
        [ 7,  7]],
       [[10,  9],
        [11, 11]]])
```
Another common use of indexing with arrays is the search of the maximum value of time-dependent series:
```
>>> time = np.linspace(20, 145, 5)                 # time scale
>>> data = np.sin(np.arange(20)).reshape(5,4)      # 4 time-dependent series
>>> time
array([  20.  ,   51.25,   82.5 ,  113.75,  145.  ])
>>> data
array([[ 0.        ,  0.84147098,  0.90929743,  0.14112001],
       [-0.7568025 , -0.95892427, -0.2794155 ,  0.6569866 ],
       [ 0.98935825,  0.41211849, -0.54402111, -0.99999021],
       [-0.53657292,  0.42016704,  0.99060736,  0.65028784],
       [-0.28790332, -0.96139749, -0.75098725,  0.14987721]])
>>>
>>> ind = data.argmax(axis=0)                  # index of the maxima for each series
>>> ind
array([2, 0, 3, 1])
>>>
>>> time_max = time[ind]                       # times corresponding to the maxima
>>>
>>> data_max = data[ind, range(data.shape[1])] # => data[ind[0],0], data[ind[1],1]...
>>>
>>> time_max
array([  82.5 ,   20.  ,  113.75,   51.25])
>>> data_max
array([ 0.98935825,  0.84147098,  0.99060736,  0.6569866 ])
>>>
>>> np.all(data_max == data.max(axis=0))
True
```

```np.argmax``` or ```np.argmin``` finds the index with the maximum or minimum values in the array, respectively.
In case when you want to find the indices that satisfy the condition, ```np.where``` or ```np.nonzero``` can be useful.
```
>>> x = np.arange(9.).reshape(3, 3)
>>> np.where( x > 5 )
(array([2, 2, 2]), array([0, 1, 2]))
>>> np.nonzero( x > 5 )
(array([2, 2, 2]), array([0, 1, 2]))
>>> x[np.where( x > 3.0 )]               # Note: result is 1D.
array([ 4.,  5.,  6.,  7.,  8.])
>>> np.where(x < 5, x, -1)               # Note: broadcasting.
array([[ 0.,  1.,  2.],
       [ 3.,  4., -1.],
       [-1., -1., -1.]])
>>> np.nonzero( x > 5 )
```
When three arguments are provided, ```np.where``` considers them as
```np.where(mask, a, b)``` which can be roughly thought of as ```a[i] if mask[i] else b[i]```.
This is what happened in the last example.

#### Linear Algebra

##### Vectors
Before starting, let me claify the notation of vectors first.
A vector of length *n* is just a sequence (or array, or tuple) of *n* numbers, which we write as $\mathbf{x}=[x_1,\dots,x_n]$. Then the sum of two vectors, $\mathbf{x}$ and $\mathbf{y}$, is
$$
\mathbf{x} + \mathbf{y} = \begin{bmatrix}
         x_1  \newline
         x_2 \newline
         \vdots \newline
         x_n
        \end{bmatrix}
        +
        \begin{bmatrix}
         y_1  \newline
         y_2 \newline
         \vdots \newline
         y_n
        \end{bmatrix}
        =
        \begin{bmatrix}
         x_1+y_1  \newline
         x_2+y_2 \newline
         \vdots \newline
         x_n+y_n
        \end{bmatrix}
$$
Scalar multiplication is expressed as
$$
\gamma \mathbf{x} = \begin{bmatrix}
                    \gamma x_1 \newline
                    \gamma x_2 \newline
                    \vdots \newline
                    \gamma x_n
                    \end{bmatrix}
$$

As we did last time, these operations can be done easily.
```
x = np.ones(3)            # Vector of three ones
y = np.array((2, 4, 6))   # Converts tuple (2, 4, 6) into array
print(x + y)
print(4 * x)
```

Another way to do summation of two vector is
```
def add_vectors(v, w):
    return [vi + wi for vi, wi in zip(v, w)]

add_vectors(x, y)
```

Similarly, the subtraction of vectors can be done using ```-``` or
```
def subtract_vectors(v, w):
    return [vi - wi for vi, wi in zip(v, w)]
subtract_vectors(x, y)
```

The inner product of vectors $\mathbf{x}$ and $\mathbf{y}$ is defined as
$$
\mathbf{x}^T\mathbf{y} = \Sigma_{i=1}^{n}x_i y_i
$$
Two vectors are called orthogonal if their inner product is zero.

The norm of a vector $\mathbf{x}$ represents its "length" (i.e., its distance from the zero vector) and is defined as
$$
||\mathbf{x}|| = \sqrt{\mathbf{x}^T\mathbf{x}}
$$

In Python, the inner product of $\mathbf{x}$ and $\mathbf{y}$ is
```
np.sum(x * y)          # Inner product of x and y
```
and the norm of it is
```
np.sqrt(np.sum(x**2))
```
or
```
np.linalg.norm(x)
```

Can you write a short function for the inner product operation using a single line ```for```
iteration?
{{%expand "How about the norm calculation?" %}}
```
def sq_sum_of_squares(v):
    """ sqrt(v1 * v1 + v2 * v2 ... + vn * vn)"""
    return sum(vi ** 2 for vi in v)**(0.5)
```
{{% /expand%}}


##### Matrices
Matrices are a neat way of organizing data for use in linear operations.
For notation, an $n\times k$ matrix $\mathbf{A}$ is expressed as
$$
\mathbf{A} = \begin{bmatrix}
                a\_{11} & a\_{12} & \cdots & a\_{1k} \newline
                a\_{21} & a\_{22} & \cdots & a\_{2k} \newline
                \vdots  & \vdots  &        & \vdots  \newline
                a\_{n1} & a\_{n2} & \cdots & a\_{nk} \newline
            \end{bmatrix}
$$
If $n=k$, it is a square matrix. If $\mathbf{A} = \mathbf{A}^T$, it is a symmetric matrix.

Here are some basic operations for matrices.
```
>>> import numpy as np
>>> a = np.array([[1.0, 2.0], [3.0, 4.0]])
>>> print(a)
[[ 1.  2.]
 [ 3.  4.]]

>>> a.transpose()
array([[ 1.,  3.],
       [ 2.,  4.]])

>>> np.linalg.inv(a)
array([[-2. ,  1. ],
       [ 1.5, -0.5]])

>>> u = np.eye(2) # unit 2x2 matrix; "eye" represents "I"
>>> u
array([[ 1.,  0.],
       [ 0.,  1.]])
>>> j = np.array([[0.0, -1.0], [1.0, 0.0]])

>>> j @ j        # matrix product
array([[-1.,  0.],
       [ 0., -1.]])

>>> np.trace(u)  # trace
2.0
>>> np.diag(u)   # Extract a diagonal
array([1., 1.])
```

##### Linear problems

One of the more common problems in linear algebra is solving a matrix-vector equation. Here is an example. We seek the vector $\mathbf{x}$ that solves the equation
$$
\mathbf{y} = \mathbf{A}\mathbf{x},
$$
where $\mathbf{y}$ is the observations and $\mathbf{A}$ is the matrix containing explanatory variables).
This problem imposes a set of linear equations, so the $i^{th}$ observation is written as
$$
y_i = a\_{i,1} x_1 + a\_{i,2} x_2 + \cdots + a\_{i,k} x_k.
$$

###### 1. When $n = k$
This problem has the same numbers of equations and unknowns. It means that there is a unique solution.

A number called the determinant of the matrix tells us whether this matrix can be inverted or not.
If the determinant of $\mathbf{A}$ is not zero, then we say that $\mathbf{A}$ is nonsingular.
Perhaps the most important fact about determinants is that $\mathbf{A}$ is nonsingular if and only if $\mathbf{A}$ is of full column rank.

Then the solution is just $\mathbf{x} = \mathbf{A}^{-1}\mathbf{y}$.

In IPython,
```
In [2]: A = np.arange(9).reshape(3,3)

In [3]: np.linalg.det(A)
Out[3]: 0.0

In [4]: A = np.arange(9).reshape(3,3) + np.random.rand(3,3)

In [5]: y = np.arange(3)

In [6]: np.linalg.inv(A) @ y
Out[6]: array([ 0.05905976,  0.79934638, -0.50158537])

In [7]: np.dot(np.linalg.inv(A),y)
Out[7]: array([ 0.05905976,  0.79934638, -0.50158537])
```

###### 2. When $n \gt k$
In this case, there is no unique solution, but we can still seek a best approximation for $\mathbf{x}$.
After admitting that there must be errors associated with this linear problem, let's introduce a vector $\mathbf{n}$ that represents the error. Now the linear problem can be written as the following.
$$
\mathbf{y} = \mathbf{A}\mathbf{x} + \mathbf{n}.
$$
That the best estimate for the solution should lead to the smallest error.
In other words, we want to pick $\mathbf{x}$ that minimizes
$$
J = \mathbf{n}^T \mathbf{n} = (\mathbf{A}\mathbf{x} - \mathbf{y})^T(\mathbf{A}\mathbf{x} - \mathbf{y}).
$$
That $\mathbf{x}$ satisfies
$$
\frac{\partial J}{\partial \mathbf{x}} = 0
$$
Using  
$$
\frac{\partial \left( \mathbf{q}^T \mathbf{r} \right)}{\partial \mathbf{q}}
= \frac{\partial \left( \mathbf{r}^T \mathbf{q} \right)}{\partial \mathbf{q}}
= \mathbf{r},
$$
$$
\frac{\partial \left( \mathbf{q}^T \mathbf{q} \right)}{\partial \mathbf{q}}
=2\mathbf{q},
$$
and
$$
\frac{\partial\left(\mathbf{q}^T\mathbf{A}\mathbf{q}\right)}{\partial \mathbf{q}}
= \left(\mathbf{A} + \mathbf{A}^T \right)\mathbf{q},
$$
we can obtain the solution as
$$
\mathbf{x} = \left(\mathbf{A}^T\mathbf{A}\right)\mathbf{A}^T\mathbf{y}
$$

###### 3. When $n \lt k$
This is the case when there are fewer equations than unknowns, suggesting there is an infinite number of solutions.

###### 4. How to solve the linear problem in Python
If you choose to compute the inverse of the matrix,
```
x = np.linalg.inv(A.T @ A) @ A.T @ y
```
or
```
x = np.dot(np.dot(np.linalg.inv(np.dot(A.T, A)), A.T), y).
```
It is generally not recommended to directly compute the inverse matrix. Numpy has a function to solve the linear problem.
```
x = np.linalg.lstsq(A, y)
```

##### Exercise
We did the exercise to compute the potential temperature using
$$
\theta = T \left(\frac{p_0}{p}\right)^k
$$
when the temperature, pressure and the reference pressure are given.

At this time, let's to find the linear expression of $T$ and $p$ for the potential temperature.
You can get the data from [this link](/ATM4110/images/T_p.npz).

#### File I/O
For Numpy's native file format, one can use ```np.save``` and ```np.load```.
These functions were used in our previous exercise.

When you want to save the array in the text file, ```np.savetxt``` does it for you.
When you need to read the text file, you can use ```np.loadtxt```.
```
a = np.array([1,2,3,4,5])
np.savetxt('out.txt',a)
b = np.loadtxt('out.txt')
print b
```

If the data are somehow formatted with either comma or space, you can use ```np.getfromtxt```.
When ```example.dat``` has
```
1800  1  1    -6.1    -6.1    -6.1 1
1800  1  2   -15.4   -15.4   -15.4 1
1800  1  3   -15.0   -15.0   -15.0 1
1800  1  4   -19.3   -19.3   -19.3 1
1800  1  5   -16.8   -16.8   -16.8 1
1800  1  6   -11.4   -11.4   -11.4 1
1800  1  7    -7.6    -7.6    -7.6 1
1800  1  8    -7.1    -7.1    -7.1 1
1800  1  9   -10.1   -10.1   -10.1 1
1800  1 10    -9.5    -9.5    -9.5 1
```
in Python, ```data``` will be 10 by 7 ndarray if is created by ```np.genfromtxt```
```
data = np.genfromtxt('example.dat')
```
