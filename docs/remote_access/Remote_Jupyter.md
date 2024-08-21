---
layout: default
title: Remote Jupyter
parent: remote_access
nav_order: 2
---


## Starting a remote jupyter session the easy way

Here 'the easy way' refers to using a [script](https://github.com/bjsilver/bag_wiki/blob/main/assets/scripts/remote-jupyter) written by Richard Rigby (thanks!). [This script](https://github.com/bjsilver/bag_wiki/blob/main/assets/scripts/remote-jupyter) will work when you have your `~/.ssh/config` file set up as suggested in the [SSH config](https://bjsilver.github.io/bag_wiki/docs/FAQs/SSH_configs.html) guide

### Configuration
* The 'jupyter notebook' can be replaced with 'jupyter lab' if preferred.

### Usage
1. Place the script in your home directory of your local machine. 
2. Ensure the script is executable with the command: `chmod +x remote-jupyter`
3. Connect to a remote machine and start a jupyter notebook session using:
```bash
. remote-jupyter viper myenv
# replace 'viper' with machine of your choice
# replace 'myenv' with your desired conda env
```

This will provide you with a link that you can copy and paste into your browser

