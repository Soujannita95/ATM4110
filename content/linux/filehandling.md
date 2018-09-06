+++
title= "File Handling"
date= 2018-09-05T16:06:36+09:00
description = ""
creatordisplayname = "Hajoon Song"
creatoremail = "hajsong@yonsei.ac.kr"
lastmodifierdisplayname = "Hajoon Song"
lastmodifieremail = "hajsong@yonsei.ac.kr"
tags = ["cat","grep"]
weight = 4
#pre ="<i class='fa fa-edit' ></i> "
#alwaysopen = true
+++

#### 1. File viewing
In Linux, you are going to handle files with lots of different types, and want to see what's in there. On this page, we will explore how to view the file contents if they are in text in the Linux system.

##### ```cat [options] [files]```
The simplest viewer is ```cat```, which just copies its files to standard output, concatenating them.
```
$ cat filename
```
This command dump all the contents on the screen, so large files will likely scroll off screen. If this is the case, you may consider using ```less``` command.

**useful options**

+ ```-n```: Prepend line numbers to every line

##### ```less [options] [files]```
Use ```less``` to view text one page at a time (or one window or screenful at a time). It's great for text files.

While running ```less```, type ```h``` for a help message, but here are a few keystroke being used often.

|  Keystroke      |        Meaning              |
|-----------------|-----------------------------|
| h, H            | View a help page.           |
| spacebar, f     | Move forward one screenful. |
| Enter           | Move forward one line.      |
| b               | Move backward one screenful |
| /               | Enter search model. ```n``` goes to the next match, while ```N``` goes to the previous match.  |
| q               | quite ```less```.           |

**useful options**

+ ```N```: Prepend line numbers to the output.

##### Other useful commands
```head``` and ```tail``` are also useful in viewing files. To find out how to use them, you can refer to the manual after calling it.
```
$ man head
or
$ man tail
```
The manual of these command will be printed on the screen using ```less``` command.
That means that you can move around between pages using the keystrokes in the table above.

#### 2. File Creation and Editing
Creating files is easy and can be done in many different ways in Linux.
Instead of printing out the output on the screen, you can create a file containing the output by redirecting it.
```
$ echo save text in the file > output
$ ls -l > listdir
```
You can also quickly create an empty file using ```touch``` command,
```
$ touch newfile
```

If you want to create and edit a file, you can try text editors.
Two major text editors are ```emacs``` and ```vim``` in Linux, and new files can be created with the following commands.
```
$ emacs newfile
or
$ vim newfile
```

There is a steep learning curve for these editors, but once you get familiar with them, you can do so many things very efficiently. Throughout the course, you need to create many text files to analyze the atmospheric data, and these text editors may boost your productivity.

I use ```vim``` daily basis. So, I will introduce it briefly here with a few examples (There are tons of material about these text editors online. Of course, you do not have to use them.)

##### vim [options] [files]
{{% alert theme="info" %}}
You can open up the tutorial of vim withe command below.
```
$ vimtutor
```
To exit from ```vimtutor```, do ```:q```.
{{% /alert %}}

```vim``` operates in two modes, *insert* and *normal*. Insert mode is for entering text in the usual manner, while normal mode is for running commands like "delete a line" or copy/paste.

Here are basic keystrokes in normal mode.

|  Keystroke                |        Meaning                         |
|---------------------------|----------------------------------------|
| ```$ vim```               | run editor in current terminal.        |
| ```i```                   | enter insert mode.                     |
| ```esc```                 | exit insert mode back to normal mode   |
| :q                        | quit vim when there is no modification |
| :q!                       | quit vim without saving modification   |
| :wq                       | quit vim by overwriting the file with modification     |
| :w                        | save modification (overwrite)          |
| :w ```filename```         | save as ```filename```                 |
| ```u```                   | undo                                   |
| ^R                        | redo                                   |
| ```l``` or right arrow    | move forward                           |
| ```h``` or left arrow     | move backward                          |
| ```k``` or up arrow       | move up                                |
| ```j``` or down arrow     | move down                              |
| ```w```                   | move to next word                      |
| ```b```                   | move to previous word                  |
| ```e```                   | move to the end of the current word    |
| ```0```                   | move to beginning of line              |
| ```$```                   | move to end of line                    |
| ^f                        | move down 1 screen                     |
| ^b                        | move up 1 screen                       |
|```gg```                   | move to beginning of buffer            |
|```G```                    | move to end of buffer i                |
|```x```                    | delete next character                  |
|```X```                    | delete previous character              |
|```dd```                   | delete current line                    |
|```de```                   | delete all characters to the end of the current word|
|```dw```                   | delete all characters before the beginning of the next word|
|```de```                   | delete all characters from the beginning of the current word|
|```d0```                   | delete all characters from the beginning of the current line|
|```d$```                   | delete all characters to the end of the current line|
|```yy```                   | copy current line                      |
|```ye```                   | copy all characters to the end of the current word|
|```yw```                   | copy all characters before the beginning of the next word|
|```ye```                   | copy all characters from the beginning of the current word|
|```y0```                   | copy all characters from the beginning of the current line|
|```y$```                   | copy all characters to the end of the current line|
|```p```                    | paste                                  |
|```r``` and character      | replace with the character             |
|```R```                    | replace mode                           |
|```o```                    | enter insert mode at the one line below|
|```O```                    | enter insert mode at the one line up   |
|```.```                    | repeat the previous action             |
|```:```                    | switch to command mode                 |


{{% note note %}}
If you are in the intert mode, editing the text is quite similar to other programs like MS words.
{{% /notice %}}
