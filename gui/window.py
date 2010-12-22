
""" Absolum: gui/window.py

    Currently based on PyGTK & libgerbv.

"""

"""Import GTK"""
import pygtk
pygtk.require('2.0')
import gtk
#from gtk import gdk

# =============================================================================

class Main(object):

    def __init__(self):
        # Create a new window
        self._window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self._window.set_title("Absolum")
        self._window.set_border_width(2)
        
        self.setup_handlers()
        
        self.create_toolbox()
        self.create_buttons()
        
        self.show_components()
       
    def setup_handlers(self):
        self._window.connect("destroy", self.destroy)
        
    def create_toolbox(self):
        # Create a new horizontal toolbox
        self._toolbox = gtk.HBox(False, 0)
        self._window.add(self._toolbox)
        
    def create_buttons(self):
        # Create a new parts button
        self._parts_button = gtk.Button("Parts")
        self._toolbox.pack_start(self._parts_button, True, True, 0)

        # Create a new search button
        self._search_button = gtk.Button("Search")
        self._toolbox.pack_start(self._search_button, True, True, 0)

    def show_components(self):
        # Show Components
        self._parts_button.show()
        self._search_button.show()
        
        self._toolbox.show()
        
        self._window.show()

    def start(self):
        gtk.main()
        
    def destroy(self, widget, data=None):
        gtk.main_quit()
        
# ============================================================================= 
