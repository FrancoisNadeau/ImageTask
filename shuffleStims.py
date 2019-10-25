# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 15:56:26 2019

@author: Francois
"""
from secrets import choice

def shuffleStims(lst1,lst2, exception=None):
#    gs = 'graysquare'
    if exception != None:
        nlst = []
        templst = lst1.__add__(lst2)
        for stimCount in range(len(templst)):
            stim = choice(templst)
            if stim != exception and stim not in nlst:
                nlst.append(stim)
            elif stim == exception:
                nlst.append(stim)
            elif stim != exception and stim in nlst:
                pass
        return nlst
lst1 = ['a','b','c','d','e','f']
lst2 = ['g','h','i','j','k','l']
ctrlstims = ['GS']*int(len(lst1)/2)
testlst = shuffleStims(lst1,lst2)
testlst2 = shuffleStims(lst1,ctrlstims)
totallst = lst1.__add__(lst2)
stim = choice(totallst)
stim = stim