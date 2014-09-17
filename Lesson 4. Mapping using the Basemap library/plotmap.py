# Script to plot data from a NetCDF file onto a Basemap

from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# Change the strings according to your dataset
nc = Dataset('../data/pottmp.2014.1time.nc')
pottmp = nc.variables['pottmp']
lons = nc.variables['lon'][:]
lats = nc.variables['lat'][:]
# Extracts a 2d field
data = pottmp[0,0] 

# Replace this with whatever map you want
m = Basemap(projection='ortho', lon_0=-50, lat_0=40, resolution='l')

# Convert the lons and lats to map coordinates
X,Y = np.meshgrid(lons, lats)
x,y = m(X,Y)

# Create the plot
pc = m.contourf(x, y, data, 30, cmap=plt.get_cmap('YlGnBu_r'))
m.bluemarble()
m.drawmapboundary()
m.drawcoastlines()
plt.title('Orthographic projection of ' + pottmp.long_name + ' (' + pottmp.units + ')')
plt.colorbar(pc, orientation='horizontal')
plt.show()