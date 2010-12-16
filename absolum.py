#! /usr/bin/env python

""" Absolum

    Absolum is an Electronic Design Automation (EDA) Suite for Robotics 
    and Gadget Development.
    Currently based on PyGTK, libgerbv, and a few other python modules.

    What can I do with Absolum?
    * Search for the right parts for your project from the top part distributors
    * Create real-time BOMs with the latest prices
    
"""

__author__ = 'Jose.Torres@8bc.org (Jose Angel Torres)'

""" System Modules """
import os
import sys
import argparse

""" Absolum Modules """
from gerbv.viewer import GerberViewer
from gui.window import Main
from project.aslan import Aslan

# ============================================================================

class Absolum():

    def __init__(self):
        self.welcome()

    # Gui 
    def load_gui(self):
        self._gui = Main()
        
    def start_gui(self):
        self._gui.start()

    # Gerber Viewer
    def load_gerber(self):
        self._gerber_viewer = GerberViewer()
        self._gerber_viewer.create_project()
        self._gerber_viewer.open_layer_from_filename()        

    # Databases
    def load_db(self):
        pass

    # Network Connection
    def atomic_connect(self):
        pass
        
    # Projects
    def create_aslan(self):
        pass
        
    def welcome(self):
        print "Welcome to Absolum!\n \
        * Always remember *Absolutely* Nothing is Impossible!"
        
# ============================================================================

if __name__ == "__main__":
    # parser = argparse.ArgumentParser(
    #             description='Absolum: The Robotic Design Suite')
    # args = parser.parse_args()

    # Create Absolum
    absolum = Absolum()

    # Start........ Gerber Viewer
    absolum.load_gerber()
    #.............. GTK Window
    absolum.load_gui()

    # Init......... Databases
    absolum.load_db()
    
    # Create....... Project
    absolum.create_aslan()
    
    # Start Last... Gui
    # absolum.start_gui()

