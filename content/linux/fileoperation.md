+++
title = "File Operation"
description = ""
weight = 3
+++

Once we arrive the working directory, the next thing we want to do might be manipulating files: copying, renaming, deleting and so forth. This page introduces a few things that can be useful in handling files in a Linux system.

##### ```ls [options] [files]```
The ```ls``` command lists attributes of files and directories. You can list files in the current directory:
```
$ ls
```
in a given directories:
```
$ ls dir1 dir2 dir3
```
or individually:
```
$ ls file1 file2 file3
```
The most important options are ```-a``` and ```-l```. By default, ```ls``` hides files whose names begin with a dot. The option ```-a``` displays all files including those starting with ```.(dot)```. 
The ```-l``` option produces a long listing, for example:
```
-rw-r--r--  1 hajsong  staff  3376 Sep  3 08:18 _index.md
-rw-r--r--  1 hajsong  staff  1340 Sep  3 12:53 configuration.md
-rw-r--r--  1 hajsong  staff  3301 Sep  3 13:05 fileoperation.md
-rw-r--r--  1 hajsong  staff  2707 Sep  3 12:52 filesystem.md
-rw-r--r--  1 hajsong  staff  1066 Sep  3 11:23 shell.md
```
that includes, from left to right: the file's permissions, owner, group, size, last modification date and name.
When using the ```-l``` option, the list is created in the alphabetical order of the file names. It is sometimes useful to find out the most recently modified file. In this case, you can change the order according to the modification times.
```
$ ls -ltr
```
The result looks like:
```
-rw-r--r--  1 hajsong  staff  3376 Sep  3 08:18 _index.md
-rw-r--r--  1 hajsong  staff  1066 Sep  3 11:23 shell.md
-rw-r--r--  1 hajsong  staff  2707 Sep  3 12:52 filesystem.md
-rw-r--r--  1 hajsong  staff  1340 Sep  3 12:53 configuration.md
-rw-r--r--  1 hajsong  staff  3787 Sep  3 13:08 fileoperation.md
``` 
Here, ```-t``` makes the order according to the modification time, and ```-r``` reverses the order so that the latest comes to the bottom of the list. You may already notice that you can combine options by just line them up. 


