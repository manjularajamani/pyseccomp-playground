# pyseccomp-playground

The libseccomp library provides and easy to use, platform independent, interface to the Linux Kernel's **syscall filtering mechanism**.
seccomp (short for secure computing mode) is a computer security facility in the Linux kernel. seccomp allows a process to make a one-way transition into a "secure" state where it cannot make any system calls except **exit()**, **sigreturn()**, **read()** and **write()** to already-open file descriptors. Should it attempt any other system calls, the kernel will either just log the event or terminate the process with SIGKILL or SIGSYS.

# Introduction            

This repository will hold python scripts that have been seccomp'd via the libseccomp python library  
               
             
# Installing the libseccomp Library

`Step 1:` Grab the latest release from the release page at [libseccomp](https://github.com/seccomp/libseccomp/releases/) repository

`Step 2:` If you are building the libseccomp library from an official release tarball, you  should follow the familiar three step process used by most autotools based applications:

```sh
./configure
make
make install
```
`Step 3:` Install `python3-devel` using your package manager of choice to fulfil the dependencies needed 
                         
