#!/usr/bin/env python

""" Python Gerber Viewer (gerbv) Extension

Gerber Viewer interacts with gEDA's libgerbv to interact with 
Gerber RS-274X, Excellon drill, and CSV pick-and-place files.


"""

__author__ = 'Jose.Torres@8bc.org (Jose Angel Torres)'

""" System Modules """
import os
import sys
# ctypes for libgerbv interaction
from ctypes import *
from ctypes.util import find_library

""" Helper (Gerber Viewer) Data Storage Module """
from data import *


# ============================================================================
class GerberViewer(object):
    """GerberViewer Class Loads & Interacts with libgerbv"""

    def __init__(self):
        self._libgerbv = CDLL(find_library("gerbv"))
        self._project = None

    def create_project(self):
        gerbv_create_project = self._libgerbv.gerbv_create_project
        gerbv_create_project.restype = POINTER(GerbvProject)
        self._project = gerbv_create_project()[0]
        self.print_project()

    def open_layer_from_filename(self, \
        filename= os.getcwd() + '/test/files/gerbers/ArduinoMp3Shield.drd'):
        gerbv_open_layer = self._libgerbv.gerbv_open_layer_from_filename
        gerbv_open_layer.argtypes = [POINTER(GerbvProject), c_char_p]
        gerbv_open_layer(byref(self._project), filename)
        self.print_project()

    def create_rs274x_image_from_file(self):
        pass

    def print_project(self):
        return [('project_instance', self._project),
                ('last_loaded', self._project.last_loaded),
                ('check_before_delete', self._project.check_before_delete),
                ('max_files', self._project.max_files)]
                
# ============================================================================

if __name__ == "__main__":
    gerber_viewer = GerberViewer()
    gerber_viewer.create_project()
    gerber_viewer.open_layer_from_file()

