---
layout: default
title: Fast conda package installs with mamba
parent: FAQs
nav_order: 2
---

# Fast conda package installs with mamba

Using mamba as an alternative to conda can resolve tricky environments that are a nightmare to maintain with conda and can be extrmely slow to install.

{: .note }
Don't be afraid to delete conda and start from scratch!
This often massively improves the speed of installs as it gets rid of older versions of packages that are unused and creating conflicts.

Mamba is a 'drop-in' replacement for conda, so after installing it, you just swap `conda` for `mamba` e.g.
```bash
mamba install -c conda-forge cartopy xesmf dask netcdf4 rioxarray regionmask
# instead of:
conda install -c conda-forge cartopy xesmf dask netcdf4 rioxarray regionmask
```

## Installing mamba
This works best in a clean environment. Create a new conda environment and install mamba using conda
```bash
conda install -c conda-forge mamba
```
