import mpmath as mp
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import random
import math
import time
from libraries.IO import saveData
from libraries.lifeDist import lifeDist, lifeDist2
from scipy.optimize import fsolve


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


def getPoint(maxN=10, type_dist = "loguniform"):

    RStarSample = sample_value(0, 2, type_dist)  # loguniform - uniform - halfgauss - lognormal - fixed

    fPlanets = sample_value(-1, 0, type_dist)  # loguniform - uniform - halfgauss - lognormal - fixed

    nEnvironment = sample_value(-1, 0, type_dist)  # loguniform - uniform - halfgauss - lognormal - fixed

    fIntelligence = sample_value(-3, 0, type_dist)  # loguniform - uniform - halfgauss - lognormal - fixed

    fCivilization = sample_value(-2, 0, type_dist)  # loguniform - uniform - halfgauss - lognormal - fixed

    N = 10**sample_value(0, maxN, type_dist)  # loguniform - uniform - halfgauss - lognormal - fixed

    fLife = float(lifeDist(mean=0, sigma=50))
    fLifeEks = float(mp.log(fLife, 10))

    f = 10**(RStarSample + fPlanets + nEnvironment + fLifeEks + fIntelligence + fCivilization)

    nStars = 10**random.uniform(11, 11.60205999132)

    A = abs(random.gauss(1, 0.2))
    v = abs(random.gauss(0.016 * 300000, 10))*365*24*60*60
    ############################################################################# TODO
    #R = v * random.uniform(0, L)  # radius of inhabited zone, I assume they have been expanding since the became detectable, which is random
    # ok tle ^ not je dejansko tudi L, nisem tega vidu prej... to je treba se nekako vkljucit
    #bom dal V*L/2

    # Tle je enacba more bit 0 na eni strani in vse ostalo na drugi
    #function = lambda L: 1 / nStars * f * A * L * (L * v * (R ** 2 - 2 * L * R * v + 2 * L ^ 2 * v ^ 2 * (1 - mp.e ** (-R / (L * v))))) - N

    B = 0.004 * ((9.461 * 10 ** (-12)) ** 3) # number density of stars as per Wikipedia
    function = lambda L: f * A * L * (B * 10**fPlanets * 10**nEnvironment * 4 * math.pi * (L * v * ((v*L/2) ** 2 - 2 * L * (v*L/2) * v + 2 * L ** 2 * v ** 2 * 0.393469)) + 1) - N
    function1 = lambda L: f * A * (L + 5.13342 * 10**10 * 10** (fPlanets + nEnvironment) * B * L**4) - N
    L_initial_guess = 10 ** 2  # to je se za malo probat
    L_solution, info, ier, mes = fsolve(function1, L_initial_guess, full_output=1)  # numerical solver

    return math.log(L_solution[0], 10), mes


drawnPoints = 0
numHorSec = 48
noIterationsPerMaxN = 10000
logPoints = np.linspace(0, 4, numHorSec)
allPoints = noIterationsPerMaxN * numHorSec

fixed_n = [1, 10, 100, 1000, 10000]

for maxN in logPoints:
    # for maxN in fixed_n:
    array = []
    type_dist = "uniform"
    for i in range(0, noIterationsPerMaxN):
        pointAll = getPoint(maxN, type_dist)
        point = pointAll[0]
        # if abs(point-6)<0.5:
        #     print(pointAll[1])
        if type(point) != type(False):
            array.append(point)

    saveData(array, "inf" + str(maxN))
    print("File: inf" + str(maxN) + ".txt created. no of points:" + str(len(array)))
    drawnPoints = drawnPoints + len(array)
    pointFraction = (drawnPoints * 100) / allPoints
print('done')
print('Drawn points: ' + str(drawnPoints) + '  Which is: ' + str(pointFraction) + '%')
