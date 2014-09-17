This file contains some notes on the source of the data used in this course and how it was prepared.

barotropic.nc - Barotropic vorticity model, kindly provided by Phil Browne. The original file contained 241 timesteps, but we extracted just the first five, using the NetCDF operators command "ncks -d Timestep,0,4 ptcl0000.nc barotropic.nc".

sst.mean.new.nc - Downloaded from NOAA's Earth System Research Laboratory (http://www.esrl.noaa.gov/psd/repository/entry/show/?entryid=e570c8f9-ec09-4e89-93b4-babd5651e7a9). Original file contained 242 timesteps, we extracted the first 100 to reduce the file size.