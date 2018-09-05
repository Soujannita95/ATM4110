+++
title = "File Operation"
date= 2018-09-04T07:45:45+09:00
description = ""
creatordisplayname = "Hajoon Song"
creatoremail = "hajsong@yonsei.ac.kr"
lastmodifierdisplayname = "Hajoon Song"
lastmodifieremail = "hajsong@yonsei.ac.kr"
tags = ["ls","cp","rm"]
weight = 3
+++

Once we arrive the working directory, the next thing we want to do might be manipulating files: copying, renaming, deleting and so forth. This page introduces a few things that can be useful in handling files in a Linux system.

{{% alert theme="info" %}}If you need a short guide for the command, try with ```--help``` option.{{% /alert %}}
{{% notice note %}}
The content on this page mostly comes from *Linux pocket guide* by Daniel J. Barrett.{{% /notice %}}

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

##### ```cp [options] [files] (file/dir)```
The ```cp``` command copies a file:
```
$ cp file file2
```
Using the ```-R``` option, you can also recursively copy directories.
```
$ cp -R dir1 dir2
```
will create ```dir2``` which is the same as ```dir1```.

**Useful options**

+ ```-f```: Force the copy. If a destination file exists, overwrite it unconditionally.
+ ```-i```: Interactive mode. Ask before overwriting destination files.

##### ```ln [options] source target```
A *link* is a reference to another file, created by the ```ln``` command. There are two kinds of links. A *symbolic link* refers to another file by its path, much like a Windows "shortcut" or a Mac "alias".
```
$ ln -s myfile softlink
```
If you delete the original file, the now-dangling link will be invalid, pointing to a nonexistent file path. A *hard link*, on the other hand, is simply a second name for a physical file on disk. Deleting the original file does not invalidate the link.

If you leave the ```softlink``` blank, then you get the link with the same name.

```
$ ln myfile hardlink
```
Symbolic link can cross disk partitions, since they are just references to file paths.
Hard links cannot. Symbolic links can also point to directories, whereas hard links cannot.

It is easy to find out where a symbolic link points with either of these command.
```
$ readlink softlink
```
or
```
$ ls -l softlink
```

**useful options**

+ ```-s```: Make a symbolic link. The default is a hard link.
+ ```-i```: Interactive mode. Ask before overwriting destination files.
+ ```-f```: Force the link. If a destination file exists, overwrite it unconditionally.

##### ```mv [options] source target```
The ```mv``` command can rename a file:
```
$ mv file1 file2
```
or move files and directories into a destination directory.
```
$ mv file1 destination_directory
```
**useful options**

+ ```-i```: Interactive mode. Ask before overwriting destination files.
+ ```-f```: Force the move. If a destination file exists, overwrite it unconditionally.

##### ```rm [options] files/directories```
The ```rm``` command can delete files:
```
$ rm file1 file2 file3
```
or recursively delete directories:
```
rm -r dir1 dir2
```
**useful options**

+ ```-i```: Interactive mode. Ask before deleting each file.
+ ```-f```: Force the deletion, ignoring any errors or warnings.
+ ```-r```: recursively remove a directory and its contents. **USE WITH CAUTION**, especially if combined with the ```-f``` option.

{{% alert theme="danger" %}}**Beware!** Once you delete the files or directories with ```rm```, it is impossible or very difficult to recover them.{{% /alert %}}
