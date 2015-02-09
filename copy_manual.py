#!/usr/bin/env python
# Author: Avinash Yenikapati
# Date: 15-10-2014

"""
copy_manual.py

This file will copy required hooks from default template dir to
already cloned repositories If file doesn't exist.

copy this file to jiva_buildout and run 'python copy_manual.py'
"""

import os

SRC = "src"
FILES_TO_CHECK = ["pre-commit"]

all_dirs = os.listdir(SRC)

for directory in all_dirs:
    for req_file in FILES_TO_CHECK:
        path = "%s/%s/.git/hooks/%s" % (SRC, directory, req_file)
        if not os.path.exists(path):
            os.system("cp /usr/share/git-core/templates/hooks/%s %s" % (req_file, path))

if __name__ == '__main__':
    pass

