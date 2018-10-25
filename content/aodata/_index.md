+++
title= "Atmos. & Ocean Data"
date= 2018-10-24T09:11:24+09:00
description = ""
creatordisplayname = "Hajoon Song"
creatoremail = "hajsong@yonsei.ac.kr"
lastmodifierdisplayname = "Hajoon Song"
lastmodifieremail = "hajsong@yonsei.ac.kr"
tags = ["tag1","tag2"]
weight = 5
#pre ="<i class='fa fa-edit' ></i> "
alwaysopen = true
+++

We will explore how to load the atmospheric and oceanic data and read variables for the analysis and visualization of the data.

### NetCDF (Network Common Data Form (NetCDF)
#### Introduction
NetCDF is a platform-independent binary file format that facilitates the storage and sharing of data along with its metadata.
Versions of the tools needed to read and write the format are available on practically every operating system and in every major language used in the atmospheric and oceanic sciences.

Before discussing how to do netCDF i/o in Python, let's briefly review the structure of netCDF.
There are four general types of parameters in a netCDF file: global attributes, variables, variable attributes, and dimensions.

Global attributes are usually strings that describe the file as a whole, e.g., a title, who
created it, what standards it follows, etc.
Variables are the entities that hold data. These include both the data-proper (e.g., temperature, meridional wind, etc.), the domain the data is defined on (delineated by the dimensions), and
metadata about the data (e.g., units).
Variable attributes store the metadata associated with a variable.
Dimensions define a domain for the data-proper, but they also have values of their own (e.g., latitude values, longitude values, etc.), and thus you usually create variables for each dimension that are the
same name as the dimension.

