+++
title= "Array operation 1"
date= 2018-10-01T13:51:55+09:00
description = ""
creatordisplayname = "Hajoon Song"
creatoremail = "hajsong@yonsei.ac.kr"
lastmodifierdisplayname = "Hajoon Song"
lastmodifieremail = "hajsong@yonsei.ac.kr"
tags = ["array","numpy"]
weight = 106
#pre ="<i class='fa fa-edit' ></i> "
+++

We handled  list variables in the previous chapter, and we can add any types of data to the list, even another list!
The computational overhead to support that flexibility, however, is non-trivial, and so lists are not practical to use for most scientific computing problems.

In other words, lists are too slow.

To solve this problem, Python has a package called ```NumPy``` which defines an array data type that in many ways is like the array data type in Fortran.

An array is like a list except: All elements are of the same type, so operations with arrays are much faster; multi-dimensional arrays are more clearly supported; and array operations are supported.
To utilize ```NumPy```’s functions and attributes, you import the package ```numpy.```
Because NumPy functions are often used in scientific computing, you usually import NumPy as an alias, e.g., ```import numpy as N``` or ```import numpy as np```, to save yourself some typing.
In the following context, it is assumed that the NumPy package is imported as ```np```.

#### Creating arrays
The most basic way of creating an array is to take an existing list and convert it into an array using the ```array``` function in NumPy.
```
mylist = [[2, 3, -5],[21, -2, 1]]
myarray = np.array(mylist)
```
- What does it happen when you try to convert the list ```[[2, 3, -5],[21, -2]]```?

A row vector and a column vector can be made differently.
```
a = np.array([2, 3, 4])          # an array with three element
b = np.array([[2, 3, 4]])        # a 1x3 row vector
c = np.array([[2], [3], [4]])    # a 3x1 column vector
```

Sometimes you will want to make sure your NumPy array elements are of a specific type. To force a certain numerical type for the array, set the ```dtype``` keyword to a type code:
```
a = np.array(mylist, dtype='d')
```
where the string "```d```" is the typecode for double-precision floating point. Other options you have are

+ ```f``` : single precision floating
+ ```i``` : short integer
+ ```l``` : long integer

To see the difference between single precision and double precision, let's try
```
>>> b = np.array(10./3., dtype = 'd')
>>> c = np.array(10./3., dtype = 'f')
>>> print(b)
>>> print(c)
```

{{% panel %}}```np.array``` is the function that create a variable with the array object called ```ndarray```.{{% /panel %}}

