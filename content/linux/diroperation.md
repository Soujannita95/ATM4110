+++
title = "Directory operation"
description = ""
weight = 2
+++

#### Filesystem structure
Every Linux file is contained in a collection called a *directory*. 
Directories are like folders on Windows and Mac systems. Directories form a hierarchy, or *tree*: one directory may contain other directories, called *subdirectories*, which may themselves contain other files and subdirectories, and so on, into infinity.
The topmost directory is called the *root directory* and is denoted by a slash (/).

#### Path
We refer to files and directories using a "names and slashes" syntax called a *path*.
To find out the current path, try
```
$ pwd
```
and you will get your current location in the filesystem.

There are two types of path. The first one is an *absolute* path. The absolute path starts from the root directory and has all the names of directories in the upper level. The second type is a *relative* path. The relative path does not start with the root directory or contain all the names of directories in the upper levels. 

##### ```cd [directory]```
To move your location in the shell environment, you can use the ```cd``` command:
```
$ cd /one/two/three
```
This command line moves you from your working directory (or current location) to ```/one/two/three```. This example uses the absolute path to go to the new working directory. From here, you can use the relative path to go to ```/one/two``` with the following command:
```
$ cd ..
```
In the shell environment, ``` ".." ``` means the upper level. (``` "." ``` means the current level.) You can use ```".."``` as many times as you want. For example, if you want to move to ```/one``` from ```/one/two/three```, you can type: 
```
$ cd ../..
```
Please note that you can achieve the same result with the absolute path:
```
$ cd /one
```

Each user has own *home directories* where users' personal files are often found.
In general, the path of the home directory starts with ```/home```.
To find out the absolute path for your home directory, try:
```
$ echo $HOME
```

Linux offers a command that brings you to your home directory from anywhere. 
All you can do is just type ```cd``` with no arguments. 
It also provides a simple way to write the absolute path of your home directory with a special character, ```~```.
Check this out.
```
$ echo ~
```
You will get the same result as above. This special character can be quite handy. Suppose you want to move to ```Documents/Public``` in your home directory from ```/one/two/three```. Then you can just type:
```
$ cd ~/Documents/Public
``` 
If another username follows ```~```, the shell expands this string to be the user's home directory:
```
$ cd ~smith
$ pwd
/home/smith
```
##### ```mkdir [options] directory```
```mkdir``` creates one or more directories:
```
$ mkdir dirname
```
{{% panel %}}```rm -r dirname``` will delete the directory called ```dirname```.{{% /panel %}}

