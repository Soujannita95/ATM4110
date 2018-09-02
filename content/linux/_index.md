+++
title = "Unix/Linux system"
description = ""
weight = 2
#alwaysopen = true
+++

#### Unix/Linux?
Most computing/programming in both atmospheric and oceanic sciences happens on Unix/Linux operating system, instead of Windows. What are the advantages of using Unix/Linux?
I do not have the exact answer for why, but there must be a reason for people preferring typing and executing programs instead of clicking on windows (although Linux also provides graphical user interfaces).

The computing/programming in the atmospheric sciences means you create/read/process/write atmospheric data. All these jobs involve the design of the workflow from you, and it is important to be powerful, efficient and flexible in doing those. Unix is particularly suited to working in such an environment and has many powerful (and flexible) commands that can help you.

Also, according to [Biocomputing Bootcamp](https://bioboot.github.io/web-2016/day1/),
"The real strength of learning Unix is that most of these commands can be combined in an almost unlimited fashion. So if you can learn just five Unix commands, you will be able to do a lot more than just five things. Our objective here is to learn a subset of Unix and to become a productive Unix user without knowing or using every program and feature."

I refered to [*Linux, pocket guide*](https://www.amazon.com/Linux-Pocket-Guide-Daniel-Barrett/dp/1449316697) by *Daniel J. Barrett* in introducing Linux system.

#### History (and family) of Unix
A varied operating systems, including macOS, have branched out from Unix.
![](../images/Unix_timeline.png?classes=border,shadow)
*Simplified history of Unix-like operating systems (Wikipedia).*

Linux is one of the operating system that stems from UNIX and naturally shares similar architecture and concepts. It is an open-source software!

#### Programing on Linux
"A common feature of Unix-like systems, Linux includes traditional specific-purpose programming languages targeted at scripting, text processing and system configuration and management in general. Linux distributions support shell scripts, awk, sed and make. Many programs also have an embedded programming language to support configuring or programming themselves. For example, regular expressions are supported in programs like grep and locate, the traditional Unix MTA Sendmail contains its own Turing complete scripting system, and the advanced text editor GNU Emacs is built around a general purpose Lisp interpreter." (From Wikipedia)

#### Four major parts in Linux
##### The kernel
The low-level operation system, handling files, disks, networking and other necessities we take for granted.
##### Supplied program
Thousands of programs for file manipulation, text editing, mathematics, typesetting, audio, video, computer programming, website creation, encryption... you name it.
##### The shell
A user interface for typing commands, executing them, and displaying results. There are various shells in existence: the Bourne shell, Korn shell, C shell, and others. We will focus on *bash*, the Bourne Shell, which is often the default for user accounts. However, all these shells have similar basic functions.
##### X
A graphical system that provides windows, menus, icons, mouse support, and other familiar GUI elements. More complex graphical environments are built on X; the most popular are KDE and GNOME. 
