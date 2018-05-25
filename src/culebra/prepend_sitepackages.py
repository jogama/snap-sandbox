#!/usr/bin/env python3

import sys
from os import environ, putenv
from subprocess import call
from site import getsitepackages

if __name__ == "__main__":
    """
    Prepend argument to path to be exported for snap installation in
    CMakeLists.txt. It may be better to have this as an argument to
    setup.py, but it might complain anyway about PYTHONPATH. That
    would be cleaner, but this is safer.
    """
    newpath = ""
    sites = getsitepackages() # could a yield be better?
    for path in sites:
        newpath += str(sys.argv[1]) + path + ":"

    print(newpath[:-1])
