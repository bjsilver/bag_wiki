---
layout: default
title: Calculating the area of gridcells
parent: Python
nav_order: 2
---

## Calculating the area of gridcells
This python code can calculate the area of gridcells in a regular lat lon grid. 

This method is fast and pretty accurate, and takes into account the fact that gridcells aren't rectangular when projected.

```python
from pyproj import Geod
from shapely.geometry import LineString, Point, Polygon

# function takes lat+lon gridcell centres as well as the resolution as input
def get_latlon_areas(latcentres, loncentres, latres, lonres):
    
    """Calculate the area of gridcells on a regular grid
       using polygons

     Parameters:
     latcentres (array): The latitude centres of the gridcells
     loncentres (array): The longitude centres of the gridcells
     latres (float): The latitude resolution
     lonres (float): The longitude resolution
    
     Returns:
     xarray.DataArray: DataArray of areas in metres squared
    
    """

    geod = Geod(ellps="WGS84")
    
    areas = pd.Series(dtype=float, index=latcentres)
    for clat in latcentres:
        # get bounds from coords
        lat_south, lat_north = clat - latres/2, clat + latres/2
        # (only need to do it for one longitude)
        lon_west, lon_east = 0 - lonres/2, 0 + lonres/2

        # create polygon
        poly = Polygon(

               LineString([
                   Point(lon_east, lat_south),
                   Point(lon_east, lat_north),
                   Point(lon_west, lat_north),
                   Point(lon_west, lat_south)
                   ])

            )
        
        # this computes the area in metres ^2
        area, _ = geod.geometry_area_perimeter(poly)
        areas.loc[clat] = area
    
    # make a dataarray
    da = xr.DataArray(areas, dims={​​​​​​'lat':latcentres}​​​​​​)
    # add longitudes in
    da = da.expand_dims({​​​​​​'lon':loncentres}​​​​​​)
    
    return da
```

### Testing it
{% include ./assets/notebooks/gricell_area.html %}
