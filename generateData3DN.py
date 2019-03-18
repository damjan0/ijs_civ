import mpmath as mp
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import random
import math
import time
from libraries.IO import saveData
from libraries.lifeDist import lifeDist, lifeDist2


def getPoint(maxN=10):
    RStarSample = random.uniform(0 , 2)
    fPlanets = random.uniform(-1 , 0)
    nEnvironment = random.uniform(-1 , 0)
    fInteligence = random.uniform(-3 , 0)
    fCivilization = random.uniform(-2 , 0)

    nStars = random.uniform(11, 11.60205999132)

    #N = np.random.uniform(0 , maxN)                         #loguniform
    #N = np.random.normal(0, maxN)                          #lognormal
    N = math.log10(np.random.uniform(10**0 , 10**maxN))    #uniform
    #N = math.log10(np.random.normal(10**0, 10**maxN))      #normal
    #...    #gauss

    fLife = lifeDist(mean=0, sigma=50)
    fLifeEks = float(mp.log(fLife, 10))

    E3 = nStars + fPlanets + nEnvironment
    E4 = E3 + fLife
    E5 = E4 + fInteligence
    
    #resitev = RStarSample + fPlanets + nEnvironment + fLifeEks + fInteligence + fCivilization + L
    L = N - (RStarSample + fPlanets + nEnvironment + fLifeEks + fInteligence + fCivilization)

    # thresholds
    if (L < 2) or E4 < math.log(2, 10) or E3 < math.log(3, 10) or L > 10.139879:       #maxL - age of the universe - if we are taking drake equation for this moment
        return getPoint(maxN)

    return L


numHorSec = 48
noIterationsPerMaxN = 30000
logPoints = np.linspace(0,7,numHorSec)

for maxN in logPoints:
    array=[]
    for _ in range(0, noIterationsPerMaxN):
        array.append(getPoint(maxN))
    
    saveData(array,"inf"+str(maxN))
    print("File: inf"+str(maxN)+".txt created")

print('done')