#! /usr/bin/env python

""" Absolum

An Electronic Design Automation (EDA) Suite for Robotic Development.
Currently based on PyGTK & libgerbv.

"""


""" System Modules """
import sys
import argparse

""" Absolum Modules """
from gerbv.gerbv import GerberViewer
from gui.gui import Gui


# =============================================================================

class Absolum():

    def __init__(self):
        print "Welcome to Absolum"
        
    def load_gui(self):
        gerber_viewer = GerberViewer()
        self._gui = Gui()
        
    def start_gui(self):
        self._gui.start()   
        
# =============================================================================

def main():
    absolum = Absolum()
    """ Load gui Last """
    absolum.load_gui()
    absolum.start_gui()

if __name__ == "__main__":
    # print sys.args
    #parser = argparse.ArgumentParser(
                 #description='Absolum: The Robotics Design Suite')
    #args = parser.parse_args()
    main()