#### A module for NetCDF files
There are a few number of modules that deal with netcdf files in python.
We are going to use the [```NetCDF4``` module](https://unidata.github.io/netcdf4-python) by [unidata](https://www.unidata.ucar.edu).

First, let's install the module using anaconda.
```
conda install -c anaconda netcdf4
```
We will explore how to handle the netCDF file using the [climatological SST data by Reynolds and Smith](/ATM4110/images/SST_Reyn_Smith.nc).

#### Reading NetCDF files
In Python, we use the ```Dataset``` constructor in ```netCDF4``` to load the netcdf file.
```
from netCDF4 import Dataset
f = Dataset('SST_Reyn_Smith.nc', 'r')
```

Then, check the structure of the file with the ```print``` statement
```
In [2]: print(f)
<class 'netCDF4._netCDF4.Dataset'>
root group (NETCDF3_CLASSIC data model, file format NETCDF3):
    dimensions(sizes): X(360), T(12), Y(180)
    variables(dimensions): float32 X(X), float32 T(T), float32 Y(Y), float32 sst(T,Y,X)
    groups:
```

This particular file does not have long description. But you may see a long list of information attached to the netcdf file.
```
In [2]: f = Dataset('ascat_20160728_000600_metopa_50709_eps_o_coa_2401_ovw.l2.nc','r')

In [3]: print(f)
<class 'netCDF4._netCDF4.Dataset'>
root group (NETCDF3_CLASSIC data model, file format NETCDF3):
    title: MetOp-A ASCAT Level 2 Coastal Ocean Surface Wind Vector Product
    title_short_name: ASCATA-L2-Coastal
    Conventions: CF-1.4
    institution: EUMETSAT/OSI SAF/KNMI
    source: MetOp-A ASCAT
    software_identification_level_1: 1000
    instrument_calibration_version: 0
    software_identification_wind: 2401
    pixel_size_on_horizontal: 12.5 km
    service_type: eps
    processing_type: O
    contents: ovw
    granule_name: ascat_20160728_000600_metopa_50709_eps_o_coa_2401_ovw.l2.nc
    processing_level: L2
    orbit_number: 50709
    start_date: 2016-07-28
    start_time: 00:06:00
    stop_date: 2016-07-28
    stop_time: 01:47:58
    equator_crossing_longitude:  321.384
    equator_crossing_date: 2016-07-28
    equator_crossing_time: 00:03:41
    rev_orbit_period: 6081.7
    orbit_inclination: 98.7
    history: N/A
    references: ASCAT Wind Product User Manual, http://www.osi-saf.org/, http://www.knmi.nl/scatterometer/
    comment: Orbit period and inclination are constant values. All wind directions in oceanographic convention (0 deg. flowing North)
    creation_date: 2016-07-28
    creation_time: 02:50:02
    dimensions(sizes): NUMROWS(3264), NUMCELLS(82)
    variables(dimensions): int32 time(NUMROWS,NUMCELLS), int32 lat(NUMROWS,NUMCELLS), int32 lon(NUMROWS,NUMCELLS), int16 wvc_index(NUMROWS,NUMCELLS), int16 model_speed(NUMROWS,NUMCELLS), int16 model_dir(NUMROWS,NUMCELLS), int16 ice_prob(NUMROWS,NUMCELLS), int16 ice_age(NUMROWS,NUMCELLS), int32 wvc_quality_flag(NUMROWS,NUMCELLS), int16 wind_speed(NUMROWS,NUMCELLS), int16 wind_dir(NUMROWS,NUMCELLS), int16 bs_distance(NUMROWS,NUMCELLS)
    groups:
```

Again, variables in python are in fact objects. Since we loaded the netcdf as ```f```, we can see all methods and attributes with ```dir(f)```.
```
In [9]: dir(f)
Out[9]:
['__class__',
 '__delattr__',
 '__dir__',
 .
 .
 .
 'variables',
 'vltypes']
```
Among them, ```dimensions``` and ```variables``` are used the most in reading the data.
As you can guess from the name of the method, ```dimensions``` shows the dimensions in the data.
```
In [13]: f.dimensions
Out[13]:
OrderedDict([('X',
              <class 'netCDF4._netCDF4.Dimension'>: name = 'X', size = 360),
             ('T',
              <class 'netCDF4._netCDF4.Dimension'>: name = 'T', size = 12),
             ('Y',
              <class 'netCDF4._netCDF4.Dimension'>: name = 'Y', size = 180)])
```
This means that variables have dimensions that are defined as ```X```, ```Y``` and ```T```.

To get the list of variables,
```
In [3]: f.variables.keys()
Out[3]: odict_keys(['X', 'T', 'Y', 'sst'])
```

To get the details of the variable, for example, ```T```,
```
In [5]: print(f.variables['T'])
<class 'netCDF4._netCDF4.Variable'>
float32 T(T)
    standard_name: time
    pointwidth: 1.0
    calendar: 360
    modulus: 12.0
    modulo: 12.0
    gridtype: 1
    units: months since 1960-01-01
unlimited dimensions:
current shape = (12,)
filling on, default _FillValue of 9.969209968386869e+36 used
```
You get the list of information associated with this variable. Following the notation of object, we can access these information. For example, the unit of ```T``` can be obtained by
```
In [7]: f.variables['T'].units
Out[7]: 'months since 1960-01-01'
```
The data can be obtained as the following.
```
In [10]: time = f.variables['T'][:]

In [11]: time
Out[11]:
masked_array(data=[ 0.5,  1.5,  2.5,  3.5,  4.5,  5.5,  6.5,  7.5,  8.5,
                    9.5, 10.5, 11.5],
             mask=False,
       fill_value=1e+20,
            dtype=float32)

In [12]: print(time)
[ 0.5  1.5  2.5  3.5  4.5  5.5  6.5  7.5  8.5  9.5 10.5 11.5]
```
The variable, ```time``` is MaskedArray.

All datasets of real-world phenomena will have missing data: instruments will malfunction, people will make measurement errors, etc.
Traditionally, missing data has been handled by assigning a value as the "missing value" and setting all elements of the dataset that are "bad" to that value. (Usually, the missing value is a value entirely out of the range of the expected values, e.g., -99999.)

As an object-oriented program, python thinks that variables are actually one type of objects carrying attributes and methods.
In the atmospheric and oceanic sciences (AOS) applications, this means that data and metadata (e.g., grid type, missing values, etc.) can both be attached to the "variable."
Using this capability, we can define array-like variables: masked arrays.
These array-like variables incorporate metadata attached to the arrays and define how that metadata can be used as part of analysis, visualization, etc.

Recall that arrays are n-dimensional vectors or grids that hold numbers (or characters).
Masked arrays, then, are arrays that also have a “mask” attributem which tells you which elements are bad, and masked variables are masked arrays that also give domain information and other metadata information.

The properties of MaskedArray type become clearer with ```sst``` variable. Let's read it.
```
In [15]: sst = f.variables['sst'][:]

In [16]: sst
Out[16]:
masked_array(
  data=[[[--, --, --, ..., --, --, --],
         [--, --, --, ..., --, --, --],
         [--, --, --, ..., --, --, --],
         ...,
         [-1.7999999523162842, -1.7999999523162842, -1.7999999523162842,
          ..., -1.7999999523162842, -1.7999999523162842,
          -1.7999999523162842],
          .
          .
          .
  mask=[[[ True,  True,  True, ...,  True,  True,  True],
       [ True,  True,  True, ...,  True,  True,  True],
       [ True,  True,  True, ...,  True,  True,  True],
       ...,
       [False, False, False, ..., False, False, False],
       [False, False, False, ..., False, False, False],
       [False, False, False, ..., False, False, False]],
       .
       .
       .
       [False, False, False, ..., False, False, False]]],
  fill_value=-999.9,
  dtype=float32)
```
As you can see, there are attributes attached to ```sst``` and they are ```data```, ```mask```, ```fill_value``` and ```dtype```.

The ```mask``` is a boolean array whose elements are set to ```True``` if the value in the corresponding array is considered "bad".
Thus, in the masked array ```sst```, the first row has mask values set to ```True```, and when the data for the masked array is printed out for a human viewer, those elements display "--" instead of a number.

We also note that the masked array ```sst``` has an attribute called ```fill_value``` that is set to ```-999.0```.
This is the value used to fill-in all the "bad" elements when we "deconstruct" the masked array.
That is to say, when we convert a masked array to a normal NumPy array, we need to put something in for all the "bad" elements (i.e., where the mask is ```True```): the value of ```fill_value``` is what we put in for the "bad" elements.

For masked arrays, operations using elements whose mask value is set to ```True``` will create results that also have a mask value set to ```True```.
For example,
```
In [24]: sst[0,10,10]
Out[24]: masked

In [25]: sst[0,20,10]
Out[25]: -0.59

In [26]: sst[0,10,10] + sst[0,20,10]
Out[26]: masked
```
Thus, the addition of a "good" value and a "bad" value yields a “bad” value.
Product of these two values also results in a "bad" value.
```
In [27]: sst[0,10,10] * sst[0,20,10]
Out[27]: masked
```

However, masked values are not considered in the statistical calculation.
For example, if you want to compute the climatological mean sea surface temperature in January,
```
In [46]: print(sst[0,:,:].mean())
13.551309957258193
```

In some cases, you can assign ```np.nan``` that represents "not a number" for "bad" values.
Assigning a specific value for a masked array can be done easily with the method ```filled```.
```
In [53]: sst.filled?
Signature: sst.filled(fill_value=None)
Docstring:
Return a copy of self, with masked values filled with a given value.
**However**, if there are no masked values to fill, self will be
returned instead as an ndarray.

Parameters
----------
fill_value : scalar, optional
    The value to use for invalid entries (None by default).
    If None, the `fill_value` attribute of the array is used instead.

Returns
-------
filled_array : ndarray
    A copy of ``self`` with invalid entries replaced by *fill_value*
    (be it the function argument or the attribute of ``self``), or
    ``self`` itself as an ndarray if there are no invalid entries to
    be replaced.

Notes
-----
The result is **not** a MaskedArray!
.
.
.

In [54]: jansst = sst[0,...]

In [55]: jansst
Out[55]:
masked_array(
  data=[[--, --, --, ..., --, --, --],
        [--, --, --, ..., --, --, --],
        [--, --, --, ..., --, --, --],
        ...,
        [-1.7999999523162842, -1.7999999523162842, -1.7999999523162842,
         ..., -1.7999999523162842, -1.7999999523162842,
         -1.7999999523162842],
        [-1.7999999523162842, -1.7999999523162842, -1.7999999523162842,
         ..., -1.7999999523162842, -1.7999999523162842,
         -1.7999999523162842],
        [-1.7999999523162842, -1.7999999523162842, -1.7999999523162842,
         ..., -1.7999999523162842, -1.7999999523162842,
         -1.7999999523162842]],
  mask=[[ True,  True,  True, ...,  True,  True,  True],
        [ True,  True,  True, ...,  True,  True,  True],
        [ True,  True,  True, ...,  True,  True,  True],
        ...,
        [False, False, False, ..., False, False, False],
        [False, False, False, ..., False, False, False],
        [False, False, False, ..., False, False, False]],
  fill_value=-999.9,
  dtype=float32)

In [56]: jansst.filled()    # fill masked spaces with "fill_value"
Out[56]:
array([[-999.9, -999.9, -999.9, ..., -999.9, -999.9, -999.9],
       [-999.9, -999.9, -999.9, ..., -999.9, -999.9, -999.9],
       [-999.9, -999.9, -999.9, ..., -999.9, -999.9, -999.9],
       ...,
       [  -1.8,   -1.8,   -1.8, ...,   -1.8,   -1.8,   -1.8],
       [  -1.8,   -1.8,   -1.8, ...,   -1.8,   -1.8,   -1.8],
       [  -1.8,   -1.8,   -1.8, ...,   -1.8,   -1.8,   -1.8]],
      dtype=float32)

In [57]: jansst.filled(np.nan)    # assign a specific value for the masked space
Out[57]:
array([[ nan,  nan,  nan, ...,  nan,  nan,  nan],
       [ nan,  nan,  nan, ...,  nan,  nan,  nan],
       [ nan,  nan,  nan, ...,  nan,  nan,  nan],
       ...,
       [-1.8, -1.8, -1.8, ..., -1.8, -1.8, -1.8],
       [-1.8, -1.8, -1.8, ..., -1.8, -1.8, -1.8],
       [-1.8, -1.8, -1.8, ..., -1.8, -1.8, -1.8]], dtype=float32)

In [58]: jansstfill = jansst.filled(np.nan)

In [59]: jansstfill.mean()
Out[59]: nan

In [70]: np.nanmean(jansstfill)
Out[70]: 13.55131
```
As you can see from this example, having ```np.nan``` as an element results in ```nan``` in the statistical calculation. Numpy provides functions for statistical calculations of arrays with ```np.nan```, and ```np.nanmean``` is one of them.

When you are done with reading the data, close the file with ```f.close()```.

#### Masked array
I think it will be useful to discuss more about the masked array.
We saw that the variables from NetCDF files are in masked array, and it has advantages in processing and visualizing the data (we will see this).

Then you may wonder whether we can create masked arrays. Yes, we can using Numpy module.
The ```numpy.ma``` module is available to work with data arrays with masks.
```
import numpy as np
import numpy.ma as ma
a = np.array([[1,2,3],[4,5,6]])
b = ma.masked_array(data=[1,2,3], mask=[True, False, False], fill_value=-999)
```
In IPython,
```
In [9]: b
Out[9]:
masked_array(data=[--, 2, 3],
             mask=[ True, False, False],
       fill_value=-999)
```
When dealing with the real data set where we cannot specify individual values for the array, other methods may be more useful to create masked arrays. For example,

|     function                       |          description                                     |
|:----------------------------------:|:--------------------------------------------------------:|
|  masked_equal(x, value[, copy])    | Mask an array where equal to a given value.              |
|  masked_greater(x, value[, copy])  | Mask an array where greater than a given integer value.  |
|  masked_less(x, value[, copy])     | Mask an array where less than a given value.             |
|  masked_invalid(a[, copy])         | Mask an array where invalid values occur (NaNs or infs). |
|  masked_values(x, value[, copy, …])| Mask using floating point equality.                      |
|  masked_where(condition, a[, copy])| Mask an array where a condition is met.                  |


### Hierarchical Data Format (HDF)
Data managed by NASA are usually in HDF type format (HDF4, HDF5, HDF EOS 5)

### GRIB

### Binary file
