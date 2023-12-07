---
layout: default
title: Conda tips
parent: FAQs
nav_order: 2
---

# Conda tips

### Installation
Instructions for installing conda on your system are available on https://docs.conda.io/projects/conda/en/stable/user-guide/install/

### Download packages from conda-forge
It is often better to use the `conda-forge` channel for the packages we commonly use to ensure that we install the most up-to-date versions of packages that are compatible with eachother. [More info on `conda-forge` here](https://conda-forge.org/docs/user/introduction.html)

By default, conda will prioritize downloading from the default channel, which could lead to conflicts or unresolvable environments if mixed with installs from `conda-forge`

To ensure that conda always prioritises installing from conda forge,

1. edit the `.condarc` file in your home directory to prioritise `conda-forge`

	```
	channel_priority: strict
	channels:
	  - conda-forge
	  - defaults
	```
3. set the channel priority to strict
   
	```conda config --set channel_priority strict```
