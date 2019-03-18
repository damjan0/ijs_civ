import mpmath as mp
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import random
import math
import time
from IO import saveData
from lifeDist import lifeDist, lifeDist2


# Bokal update


def getPoint(maxN=10):
    RStarSample = random.uniform(0, 2)
    fPlanets = random.uniform(-1, 0)
    nEnvironment = random.uniform(-1, 0)
    fIntelligence = random.uniform(-3, 0)
    fCivilization = random.uniform(-2, 0)

    nStars = random.uniform(11, 11.60205999132)

    N = maxN
    #N = np.random.uniform(0, maxN)
    # N = np.random.lognormal(0, maxN)
    # N = np.random.normal(0, maxN)

    fLife = lifeDist(mean=0, sigma=50)
    fLifeEks = float(mp.log(fLife, 10))

    E3 = nStars + fPlanets + nEnvironment
    E4 = E3 + fLife
    E5 = E4 + fIntelligence

    # resitev = RStarSample + fPlanets + nEnvironment + fLifeEks + fIntelligence + fCivilization + L
    L = np.log10(N) - (RStarSample + fPlanets + nEnvironment + fLifeEks + fIntelligence + fCivilization)

    # thresholds
    if (L < 2) or E4 < math.log(2, 10) or E3 < math.log(3,
                                                        10) or L > 10.139879:  # maxL - age of the universe - if we are taking drake equation for this moment
        return getPoint(maxN)

    # file.write(str(L)+"\t " + str(fLife) +"\t " + str(fLifeEks) + "\n")
    # file.write(str(L) + "\t  " + str(N) + "\t " +str(RStarSample) + "\t " +str( fPlanets) + "\t " +str( nEnvironment) + "\t " +str( fLifeEks) + "\t " +str( fIntelligence) + "\t " +str( fCivilization) + '\n')
    return L


# fileName = 'kakec.txt'
# file = open(fileName, 'w')

numHorSec = 48
noIterationsPerMaxN = 75000
# logPoints = np.linspace(0,7,numHorSec)
linPoints = range(1, 11)

for maxN in linPoints:
    array = []
    for _ in range(0, noIterationsPerMaxN):
        array.append(getPoint(maxN))

    saveData(array, "linN/lin" + str(maxN))
    print("File: linN/lin" + str(maxN) + ".txt created")

# file.close()
print('done')
