
""" Absolum

An Electronic Design Automation (EDA) Suite for Robotic Development.
Currently based on PyGTK & libgerbv.

"""

"""Import GTK"""
import pygtk
pygtk.require('2.0')
import gtk
#from gtk import gdk

# =============================================================================

class Gui:

    def __init__(self):
        # Create a new window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("Absolum")
        self.window.set_border_width(0)

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

    def start(self):
        gtk.main()

    def.stop(self):
        gtk.main_quit()

