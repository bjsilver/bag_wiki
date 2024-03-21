---
layout: default
title: SSH config
parent: FAQs
nav_order: 2
---


## Smoother SSH logins using a config file

To make the process of logging into FoE remote machines smoother you can add a config file (`~/.ssh/config`) so that SSH knows to automatically jump via `remote-access` etc.

For example adding the following (**replace with your username!**):
```bash
Host foe-linux-0?
  Hostname %h.leeds.ac.uk
  ProxyJump remote-access
  User earrr
ForwardAgent yes
```
so you can SSH in simply with `ssh foe-linux-02`

or
```bash
Host viper
  Hostname %h.leeds.ac.uk
  ProxyJump remote-access
  User earrr
ForwardAgent yes
```
so you can SSH in simply with `ssh viper`

_Thanks Richard R for showing me this!_
