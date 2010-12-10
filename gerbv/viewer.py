#!/usr/bin/env python

""" Python Gerber Viewer (gerbv)

Gerber Viewer interacts with gEDA's libgerbv to interact with 
Gerber RS-274X, Excellon drill, and CSV pick-and-place files.


"""

__version__ = '0.0.1'


""" System Modules """
import os
import sys
from ctypes import *
from ctypes.util import find_library

""" libgerbv Helper Modules """
from data import *


# ============================================================================
class GerberViewer():
    """GerberViewer Class Loads & Interacts with libgerbv"""

    def __init__(self):
        """Import libgerbv"""
        self._libgerbv = CDLL(find_library("gerbv"))
        self._filename = c_char_p(os.getcwd() \
                            + '/test/ex/ArduinoMp3Shield.drd')
        self._project = None

    def create_project(self):
        """Initialize GerbvProject Structure"""
        gerbv_create_project = self._libgerbv.gerbv_create_project
        gerbv_create_project.restype = POINTER(GerbvProject)
        self._project = gerbv_create_project()[0]
        self.print_project()

    def open_layer_from_file(self):
        """ Open a file, parse contents, 
            and add a new layer to an existing project."""
        gerbv_open_layer = self._libgerbv.gerbv_open_layer_from_filename
        gerbv_open_layer.argtypes = [POINTER(GerbvProject), c_char_p]
        gerbv_open_layer(byref(self._project), self._filename)
        self.print_project()

    def create_rs274x_image_from_file(self):
        pass

    def print_project(self):
        return [('project_instance', self._project),
                ('last_loaded', self._project.last_loaded),
                ('check_before_delete', self._project.check_before_delete),
                ('max_files', self._project.max_files)]

if __name__ == "__main__":
    gerber_viewer = GerberViewer()
    gerber_viewer.create_project()
    gerber_viewer.open_layer_from_file()

