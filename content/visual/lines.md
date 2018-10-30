+++
title= "Lines"
date= 2018-10-29T16:57:56+09:00
description = ""
creatordisplayname = "Hajoon Song"
creatoremail = "hajsong@yonsei.ac.kr"
lastmodifierdisplayname = "Hajoon Song"
lastmodifieremail = "hajsong@yonsei.ac.kr"
tags = ["matplotlib","plot"]
weight = 1
#pre ="<i class='fa fa-edit' ></i> "
#alwaysopen = true
+++

Line plots are created by the pyplot ```plot``` function.
I think it is helpful to use the example to explore the matplotlib's ```plot``` command.
Let's imagine we want to see the trend of global air temperature. Then one of the best way to show the trend is a line plot against the time.

# Draw lines using the data
In this example, we will plot the time series of air temperature using the dataset from [HadCRUT4](https://crudata.uea.ac.uk/cru/data/temperature/)


```python
import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset, num2date
%matplotlib qt                # Figures in a separate window
# %matplotlib inline          # Figures in this browser
```

    UsageError: unrecognized arguments: # Figures in a separate window


### Read the temperature data
We are going to read two datasets: one for the mean temperature (absolute.nc) and the other one for the time series of temperature anomaly (HadCRUT.4.6.0.0.median.nc).


```python
f = Dataset('absolute.nc', 'r')
print(f.variables.keys())
T = f.variables['tem'][:]    # monthly data
lon = f.variables['lon'][:]
lat = f.variables['lat'][:]
f.close()
```


```python
f = Dataset('HadCRUT.4.6.0.0.median.nc', 'r')
print(f.variables.keys())
Tanom = f.variables['temperature_anomaly'][:]
time = f.variables['time'][:]
# print(f.variables['time'])
f.close()
```

### The trend of the global temperature.
First we want to see the time change of the global temperature anomaly.  
Let's compute the global mean of temperature anomaly.


```python
[nt, ny, nx] = Tanom.shape    # Dimension size
mTanom = np.mean( np.mean(Tanom, axis=2), axis=1)
```


```python
f = plt.figure(1)             # Number is assigned to the window
plt.plot(time, mTanom)
```

The plot shows the increasing trend of the global mean temperature.  
But, the time axis is not easy to interpret, maybe because it is in the unit of second?  
Let's check.


```python
f = Dataset('HadCRUT.4.6.0.0.median.nc', 'r')
Tunit = f.variables['time'].units
Tcalendar = f.variables['time'].calendar
print(Tunit, Tcalendar)
f.close()
```

    days since 1850-1-1 00:00:00 gregorian


If we convert the unit from days to years, that makes the plot easier to read.  
This means that we need to either change the unit or touch the x-axis.

#### 1. Change the time unit
The module ```netCDF4``` provides a handy function called ```num2date```. Using this function, the float numbers for time become a new type called ```datetime```.


```python
Tdate = num2date(time, Tunit, Tcalendar)    # At least 2 arguments are required.
```


```python
print(Tdate[0], type(Tdate[0]))
```

    1850-01-16 12:00:00 <class 'datetime.datetime'>


This ```datetime``` type variables can dump out year, month and day with methods called ```year```, ```month``` and ```day```, respectively.  
To see the full list of methods and attributes, try ```dir(Tdate[0])```.


```python
f = plt.figure(2)
plt.plot(Tdate, mTanom)
```




    [<matplotlib.lines.Line2D at 0x13f6ee2e8>]



#### 2. Change the x-axis
We can directly modify the x-axis using the axis object.


```python
f = plt.figure(3)
plt.plot(time, mTanom)
```




    [<matplotlib.lines.Line2D at 0x13fd49668>]




```python
# new x axis
ax = plt.gca()
ix = np.arange(0,nt,240)
ixlabel = time[ix]/365 + 1850
ax.set_xticks(time[ix])
ax.set_xticklabels(ixlabel.astype(int))
ax.set_xlabel('year')
ax.set_ylabel('T anomaly (degC)')
ax.set_title('Time series of T anomaly, HadCRUT4')
```




    Text(0.5,1,'Time series of T anomaly, HadCRUT4')



### More than one lines in one plot
At this time, let's separate the temperature trend into global, northern hemisphere and southern hemisphere.


```python
# T in the northern hemisphere
inorth = np.where(lat>0)
T_nh = np.mean(np.mean(Tanom[:, inorth[0], :], axis=2), axis=1)
```


```python
# T in the southern hemisphere
isouth = np.where(lat<0)
T_sh = np.mean(np.mean(Tanom[:, isouth[0], :], axis=2), axis=1)
```


```python
T_nh.shape
```




    (2025,)




```python
f, ax = plt.subplots(1, 1, figsize=(12,6))
ax.plot(Tdate, mTanom)
ax.plot(Tdate, T_nh)
ax.plot(Tdate, T_sh)
ax.set_xlabel('year')
ax.set_ylabel('T anomaly (degC)')
ax.set_title('Time series of T anomaly, HadCRUT4')
```




    Text(0.5,1,'Time series of T anomaly, HadCRUT4')



You can plot every lines with a single command


```python
f, ax = plt.subplots(1, 1, figsize=(12,6))
ax.plot(Tdate, mTanom, Tdate, T_nh, Tdate, T_sh)
ax.set_xlabel('year')
ax.set_ylabel('T anomaly (degC)')
ax.set_title('Time series of T anomaly, HadCRUT4')
```




    Text(0.5,1,'Time series of T anomaly, HadCRUT4')



As you can see, you can keep adding lines on top of others. But, it is already hard to tell which one is which.  
Let's plot each line differently.  
You can get the full list of markers from [here](https://matplotlib.org/api/markers_api.html), and line-style from [here](https://matplotlib.org/gallery/lines_bars_and_markers/line_styles_reference.html).


```python
f, ax = plt.subplots(1, 1, figsize=(12,6))
ax.plot(Tdate, mTanom, '.', Tdate, T_nh, '^', Tdate, T_sh, '*')
# ax.plot(Tdate, mTanom, '-', Tdate, T_nh, ':', Tdate, T_sh, '--')
ax.set_xlabel('year')
ax.set_ylabel('T anomaly (degC)')
ax.set_title('Time series of T anomaly, HadCRUT4')
```




    Text(0.5,1,'Time series of T anomaly, HadCRUT4')



Or we need to label them.


```python
f, ax = plt.subplots(1, 1, figsize=(12,6))
ax.plot(Tdate, mTanom, label = 'global')
ax.plot(Tdate, T_nh, label = 'NH')
ax.plot(Tdate, T_sh, label = 'SH')
ax.legend()
ax.set_xlabel('year')
ax.set_ylabel('T anomaly (degC)')
ax.set_title('Time series of T anomaly, HadCRUT4')
```




    Text(0.5,1,'Time series of T anomaly, HadCRUT4')




```python
f, ax = plt.subplots(1, 1, figsize=(12,6))
ax.plot(Tdate, mTanom, label = 'global')
ax.plot(Tdate, T_nh, label = 'NH')
ax.plot(Tdate, T_sh, label = 'SH')
ax.legend()
ax.set_xlabel('year')
ax.set_ylabel('T anomaly (degC)')
ax.set_title('Time series of T anomaly, HadCRUT4')
```




    Text(0.5,1,'Time series of T anomaly, HadCRUT4')



It may be helpful to read if the lines are thinner than this and in different colors.
(The full list of available colors can be found [here](https://matplotlib.org/examples/color/named_colors.html))


```python
f, ax = plt.subplots(1, 1, figsize=(12,6))
l1 = ax.plot(Tdate, mTanom, color='black', linewidth=0.5, label='global')
l2 = ax.plot(Tdate, T_nh, color='dodgerblue', linewidth=0.5, label='NH')
l3 = ax.plot(Tdate, T_sh, color=np.array([189, 48, 57])/255, linewidth=0.5, label = 'SH')
# l3 = ax.plot(Tdate, T_sh, color='#BD3039', label = 'SH')
ax.legend()
ax.set_xlabel('year')
ax.set_ylabel('T anomaly (degC)')
ax.set_title('Time series of T anomaly, HadCRUT4')
```




    Text(0.5,1,'Time series of T anomaly, HadCRUT4')



It is still not easy to see all the lines,


```python
intv = 6    # every 6 month
f, ax = plt.subplots(1, 1, figsize=(12,6))
ax.plot(Tdate[::intv], mTanom[::intv], color='black', label='global')
ax.plot(Tdate[::intv], T_nh[::intv], color='dodgerblue', label='NH')
ax.plot(Tdate[::intv], T_sh[::intv], color=np.array([189, 48, 57])/255, label = 'SH')
# l3 = ax.plot(Tdate, T_sh, color='#BD3039', label = 'SH')
ax.legend()
ax.set_xlabel('year')
ax.set_ylabel('T anomaly (degC)')
ax.set_title('Time series of T anomaly, HadCRUT4')
```




    Text(0.5,1,'Time series of T anomaly, HadCRUT4')



I want to make this plot more charming.


```python
# Remove the plot frame lines.    
f, ax = plt.subplots(1, 1, figsize=(12,6))    
ax.spines["top"].set_visible(False)    
ax.spines["bottom"].set_visible(False)    
ax.spines["right"].set_visible(False)    
ax.spines["left"].set_visible(False)    
```


```python
# Ensure that the axis ticks only show up on the bottom and left of the plot.    
# Ticks on the right and top of the plot are generally unnecessary chartjunk.    
ax.get_xaxis().tick_bottom()    
ax.get_yaxis().tick_left()   
```


```python
# Limit the range of the plot to only where the data is.    
# Avoid unnecessary whitespace.    
ax.set_ylim(-2, 2)    
```




    (-2, 2)




```python
# Provide tick lines across the plot to help your viewers trace along    
# the axis ticks. Make sure that the lines are light and small so they    
# don't obscure the primary data lines.    
intv = 6    # every 6 month
for y in np.arange(-2, 2.1, 0.5):    
    ax.plot(Tdate[::intv], [y] * len(Tdate[::intv]), "--", lw=0.5, color="black", alpha=0.3)    
```


```python
# Remove the tick marks; they are unnecessary with the tick lines we just plotted.    
ax.tick_params(axis="both", which="both", bottom="off", top="off",
               labelbottom="on", left="off", right="off", labelleft="on",
               labelsize = 12)    
```

    /Users/hajsong/miniconda2/envs/py36/lib/python3.6/site-packages/matplotlib/cbook/deprecation.py:107: MatplotlibDeprecationWarning: Passing one of 'on', 'true', 'off', 'false' as a boolean is deprecated; use an actual boolean (True/False) instead.
      warnings.warn(message, mplDeprecation, stacklevel=1)



```python
ax.plot(Tdate[::intv], mTanom[::intv], color='black', label='global')
ax.plot(Tdate[::intv], T_nh[::intv], color='dodgerblue', label='NH')
ax.plot(Tdate[::intv], T_sh[::intv], color=np.array([189, 48, 57])/255, label = 'SH')
ax.legend()
```




    <matplotlib.legend.Legend at 0x143293da0>
