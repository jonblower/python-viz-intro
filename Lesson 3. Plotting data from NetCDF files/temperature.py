# Script to create a latitude-longitude plot of potential temperature
# from a NetCDF data file

import netCDF4
import matplotlib.pyplot as plt

# Open the data file
nc = netCDF4.Dataset('../data/pottmp.2014.1time.nc')
# Get a handle to the variable (this doesn't actually read any data yet)
pottmp = nc.variables['pottmp']
# Read a 2D slice of data at the first vertical level and time value
data = pottmp[0,0]

# Get handles to the longitude and latitude variables
lon = nc.variables['lon']
lat = nc.variables['lat']
# Read the values of lon and lat
# ("[:]" means "read the whole array")
lonvals = lon[:]
latvals = lat[:]

# Now plot the data
plt.contourf(lonvals, latvals, data, 20, cmap=plt.get_cmap('YlGnBu_r'))
plt.title (pottmp.long_name + ' (' + pottmp.units + ')')
plt.xlabel(lon.long_name    + ' (' + lon.units    + ')')
plt.ylabel(lat.long_name    + ' (' + lat.units    + ')')
plt.colorbar()
plt.show()