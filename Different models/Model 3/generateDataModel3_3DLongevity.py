import numpy as np
import mpmath as mp
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import random
import math
import time
from libraries.IO import saveData
from libraries.lifeDist import lifeDist, lifeDist2
from scipy import integrate


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


# Generate a point
def getPoint(maxL=10, type_dist="loguniform"):
    RStarSample = sample_value(0, 2, type_dist)  # loguniform - uniform - halfgauss - lognormal - fixed

    fPlanets = sample_value(-1, 0, type_dist)  # loguniform - uniform - halfgauss - lognormal - fixed

    nEnvironment = sample_value(-1, 0, type_dist)  # loguniform - uniform - halfgauss - lognormal - fixed

    fIntelligence = sample_value(-3, 0, type_dist)  # loguniform - uniform - halfgauss - lognormal - fixed

    fCivilization = sample_value(-2, 0, type_dist)  # loguniform - uniform - halfgauss - lognormal - fixed

    L = sample_value(2, maxL, type_dist)  # loguniform - uniform - halfgauss - lognormal - fixed

    fLife = lifeDist(mean=0, sigma=50)
    fLifeEks = float(mp.log(fLife, 10))
    # fLifeEks = np.random.lognormal(-2 , 0)

    resitev = RStarSample + fPlanets + nEnvironment + fLifeEks + fIntelligence + fCivilization + L  # calculates N

    # threshold if N values are very low
    # if (resitev < 0):
    #    return False

    resitev1 = 10 ** resitev  # rounded de-logarithmised solution

    # for i in range(resitev1):
    # A = abs(random.gauss(1, 0.2))
    A = 1
    v = abs(random.gauss(0.016 * 300000, 10)) * 365 * 24 * 60 * 60
    # L1 = random.uniform(2, maxL)
    L1 = 10 ** L
    B = 0.004 / ((9.461 * 10 ** (12)) ** 3)  # number density of stars as per Wikipedia
    R = v * random.uniform(0,
                           L1)  # radius of inhabited zone, I assume they have been expanding since the became detectable, which is random
    # integral = integrate.quad(lambda r: r ** 2 * math.exp(-(R - r) / (v * 10 ** L1)), 0, R)
    integral = L1 * v * (R ** 2 - 2 * L1 * R * v + 2 * (1 - math.e ** (-R / (L1 * v))) * L1 ** 2 * v ** 2)

    n = B * 10 ** fPlanets * 10 ** nEnvironment * 4 * math.pi * integral

    koncnaResitev0 = A * (n + 1) * resitev1

    if koncnaResitev0 < 0:
        return False, False

    koncnaResitev1 = math.log10(koncnaResitev0)

    # print('n ',n,' integral ',integral,' resitev1', resitev1,'resitev', resitev,' koncnaResitev0 ',koncnaResitev0,' koncnaResitev1 ',koncnaResitev1)

    glajenje = 0.2
    nStars = random.uniform(11, 11.60205999132)
    E3 = nStars + fPlanets + nEnvironment
    E4 = E3 + fLife

    #if koncnaResitev1 < np.random.normal(0, glajenje) or koncnaResitev1 > np.random.normal(4, glajenje):
    '''
    if E4 < np.random.normal(math.log(2, 10), glajenje) \
            or E3 < np.random.normal(math.log(3, 10), glajenje) \
            or koncnaResitev1 < -6 :
            #or koncnaResitev1 > np.random.normal(3.5, glajenje):
        return False, False

    # if koncnaResitev1 < -6 or koncnaResitev1 > np.random.normal(3.5, glajenje):
    #     return False
    if koncnaResitev1 > nStars:
        return False, False
    '''
    return koncnaResitev1, koncnaResitev0/resitev1


# divide Lmax scale
numHorSec = 48  # on how many parts should we devide L - how many different Lmax should we take
noIterationsPerMaxL = 50000  # How many points N per each file/maxL - should be as big as possible  ##trenutno 1000, da jih hitreje generira


logPoints = np.linspace(2, 10, numHorSec)  # divide on numHorSec equal parts a scale from 2 to 10 -

# for each Lmax create a file with points
for maxL in logPoints:
    array = []
    array1 = []
    type_dist = "loguniform"
    for _ in range(0, noIterationsPerMaxL):
        point, nrsettlements = getPoint(maxL, type_dist)
        if type(point) != type(False):
            array.append(point)
            array1.append(nrsettlements)

    saveData(array, "/inf_" + type_dist + "_" + str(maxL))
    #saveData(array1, "/inf_" + type_dist + "_settlements_" + str(maxL))
    print("File: inf_" + type_dist + "_" + str(maxL) + ".txt created")

print('done')
