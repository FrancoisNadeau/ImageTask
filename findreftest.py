# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 02:21:01 2019

@author: Francois
"""

import os
import pandas as pd
from flatten import flatten
def refFinder(cat_path):
    cwd = os.getcwd()
    subDirs = [os.path.join(cat_path,dirname) 
              for dirname in os.listdir(cat_path)]
    fPaths = flatten([[os.path.abspath(os.path.join(subDir,filename))
             for filename in os.listdir(subDir)]
             for subDir in subDirs.__iter__()])
    sources = pd.read_csv(cwd + '\\' + 'sources.csv')
    references = sources['reference'].tolist()
    shortpathlist = []
    for imName in fPaths.__iter__():
        for ref in references.__iter__():
            refInd = imName.find(ref)
            if refInd != -1:
                longpath, ext = os.path.splitext(imName)
                shortpath = longpath[:longpath.find(ref)]+ext
                shortpathlist.append(shortpath+ext,imName)
    return(shortpathlist,fPaths)
