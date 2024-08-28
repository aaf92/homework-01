# Homework 01 - Bash introduction

## Due 2024-09-03 at 11:59pm

This assignment will make sure you are comfortable working with the command line and writing simple bash scripts. It will also familiarize you with our handin process.
 

## 70% Credit

You will create a bash script, `assign1.sh`, that can be run as a program and prints out the first argument provided to the script. The first argument passed to the shell script is available as $1 (The second argument is $2 and so on).

Here is the expected behavior:

```bash
$ ./assign1.sh 
$ ./assign1.sh hello
hello
$ ./assign1.sh good bye
good
```

The `assign1.sh` file is a text file where the first line is:

`#!/bin/bash`  

This tells the shell to run the commands in the file using the bash file when the file is run like an executable.
For this to work, you have to make the file executable using chmod:

`$ chmod +x assign1.sh`  

Linux and Mac users both have access to a bash command line by default. For Windows users we recommend WsL2 to get a linux environment. See [here](https://docs.microsoft.com/en-us/windows/wsl/install-win10) for installation instructions You can use an editor of your choice or nano as your text editor. If you want to use an IDE, we recommend VS Code. 


## 80% Credit

Modify assign1.sh to print out the first line of a file that is specified as an argument. For example, given a file `hello.txt`:

```
hello there
how are you?
```

The command:

```bash
./assign1.sh hello.txt
```

Would get this output:

```
hello there
```


## 90% Credit

Modify `assign1.sh` to process a file that is specified as an argument. The file is assumed to be comma delimited text and assign1.sh should print out the first column.

For example, given this file:

```
abc,1,2,3
abc,3,3,3
xyz,3,2,1
xyz,3,2,3
ijk,0,0,0
xyz,1,1,1
```

You would get this output:

```
abc
abc
xyz
xyz
ijk
xyz
```

## 100% Credit

Instead of printing the first column, print out counts of the values in the first column, in increasing order.

For example, given this file:

```
abc,1,2,3
abc,3,3,3
xyz,3,2,1
xyz,3,2,3
ijk,0,0,0
xyz,1,1,1
```

You would get this output

```
  1 ijk
  2 abc
  3 xyz
```

## Submission

Submit `assign1.sh` on GitHub Classroom and it will automatically grade your submission.  Note we have constructed the partial credit to build up to the final solution, but you do not need to submit the partial credit portions (other than to "lock in" your current grade).  That is, if you submit a script that achieves the 100% task, you will receive a 100% even if you haven't demonstrated to the autograder that you achieved the other previous tasks.