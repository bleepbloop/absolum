#!/usr/bin/env python

import git
from git.cmd import Git


if __name__ == "__main__":
    g = Git("/home/rampage/py/absolum")
    rval = g.ls_files()
    print rval
