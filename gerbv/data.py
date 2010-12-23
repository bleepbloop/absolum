""" Absolum: gerbv/data.py

    GerberViewer (libgerbv) Ctype Enumerations & Structures

"""

__author__ = 'Jose.Torres@8bc.org (Jose Angel Torres)'

""" System Modules """
from ctypes import *

# ============================================================================
class GdkColor(Structure):
    _fields_ = [("red", c_uint64), 
                ("green", c_uint64),
                ("blue", c_uint64),
                ("pixel", c_uint64)]

# ============================================================================
# Enumerations

# =====================================
# gerbv_aperature_state_t
class GerbvAperatureState(Structure):
    """  """
    pass
    
# =====================================
# gerbv_interpolation_t
class GerbvInterpolation(Structure):
    pass

# ============================================================================
# Structures

# =====================================
# gerbv_layer_t
class GerbvLayer(Structure):
    _fields_ = [("stepAndRepeat", c_int),           # gerbv_step_and_repeat_t
                ("knockout", c_int),                # gerbv_knockout_t
                ("rotation", c_double),             # xx gdouble
                ("polarity", c_int),                # gerbv_polarity_t
                ("name", c_char_p),                 # xx gchar *
                ("next", c_void_p)]                 # xx gpointer
                
# =====================================
# gerbv_netstate_t
class GerbvNetstate(Structure):
    _fields_ = [("axisSelect", c_int),              # gerbv_axis_select_t
                ("mirrorState", c_int),             # gerbv_mirror_state_t
                ("unit", c_int),                    # gerbv_unit_t
                ("offsetA", c_double),              # xx gdouble
                ("offsetB", c_double),              # xx gdouble
                ("scaleA", c_double),               # xx gdouble
                ("scaleB", c_double),               # xx gdouble
                ("next", c_void_p)]                 # xx gpointer
                
# =====================================             
# gerbv_net_t
class GerbvNet(Structure):
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
                ("label", c_void_p),                # xx GString *
                ("layer", POINTER(GerbvLayer)),     # xx gerbv_layer_t *
                ("state", POINTER(GerbvNetstate))]  # xx gerbv_netstate_t *
                
# =====================================
# gerbv_image_t
class GerbvImage(Structure):
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
                
# =====================================
# gerbv_user_transformation_t
class GerbvUserTransformation(Structure):
    _fields_ = [("translateX", c_double),           # xx gdouble
                ("translateY", c_double),           # xx gdouble
                ("scaleX", c_double),               # xx gdouble
                ("scaleY", c_double),               # xx gdouble
                ("inverted", c_bool)]               # xx gboolean

# =====================================
# gerbv_fileinfo_t
class GerbvFileInfo(Structure):
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

# =====================================
# gerbv_project_t
class GerbvProject(Structure):
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

# ============================================================================
