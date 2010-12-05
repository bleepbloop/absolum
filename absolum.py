#! /usr/bin/env python

""" Absolum

An Electronic Design Automation (EDA) Suite for Robotic Development.
Currently based on PyGTK & libgerbv.

"""

""" System Modules """
import sys
import argparse

""" Absolum Modules """
import gerbv
import gui
from gerbv import gerbv

# =============================================================================

class Absolum:

    def __init__(self):
        pass

    def load_gerber(self):
    	gerber = gerbv.GerberViewer()
	print gerber

    def load_gui(self):
        pass 

        
# =============================================================================

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
             description='Absolum: The Robotic Design Suite')
    args = parser.parse_args()
    absolum = Absolum()
    absolum.load_gerber()
