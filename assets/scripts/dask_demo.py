#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 18:12:32 2021

@author: eebjs
"""

import xarray as xr
import pandas as pd
import numpy as np
from dask.diagnostics import ProgressBar
import time

# I got ChatGPT to write me this!
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__}",
              f"took {round(end_time - start_time)}",
              "seconds to execute.")
        return result
    return wrapper


ds = xr.open_dataset('/nfs/a68/eebjs/hardknott/drought/vpd_variables.grib',
                     engine='cfgrib')


#%% calculate vpd with chunking and dask

@timer
def calculate_vpd_with_chunking(ds):

    ds = ds.chunk({'time':1})
    
    # first calculate saturated vapour pressure
    fw = 1 + 7e-4 + 3.46e-6 * ds['sp']
    svp = 6.112 * fw * np.exp( (17.67 * ds['t2m']) / (ds['t2m'] + 243.5) )
    
    # then calculate actual vapour pressure
    avp = 6.112 * fw * np.exp( (17.67 * ds['d2m']) / (ds['d2m'] + 243.5) )
    
    # then vapour pressure deficit is:
    vpd = svp - avp
    
    with ProgressBar():
        vpd = vpd.compute(num_workers=30, scheduler='threads')
        
    return vpd
        
vpd = calculate_vpd_with_chunking(ds)
# took 20 seconds in test



#%% calculate vpd without dask

@timer
def calculate_vpd_without_chunking(ds):

    # first calculate saturated vapour pressure
    fw = 1 + 7e-4 + 3.46e-6 * ds['sp']
    svp = 6.112 * fw * np.exp( (17.67 * ds['t2m']) / (ds['t2m'] + 243.5) )
    
    # then calculate actual vapour pressure
    avp = 6.112 * fw * np.exp( (17.67 * ds['d2m']) / (ds['d2m'] + 243.5) )
    
    # then vapour pressure deficit is:
    vpd = svp - avp
    
    return vpd
        
vpd = calculate_vpd_without_chunking(ds)
# took 384 seconds in test

# so 19.2x speedup


#%% say we want to calculate the mean across time and plot
# we could either chunk this the wrong or the right way
# the wrong way is to chunk across time, as this sends the data to seperate
# cores

@timer
def calculate_spatial_mean_vpd_without_chunking(vpd):
    mean_vpd = vpd.mean(dim='time')
    return mean_vpd

mean_vpd = calculate_spatial_mean_vpd_without_chunking(ds)
# took 80 seconds in test

mean_vpd.plot.imshow()

#%% i.e. the WRONG chunking!
@timer
def calculate_spatial_mean_vpd_chunking_across_time(vpd):
    
    # chunk across time
    vpd = vpd.chunk({'time':1})
    
    # compute the mean
    with ProgressBar():
        mean_vpd = vpd.mean('time').compute(num_workers=30, scheduler='threads')
    return mean_vpd

mean_vpd = calculate_spatial_mean_vpd_chunking_across_time(vpd)
# took 27 seconds in test


#%% i.e. the RIGHT chunking!
@timer
def calculate_spatial_mean_vpd_chunking_across_latlon(vpd):
    
    # chunk across lat and lon
    vpd = vpd.chunk({'longitude':400, 'latitude':500})
    
    # compute the mean
    with ProgressBar():
        mean_vpd = vpd.mean('time').compute(num_workers=30, scheduler='threads')
    return mean_vpd

mean_vpd = calculate_spatial_mean_vpd_chunking_across_latlon(vpd)
# took 22 seconds in test
# only marginally shorter due to the overhead of chunking the array

# NOTE: nothing specific about space/time here. just depends what dimension
# you are doing the calculation across


#%% when should we chunk across time?
# when calculating the temporal mean

@timer
def calculate_temporal_mean_vpd_without_chunking(vpd):
    mean_vpd = vpd.mean(dim=['latitude', 'longitude'])
    return mean_vpd

mean_vpd = calculate_temporal_mean_vpd_without_chunking(vpd)
# took 24 seconds in test

#%% the WRONG chunking (i.e. space)
@timer
def calculate_temporal_mean_vpd_across_latlon(vpd):
    
    # chunk across lat and lon
    vpd = vpd.chunk({'longitude':400, 'latitude':500})
    
    # compute the mean
    with ProgressBar():
        mean_vpd = vpd.mean(dim=['latitude', 'longitude']).compute(num_workers=30, scheduler='threads')
    return mean_vpd

mean_vpd = calculate_temporal_mean_vpd_across_latlon(vpd)
# took 21 seconds in test


#%% the RIGHT chunking (i.e. time)
@timer
def calculate_temporal_mean_vpd_across_time(vpd):
    
    # chunk across time
    vpd = vpd.chunk({'time':1})
    
    # compute the mean
    with ProgressBar():
        mean_vpd = vpd.mean(dim=['latitude', 'longitude']).compute(num_workers=30, scheduler='threads')
    return mean_vpd

mean_vpd = calculate_temporal_mean_vpd_across_time(vpd)
# took 19 seconds in test


#%% choosing chunk sizes

# depends on shape of array
# usually worth a bit of experimenting to find a good size

da = vpd[:20]

def calculate_mean(da, chunksize):
    
    # time the chunking overhead
    start = time.time()
    da = da.chunk({'latitude':chunksize, 
                   'longitude':chunksize})
    end = time.time()
    chunking_time = end-start
    
    # time the actual calculation
    start = time.time()
    _ = da.mean('time').compute(num_workers=30, scheduler='threads')
    end = time.time()
    calculation_time = end-start
    
    return pd.Series(
        [chunking_time, calculation_time],
        index=['chunking time', 'calculation time']
                     )

calculate_mean(da, chunksize=500)

results = pd.DataFrame()
for chunksize in [10,20,40,80,160,320,640,1280]:
    print(chunksize)
    results[chunksize] = calculate_mean(da, chunksize=chunksize)
    
results.T.plot.bar(grid=True, xlabel='chunksize', ylabel='time (seconds)',
                   stacked=True)

# trivial example but could be important with larger operations