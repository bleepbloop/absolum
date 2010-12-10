#!/usr/bin/env python

import git
from git.cmd import Git


class Update(object):
    def __init__(self, path):
        self.g = Git(path)
        
    def list_files(self):
        return self.g.ls_files()

if __name__ == "__main__":
    update = Update("/home/rampage/py/absolum")
    print update.list_files()
