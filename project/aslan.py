""" Absolum: projects/aslan.py

    An _Aslan_ project object holds bom, schem, pcb, and cnc info. for Absolum.
    Default workspace is '~/aslan/<project name>'.
    

"""

__author__ = 'Jose.Torres@8bc.org (Jose Angel Torres)'

""" System Modules """
import os
import datetime

""" Aslan Modules """
from bom.list import Catalog
import schem
import pcb
import cnc

#=============================================================================

class Aslan(object):

    def __init__(self):
        bom_list = Catalog()
    
    def modification_date(filename):
        t = os.path.getmtime(filename)
        return datetime.datetime.fromtimestamp(t)



