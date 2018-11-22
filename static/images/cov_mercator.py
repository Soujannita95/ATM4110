import numpy as np
import numpy.ma as ma
import scipy.io as sio

# fraction of data to retain for mapping
frac = 0.1

# random error to add to observation
e = 0.4

# choose the level
k = 9

# load the data
data = sio.loadmat('mercator_temperature')
x = data['x']
y = data['y']
data = data['temp'][k, :, :]
xx, yy = np.meshgrid(x, y)

# consider valid values and their locations
ival = np.isfinite(data)
xx = xx[ival]
yy = yy[ival]
data = data[ival]

# Remove data for the optimal interpolation problem
N = len(data)
ikeep = np.round(N*np.random.rand(int(frac*N)))
ikeep = ikeep.astype('int')
xx = xx[ikeep]
yy = yy[ikeep]
data = data[ikeep]

# Assuming isotropic homogeneous variability, 
# make an estimate of the data covariance function
# by computing binned-lagged covariance for all possible
# data-data pairs

# Get distances separating every pair of stations
# using approximate spherical geometry

radius = 6370800     # meters
lonm = np.mean(x)    # define the reference point
latm = np.mean(y)    # define the reference point
ykm = radius * (yy-latm) * np.pi/180 / 1000
xkm = radius * ((xx-lonm)* np.pi/180) * np.cos(np.pi/180*yy) / 1000

# Build matrices that repeat colums of x and rows of y.
# Then X-X.T and Y-Y.T will be all posible distance combinations
# between pairs of points
X = np.tile(xkm, [len(ykm), 1])
Y = np.tile(ykm, [len(xkm), 1])
Rdd = np.sqrt((X-X.T)**2 + (Y-Y.T)**2)

# Maybe set the lower triangle to zeros

# Add some random noise to data
data = data * e*np.random.randn(len(data))

# Removing the mean before calculating covariance
d = np.zeros((len(data), 1))
d[:, 0] = data - np.mean(data)

b = 20

# covariance data-data
#Cdd = d @ d.T
Cdd = (1+Rdd/b)*np.exp(-Rdd/(b)) + np.diag(e*np.random.randn(len(data)));

# regular grid of coordinates to map data to
grdres = 1/3
xtmp = np.arange(x.min(), x.max()+grdres, grdres)
ytmp = np.arange(y.min(), y.max()+grdres, grdres)
[xg, yg] = np.meshgrid(xtmp, ytmp)
xg = xg.flatten()
yg = yg.flatten()

# Convert these to x,y in kilometers
ygkm = radius*(yg-latm)*np.pi/180/1000;
xgkm = radius*(np.pi/180*(xg-lonm))*np.cos(np.pi/180*yg)/1000;

# distances between any pair of points
Xg = np.tile(xgkm, [len(ykm), 1]);
Xd = np.tile(xkm,[len(ygkm), 1]);
Yg = np.tile(ygkm,[len(xkm), 1]);
Yd = np.tile(ykm,[len(ygkm), 1]);
Rmd = np.sqrt((Xg.T-Xd)**2+(Yg.T-Yd)**2)

Cmd = (1+Rmd/b)*np.exp(-Rmd/b);

D = data.mean() + Cmd @ np.linalg.inv(Cdd) @ (data-data.mean())

