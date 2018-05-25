#!/usr/bin/env python3

import sys
from os import makedirs
from os.path import isdir
from site import getsitepackages

if __name__ == "__main__":
    """
    Prepend argument to path to be exported for snap installation in
    CMakeLists.txt. Optionally make the directories if they don't
    exist. It may be better to have this as an argument to setup.py,
    but it might complain anyway about PYTHONPATH. That would be
    cleaner, but this is safer.
    """
    
    newpath = ""
    paths = getsitepackages() # could a yield be better?

    # see [1]. We're trying to cover every case possible here. Sure,
    # we could find the single one that is used by snaps, but then
    # things are more likely to break in a snapcraft update. It should
    # be possible to integate this into the setup.py later
    # on. Regardless, this whole file shouldn't be necessary...
    for path in paths:
        if "dist-" in path:
            p = path.replace("dist-", "site-")
        elif "site-" in path:
            p = path.replace("site-", "dist-")
            
        if "usr/lib" in path:
            # TODO: need reference as to why this was necessary.
            p = path.replace("usr/", "")        
            
        if p not in paths:
            paths.append(p)    
    
    for path in paths:
        # prepend
        nextsite=str(sys.argv[1]) + path
        newpath += nextsite + ":"

        # mkdir if doesn't exist. 
        if(not isdir(nextsite) and sys.argv[2] == 'mkdir'):
            makedirs(nextsite, exist_ok=True)
        

    print(newpath[:-1], end='') # no newline
    
# [1] https://stackoverflow.com/questions/9387928/whats-the-difference-between-dist-packages-and-site-packages#9388115    
