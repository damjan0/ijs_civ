'''
Created on 9 Aug 2018

@author: benos
'''
from mpmath import mp

def mpLogspace(start,end,size):
    l = mp.linspace(mp.log(start), mp.log(end), size)
    return [mp.exp(x) for x in l]
    