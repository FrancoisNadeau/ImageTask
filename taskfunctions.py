# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 19:06:24 2019

@author: Francois
"""
import numpy as np
import os
from os.path import basename as bname
from os.path import dirname as dname
from os.path import join
import pandas as pd
from random import sample
from tqdm import tqdm
from typing import Sequence

def splitall(path):
    allparts = []
    while 1:
        parts = os.path.split(path)
        if parts[0] == path:  # sentinel for absolute paths
            allparts.insert(0, parts[0])
            break
        elif parts[1] == path: # sentinel for relative paths
            allparts.insert(0, parts[1])
            break
        else:
            path = parts[0]
            allparts.insert(0, parts[1])
    return allparts

def inventory(topdir='neuromod_image_bank'):
    dirlist = list(dict.fromkeys(flatten([bname(allpics[0]).split(sep='_')
                                         for allpics in os.walk(os.getcwd())
                                         if os.path.isdir(allpics[0])])))[3:]
    filelist = []
    for allpics in os.walk(os.getcwd()):
        for picture in allpics[2]:
            picpath = join(allpics[0], picture)
            if os.path.isfile(picpath):
                filelist.append(picpath)
    matrix = np.asarray(dirlist)
    matrix2 = np.asarray([flatten([part.split(sep='_')
                          for part in splitall(
                          fpath[fpath.find(topdir)+len(topdir)+1:])])
                          for fpath in filelist])
    matrix3 = np.empty(shape=(len(filelist), len(dirlist)), dtype=bool)
    for tags in enumerate(matrix2):
        for label in enumerate(matrix):
            matrix3[tags[0]][label[0]] = tags[1].__contains__(label[1])
    inventory_df = pd.DataFrame(matrix3,
                                index=[bname(fpath) for fpath in filelist],
                                columns=matrix)
    inventory_df.to_excel(join(os.getcwd(), topdir+'.xlsx'))
    
def flatten(nestedlst):
    """
    Description
    -----------
    Returns unidimensional list from nested list using list comprehension.

    Parameters
    ----------
        nestedlst: list containing other lists etc.

    Variables
    ---------
        bottomElem: type = str
        sublist: type = list

    Return
    ------
        flatlst: unidimensional list
    """
    flatlst = [bottomElem for sublist in nestedlst
               for bottomElem in (flatten(sublist)
               if (isinstance(sublist, Sequence)
               and not isinstance(sublist, str))
               else [sublist])]
    return flatlst

def loadimages(impath):
    '''
    Description
    -----------
    Lists the full relative path of all '.jpeg' files in a directory.

    Parameters
    ----------
    imdir: type = str
        Name of the directory containing the images.

    Return
    ------
    imlist: type = list
        1D list containing all '.jpeg' files' full relative paths
    '''
    imlist = []
    for allimages in os.walk(os.path.abspath(impath)):
        for image in allimages[2]:
            if '.jpg' in image:
                imlist.append(os.path.join(allimages[0], image))
    return imlist

def sampling(lst, nsize, nsamples, exclusives=[]):
    '''
    Description
    -----------
    Draws desired amount of samples of desired size without
    replacement from population.
    Output can be either list or dict.

    Parameters
    ----------
    lst: type=list
        Input list from where population elements are sampled.

    nsize: type=int
        Size of each sample.

    nsamples: type=int
        Number of samples to be drawn from 'lst'

    exclusives: type=list or type=dict
    '''
    samples = list(range(nsamples))#len=16
    inds = sample(range(0, len(lst)), nsize*nsamples)#len = 640
    exclusives = flatten(exclusives)
    for item in range(len(exclusives)):
        if item in flatten(inds) and item in exclusives:
            inds.remove(item)
    samples = [inds[ind:ind+nsize] for ind in range(0, len(inds), nsize)]
    try:
        for exclusive in exclusives:
            error_msg = 'non-exlusive samples'
            shared_items = []
            for item in flatten(samples):
                if item in flatten(exclusive):
                    shared_items.append(item)
        len(shared_items) != 0
        print(error_msg)
    except:
        return samples

def get_answers(rundict):
    '''
    Returns the answers based on keys pressed by subject
    in a list and adds this list as 'Answers' in 'self.rundict'.
    '''
    answerlist = []
    encnames = [rundict['encstims'][stim][0]
                for stim in range(len(rundict['encstims']))]
    encpos = [rundict['encstims'][stim][1]
              for stim in range(len(rundict['encstims']))]
    recnames = [rundict['recstims'][stim][0]
                for stim in range(len(rundict['recstims']))]
    recpos = [rundict['recstims'][stim][1]
              for stim in range(len(rundict['recstims']))]
    for ans in range(len(encnames)):
        if recnames[ans] in encnames:
            if recpos[ans] == encpos[ans]:
                answerlist.append('HIT')
            else:
                answerlist.append('WS')
        elif recnames[ans] not in encnames and recpos[ans] != 'None':
            answerlist.append('FA')
        else:
            answerlist.append('CR')
    rundict.update({'answers':answerlist})

# Can be run after scanning easily to avoid additional computations
#def ams_score(self):
#    '''Calculates the Amnestic Memory Score for a participant'''
#    anslist = self.rundict['Answers']
#    good = anslist.count('recogOKposOK')
#    wrong_source = anslist.count('recogOKposWrong')
#    false_alarm = anslist.count('falseAlarm')
#    denum = (wrong_source + false_alarm)
#    if denum != 0:
#        amscore = good /(wrong_source + false_alarm)
#    else:
#        amscore = good
#    return amscore

#examples
#nsize,nsamples,lst = 80,8,loadimages()
#invalid = sampling(lst,40,8)
#estims = sampling(lst,80,8,exclusives=invalid)
#rstims = [estims[nsample]+invalid[nsample] for nsample in range(len(estims))]
#encstims,recstims = imMatrix(estims),imMatrix(rstims)
