# -*- coding: utf-8 -*-
'''
Copyright@USTC SSE
Author by ch yy in suzhou ,08/12/2015
Use d3.js to display
'''

import os
import sys

def display_service(port):
    cmdstr = "python3 -m http.server %s" % int(''.join(port))
    os.system(cmdstr)

if __name__ == '__main__':
    display_service(sys.argv[1:])