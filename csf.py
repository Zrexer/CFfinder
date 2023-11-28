#!/usr/bin/env python3 

"""
Importer and read Classes and Functions
"""

import sys
import os

lis = sys.argv

s = '{'
bs = '}'

if len(lis) == 1:
    print('{} -l {}#library name{}'.format(lis[0], s, bs))
    
if '-l' in lis:
    libname = lis[lis.index('-l') + 1]
    
    try:
        import_ = __import__(libname)
        print(dir(import_))
    except ModuleNotFoundError as E:
        try:
            os.system('pip install {}'.format(libname))
            import__ = __import__(libname)
            print(dir(import__))
        except Exception as emain:
            print(emain)
            pass
