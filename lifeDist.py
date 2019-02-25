'''
Created on 7 Aug 2018

@author: benos
'''
import random
import numpy as np
import matplotlib.pyplot as plt
import math
from mpmath import mpmathify,mp,mpf
from logHistogramAdd import logHistogramAdd

'''
Sandberg: We used a lognormal distribution for the life emergence 
rate (log lambda ~ N(0,50)) and then transformed it into a probability 
as fLife = 1-exp(-lambda).
'''
def lifeDist(mean=0, sigma=50):
    lambdaa = np.random.lognormal(mean, sigma)
    lambdaa *= (-1)
    vmesniResult = math.exp(lambdaa)
    result = 1-vmesniResult
    if (result==0):         #can't be 0 because we exist and math no work after
        return lifeDist(mean, sigma)
    else:
        return result

#everything below is not important
def lifeDistSave(vMin=-35,vMax=15,tMin=7,tMax=10,mean=1, sigma=50):
    #mp.dps = 230
    val = mpf('1')
    #r = np.random.lognormal(1,50)
    r = np.random.lognormal(-50, 50)
    r = 10**r
    v=10**sampleU(-35,15)
    t=10**sampleU(7, 10)
    #t=1
    #v=1

    val *= r        #lambda
    val *= v        #v
    val *= t        #t

    #val=np.random.normal(0,50)
    #val = 10**val

    val = 0-val
    expo = mp.exp(val)
    val = mpf('1') - expo
    #mp.dps=15
    return float(val)

def sample(dist):
    r = random.uniform(mp.log(dist[0]), mp.log(dist[1]))
    return mp.exp(r)

def sampleU(dist0, dist1):
    return random.uniform(dist0, dist1)


def lifeDist2(vMin=-35,vMax=15,tMin=14,tMax=17,lambMin = -188 , lambMax = 15 ):
    V = (mpmathify(10 ** (vMin)), mpmathify(10 ** (vMax)))
    t = (mpmathify(10 ** (tMin)), mpmathify(10 ** (tMax)))
    lamb = (mpmathify(10 ** ( lambMin )), mpmathify(10 ** lambMax))
    mp.dps = 230

    val = mpf('1')
    val *= sample( lamb )
    val *= sample(V)
    val *= sample(t)
    val = 0-val
    expo = mp.exp(val)
    val = mpf('1') - expo
    mp.dps = 15
    return val
