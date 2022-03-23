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

* https://docs.python.org/3/library/subprocess.html
* https://github.com/seccomp/libseccomp/blob/main/src/python/seccomp.pyx#L339
* https://spinscale.de/posts/2020-10-27-seccomp-making-applications-more-secure.html
* https://stackoverflow.com/questions/21009416/python-subprocess-security
* https://docs.python.org/3/library/
* https://filippo.io/linux-syscall-table/

* https://linuxhint.com/list_of_linux_syscalls/

* https://rhodesmill.org/brandon/slides/2014-07-pyohio/strace/

* https://libseccomp.readthedocs.io/en/latest/

* https://scribe.rip/linux-security-understand-and-practice-seccomp-syscall-filter-37004bc4b53d

* https://noti.st/spinscale/NPWbNV#spsFKWs

* https://github.com/antitree/syscall2seccomp/blob/master/syscall2seccomp.py

* https://www.antitree.com/2017/09/tool-syscall2seccomp/

* https://docs.aws.amazon.com/AmazonECS/latest/bestpracticesguidesecurity-runtime.html

* https://www.youtube.com/watch?v=6lRHK_LLUGI

* https://blog.heroku.com/applying-seccomp-filters-on-go-binaries

* https://packages.ubuntu.com/focal/libseccomp-dev

* https://archive.fosdem.org/2020/schedule/event/debugging_strace_modern/attachments/slides/4109/export/events/attachments/debugging_strace_modern/slides/4109/fosdem_2020_slides_postmodern_strace.pdf

* https://arxiv.org/pdf/2012.02554.pdf

* https://github.com/IAIK/Chestnut

* https://gist.github.com/chrisdlangton/f94fd36028a0ba46b73e6629524d5710

* https://firejail.wordpress.com/documentation-2/seccomp-guide/

* https://adil.medium.com/allow-disallow-syscalls-via-seccomp-d5fc8816d34e

* https://www.brendangregg.com/blog/2014-05-11/strace-wow-much-syscall.html

* https://blog.cloudflare.com/sandboxing-in-linux-with-zero-lines-of-code/

* https://kubernetes.io/docs/tutorials/security/seccomp/