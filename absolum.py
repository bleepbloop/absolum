#! /usr/bin/env python

""" Absolum

An Electronic Design Automation (EDA) Suite for Robotic Development.
Currently based on PyGTK & libgerbv.

"What do I do with Absolum?"

"""


""" System Modules """
import sys
import argparse

""" Absolum Modules """
from gerbv import viewer
from gui import window

# ============================================================================

class Absolum():

    def __init__(self):
        print "Welcome to Absolum"

    # Gui 
    def load_gui(self):
        self._gui = window.Main()
        
    def start_gui(self):
        self._gui.start()

    # Gerber
    def load_gerber(self):
        self._gerber_viewer = viewer.GerberViewer()
        print dir(self._gerber_viewer)

    # Database
    def load_db(self):
        pass

    # Network
    def connect_atomic(self):
        pass
        
#=============================================================================
>>>>>>> 3390560b27788497f3945e356fc06f3f73b7df38:absolum.py

<<<<<<< HEAD:absolum.py
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                description='Absolum: The Robotic Design Suite')
    args = parser.parse_args()

    # Create Absolum
    absolum = Absolum()

    # Start...  Gerber Viewer
    absolum.load_gerber()
    #           GTK Window
    absolum.load_gui()

    # Init...   Databases
    absolum.load_db()
=======
    """ Start gui Last """
    absolum.start_gui()
>>>>>>> 3390560b27788497f3945e356fc06f3f73b7df38:absolum.py

<<<<<<< HEAD:absolum.py
=======
if __name__ == "__main__":
    # parser = argparse.ArgumentParser(description='Absolum: The Robotics Design Suite')
    # args = parser.parse_args()
    main()
    
    
>>>>>>> 3390560b27788497f3945e356fc06f3f73b7df38:absolum.py
