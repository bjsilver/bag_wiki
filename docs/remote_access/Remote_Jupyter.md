---
layout: default
title: Remote Jupyter
parent: Remote Access
nav_order: 2
---


## Starting a remote jupyter session the easy way

Here 'the easy way' refers to using a [script](https://github.com/bjsilver/bag_wiki/blob/main/assets/scripts/remote-jupyter) written by Richard Rigby (thanks!). [This script](https://github.com/bjsilver/bag_wiki/blob/main/assets/scripts/remote-jupyter) will work when you have your `~/.ssh/config` file set up as suggested in the [SSH config](https://bjsilver.github.io/bag_wiki/docs/FAQs/SSH_configs.html) guide

### Configuration
* You will need to change the `PYTHON_LOAD` variable so your desired conda environment is loaded.
* The 'jupyter notebook' can be replaced with 'jupyter lab' if preferred.

### Usage
Place the script in your home directory of your local machine. Connect to a remote machine and start a jupyter notebook session using:
```bash
. remote-jupyter viper # or your machine of choice
```

This will provide you with a link that you can copy and paste into your browser

