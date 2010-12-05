#! /usr/bin/env python

""" Absolum

An Electronic Design Automation (EDA) Suite for Robotic Development.
Currently based on PyGTK & libgerbv.

"""

""" System Modules """
import argparse
import sqlite3
import sys

""" Absolum Modules """
from gerbv import viewer
from gui import window

# =============================================================================

class Absolum:

    def __init__(self):
        pass

    def load_gerber(self):
    	gerber_viewer = viewer.GerberViewer()
	print dir(gerber_viewer)

    def load_gui(self):
        pass

    def connect_atomic(self):
    	pass


        
# =============================================================================

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
             description='Absolum: The Robotic Design Suite')
    args = parser.parse_args()
    absolum = Absolum()
    absolum.load_gerber()
