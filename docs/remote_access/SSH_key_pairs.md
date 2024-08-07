---
layout: default
title: SSH Keys
parent: Remote Access
nav_order: 2
---


## Using ssh key pairs to avoid having to use password/Duo 

On a terminal (MobaXterm etc.) use ssh-keygen to generate an ssh key pair on your local machine. It will ask for a location to save the keys. Hit enter to accept the default. Then you can set a password (recommended) or just press enter to not have a local password. 

Use `ssh-copy-id` to push the ssh key onto the remote machine you want easy access to e.g. 
`ssh-copy-id <username>@remote-access.leeds.ac.uk`. After entering your password, the key will be copied over to the remote machine and can usually be found in `~/.ssh/ `

After this you should be able to login without using a password. Note that if you are logging into multiple machines (e.g. `remote-access` then `foe-linux` then `viper`), you will need to repeat this process so the keys get copied to each of the machines.
