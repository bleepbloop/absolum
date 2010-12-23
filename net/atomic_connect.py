#! /usr/bin/env python

""" Absolum: net/atomic_connect.py

    Helper module for custom socket communication.

"""

__author__ = 'Jose.Torres@8bc.org (Jose Angel Torres)'

""" System Modules """
import httplib
import urllib

""" Absolum Modules """

# ============================================================================

class AtomicHandler(object):
    
    def __init__(self):
        self._data = None
        
# =====================================
    
    def connect(self):
        conn = httplib.HTTPConnection("1024bit.org")
        response = conn.getresponse()
        if response.status == 200:
            self._data = response.read()
        return response

# ============================================================================     

if __name__ == "__main__":
    print 'Testing Atomic Handle...'
    
# ============================================================================
