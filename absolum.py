#! /usr/bin/env python

""" Absolum

An Electronic Design Automation (EDA) Suite for Robotic Development.
Currently based on PyGTK & libgerbv.


"""

import sys
import gerbv
"""Import GTK"""
import pygtk
pygtk.require('2.0')
import gtk

# =============================================================================

class Absolum:

    def __init__(self):
        # Create a new window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("Absolum")
        self.window.set_border_width(10)

        # Create a new box
        self.box = gtk.HBox(False, 0)
        self.window.add(self.box)

        # Create a new button
        self.button = gtk.Button("Start")
        self.box.pack_start(self.button, True, True, 0)


        # Show Components
        self.button.show()
        self.box.show()
        self.window.show()
        
# =============================================================================

if __name__ == "__main__":
    absolum = Absolum()
    gerber_viewer = gerbv.GerberViewer()
    gerber_viewer.create_project()
    gerber_viewer.open_layer_from_file()
    gtk.main()
