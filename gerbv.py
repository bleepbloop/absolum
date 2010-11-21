from ctypes import *

class GerbView:
    def __init__(self):
        """ import libgerbv """
        libgerbv = CDLL("libgerbv.so.1.0.5")
        print libgerbv

        project = GerbvProject()
        print project
        
        create_project = libgerbv.gerbv_create_project
        create_project.restype = POINTER(GerbvProject)
        project = create_project()[0]
        print project
       

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
