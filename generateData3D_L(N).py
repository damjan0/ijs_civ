import mpmath as mp
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import random
import math
import time
from libraries.IO import saveData
from libraries.lifeDist import lifeDist, lifeDist2


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


def getPoint(maxN=10):
    type_dist = "loguniform"

    RStarSample = sample_value(0, 2, type_dist)  # loguniform - uniform - halfgauss - lognormal - fixed

    fPlanets = sample_value(-1, 0, type_dist)  # loguniform - uniform - halfgauss - lognormal - fixed

    nEnvironment = sample_value(-1, 0, type_dist)  # loguniform - uniform - halfgauss - lognormal - fixed

    fIntelligence = sample_value(-3, 0, type_dist)  # loguniform - uniform - halfgauss - lognormal - fixed

    fCivilization = sample_value(-2, 0, type_dist)  # loguniform - uniform - halfgauss - lognormal - fixed

    N = sample_value(0, maxN, type_dist)  # loguniform - uniform - halfgauss - lognormal - fixed

    fLife = lifeDist(mean=0, sigma=50)
    fLifeEks = float(mp.log(fLife, 10))

    nStars = random.uniform(11, 11.60205999132)
    E3 = nStars + fPlanets + nEnvironment
    E4 = E3 + fLife
    E5 = E4 + fIntelligence

    # resitev = RStarSample + fPlanets + nEnvironment + fLifeEks + fInteligence + fCivilization + L
    L = N - (RStarSample + fPlanets + nEnvironment + fLifeEks + fIntelligence + fCivilization)

    glajenje = 0.4

    # thresholds
    # if (L < np.random.normal(0, glajenje)

    if  (E4 < np.random.normal(math.log(2, 10), glajenje)
            or E3 < np.random.normal(math.log(3, 10), glajenje)
            or L > np.random.normal(10.139879, glajenje)):  # maxL - age of the universe - if we are taking drake equation for this moment
        # return getPoint(maxN)
        return False

    return L


drawnPoints = 0
numHorSec = 48
noIterationsPerMaxN = 1000
#logPoints = np.linspace(-10, 4, numHorSec)
logPoints = np.linspace(0, 4, numHorSec)
allPoints = noIterationsPerMaxN * numHorSec

fixed_n = [1, 10, 100, 1000, 10000]

for maxN in logPoints:
    # for maxN in fixed_n:
    array = []
    for _ in range(0, noIterationsPerMaxN):
        point = getPoint(maxN)
        if type(point) != type(False):
            array.append(point)

    saveData(array, "inf_l_" + str(maxN))
    print("File: inf_l_" + str(maxN) + ".txt created. no of points:" + str(len(array)))
    drawnPoints = drawnPoints + len(array)
    pointFraction = (drawnPoints * 100) / allPoints
print('done')
print('Drawn points: ' + str(drawnPoints) + '  Which is: ' + str(pointFraction) + '%')
