import numpy as np
import mpmath as mp
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import random
import math
import time
from IO import saveData
from lifeDist import lifeDist, lifeDist2

'''''
Model 2: https://arxiv.org/ftp/arxiv/papers/1510/1510.08837.pdf
Using Sandberg distribution

Model 2 opposite to original Drake equation (calculates how many int.civs are out there now), this model caluclates how many int.civs. were ever out there
/to do so.. it does not use L variable and uses total no. of stars in the universe instead of the rate at which the stars are apperaing
/for less known parameters: biotechnicalProbability, the paper calculates minimal threshold and uses different values for that. We use Sandberg
'''''
#Generate a point
def getPoint(maxL=10):
    RStarSample = random.uniform(0 , 2) #logaritmic
    Nstar = 22.30103      #total number of stars. Paper persumes there are 2*10^22 oz. 22.30103  in our observable universe - only for our galaxy 3*10^11 oz. 11,4771212547
    fPlanets = random.uniform(-1 , 0)   #paper suggests 1           np.random.normal(1)
    nEnvironment = random.uniform(-1 , 0)    #paper suggests 0.2    np.random.normal(0.2)

    fInteligence = random.uniform(-3 , 0)
    fCivilization = random.uniform(-2 , 0)      #in the paper it is mentioned as ft
    fLife = lifeDist(mean=0, sigma=50)
    fLifeEks = float(mp.log(fLife, 10))

    L = random.uniform(2, maxL)

    #biotechnicalProbability  - lower bound calcuclated to be 2.5*10^-24   aka -23.60206 - only for our galaxy 	1.7*10^-11 aka -10.76955

    astrophysicsProbability = RStarSample + fPlanets + nEnvironment         #use Nstar instead of rstarsample if no L
    #biotechnicalProbability = fInteligence + fCivilization + fLifeEks
    biotechnicalProbability = random.uniform(-23.602060, 0)

    #resitev = astrophysicsProbability + biotechnicalProbability   #calculates A = number of civ that have ever apperared in the world
    resitev = astrophysicsProbability + biotechnicalProbability + L  # calculates A = number of civ that have ever apperared in the world

    #threshold if N values are very low
    if (resitev<0):
        return getPoint(maxL)

    return resitev

#devide Lmax scale
numHorSec = 48  #on how many parts should we devide L - how many different Lmax should we take
noIterationsPerMaxL = 50000     #How many points N per each file/maxL - should be as big as possible  ##trenutno 1000, da jih hitrej generira
logPoints = np.linspace(2,10,numHorSec) #devide on numHorSec equal parts a scale from 2 to 10 -

#for each Lmax create a file with points
for maxL in logPoints:
    array=[]
    for _ in range(0, noIterationsPerMaxL):
        array.append(getPoint(maxL))

    saveData(array,"/inf"+str(maxL))
    print("File: inf"+str(maxL)+".txt created")


print('done')