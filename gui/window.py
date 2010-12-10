
""" Absolum: gui/window.py

    Currently based on PyGTK & libgerbv.

"""

"""Import GTK"""
import pygtk
pygtk.require('2.0')
import gtk
#from gtk import gdk

# =============================================================================

class Main():

    def __init__(self):
        # Create a new window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("Absolum")
        self.window.set_border_width(10)

        # Create a new horizontal toolbox
        self.box = gtk.HBox(False, 0)
        self.window.add(self.box)

        # Second horizontal toolbox
        self.toolbox = gtk.HBox(False, 0)
        # self.window.add(self.toolbox)

        # Create a new parts button
        self.parts_button = gtk.Button("Parts")
        self.box.pack_start(self.parts_button, True, True, 0)

        # Create a new search button
        self.search_button = gtk.Button("Search")
        self.box.pack_start(self.search_button, True, True, 0)

        # Show Components
        self.parts_button.show()
        # self.search_button.show()
        self.box.show()
        self.window.show()

    def start(self):
        gtk.main()

    def stop(self):
        gtk.main_quit()
