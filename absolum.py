#! /usr/bin/env python
""" Absolum """

import sys

import pygtk
pygtk.require('2.0')
import gtk

import gerbv


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

    def gerbv(self):
        gerber_viewer = gerbv.GerberViewer()
        gerber_viewer.create_project()


def main(argv):
        absolum = Absolum()
        absolum.gerbv()
        gtk.main()


# start the ball rolling.
if __name__ == "__main__":
    main(sys.argv[1:])
