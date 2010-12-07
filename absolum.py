#! /usr/bin/env python

""" Absolum

An Electronic Design Automation (EDA) Suite for Robotic Development.
Currently based on PyGTK & libgerbv.

"What do I do with Absolum?"

"""


""" System Modules """
import argparse
import sqlite3
import sys

""" Absolum Modules """

from gerbv import viewer
from gui import window

# =============================================================================

class Absolum():

    def __init__(self):
        print "Welcome to Absolum"
        
    def load_gui(self):
        self._gui = window.Main()
        
    def start_gui(self):
        self._gui.start()   
        
    def load_gerber(self):
    	self._gerber_viewer = viewer.GerberViewer()
    	print dir(self._gerber_viewer)
    	
    def connect_atomic(self):
    	pass
        
#=============================================================================

def main():
    absolum = Absolum()

    absolum.load_gui()
    absolum.load_gerber()
    
    """ Start gui Last """
    absolum.start_gui()

if __name__ == "__main__":
    # parser = argparse.ArgumentParser(description='Absolum: The Robotics Design Suite')
    # args = parser.parse_args()
    main()
    
    
