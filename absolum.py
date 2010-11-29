#! /usr/bin/env python

""" Absolum

An Electronic Design Automation (EDA) Suite for Robotic Development.
Currently based on PyGTK & libgerbv.

"""

import sys
import gerbv


# =============================================================================

class Absolum:

    def __init__(self, args):
        if args[0] == "-h":
            usage()

    def usage(self):
        print """
        Usage: thingy [options]
	        -h
	        -H hostname
        """

        
# =============================================================================

if __name__ == "__main__":
    absolum = Absolum(sys.argv[:1])

