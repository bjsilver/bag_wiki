---
layout: default
title: Conda and JupyterLab setup
parent: FAQs
nav_order: 2
---

**Conda and Jupyter Lab Setup**

_Contributor: Ailish Graham_

connect to local cluster   

`ssh -Y username@remote-access.leeds.ac.uk   `

activate environment   

`conda activate my_env   `

need to do this to be able to access your environment as a kernel in jupyterlab, your environment should still be activated – this will only work if jupyterlab installed   

`python –m ipykernel install --user --name my_env --display-name “my_env”   `

do this once only (first time you set up jupyter) to set jupyter password (not same as uni password)   

`jupyter-notebook --generate-config    `

jupyter notebook password (NOT SAME as uni password)   

now create the jupyter lab session from a LOCAL machine (i.e. your own laptop command line) using the following command     

Things to note: #use a different machine if not working (e.g. foe-linux-02, lytham etc instead of foe-linux-03) # the sequence of 5 digit numbers can be anything in the range of (approx) 1100 -> 65000 (in this case 13029/13030) but pick something that no one else is likely to be using (i.e. not 12345)    

`ssh -L 13029:localhost:13029 -L 13030:localhost:13030 foe-linux-03.leeds.ac.uk 'conda activate my_env; cd /nfs/; jupyter lab --no-browser --port=13029'  `   

n.b may need username too:   

`ssh -L 13029:localhost:13029 -L 13030:localhost:13030 username@foe-linux-03.leeds.ac.uk 'conda activate my_env; cd /nfs/; jupyter lab --no-browser --port=13029’   `  

paste resulting html into browser on your laptop and enter password you set up   

`http://localhost:13029/lab   `

Note you will need the ssh –L command each time you want to connect (ssh -L 13029:localhost:13029 -L 13030:localhost:13030 foe-linux-03.leeds.ac.uk 'conda activate my_env; cd /nfs/; jupyter lab --no-browser --port=13029’)   

or you can use the below examples to generate shortcuts.     

Here are some examples that you can adapt and add to ~/.bashrc file (or similar [bash_profile on Mac] for shortcut access from your laptop – here the shortcut is in bold and command that will be executed is after the ‘=’   

`alias open_jupyterlab_foelinux01="ssh -L 25122:localhost:25122 -L 25123:localhost:25123 foe-linux-01.leeds.ac.uk 'conda activate python3; cd /nfs/; jupyter lab --no-browser --port=25122'" `
   
`alias open_jupyterlab_foelinux02="ssh -L 25122:localhost:25122 -L 25123:localhost:25123 foe-linux-02.leeds.ac.uk 'conda activate python3; cd /nfs/; jupyter lab --no-browser --port=25122'"`   
 
`alias open_jupyterlab_foelinux03="ssh -L 25122:localhost:25122 -L 25123:localhost:25123 foe-linux-03.leeds.ac.uk 'conda activate python3; cd /nfs/; jupyter lab --no-browser --port=25122'"   `
 
`alias open_jupyterlab_foelinux04="ssh -L 25122:localhost:25122 -L 25123:localhost:25123 foe-linux-04.leeds.ac.uk 'conda activate python3; cd /nfs/; jupyter lab --no-browser --port=25122'"   `
 
`alias open_jupyter_lytham="ssh -L 25122:localhost:25122 -L 25123:localhost:25123 lytham.leeds.ac.uk 'cd /nfs/; conda activate python3; jupyter lab --no-browser --port=25122'"   `
