---
layout: default
title: Mounting OneDrive on a Linux system
parent: Remote Access
nav_order: 2
---


## Mounting OneDrive on a Linux system
_Contributors: Ben Silver_

Your University of Leeds OneDrive can be 'mounted' in Linux, so the files on
it can be accessed (almost) as if it was any other directory.

I find this useful for synchronising scripts and figures across machines. 
For example, if you are working on a Linux machine, and you save a figure 
to OneDrive, it will be available (almost) instantly to copy into powerpoint
if you're also working on a Windows machine.

Also useful for if you're running scripts on a remote machine, you can edit
the script locally, your changes will be automatically synchronised with 
the remote machine.

### Do I need to 'mount' OneDrive?
Please note that mounting OneDrive in this way is only necessary if you are on a Linux
machine (e.g. `foe-linux`). If you are in MobaXterm or on WSL, you can just 
'soft link' OneDrive so it can be easily accessed from your Linux home directory.

OneDrive can usually be found at `C:\Users\[USERNAME]\OneDrive - University of Leeds`
or similar

### 1. RClone

The first step is to use RClone to setup OneDrive. This step makes it accessible
on Linux using the `rclone` command but does not mount it. For this step, [use the guide 
IT have written](https://it.leeds.ac.uk/it?id=kb_article_view&table=kb_knowledge&sys_kb_id=5cdadc241bb1c950ba670ed0f54bcb04) 
for how to set it up on ARC.

### 2. Mount automatically
{: .important-title }
> Update!
> Richard Rigby recommends we don't mount OneDrive in our home directory since it's a networked drive. We can mount it on `/dev/shm` instead

To mount it automatically each time you login on a Linux machine, add the
following code to your `~/.bashrc` file:

```bash
# Automatically mount OneDrive with rclone
MOUNT_POINT="/dev/shm/OneDrive-$USER"
RCLONE_REMOTE="onedrive" # the name that you gave onedrive when setting up with rclone
RCLONE_COMMAND="rclone mount $RCLONE_REMOTE: $MOUNT_POINT --vfs-cache-mode writes --daemon"

# Function to check and mount OneDrive
mount_onedrive() {
  if mountpoint -q "$MOUNT_POINT"; then
    :
  else
    echo "Mounting OneDrive..."
    fusermount -uz "$MOUNT_POINT" 2>/dev/null  # Attempt to unmount if needed
    $RCLONE_COMMAND
  fi
}

# Call the function to mount OneDrive
mount_onedrive
```

{: .warning}
> You will have to create the `/dev/shm/OneDrive-$USER` on each of the remote machines you plan to use (e.g. `foe-linux-01`, `foe-linux-02`, `viper` etc.)

Finally, create a soft link to `/dev/shm/OneDrive-$USER` in your home directory so you can easily access OneDrive from there, e.g.
```bash
ln -s /dev/shm/OneDrive-$USER ~/onedrive
```
This step only needs to be done once (you don't have to do it for each remote machine)

Once you login and logout, this should work! and you should find `onedrive`
in your home directory
