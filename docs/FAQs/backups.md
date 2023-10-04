---
layout: default
title: Backups
parent: FAQs
nav_order: 2
---

## What is backed up?
Files on your linux home directory (e.g. `/nfs/see-fs-02_users/eebjs/<USERNAME>/`) and on the storage drives (e.g. `a68`) are backed up daily.

## NOTE!!
Backups should be able to get you out of a sticky situation where you've deleted something by mistake, but when the drives become full your files are not always backed up.
It may be worth keeping a second backup of your most precious files. I recommend you do this for your scripts, as they are tiny files and contain so much work. I use onedrive

## Home directories
A complete backup of your home directory as it was yesterday evening is here: `/backup/see-fs-02_users/<USERNAME>/`
Daily changes for the last month are here `/backup/see-fs-02_users/daily_changes/`. 

This directory contains daily directories which contain changed files.
For example, if you deleted or modified a file on the 22nd of the month, it should be in `/backup/see-fs-02_users/daily_changes/22/<USERNAME>/`.

The daily changes only record *changes* so there is not a complete backup for each day of the month here, but by combining this with the 'last night's backup' directory,
you effectively have a backup of everything for the last month

## Storage drives
The storage drive backups work in the same way as the home directories. For example, the backup of your a68 directory is at `/backup/a68/<USERNAME>/`
and the daily changes are at `/backup/a68/daily_changes/`
