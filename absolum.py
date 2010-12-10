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
from gerbv import viewer
from gui import window

# =============================================================================

class Absolum:

	def __init__(self):
		pass

	def load_gerber(self):
		gerber_viewer = viewer.GerberViewer()
		print gerber_viewer

	def load_gui(self):
		gui = window.Main()
		print gui 
		
	def load_db(self):
		pass

        
# =============================================================================

if __name__ == "__main__":
	parser = argparse.ArgumentParser(
				description='Absolum: The Robotic Design Suite')
	args = parser.parse_args()

	absolum = Absolum()

	""" Starting Gerber Viewer: """
	absolum.load_gerber()
    
	""" Starting GTK Window """
	absolum.load_gui()
	
	""" Initializing Databases """
	absolum.load_db()
	
