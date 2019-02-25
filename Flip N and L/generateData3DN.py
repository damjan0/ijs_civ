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


def getPoint(maxN=10):
    RStarSample = random.uniform(0 , 2)
    fPlanets = random.uniform(-1 , 0)
    nEnvironment = random.uniform(-1 , 0)
    fInteligence = random.uniform(-3 , 0)
    fCivilization = random.uniform(-2 , 0)

    N = np.random.uniform(0 , maxN)
    #N= np.random.lognormal(0, maxN)


    fLife = lifeDist(mean=0, sigma=50)
    fLifeEks = float(mp.log(fLife, 10))

    if (fLife==0):
        return getPoint(maxN)
    
    #resitev = RStarSample + fPlanets + nEnvironment + fLifeEks + fInteligence + fCivilization + L
    L = N - (RStarSample + fPlanets + nEnvironment + fLifeEks + fInteligence + fCivilization)

    file.write(str(L)+"\t " + str(fLife) +"\t " + str(fLifeEks) + "\n")
    #file.write(str(L) + "\t  " + str(N) + "\t " +str(RStarSample) + "\t " +str( fPlanets) + "\t " +str( nEnvironment) + "\t " +str( fLifeEks) + "\t " +str( fInteligence) + "\t " +str( fCivilization) + '\n')
    return L

fileName = 'kakec.txt'
file = open(fileName, 'w')

numHorSec = 48
noIterationsPerMaxN = 10000
logPoints = np.linspace(0,10,numHorSec)


for maxN in logPoints:
    array=[]
    for _ in range(0, noIterationsPerMaxN):
        array.append(getPoint(maxN))
    
    saveData(array,"inf"+str(maxN))
    print("File: inf"+str(maxN)+".txt created")

file.close()
print('done')