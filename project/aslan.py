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

# ============================================================================
class Aslan(object):
    def __init__(self):
        self.new_project()        
        
# =====================================
# Project
    def new_project(self):
        self.new_doc()
        self.new_bom()
        self.new_schematic()
        self.new_pcb()
        self.new_cnc()
        
# =====================================
# Docs
    def new_doc(self):
        self._docs = DocumentViewer()
        
# =====================================
# Bill of Materials
    def new_bom(self):
        self._bom_list = Catalog()
        
# =====================================
# Schematics
    def new_schematic(self):
        self._schem = Diagram()
        
# =====================================
# PCBs
    def new_pcb(self):
        pass

# =====================================       
# CNC
    def new_cnc(self):
        pass
        
# ============================================================================
if __name__ == "__main__":
    aslan = Aslan()

# ============================================================================