Often you will find the moment when you want to create an array of a specific size but with unknown or undetermined values. In this case, you can use either ```zeros``` or ```empty``` functions.
```
a = np.zeros((3, 2), dtype = 'd')
```
or
```
a = np.zeros([3, 2], dtype = 'd')
```
{{%expand "How do np.zeros and np.empty differ?" %}}
Here is the answer [from stackoverflow](https://stackoverflow.com/questions/43145332/numpy-array-of-zeros-or-empty):

- ```empty()``` does not initialize the memory, therefore your array will be filled with garbage and you will have to initialize all cells.
- ```zeros()``` initializes everything to 0. Therefore, if your final result includes lots of zeros, this will save you the time to set all those array cells to zero manually.
{{% /expand%}}

Another array you will commonly create is the array whose elements increase or decrease monotonically. In this case, you can use the ```arange``` function.
```
>>> a = np.arange(10)
>>> print(a)
[0 1 2 3 4 5 6 7 8 9]
```
The array ```a``` has 10 integer elements.
What if you want to create an array with floating numbers?
```
In [10]: a = np.arange(10.0)

In [11]: b = np.arange(10, dtype = 'f')

In [12]: print(a)
[0. 1. 2. 3. 4. 5. 6. 7. 8. 9.]

In [13]: print(b)
[0. 1. 2. 3. 4. 5. 6. 7. 8. 9.]

In [14]: whos
Variable   Type       Data/Info
-------------------------------
a          ndarray    10: 10 elems, type `float64`, 80 bytes
b          ndarray    10: 10 elems, type `float32`, 40 bytes
np         module     <module 'numpy' from '/Us<...>kages/numpy/__init__.py'>
```

In case you want to create an 3 by 4 array with random numbers,
```
In [22]: np.random.random((3,4))
Out[22]:
array([[0.59544951, 0.38485189, 0.42626703, 0.38313338],
       [0.51624656, 0.04025792, 0.65402374, 0.70589402],
       [0.1984409 , 0.8254778 , 0.25162249, 0.89099201]])
```
It is noted that ```np.random``` is a submodule and it has a method called ```random```.

#### Array indexing
Like lists, element addresses start with zero, so the first element of a 1-D array ```a``` is ```a[0]```, the second is ```a[1]```, etc.
You can also reference elements starting from the end, e.g., element ```a[-1]``` is the last element in a 1-D array ```a```.

Array slicing follows rules very similar to list slicing:

- Element addresses in a range are separated by a colon.
- The lower limit is inclusive, and the upper limit is exclusive.
- If one of the limits is left out, the range is extended to the end of the
range (e.g., if the lower limit is left out, the range extends to the very
beginning of the array).
- Thus, to specify all elements, use a colon by itself.

```
In [14]: a = np.array([2, 3.2, 5.5, -6.4, -2.2, 2.4])

In [15]: print(a[1])
3.2

In [16]: print(a[1:4])
[ 3.2  5.5 -6.4]

In [17]: print(a[2:])
[ 5.5 -6.4 -2.2  2.4]

In [18]: print(a[-2:])
[-2.2  2.4]
```

For multi-dimensional arrays, indexing between different dimensions is separated by commas.
Note that the fastest varying dimension is always the last index, the next fastest varying dimension is the next to last index, and so forth (this follows C convention).
Thus, a 2-D array is indexed [row, col].
Slicing rules also work as applied for each dimension (e.g., a colon selects all elements in that dimension). Here’s an example:
```
>>> a = np.array([[2, 3.2, 5.5, -6.4, -2.2, 2.4],
                 [1, 22, 4, 0.1, 5.3, -9],
                 [3, 1, 2.1, 21, 1.1, -2]])
>>> print(a)
[[ 2.   3.2  5.5 -6.4 -2.2  2.4]
 [ 1.  22.   4.   0.1  5.3 -9. ]
 [ 3.   1.   2.1 21.   1.1 -2. ]]
```
Then, what is ```a[1,2]```? How about ```a[:,3]```? ```a[1,:]```? ```a[1,1:4]```?
```
>>> print(a[1,2])
4.0
>>> print(a[:,3])
[-6.4  0.1 21. ]
>>> print(a[1,:])
[ 1.  22.   4.   0.1  5.3 -9. ]
>>> print(a[1,1:4])
[22.   4.   0.1]
```

It is also possible to get, for example, every other elements or every third elements.
```
In [13]: a[1,::2]
Out[13]: array([1. , 4. , 5.3])
```
Python reverses the order if we give a negative number after two colons.
```
In [14]: a[1,::-1]
Out[14]: array([-9. ,  5.3,  0.1,  4. , 22. ,  1. ])
```


The extraction of the element can be possible by passing the list of the index.
```
In [84]: i = [1, 3, 4]

In [85]: a[2,i]
Out[85]: array([ 1. , 21. ,  1.1])
```

How about this?
```
In [7]: j = [0,1]

In [8]: i = [2,4]

In [9]: a[j,i]
```
This will give you the elements at the index (0,2) and (1,4) so that
```
Out[9]: array([5.5, 5.3])
```
Suppose you want to extract all elements that are at the first two rows and the third and fifth columns.
```
In [11]: a[j,:]
Out[11]:
array([[ 2. ,  3.2,  5.5, -6.4, -2.2,  2.4],
       [ 1. , 22. ,  4. ,  0.1,  5.3, -9. ]])

In [12]: a[j][:,i]
Out[12]:
array([[ 5.5, -2.2],
       [ 4. ,  5.3]])
```

#### Array inquiry
Arrays in Python are eventually object to which a list of attributes and methods are attached.
Here are some of functions for the array inquiry.

For the 2-D array ```a``` where
```
a = np.array([[2, 3.2, 5.5, -6.4, -2.2, 2.4],
             [1, 22, 4, 0.1, 5.3, -9],
             [3, 1, 2.1, 21, 1.1, -2]])
```
To get the size of the array, one can use ```np.shape(a)``` that gives ```(3, 6)``` in this example.
If we want to know the total number of elements in the array, ```np.size(a)``` gives ```18```.
It is noted that ```len(a)``` function that was used for list variables will return ```3```.
To find out the data type, try ```a.dtype.char```.

#### Array manipulation
In addition to finding things about an array, NumPy includes many functions to manipulate arrays.
Some, like ```transpose```, come from linear algebra, but NumPy also includes a variety of array manipulation functions that enable you to modify arrays into the form you need to do the calculations you want.

##### Copying
Let's suppose we want to copy the array ```a``` to ```b``` as ```b = a```.
Then change the element ```b[0,0] = -2.0```. What happens to ```a```?
```
In [13]: b = a

In [14]: b[0,0] = -2.0

In [15]: print(b)
[[-2.   3.2  5.5 -6.4 -2.2  2.4]
 [ 1.  22.   4.   0.1  5.3 -9. ]
 [ 3.   1.   2.1 21.   1.1 -2. ]]

In [16]: print(a)
[[-2.   3.2  5.5 -6.4 -2.2  2.4]
 [ 1.  22.   4.   0.1  5.3 -9. ]
 [ 3.   1.   2.1 21.   1.1 -2. ]]
```
Interestingly, the array ```a``` is also changed and ```a``` and ```b``` are the same!
In Python, the equal sign is not copying variables.

To copy the array, we can use the function, ```np.copy```.
```
In [3]: b = a.copy()

In [4]: b[0,0] = -2.0

In [5]: print(b)
[[-2.   3.2  5.5 -6.4 -2.2  2.4]
 [ 1.  22.   4.   0.1  5.3 -9. ]
 [ 3.   1.   2.1 21.   1.1 -2. ]]

In [6]: print(a)
[[ 2.   3.2  5.5 -6.4 -2.2  2.4]
 [ 1.  22.   4.   0.1  5.3 -9. ]
 [ 3.   1.   2.1 21.   1.1 -2. ]]
```
{{% alert theme="danger" %}}This also applies to the list. To copy the list variable ```a``` to ```b```, do ```b = a.copy()```.{{% /alert %}}

##### Transpose
The transpose of an array ```a``` can be done with ```np.transpose(a)``` or ```a.T```:
```
In [44]: np.transpose(a)
Out[44]:
array([[ 2. ,  1. ,  3. ],
       [ 3.2, 22. ,  1. ],
       [ 5.5,  4. ,  2.1],
       [-6.4,  0.1, 21. ],
       [-2.2,  5.3,  1.1],
       [ 2.4, -9. , -2. ]])

In [45]: a.T
Out[45]:
array([[ 2. ,  1. ,  3. ],
       [ 3.2, 22. ,  1. ],
       [ 5.5,  4. ,  2.1],
       [-6.4,  0.1, 21. ],
       [-2.2,  5.3,  1.1],
       [ 2.4, -9. , -2. ]])
```

If we define an array as in the first example and transpose it, there is no change.
```
In [59]: a = np.arange(5)

In [60]: print(a)
[0 1 2 3 4]

In [61]: print(a.T)
[0 1 2 3 4]
```

To make the transpose effective, the array has to be a vector or a multi-dimensional array.
```
In [62]: b = np.array([[2, 3, 4]])          # a row vector

In [63]: print(b)
[[2 3 4]]

In [64]: print(b.T)
[[2]
 [3]
 [4]]

In [65]: c = np.array([[2], [3], [4]])    # a column vector

In [66]: print(c)
[[2]
 [3]
 [4]]

In [67]: print(c.T)
[[2 3 4]]
```

##### Convert from N-D to 1-D array
We can make a N-dimensional array to a 1-D array or a vector.
There are two functions that make this happen : ```ravel``` and ```flatten```.
```
In [5]: np.ravel(a)
Out[5]:
array([ 2. ,  3.2,  5.5, -6.4, -2.2,  2.4,  1. , 22. ,  4. ,  0.1,  5.3,
       -9. ,  3. ,  1. ,  2.1, 21. ,  1.1, -2. ])

In [6]: a.ravel()
Out[6]:
array([ 2. ,  3.2,  5.5, -6.4, -2.2,  2.4,  1. , 22. ,  4. ,  0.1,  5.3,
       -9. ,  3. ,  1. ,  2.1, 21. ,  1.1, -2. ])

In [7]: a.flatten()
Out[7]:
array([ 2. ,  3.2,  5.5, -6.4, -2.2,  2.4,  1. , 22. ,  4. ,  0.1,  5.3,
       -9. ,  3. ,  1. ,  2.1, 21. ,  1.1, -2. ])
```

The function ```flatten``` is built-in in the NumPy array class, and it is not possible to use as ```np.flatten(a)```.

Another important difference between two is that while ```flatten``` copies the array, ```ravel``` doesn't.
```
In [34]: a_r = a.ravel()

In [35]: a_f = a.flatten()

In [36]: a_f = a.flatten()

In [37]: a_f[3] = 10

In [38]: print(a_f)
[ 2.   3.2  5.5 10.  -2.2  2.4  1.  22.   4.   0.1  5.3 -9.   3.   1.
  2.1 21.   1.1 -2. ]

In [39]: print(a)
[[ 2.   3.2  5.5 -6.4 -2.2  2.4]
 [ 1.  22.   4.   0.1  5.3 -9. ]
 [ 3.   1.   2.1 21.   1.1 -2. ]]

 In [40]: a_r = a.ravel()

In [41]: a_r[3] = 10

In [43]: print(a_r)
[ 2.   3.2  5.5 10.  -2.2  2.4  1.  22.   4.   0.1  5.3 -9.   3.   1.
  2.1 21.   1.1 -2. ]

In [44]: print(a)
[[ 2.   3.2  5.5 10.  -2.2  2.4]
 [ 1.  22.   4.   0.1  5.3 -9. ]
 [ 3.   1.   2.1 21.   1.1 -2. ]]

```

##### Reshaping
We can convert the shape of the array as long as we keep the size the same.
```
Out[50]:
array([[ 2. ,  3.2],
       [ 5.5, -6.4],
       [-2.2,  2.4],
       [ 1. , 22. ],
       [ 4. ,  0.1],
       [ 5.3, -9. ],
       [ 3. ,  1. ],
       [ 2.1, 21. ],
       [ 1.1, -2. ]])

In [51]: a.reshape(9,2)
Out[51]:
array([[ 2. ,  3.2],
       [ 5.5, -6.4],
       [-2.2,  2.4],
       [ 1. , 22. ],
       [ 4. ,  0.1],
       [ 5.3, -9. ],
       [ 3. ,  1. ],
       [ 2.1, 21. ],
       [ 1.1, -2. ]])
```

##### Concatenation
Concatenation, or joining of two arrays in NumPy, is primarily accomplished using the routines ```np.concatenate```, ```np.vstack```, and ```np.hstack```.
```np.concatenate``` takes a tuple or list of arrays as its first argument, as we can see here:
```
In [46]: x = np.array([1, 2, 3])

In [47]: y = np.array([3, 2, 1])

In [48]: np.concatenate([x, y])
Out[48]: array([1, 2, 3, 3, 2, 1])
```
You can concatenate more than two arrays.
```
In [49]: np.concatenate([x, y, x])
Out[49]: array([1, 2, 3, 3, 2, 1, 1, 2, 3])
```
And even 2-D arrays.
```
In [60]: a = np.arange(6).re(2,3)

In [61]: print(a)
[[0 1 2]
 [3 4 5]]

In [62]: np.concatenate((a, a))
Out[62]:
array([[0, 1, 2],
       [3, 4, 5],
       [0, 1, 2],
       [3, 4, 5]])
```

We can control the axis along which the arrays are concatenated.
```
In [63]: np.concatenate((a, a), axis=1)
Out[63]:
array([[0, 1, 2, 0, 1, 2],
       [3, 4, 5, 3, 4, 5]])
```
In some cases, ```vstack``` and ```hstack``` functions are more intuitive.
```
In [64]: np.vstack((a, a))
Out[64]:
array([[0, 1, 2],
       [3, 4, 5],
       [0, 1, 2],
       [3, 4, 5]])

In [65]: np.hstack((a, a))
Out[65]:
array([[0, 1, 2, 0, 1, 2],
       [3, 4, 5, 3, 4, 5]])
```

##### Repetition
When repeating each element is desired, ```repeat``` function is the right choice.
```
In [66]: print(d)
[[0. 1. 2.]
 [3. 4. 5.]]

In [67]: np.repeat(a,3)
Out[67]: array([0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5])
```
By default, it use the flattened input array, and return a flat output array.
We can specify the axis along which to repeat values.
```
In [76]: np.repeat(a,3, axis=0)
Out[76]:
array([[0, 1, 2],
       [0, 1, 2],
       [0, 1, 2],
       [3, 4, 5],
       [3, 4, 5],
       [3, 4, 5]])

In [77]: np.repeat(a,3, axis=1)
Out[77]:
array([[0, 0, 0, 1, 1, 1, 2, 2, 2],
       [3, 3, 3, 4, 4, 4, 5, 5, 5]])
```

##### Convert type
The type of elements of the array can be converted using ```astype``` function.
```
In [69]: d = a.astype('f')

In [70]: print(d)
[[0. 1. 2.]
 [3. 4. 5.]]
```

#### Creating arrays representing the grid information of data
In the atmospheric and oceanic sciences, we often find ourselves using 2-D regularly gridded slices of data where the *x*-and *y*-locations of each array element is given by the corresponding elements
of the *x* and *y* vectors.
Wouldn't it be nice to get a 2-D array whose elements are the x-values for each column and a 2-D array whose elements are the y-values for each row? The ```meshgrid``` function does just that.

Let's first create vectors for longitude and latitude with the space of 5 degrees.
```
In [2]: lon = np.arange(-180, 180, 5)

In [3]: lat = np.arange(-90, 91, 5)
```
According to the indexing rule in Python, ```lon``` starts from -180 with the increment of 5 but stops just before 180. That means that 180 is not a part of the array ```lon```.
On the other hand, ```lat``` stops at 91, so it includes 90.

To create 2-D arrays for longitude and latitude,
```
In [4]: [X, Y] = np.meshgrid(lon, lat)    # or X, Y = np.meshgrid(lon, lat)

In [5]: print(X)
[[-180 -175 -170 ...  165  170  175]
 [-180 -175 -170 ...  165  170  175]
 [-180 -175 -170 ...  165  170  175]
 ...
 [-180 -175 -170 ...  165  170  175]
 [-180 -175 -170 ...  165  170  175]
 [-180 -175 -170 ...  165  170  175]]

In [6]: print(Y)
[[-90 -90 -90 ... -90 -90 -90]
 [-85 -85 -85 ... -85 -85 -85]
 [-80 -80 -80 ... -80 -80 -80]
 ...
 [ 80  80  80 ...  80  80  80]
 [ 85  85  85 ...  85  85  85]
 [ 90  90  90 ...  90  90  90]]
```

You may have just one output
```
In [7]: G = np.meshgrid(lon, lat)

In [8]: G?
Type:        list
String form:
[array([[-180, -175, -170, ...,  165,  170,  175],
           [-180, -175, -170, ...,  165,  170,  17 <...> ,  80],
           [ 85,  85,  85, ...,  85,  85,  85],
           [ 90,  90,  90, ...,  90,  90,  90]])]
Length:      2
Docstring:
list() -> new empty list
list(iterable) -> new list initialized from iterable's items
```
As you can see, ```meshgrid``` returns the list variable ```G```, and ```G[0]``` is equivalent to ```X``` and ```G[1]``` to ```Y```.

When dealing with a 3-D data set, you need to include the third axis which is usually either height or depth.
```
In [9]: lev = np.array([0, 250, 500, 850, 1000])
```
Here, we want to replicate ```lev``` for each horizontal grid point. NumPy provides a function called ```tile``` to make this happen.

For ```X``` and ```Y```,
```
In [71]: nz = len(lev)

In [72]: XX = np.tile(X, [nz, 1, 1])

In [73]: YY = np.tile(Y, [nz, 1, 1])
```

For ```Z```,
```
In [10]: ny, nx = X.shape

In [11]: Z = np.tile(lev, [ny, nx, 1])

In [12]: print(Z.shape)
(37, 72, 5)
```
Although we were able to create a 3-D array, ```Z```, the location of the axis is little different from the convention we use (usually [t,z,y,x]). Using ```transpose``` function in NumPy, we can easily permute the order of axis.

{{% panel %}}Why on earth do we have to go through the transpose of the array? According to the docstring of ```tile```, if the number of the dimension of the array is smaller than the length of the list in the second argument, NumPy prepends new axes to match the number of dimension. So a shape (3,) array is promoted to (1, 1, 3) for 3-D replication. {{% /panel %}}
