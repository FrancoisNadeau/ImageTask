# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 12:58:45 2019

@author: Francois
"""
from PIL import Image
import glob
import pandas as pd
import os
#from tqdm import tqdm
def findRef(cat_path,extension='.jpg'):
    cwd = os.getcwd()
    subDirs = [os.path.join(cat_path,dirname) 
              for dirname in os.listdir(cat_path)]
    fPaths = [[os.path.join(subDir,filename)
             for filename in os.listdir(subDir)]
             for subDir in subDirs.__iter__()]
    sources = pd.read_csv(cwd + '\\' + 'sources.csv')
    references = sources['reference'].tolist()

    databankNames = []
    websiteNames = []
    refsFound = []
    for subcat in fPaths.__iter__():
        for imPath in subcat.__iter__():
            for ref in references:
                if ref in imPath:
                    return substring
#            ref = next(reference for reference in references if reference in imPath)
#            refsFound.append(ref)
#            return refsFound
            
#        for imPath in fPath.__iter__():
#            longpath, extension = os.path.splitext(imPath)
##            match = (ref for ref in references.__iter__() if ref in longpath)
##            a = any(ref in longpath for ref in references)
##            while a:
##                print(ref)
##            else:
#            count = 0
#            ref = (ref for ref in references)
#            if ref not in longpath:
#                next(ref)
#            else:
#                    
#                if ref not in longpath:
#                    count+=1
#                else:
#                    databankName = longpath[:longpath.index(ref)]+extension
#                    websiteNames.append(longpath)
#                    databankNames.append(databankName)
#
##                if ref not in longpath:
##                    next(references.__iter__())
##                    databankNamesDF = pd.DataFrame(databankNames)
##                    websiteNamesDF = pd.DataFrame(websiteNames)
#    return fPaths
tryinghard = findRef('bathroom')

for ref in references.__iter__():
    print(ref)
testRef = findRef('testItem01_pxh_randomLongNameFromWebsite')
#print(testRef)
def square_resize(maindir,image_size=(500,500),extension='.jpg'):
    cwd = os.getcwd()
    sources = pd.read_csv(cwd + '\\' + 'sources.csv')
    references = sources['reference'].tolist()
    
#for Mac/Linux users, replace '\\' by '/'  
    cat_path = cwd +'\\'+ maindir
#    dirnames = os.listdir(cat_path)
    subDirs = [os.path.join(cat_path,dirname) 
              for dirname in os.listdir(cat_path)]
    fPaths = [[os.path.join(subDir,filename)
             for filename in os.listdir(subDir)]
             for subDir in subDirs.__iter__()]
    websiteNames = []
    databankNames = []
    for pathlist in fPaths.__iter__():
        for fpath in pathlist:
            pre, ext = os.path.splitext(fpath)
            if ext != extension:
                os.rename(fpath, pre + extension)
            
#            databankNames.append(shortpath)
#                    longpathslist.append()
#                    os.rename(fpath,shortpath)
#                    im = Image.open(shortpath)
#                    width, height = im.size
#                    if width > height:
#                        im = im.crop(((width-height)/2,0,(width+height)/2,height))
#                    elif width < height:
#                        im = im.crop((0,(height-width)/2,width,(height+width)/2))
#                    imResized = im.resize(image_size, Image.ANTIALIAS)
#    
#            new_category_path = os.path.join(cwd, '500_' + maindir)
#            os.system("mkdir {}".format(new_category_path))
#
#            new_subcat_path = os.path.join(new_category_path, "500_"+subcat_name)
#            os.system("mkdir {}".format(new_subcat_path))
#            imResized.save(os.path.join(new_subcat_path, "500_"+im_name), 'JPEG', quality = 90)
#    webNamesDF = pd.DataFrame(websiteNames)
#    webNamesDF.to_csv(os.getcwd()+'\\'+ maindir + '_websiteNames')
#    databankNamesDF.to_csv(os.getcwd()+'\\'+ maindir + '_databankNames')
            
#            for ref in references:
#                if ref in longpath:
#                    refInd = longpath.find(ref)
#                    shortpath = longpath[:refInd]+ext 
#                    shortpathlist.append(shortpath)
                
                
            
#    images = [f for f in glob.glob(cat_path +  "**/**/**/*.jpg", recursive=True)]
#    for im_path in tqdm(images):
#        subcat_path, im_name = os.path.split(im_path)
#        subcat_name = os.path.basename(subcat_path)
def findref():
    cwd = os.getcwd()
    sources = pd.read_csv(cwd + '\\' + 'sources.csv')
    references = sources['reference'].tolist()

    testname = 'testItem01_pxh_randomLongNameFromWebsite'
    refgen = (references[refer] for refer in range(len(references)))
    if ref in testname:
        return ref
findref()
shortPaths = square_resize('bathroom',extension='.jpg')
for ref in references.__iter__():
    if ref in 