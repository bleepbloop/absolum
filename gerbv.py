from ctypes import *

libgerbv = None
project = None

class GerberViewer:
    """GerberViewer Class Loads & Interacts with libgerbv"""

    def __init__(self):
        """Import libgerbv"""
        global libgerbv
        libgerbv = CDLL("libgerbv.so.1.0.5")

    def create_project(self):
        """Initialize GerbvProject Structure"""
        global libgerbv
        global project
        gerbv_create_project = libgerbv.gerbv_create_project
        gerbv_create_project.restype = POINTER(GerbvProject)
        project = gerbv_create_project()[0]
        print project        
        print "Last Loaded = -1?", project.last_loaded
        print "Check Before Delete = True?", project.check_before_delete
        print "Max Files = 1?", project.max_files

    def open_layer_from_filename(self):
        pass

    def create_rs274x_image_from_filename(self):
        pass
       

"""libgerbv Structures"""

class GerbvProject(Structure): 
    """GdkColor, gerbv_fileinfo_t"""
    _fields_ = [("background", c_int),             # GdkColor
                ("max_files", c_int),              # int
                ("file", c_int),                   # gerbv_fileinfo_t **
                ("curr_index", c_int),             # int
                ("last_loaded", c_int),            # int
                ("renderType", c_int),             # int
                ("check_before_delete", c_bool),   # gboolean
                ("path", c_char_p),                # gchar *
                ("execpath", c_char_p),            # gchar *
                ("project", c_char_p)]             # gchar *
