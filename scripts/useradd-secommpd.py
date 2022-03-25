#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#https://gist.githubusercontent.com/Micro-Biology/ba343ba7d8763d34eec80a16b66b12c4/raw/f115715dfff2f4483f6c441edeab16f5379f7ac7/addME.py

#I have modified the above script to use the subprocess and libseccomp libraries and added seccomp filters to restrict syscalls to only those which are necessary for the time the program is run.
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#!/usr/bin/env python3


import sys
import getpass
import re
import pwd
import subprocess

# Python bindings for the libseccomp library
from seccomp import *


def setup_seccomp():

    # create a filter object with a default KILL action
    f = SyscallFilter(defaction=KILL)

    '''Arguments:
        defaction - the default filter action'''
    
    # add syscall filter rules to allow certain syscalls
    f.add_rule(ALLOW, "execve")
    f.add_rule(ALLOW, "mmap")
    f.add_rule(ALLOW, "access")
    f.add_rule(ALLOW, "open")
    f.add_rule(ALLOW, "fstat")
    f.add_rule(ALLOW, "mprotect")
    f.add_rule(ALLOW, "set_tid_address")
    f.add_rule(ALLOW, "set_robust_list")
    f.add_rule(ALLOW, "rt_sigaction")
    f.add_rule(ALLOW, "rt_sigprocmask")
    f.add_rule(ALLOW, "getrlimit")
    f.add_rule(ALLOW, "futex")
    f.add_rule(ALLOW, "getrandom")
    f.add_rule(ALLOW, "ioctl")
    f.add_rule(ALLOW, "readlink")
    f.add_rule(ALLOW, "stat")
    f.add_rule(ALLOW, "munmap")
    f.add_rule(ALLOW, "sigaltstack")
    f.add_rule(ALLOW, "brk")
    f.add_rule(ALLOW, "openat")
    f.add_rule(ALLOW, "getdents")
    f.add_rule(ALLOW, "fcntl")
    f.add_rule(ALLOW, "lseek")
    f.add_rule(ALLOW, "read")
    f.add_rule(ALLOW, "close")
    f.add_rule(ALLOW, "dup")
    f.add_rule(ALLOW, "geteuid")
    f.add_rule(ALLOW, "getuid")
    f.add_rule(ALLOW, "getegid")
    f.add_rule(ALLOW, "getgid")
    f.add_rule(ALLOW, "lstat")
    f.add_rule(ALLOW, "getcwd")
    f.add_rule(ALLOW, "futex")
    f.add_rule(ALLOW, "write")
    f.add_rule(ALLOW, "socket")
    f.add_rule(ALLOW, "connect")
    f.add_rule(ALLOW, "wait4")
    f.add_rule(ALLOW, "pipe2")
    f.add_rule(ALLOW, "clone")
    f.add_rule(ALLOW, "sigaltstack")
    f.add_rule(ALLOW, "exit_group")

    # load the filter into the kernel
    f.load()
    print(f'Seccomp enabled...')

setup_seccomp()

def root_check():
    """Exit if login name not root."""

    if not getpass.getuser() == 'root':
        print("ERROR: THIS PROGRAM REQUIRES ROOT PRIVILEGES. EXITING.")
        sys.exit()

def username_prompt():
    """Prompt user. Check that input matches, and cotains at least one allowable character."""

    print("Valid usernames contain only the characters 'a-z', e.g. trex")

    while True:
        username = str(input("Enter username to add: "))
        confirm_name = str(input("To confirm, re-enter username: "))

        if username != confirm_name or not re.match("^[a-z]+$", username):
            print("SORRY, THAT'S NOT ALLOWED. TRY AGAIN.")
            continue

        else:
            print("OK, checking if user: %s exists." %(username))
            return username

def username_check():
    """Check if username exists."""

    while True:
        check = username_prompt()

        try:
            pwd.getpwnam(check)
            print("USER %s EXISTS. TRY A DIFFERENT USERNAME." % (check))

        except KeyError:
            print("User %s does not exist. Continuing..." % (check))
            return check

def comment_prompt():
    """Prompt for input. Check that input matches and contains allowable characters. No input is allowable."""

    print("Valid comments contain only the characters 'a-z' and ',', e.g. rex,tyrannosaurus. This field can be left blank.")

    while True:
        comment = str(input("Enter user comments, or press 'return' twice to leave blank: "))
        confirm_comment = str(input("To confirm, re-enter comments: "))

        if comment != confirm_comment or not re.match("^[a-z,]*$", comment):
            print("SORRY, THAT'S NOT ALLOWED. TRY AGAIN.")
            continue

        else:
            print("Comments match. Continuing...")
            return comment

def passwd_prompt():
    """Prompt user for input. Check that input matches and meets password complexity requirements."""

    print("Password MUST contain AT LEAST: one lower-case letter, one number, one symbol, and be a MINIMUM of 8 characters in length, e.g. 4.lizard")

    while True:

        passy = getpass.getpass(prompt="Enter password for user: ")
        confirm_passy = getpass.getpass(prompt="To confirm, re-enter password: ")


        # check for the following conditions: 
        # user input matches
        # length of input is at least 8 characters
        # input contains at least 1 number  
        # input contains at least 1 letter      
        # input contains at least 1 symbol 

        if passy != confirm_passy \
        or len(passy) <8 \
        or not re.search('\d', passy) \
        or not re.search(r"[a-z]",passy) \
        or not re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~"+r'"]', passy):

            print("SORRY, THAT'S NOT ALLOWED. TRY AGAIN.")
            continue

        else:
            print("Password meets complexity requirement. Continuing...")
            return passy

def add_usr():
    """Call the useradd command to create an account with given parameters."""

    name = username_check()
    note = comment_prompt()
    code = passwd_prompt()
    home = "/home/"+name

    print("Adding user: %s" % (name))

    # create user  
    # create group with same name as user, adding user to group
    # comment (lastname, firstname) 
    # create home directory           
    # login shell 
    # password (encrypted via openssl) 

    password =  name+":"+code
    subprocess.run(["useradd" , "-c" , note , "-s" , "/bin/bash" , "-d" , home , name ])
    user_pass="bash -c \"echo -e '"+password+"\\n"+password+"\\n' | passwd "+name+"\""
    print(user_pass)
    subprocess.check_call(user_pass, shell=True)
    subprocess.call(["sudo","getent","passwd",name])
    subprocess.call(["sudo","getent","shadow",name])

    print("Done.")

def addME():
    """Add user to Linux OS."""

    root_check()
    add_usr()

if __name__ == '__main__':
    addME()
