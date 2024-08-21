---
layout: default
title: SSH config
parent: Remote Access
nav_order: 2
---
_author: Callum_

## UPDATED: Smoother SSH logins using a config file

Since the IT Leeds _crisis_, there is a new way of logging into remote machines, using 'rash', which replaces the 'remote-access' pathway. \
This can be used in place of access via the VPN and I've found it more stable and faster. \
More info here: https://it.leeds.ac.uk/it?id=kb_article_view&table=kb_knowledge&sys_kb_id=c781b24e1b978a94d5d60e51f54bcb16 \
To use this facility, you need to request access to use 'rash', via the link above. The article explains quite well the process of accessing the remote machines, here we provide an example of what your ssh/config file could look like for our use cases. 

To make the process of logging into FoE remote machines smoother you can add a config file (`~/.ssh/config`) so that SSH knows to automatically jump via `rash` etc. You can store your info and requests in this file, so it makes logging in to the remote maachines faster and easier. 

If you've not created this file, you may need to make a config file, you can do this by 
```bash
touch ~/.ssh/config
```
Then, to access this file, use
```bash
vi ~/.ssh/config
```

Below are some examples of what you can populate your config file with. \
 (**replace _username_ with your username!**):
```bash
Host foe
        HostName foe-linux-01.leeds.ac.uk
        ForwardX11Trusted yes
        ForwardAgent yes
        User username
        TCPKeepAlive no
        ProxyJump rash
        RequestTTY force
        RemoteCommand cd /path/to/your/dir/ && bash -l 

Host jester
        HostName jester.leeds.ac.uk
        ForwardX11Trusted yes
        User username
        ForwardAgent yes
        TCPKeepAlive no
        ProxyJump foe
        RequestTTY force
        RemoteCommand cd /path/to/your/dir/ && bash -l

Host rash
        Hostname rash.leeds.ac.uk
        ForwardX11Trusted yes
        User username
        ForwardAgent yes
        ForwardX11 yes
```

**Notes:**\
This setup enables you to SSH by simply using the command `ssh foe` or `ssh jester`. \
It will automatically connect you to these machines, by proxyjumping through `rash.leeds.ac.uk` 
I've found it necessary to add the commands `ForwardX11Trusted` and `ForwardAgent`, which pass your credentials to the remote machines and allow you to log in. \
I've successfully paired this approach with `ssh-keys`, allowing me to reduce the number of passwords I need to supply when logging in. I can supply an FAQ about this if people want. \
You can supply additional commands, such as `RemoteCommand` as shown, to specify your landing path when connecting into these machines.
As shown in the knowledge article, once you've logged in once, you can allow that log in instance to persist, meaning subsequent log ins don't require password and duo access (making things a lot faster). To do this, you can use the commands (more info on article webpage):
```bash
ControlPath ~/.ssh/controlmasters/%r@%h:%p
ControlMaster auto
ControlPersist 12h
```


