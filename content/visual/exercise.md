+++
title= "Exercise"
date= 2018-11-08T11:50:53+09:00
description = ""
creatordisplayname = "Hajoon Song"
creatoremail = "hajsong@yonsei.ac.kr"
lastmodifierdisplayname = "Hajoon Song"
lastmodifieremail = "hajsong@yonsei.ac.kr"
tags = ["cartopy","Basemap"]
weight = 100
#pre ="<i class='fa fa-edit' ></i> "
+++

We learned how to make 2D plots, and touched a little bit of ```cartopy``` and ```Basemap```.
(I prepared example jupyter notebooks for [```cartopy```](https://github.com/hajsong/ATM4110/blob/master/static/images/plot_map_cartopy.ipynb) and [```Basemap```](https://github.com/hajsong/ATM4110/blob/master/static/images/plot_map_basemap.ipynb).)

Based on these lessons, we will finalize python lectures with [this exercise](https://github.com/hajsong/ATM4110/blob/master/static/images/plot_exercise.ipynb)!



# Plotting exercise

We will practice what we learned about plotting data on a 2D space.  
First, let's get the data.


```python
import numpy as np
import numpy.ma as ma
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import cartopy.crs as ccrs
%matplotlib inline
```


```python
data = np.load('exercisedata.npz')
LON = data['LON']
LAT = data['LAT']      
u10 = data['u10']      # zonal velocity at 10m (m/s)
v10 = data['v10']      # meridional velocity at 10m (m/s)
T2m = data['T2']       # temperature at 2m (K)
LH = data['LH']        # latent heat (W/m2)
Psfc = data['Psfc']    # surface pressure (Pa)
w = data['w']          # vertical velocity (m/s)
date = data['date']
mask = data['mask']    # land mask
mask = ma.masked_where(mask==1, mask)
mask += 1
```

### 1. Plot surface pressure
Using the ```imshow``` function

### 2. Plot temperature at 2m
Using the ```pcolormesh``` function

### 3. Plot latent heat
Using the ```contour``` function

### 4. Plot wind and its speed

#### 4-1 Using arrows with colors

#### 4-2 Using arrows with the same size on the background of wind speed

### 5. Find the hurricane track (using either cartopy or Basemap)


The solution can be found [here](https://github.com/hajsong/ATM4110/blob/master/static/images/plot_exercise_answer.ipynb)
