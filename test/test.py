#! /usr/bin/env python

import os
import sys


def main():
    print sys.version
    print sys.path
    dirtest()
    #fib(100000)


def dirtest(): 
    """ Do some Directory Testing """

    # test system directory calls
    print "Current Directory:"
    print os.getcwd()
    print os.listdir(os.getcwd())

    print "Is '.ssh' in user's home?", '.ssh' in os.listdir('/home/rampage')

    print "Is /home a mount point?", os.path.ismount('/home')

def usage():
    # test print 
    print """
    Usage: thingy [options]
	    -h
	    -H hostname
    """

def fib(n):
    a, b = 0,1
    while a < n:
        print a,
        a, b = b, a+b


# start the ball rolling.
if __name__ == "__main__":
    main()
