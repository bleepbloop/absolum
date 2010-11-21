from ctypes import *

class GerbView:

    def __init__(self):
        pass

    def GerbvProject(Structure):
        """GdkColor, gerbv_fileinfo_t"""
        _fields_ = [("background", c_int),          #GdkColor
                    ("max_files", c_int),
                    ("file", c_int),                #gerbv_fileinfo_t
                    ("curr_index", c_int),
                    ("last_loaded", c_int),
                    ("last_loaded", c_int),
                    ("check_before_delete", c_int), #gboolean
                    ("path", c_int),                #gchar
                    ("execpath", c_int),            #gchar
                    ("project", c_int)]             #gchar
