---
layout: default
title: Remote console in Spyder
parent: FAQs
nav_order: 2
---


Remote console in Spyder to reduce lag 

_Contributors: Richard Rigby, Ben Silver_

Currently most of us who use Spyder launch it from a linux machine we have ssh'ed into which can create lag (especially if you are off campus). But in Spyder there is a feature where you can run Spyder locally but the terminal can be a remote one. This means the terminal will have access to all the packages/files on the remote machine, but the application is being run locally (i.e. you have to install it on your own computer) so there will be no lag. I've found this connection to be much more stable than running Spyder in an Xwindow using ssh. 



Richard Rigby worked out how to set this up and wrote this bash script:  [remote-spyder](https://github.com/bjsilver/bag_wiki/blob/main/assets/scripts/remote-spyder)

Use it by running (where ${ USER}  is your username and [remote] is a machine e.g. viper/carnegie): 

`./remote-spyder ${​​​​​​​​​​​​​​​​​​​​​​​USER}​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​@[remote].leeds.ac.uk`

If you have setup ssh keys you should only have to enter your password once. Then from within your local Spyder: 

- Click the 'hamburger' menu in the top right corner of the console pane and choose the option 'Connect to an existing kernel'. 

- In the window that pops up, untick 'This is a remote kernel', and use the 'browse' button to open the .json file which will be named according to the machine you logged onto (e.g. eebjs@carnegie.leeds.ac.uk.json).  

- Click ok and then console should open. You can check whether the connection has been made by doing pwd in the console. It should show your linux home directory. 


A few things to note: 

- The stop button in spyder will not be able to interrupt the kernel.
- To do the you need to go to the bash terminal from which you launched the remote-spyder script, and do ctrl+c there.
- When you want to shut down the connection, ctrl+c will not work (as this is used to interrupt the kernel) you instead need to do ctrl + \ (backslash)
- You need to find a way to access your scripts that are on the remote machine on your local machine before you can open them in spyder, and a way to keep the scripts sychronised between the local and remote machines. 
