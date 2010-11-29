#! /usr/bin/env python

""" Absolum

An Electronic Design Automation (EDA) Suite for Robotic Development.
Currently based on PyGTK & libgerbv.

"""

""" System Modules """
import sys
import argparse

""" Absolum Modules """
import gerbv
import gui


# =============================================================================

class Absolum:

    def __init__(self):
        pass

        
# =============================================================================

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
             description='Absolum: The Robotics Design Suite')
    args = parser.parse_args()
    absolum = Absolum()

