# Example of Empirical Orthogonal Function analysis
# based on the code by John Wilkin

# Load a data set of monthly sea surface temperatures for the Pacific Ocean
# from the "Reynolds SST" product from the Climate Analysis Center.
import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

makeplot = 0

# Read the sea surface temperature data
data1 = sio.loadmat('cac.mat', squeeze_me=True, struct_as_record=False)
cac = data1['cac']

lat = cac.lat
lon = cac.lon
sst = cac.sst
land = cac.land
year = cac.year

nlats, nlons, ntimes = sst.shape

# This data include both land and sea temperatures. 
# Since we don't expect temperature variability to necessarily be 
# strongly correlated to the adjacent sea temperature, we should 
# exclude land values from the data set. This can be done by setting 
# all land values to zero.
mask = np.ones([nlats,nlons]).flatten()
mask[land-1] = 0
mask = mask.reshape(nlons, nlats).T
mask = np.tile(mask, [ntimes, 1, 1])
mask = mask.transpose(1, 2, 0)
sst = sst*mask

if makeplot == 1:
    # plot the data
    plt.figure(1, figsize=(10,4))
    for i in range(ntimes):
        plt.clf()
        ax = plt.axes(projection=ccrs.Geostationary(central_longitude=lon.mean(), satellite_height=35785831))
        ax.pcolormesh(lon, lat, sst[:, :, i], vmin=10, vmax=30, cmap='rainbow', transform=ccrs.PlateCarree())
        ax.coastlines(resolution='110m')
        mon = int(np.remainder(year[i],1)*12 + 0.5)
        plt.title('SST, year='+str(int(year[i]))+', mon='+str(mon))
        plt.pause(0.1)

    # Plot a longitude-time Hovmuller diagram
    iy = 7
    f, ax = plt.subplots(1, 1, figsize=(10,6))
    X, Y = np.meshgrid(lon, year)
    ax.pcolormesh(X, Y, sst[iy, :, :].T, vmin=20, vmax=30, cmap='rainbow')
    ax.set_title('SST along the latitude = '+str(lat[iy])+' deg')
    
# Construct Data matrix
D = sst.reshape([nlons*nlats, ntimes])

# if you want to remove land points
rmland = False 
if rmland is True:
    isea = np.nonzero(D[0,:]!=0)[0]
    D = D[:,isea]

# if you want to remove the seasonal variability in the data
rmseason = True
if rmseason is True :
    print('Removing seasonal variability')
    Eann = np.block([[np.ones(ntimes)], [np.cos(2*np.pi*year)], [np.sin(2*np.pi*year)]]).T
    Dann = np.zeros(D.shape)
    for m in range(D.shape[0]):
        d = D[m,:]
        coeff = np.linalg.inv(Eann.T @ Eann) @ Eann.T @ d
        dfit = Eann @ coeff
        Dann[m, :] = dfit
    D = D - Dann
    sstmean = Dann.reshape(nlats, nlons, ntimes)
else:
    print('Removing a long term mean')
    sstmean = np.tile(np.mean(D, axis=1), [ntimes, 1]).T
    D = D - sstmean

sstanom = D.reshape(nlats, nlons, ntimes)

# Solve the eigenvalue/eigenvector decomposition problem
gam, E = np.linalg.eigh(D @ D.T)
gam = np.flip(gam)
E = np.flip(E, axis=1)
percent_var = 100*gam/np.sum(gam)

# time series of each mode
A = E.T @ D

# Evaluate the result!
# plot EOFs pattern
f = plt.figure(figsize=(10, 8))
for i in [1, 2]:
    ax = plt.subplot(2, 1, i, projection=ccrs.Geostationary(central_longitude=lon.mean(), satellite_height=35785831))
    ax.coastlines(resolution='110m')
    c = ax.contourf(lon, lat, E[:,i-1].reshape(nlats, nlons), np.arange(-.15, .16, .01), cmap='RdBu_r', extend='both',
                    transform=ccrs.PlateCarree())
    plt.colorbar(c)

# plot EOF amplitude time series
f, ax = plt.subplots(2, 1, figsize=(10, 8))
xmin, xmax = 1980, 2005
ymin, ymax = -30, 30
plt.style.use('fivethirtyeight')
for i in range(2):
    ax[i].plot(year, A[i,:], color='black', linewidth=2, label='SST data')
    ax[i].set_xlim([xmin, xmax])
    ax[i].set_ylim([ymin, ymax])
    ax[i].set_title('The amplitude time series of mode '+str(i+1))
ax[0].set_xticklabels([])

data2 = sio.loadmat('soi.mat', squeeze_me=True, struct_as_record=False)
soi = data2['soi']
soit = data2['soit']
ax[0].plot(soit/365.25, soi*np.std(A[0,:]), 'r', linewidth=1, label='SOI')
ax[0].legend()

# Reconstruct the data using modes with the kth biggest variance.
it = 10
mon = int(np.remainder(year[i],1)*12 + 0.5)
K = 30
f = plt.figure(figsize=(10, 8))
ax = plt.subplot(2, 1, 1, projection=ccrs.Geostationary(central_longitude=lon.mean(), satellite_height=35785831))
ax.coastlines(resolution='110m')
c = ax.contourf(lon, lat, sst[:,:,it]*mask[:,:,it], np.arange(10, 31, 1), cmap='rainbow', extend='both',
                transform=ccrs.PlateCarree())
ax.set_title('SST, year='+str(int(year[i]))+', mon='+str(mon))
plt.colorbar(c)

K = 3
sstdata = np.zeros((nlats, nlons, ntimes))
for i in range(K):
    sst0 = E[:,:i] @ A[:i, :]
    sst0 = sst0.reshape(nlats, nlons, ntimes)
    sstdata += sst0
sstdata += sstmean
ax = plt.subplot(2, 1, 2, projection=ccrs.Geostationary(central_longitude=lon.mean(), satellite_height=35785831))
ax.coastlines(resolution='110m')
c = ax.contourf(lon, lat, sstdata[:,:,it]*mask[:,:,it], np.arange(10, 31, 1), cmap='rainbow', extend='both',
                transform=ccrs.PlateCarree())
ax.set_title('Estimated SST using '+str(K)+' modes')
plt.colorbar(c)
