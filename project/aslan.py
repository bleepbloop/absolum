""" Absolum: projects/aslan.py

    An _Aslan_ project object holds bom, schem, pcb, and cnc info. for Absolum.
    Default workspace is '~/aslan/<project name>'.
    

"""

__author__ = 'Jose.Torres@8bc.org (Jose Angel Torres)'

""" System Modules """
import os
import datetime

""" Aslan Modules """
import helper.file

# project module
from bom.list import Catalog
from docs.pdf import DocumentViewer
from schem.capture import Diagram

import pcb
import cnc

#=============================================================================

class Aslan(object):

    def __init__(self):
        self.bom_list = Catalog()
        self.pdf_docs = DocumentViewer()
        self.schem = Diagram()
        
    def new_project(self):
        new_schematic()
        new_pcb()
        
    def new_schematic(self):
        pass
    
    def new_pcb(self):
        pass
        


