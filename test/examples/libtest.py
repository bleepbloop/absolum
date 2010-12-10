#! /usr/bin/env python

import sys
from ctypes import *

def main():

    #ctypes.util.find_library('gerbv')

    libgerbv = CDLL("libgerbv.so.1.0.5")
    print libgerbv

    print "libgerbv is referred", sys.getrefcount(libgerbv), "times"

    print hex(libgerbv.gerbv_create_project())

# start the ball rolling.
if __name__ == "__main__":
    main()
