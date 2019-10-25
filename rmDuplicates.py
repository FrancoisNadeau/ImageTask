# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 10:04:49 2019

@author: Francois
"""

def rmDuplicates(lst,exception=None):
    """
        Removes all duplicate values from 'lst', but keeps all
        occurences of 'exception'. Used to insert control stimlulus
        (gray square) at random indexes 'self.EncStims'.
        ...
        
        Parameters
        ----------
        lst: tupe = list
            List in which duplicate elements will be suppressed
            (except for 'exception').
            
        exception: type = any value a list can deal with
            Element in 'lst' to be exempted from suppression of
            duplicates.
            
        Variables
        ----------
        elem: type = any value a list can deal with
            Element contained in 
        
        uniqueList: type = list
            Empty list in which elements ('elem') from 'lst'
            will be appended if not already in 'uniqueList'.
        ...
        
        Return
        ------
        uniqueList: type = str
            List containing a single occurence of each 'elem' in 'lst',
            except for 'exception', which will occur as often as in 'lst'.
    """
    defaultException = 'nothing'
    uniqueList = []
    if exception is None:
        exception = defaultException
    for elem in lst:
        if elem == exception:
            uniqueList.append(exception)
        if elem not in uniqueList:
            uniqueList.append(elem)       
    return uniqueList
