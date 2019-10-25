# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 20:18:29 2019

@author: Francois
"""

import os # Import this one 1st if not already in the directory of the task
import pandas as pd
#import secrets # secrets module prefered to default module "random" Generates cryptographically strong random numbers 
from secrets import choice
from secrets import randbelow as rb
from flatten import flatten
from randInsert import randInsert
from rmDuplicates import rmDuplicates
from shuffleStims import shuffleStims
#from psychopy import logging
#@@@@@@@@@ @@@@@@@@@@ @@@@@@@@@@ @@@@@@@@@@ @@@@@@@@@@ @@@@@@@@@@ @@@
#logging.console.setLevel(logging.INFO)

class cimaqCategs(object):
    """
    Creates list containing a dictionary of stimuli for each trial.
    Dictionary keys: Encoding, Recall
    Values: list of nStim stimuli
    Attribute 'self.trialslist' is compatible with 
    psychopy.data.TrialHandler object
    ...
    
    Attributes (specified by user)
    ------------------------------
    nTrial : int
    
        Integer of nTrial desired trials.
        Each trial contains conditions 'Encoding' and 'Recall'.
    
    nStim : int
    
        Integer of nStim desired image stimuli per condition.
    ...
    
    
    Public Methods
    --------------
    os.walk()
    os.path.abspath()
    os.path.join()
       
    See documentation here: 
    
    os.path()
    https://github.com/FrancoisNadeau/ImageTask/blob/docBranch/os_path_doc.md
    
    os.walk()
    https://github.com/FrancoisNadeau/ImageTask/blob/docBranch/os_walk_doc.md
    ...
    
    Methods
    -------
    filePathlist(maindir = '500_imageDirectory')
        
        lists full image paths in maindir as strings
           
    categCreate(maindir = '500_imageDirectory')
        
        lists images (full paths) returned from filePathlist
        in respective image subdirectory in listdir(maindir)
        
    randImage()
        
        Returns a random image path (type = str) from self.categs
    ...
    
    Imported methods (user-defined)
    -------------------------------
    flatten(nestedList = list)
    
        Returns unidimensional list from nested list
        using list comprehension
        see <help(flatten)> for more details
    
    randInsert(lst,item)
    
        Insert item to random index in lst
        see <help(randInsert)> for more details
        
    """
    @classmethod
    def filePathlist(cls, maindir):
        """
        Lists full image paths in maindir as strings
        ...
        
        Parameters
        ----------
        maindir: type = str
            Name of image directory. 
            Must be in current working directory
        ...
        
        Return
        ------
        filePathlist: type = list
            List of all image fullpaths in a subcategory 
            (last one by default) in maindir. Meant to be called
            by 'categCreate()'.
        """
        for maindir, dirnames,filenames in os.walk(os.path.abspath(maindir)):
            filePathlist = [os.path.join(maindir,filename)
                           for filename in filenames 
                           if '.jpg' in filename]               
            return (sorted(filePathlist))

    @classmethod     
    def categCreate(cls,maindir):
        """
        Allows to create a single Category object
        ...
        
        Parameters
        ----------
        maindir: type = str
            Name of image directory. 
            Must be in current working directory
            Will be passed to 'filePathlist()'
        ...
        
        Return
        ------
        imMatrix: type = tuple
            Tuple containing all image paths for all subcategories
            (subdirectories) in maindir.
            Can be called alone (if only a specific image directory
            is to be used)
            Otherwise meant to be called in 'self.categs'
            to list all image categories in current working
            directory.
        """
        imMatrix = [cls.filePathlist(os.path.join(maindir,dirname))
        for dirname in os.listdir(maindir)]
        return tuple(imMatrix)
    
#    def getRecStims(self):
#        recStims = []
#        for trial in range(self.nTrial-1):
#            for dist in range(self.nStim//2):
#                newlist = randInsert(self.EncStims[trial],
#                                     self.Distractors[trial][dist])
#            recStims[trial].append(newlist)
#        return recStims

    def getEncStims(self):
        for trial in range(self.nTrial):
            GS = self.graySquare
            insF = len(self.EStims[trial])//2
            ctrlStimlist = [GS]*insF
            CSCount = range(len(ctrlStimlist))
            EStims = self.EStims[trial]
            tempES = flatten([randInsert(EStims,ctrlStimlist[rInd])
                             for rInd in CSCount])
            encStims = rmDuplicates(tempES,exception=GS)
            return encStims
#lst1 = ['a','b','v','t','y','w']
#lst2 = ['e','g','r','i','o','q']
#gs = 'graysquare'
#
#newlist = [randInsert(lst1,gs) for insF in range(2)]
#insF = len(lst1)//2
#randInd = 
#nlst = [randInsert(lst1,gs) for freq in range(3)]
#nlst = [randInsert(lst1,gs)*3]
#
#nlst2 = rmDuplicates(nlst,gs)       
#nlst = list(dict.fromkeys(nlst))
            
#TODO:     def getRecStims(self):
#        for trial in range(self.nTrial):
#            EStims = self.EStims[trial]
#            DStims = self.Distractors[trial]
##            DSCount = range(len(self.Distractors))
#            for elem in DStims :
#                EStims.insert(rb(len(EStims)), elem)
##            tempRS = flatten([randInsert(EStims,DStims[dist])
##                               for dist in DSCount])
##            RStims = rmDuplicates(tempRS)
#                return EStims
        
    def randImage(self):
        """
        Returns a random image path (type = str) from self.categs
        Used to select stimuli for the task
        ...
        
        Variables
        ----------
        randCateg: type = int
            Index of random image category in 'self.categs'
        
        randSubcat: type = int
            Index of random image subcategory in 'self.categs[randCateg]'
        ...
        
        Return
        ------
        randIm: type = str
            Randomly selected image path (string) from 'self.categs'
        """
        randCateg = rb(len(self.categs)-1)
        randSubcat = rb(len(self.categs[randCateg])-1)
        randIm = choice(self.categs[randCateg][randSubcat])
        return randIm
    
    def __init__(self,nTrial,nStim):
        """
        Parameters
        ----------
        nTrial: Specified number of trials
        
        nStim: Specified number of stimuli per condition 
        
        graySquare : str
        
        Path of control stimuli used in Encoding condition.
        A simple 500x500p gray square
        
        categs : list
        
            List containing all pre-processed image categories found
            in current working directory.
            
        Encod : list
        
            List of nStim image paths (str) randomly selected from
            'self.categs'. Will be used in Encoding condition.
            
        EnStims : list
        
            List of image paths from 'self.Encod' and
            'self.graySquare' (inserted at random index).
            <len(self.EnStim)> = <len(self.Encod)+1>
              
        Targs : list
        
            List of target images for each trial's Recall condition.
            Target images are randomly selected from 'self.Encod'.
            
        Distractors : list
        
            List of nStim image paths (str) randomly selected from
            'self.categs', provided they have not already been selected
            in 'self.Encod' (all new images). 
            Will be used in Recall condition.
            
        recStims : list
        
            List of image paths from 'self.Distractors' and
            'self.Targs' (inserted at random index). Each target image
            is inserted in its respective trial's Recall condition
            stimuli list.
            <len(self.EnStim)> = <len(self.Encod)+1>
        
        imDF = pd.DataFrame object
        
            Dataframe of all stimuli for each condition for each trial.
            Row = trial (number of rows = 'self.nTrial')
            Column = conditions 
                col[0] = 'Encoding' (contains items in 'self.EnStims'
                col[1] = 'Recall' (contains items in 'self.recStims')
            
        trialslist : list
        
            List of each row (trial) in 'self.imDF' as dictionary.
            In each trial dictionary:
                keys = 'Encoding': values = items in 'self.Enstim'
                       'Recall': values = items in 'self.recStims'
            Compatible with psychopy.data.TrialHandler object
        """
           
        self.nTrial = nTrial #type = int: num desired trials
        self.nStim = nStim #type = int: n desired stim per condition
        self.graySquare = os.path.abspath('gs_318364508_17317b9b36_o.jpg')
        self.categs = [cimaqCategs.categCreate(maindir) 
                      for maindir in os.listdir(os.getcwd()) 
                      if maindir.startswith('500_')]
        
        self.EStims = [[self.randImage() for stim in range(self.nStim)]
                      for trial in range(self.nTrial)]
        
        self.Distractors = [[self.randImage() for stim in range(self.nStim//2) 
                           if stim not in flatten(self.EStims)]
                           for trial in range(self.nTrial)]
        
        self.encStims = self.getEncStims()
        
#TODO:        self.recStims = self.getRecStims()
#        

        


#
#nlist = flatten([randInsert(lst1,lst2[item])
#                for item in range(len(lst2))])
#outlist = rmDuplicates(nlist)        
#lst1 = ['a','b','c','d']
#lst2 = ['e','f']

#categs = Categories(2,6)
#encstims = categs.getEncStims()



#        self.Targs = [choice(self.Encod[trial]) 
#                     for trial in range(self.nTrial)]
#        

        
        
#        self.recStims = flatten([self.EncStims,self.Distractors])
        
        def getEncStims(self):
            for trial in range(self.nTrial):
                ctrlStims = [self.graySquare]*int(self.nStim/2)
                for  ctrlStim in range(len(ctrlStims)):
                    self.EStims[trial].insert(rb(len(self.EStims[trial])+1),
                                                         ctrlStim)
        
        def random_insert_seq(lst, seq):
            insert_locations = sample(xrange(len(lst) + len(seq)), len(seq))
            inserts = dict(zip(insert_locations, seq))
            input = iter(lst)
            lst[:] = [inserts[pos] if pos in inserts else next(input)
                     for pos in xrange(len(lst) + len(seq))]
#        self.recStims = self.getRecStims()
        

#        self.recStims = [randInsert(self.Distractors[trial],
#                                        self.Targs[trial])
#                        for trial in range(self.nTrial)]
#
#        self.encDF = pd.DataFrame(self.encStims)
#        
#        self.recDF = pd.DataFrame(self.recStims)

#Usage examples:
categs = cimaqCategs(2,6)
encstims = categs.encStims
encstims2 = cimaqCategs(2,6).encStims
#recstims = categs.recStims
#distractors = categs.Distractors
#EDF = categs.encDF
#RDF = categs.recDF
#

#test = [randInsert(lst1,lst2[item])
#       for item in range(len(lst2))]
#    test = randInsert(lst1,lst2[item])

    