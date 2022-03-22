# Linux Syscalls

System call **provides the services of the operating system to the user programs via Application Program Interface(API)**. It provides an interface between a process and operating system to allow user-level processes to request services of the operating system.

# Strace

strace is **a powerful command line tool for debugging and trouble shooting programs in Unix-like operating systems such as Linux**. It captures and records all system calls made by a process and the signals received by the process. 

```sh
strace -o file.txt python3 <your_script>
strace -c python3 <your_script>
strace -t python3 <your_script>
strace -i python3 <your_script>
``` 

# Seccomp

seccomp (short for secure computing mode) is a computer security facility in the Linux kernel. seccomp allows a process to make a one-way transition into a "secure" state where it cannot make any system calls except **exit() , sigreturn() , read() and write()** to already-open file descriptors.

# libseccomp

The libseccomp library provides an easy to use, platform independent, interface to the Linux Kernel's syscall filtering mechanism.

# References

`[0]` https://docs.python.org/3/library/subprocess.html

`[1]`https://github.com/seccomp/libseccomp/blob/main/src/python/seccomp.pyx#L24

`[2]`https://github.com/seccomp/libseccomp/blob/main/src/python/seccomp.pyx#L339

`[3]` https://spinscale.de/posts/2020-10-27-seccomp-making-applications-more-secure.html

`[4]` https://stackoverflow.com/questions/21009416/python-subprocess-security

`[5]` https://docs.python.org/3/library/subprocess.html#security-considerations

`[6]` https://docs.python.org/3/library/

`[7]` https://stackoverflow.com/a/32199696

`[8]` https://filippo.io/linux-syscall-table/

`[9]` https://linuxhint.com/list_of_linux_syscalls/

`[10]` https://rhodesmill.org/brandon/slides/2014-07-pyohio/strace/

`[11]` https://libseccomp.readthedocs.io/en/latest/

`[12]` https://scribe.rip/linux-security-understand-and-practice-seccomp-syscall-filter-37004bc4b53d

`[13]`https://twitter.com/_JohnHammond/status/1265258932269957121/photo/1

`[14]` https://noti.st/spinscale/NPWbNV#spsFKWs

`[15]`https://github.com/antitree/syscall2seccomp/blob/master/syscall2seccomp.py

`[16]` https://www.antitree.com/2017/09/tool-syscall2seccomp/

`[17]`https://docs.aws.amazon.com/AmazonECS/latest/bestpracticesguide/security-runtime.html

`[18]` https://www.youtube.com/watch?v=6lRHK_LLUGI

`[19]` https://blog.heroku.com/applying-seccomp-filters-on-go-binaries

`[20]` https://packages.ubuntu.com/focal/libseccomp-dev

`[21]`https://archive.fosdem.org/2020/schedule/event/debugging_strace_modern/attachments/slides/4109/export/events/attachments/debugging_strace_modern/slides/4109/fosdem_2020_slides_postmodern_strace.pdf

`[22]` https://arxiv.org/pdf/2012.02554.pdf

`[23]` https://github.com/IAIK/Chestnut

`[24]`https://gist.github.com/chrisdlangton/f94fd36028a0ba46b73e6629524d5710

`[25]`https://firejail.wordpress.com/documentation-2/seccomp-guide/

`[26]`https://adil.medium.com/allow-disallow-syscalls-via-seccomp-d5fc8816d34e

`[27]` https://www.brendangregg.com/blog/2014-05-11/strace-wow-much-syscall.html

`[28]`https://blog.cloudflare.com/sandboxing-in-linux-with-zero-lines-of-code/

`[29]`https://kubernetes.io/docs/tutorials/security/seccomp/

