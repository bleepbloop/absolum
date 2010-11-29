#!/usr/bin/env python

""" Python Gerber Viewer (gerbv)

Gerber Viewer interacts with gEDA's libgerbv to interact with 
Gerber RS-274X, Excellon drill, and CSV pick-and-place files.


"""

__version__ = '0.0.1'

import os
import sys
from ctypes import *
from ctypes.util import find_library

# =============================================================================
class GdkColor(Structure):
    _fields_ = [("red", c_uint64), 
                ("green", c_uint64),
                ("blue", c_uint64),
                ("pixel", c_uint64)]

# =============================================================================
class GerberViewer:
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
        print self._project        
        print "Last Loaded = ", self._project.last_loaded
        print "Check Before Delete = ", self._project.check_before_delete
        print "Max Files = ", self._project.max_files

# =============================================================================
"""libgerbv Structures"""

class GerbvLayer(Structure):
    """ gerbv_layer_t """
    _fields_ = [("stepAndRepeat", c_int),           # gerbv_step_and_repeat_t
                ("knockout", c_int),                # gerbv_knockout_t
                ("rotation", c_double),             # xx gdouble
                ("polarity", c_int),                # gerbv_polarity_t
                ("name", c_char_p),                 # xx gchar *
                ("next", c_void_p)]                 # xx gpointer

class GerbvNetstate(Structure):
    """ gerbv_netstate_t """
    _fields_ = [("axisSelect", c_int),              # gerbv_axis_select_t
                ("mirrorState", c_int),             # gerbv_mirror_state_t
                ("unit", c_int),                    # gerbv_unit_t
                ("offsetA", c_double),              # xx gdouble
                ("offsetB", c_double),              # xx gdouble
                ("scaleA", c_double),               # xx gdouble
                ("scaleB", c_double),               # xx gdouble
                ("next", c_void_p)]                 # xx gpointer

class GerbvNet(Structure):
    """ gerbv_net_t """
    pass
GerbvNet._fields_ = [("start_x", c_double),         # xx double
                ("start_y", c_double),              # xx double
                ("stop_x", c_double),               # xx double
                ("stop_y", c_double),               # xx double
                ("aperture", c_int),                # xx int
                ("aperture_state", c_int),          # gerbv_aperture_state_t
                ("interpolation", c_int),           # gerbv_interpolation_t 
                ("gerbv_cirseg_t", c_int),          # gerbv_cirseg_t *
                ("next", POINTER(GerbvNet)),        # xx gerbv_net *
                ("label", c_void_p),                # GString *
                ("layer", POINTER(GerbvLayer)),     # xx gerbv_layer_t *
                ("state", POINTER(GerbvNetstate))]  # xx gerbv_netstate_t *

class GerbvImage(Structure):
    """ gerbv_image_t """
    _fields_ = [("layertype", c_int),               # gerbv_layertype_t
                ("aperture", c_int),                # gerbv_aperature_t *
                ("layers", GerbvLayer),             # xx gerbv_layer_t *
                ("states", GerbvNetstate),          # xx gerbv_netstate_t *
                ("amacro", c_int),                  # gerbv_amacro_t *
                ("format", c_int),                  # gerbv_format_t *
                ("info", c_int),                    # gerbv_image_info_t *
                ("netlist", c_int),                 # gerbv_net_t *
                ("gerbv_stats", c_int),             # gerbv_stats_t *
                ("drill_stats", c_int)]             # gerbv_drill_status_t *

class GerbvUserTransformation(Structure):
    """ gerbv_user_transformation_t """
    _fields_ = [("translateX", c_double),           # xx gdouble
                ("translateY", c_double),           # xx gdouble
                ("scaleX", c_double),               # xx gdouble
                ("scaleY", c_double),               # xx gdouble
                ("inverted", c_bool)]               # xx gboolean

class GerbvFileInfo(Structure):
    """ gerbv_fileinfo_t """
    _fields_ = [("image", POINTER(GerbvImage)),     # xx gerbv_image_t *
                ("color", GdkColor),                # xx GdkColor
                ("alpha", c_uint16),                # xx guint16
                ("isVisible", c_bool),              # xx gboolean
                ("privateRenderData", c_void_p),    # xx gpointer
                ("fullPathname", c_char_p),         # xx gchar *         
                ("name", c_char_p),                 # xx gchar *                
                ("transform", GerbvUserTransformation), 
                    # xx gerbv_user_transformation_t
                ("layer_dirty", c_bool)]            # xx gboolean

class GerbvProject(Structure):
    """ gerbv_project_t """
    _fields_ = [("background", POINTER(GdkColor)),  # xx GdkColor
                ("max_files", c_int),               # xx int
                ("file", GerbvFileInfo),            # xx gerbv_fileinfo_t **
                ("curr_index", c_int),              # xx int
                ("last_loaded", c_int),             # xx int
                ("renderType", c_int),              # xx int
                ("check_before_delete", c_bool),    # xx gboolean
                ("path", c_char_p),                 # xx gchar *
                ("execpath", c_char_p),             # xx gchar *
                ("project", c_char_p)]              # xx gchar *

# =============================================================================
if __name__ == "__main__":
    gerber_viewer = GerberViewer()
    gerber_viewer.create_project()
    gerber_viewer.open_layer_from_file()
