import numpy as np
import mpmath as mp
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import random
import math
import time
#from libraries.IO import saveData
#from libraries.lifeDist import lifeDist, lifeDist2

def saveData(data,filename):
    file = open('data/'+filename+'.txt', 'w')
    for i in range(0,len(data)):
        file.write(str(data[i])+'\n')
    file.close()

def lifeDist(mean=0, sigma=50):
    lambdaa = np.random.lognormal(mean, sigma)
    lambdaa *= (-1)
    vmesniResult = math.exp(lambdaa)
    result = 1-vmesniResult
    if (result==0):         #can't be 0 because we exist and math no work after
        return lifeDist(mean, sigma)
    else:
        return result

def sample_value(fromv, tov, dist="fixed"):
    if dist == "loguniform":
        return random.uniform(fromv, tov)
    elif dist == "uniform":
        return math.log10(np.random.uniform(10 ** fromv, 10 ** tov))
    elif dist == "halfgauss":
        sigmaHalfGauss = (
                                 10 ** tov - 10 ** fromv) / 3  # /3 je tako da bo 3sigma cez cel interval
        return np.log10(np.abs(np.random.normal(0, sigmaHalfGauss)) + 10 ** fromv)  # gauss
    elif dist == "lognormal":
        median = (tov - fromv) / 2 + tov  # polovica intervala
        sigma = (median - tov) / 3  # tako, da je 3sigma cez cel obseg
        return np.random.normal(median, sigma)  # lognormal
    return tov


def getPoint(maxL=10):
    type_dist = "loguniform"

    RStarSample = sample_value(0, 2, type_dist)  # loguniform - uniform - halfgauss - lognormal - fixed

    fPlanets = sample_value(-1, 0, type_dist)  # loguniform - uniform - halfgauss - lognormal - fixed

    nEnvironment = sample_value(-1, 0, type_dist)  # loguniform - uniform - halfgauss - lognormal - fixed

    fIntelligence = sample_value(-3, 0, type_dist)  # loguniform - uniform - halfgauss - lognormal - fixed

    fCivilization = sample_value(-2, 0, type_dist)  # loguniform - uniform - halfgauss - lognormal - fixed

    L = sample_value(2, maxL, type_dist)  # loguniform - uniform - halfgauss - lognormal - fixed

    fLife = lifeDist(mean=0, sigma=50)
    fLifeEks = float(mp.log(fLife, 10))

    nStars = random.uniform(11, 11.60205999132)
    E3 = nStars + fPlanets + nEnvironment
    E4 = E3 + fLife
    E5 = E4 + fIntelligence

    resitev = RStarSample + fPlanets + nEnvironment + fLifeEks + fIntelligence + fCivilization + L  # calculates N

    # thresholds
    # rand_tresh = 4
    # if random.random()<0.5:
    rand_tresh = 3
    glajenje = 0.2

    if (E4 < np.random.normal(math.log(2, 10), glajenje) \
            or E3 < np.random.normal(math.log(3, 10), glajenje)
            or resitev > np.random.normal(3.5, glajenje)):
        # return getPoint(maxL)
        return False

    return resitev


# divide Lmax scale
drawnPoints = 0
numHorSec = 48  # on how many parts should we divide L - how many different Lmax should we take
noIterationsPerMaxL = 100000  # How many points N per each file/maxL - should be as big as possible  ##trenutno 1000, da jih hitreje generira
logPoints = np.linspace(2, 10, numHorSec)  # devide on numHorSec equal parts a scale from 2 to 10 -
allPoints = noIterationsPerMaxL * numHorSec

# for each Lmax create a file with points
for maxL in logPoints:
    array = []
    for _ in range(0, noIterationsPerMaxL):
        point = getPoint(maxL)
        if type(point) != type(False):
            array.append(point)

    saveData(array, "/inf" + str(maxL))
    print("File: inf" + str(maxL) + ".txt created. Size: " + str(len(array)))
drawnPoints = drawnPoints + len(array)
pointFraction = (drawnPoints * 100) / allPoints
print('done')
print('Drawn points: ' + str(drawnPoints) + '  Which is: ' + str(pointFraction) + '%')
