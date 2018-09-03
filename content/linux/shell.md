+++
title = "Installation"
description = ""
weight = 1
+++

To get the most out of Linux, you should become proficient in using the shell. It might initially be more difficult than icons and menus, but once you're used to it, the shell is quite easy to use and very powerful.

#### How to run a shell

If you have Linux, running a shell is just opening *Terminal* or something similar to it. However, if you are running Windows (I think this is the most case), then you can experience Linux with the third-party program like [MobaXterm](https://mobaxterm.mobatek.net).

![](/ATM4110/images/feature-terminal.png?classes=border,shadow)

This program offers a shell environment and (I think) you can do most of the common tasks of Linux with it.

Please get this (free) and set up in your computer.

#### Quick start

This method results that files are checked out locally, but won't be visible from parent git repo. Probably you will build site locally with `hugo` command and use result from `public/` on your own.

```
$ git clone https://github.com/vjeantet/hugo-theme-docdock.git themes/docdock
```


### 3. Install DocDock from ZIP

All files from theme will be tracked inside parent repo, to update it, have to override files in theme. [{{%icon download%}} download following zip](https://github.com/vjeantet/hugo-theme-docdock/archive/master.zip) and extract inside `themes/`.

```
https://github.com/vjeantet/hugo-theme-docdock/archive/master.zip
```
Name of theme in next step will be `hugo-theme-docdock-master`, can rename as you wish.

## Configuration

[Follow instructions here]({{%relref "configuration.md"%}})
