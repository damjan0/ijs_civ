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


# Generate a point
def getPoint(maxL=10):
    RStarSample = random.uniform(0, 2)  # logaritmic
    fPlanets = random.uniform(-1, 0)
    nEnvironment = random.uniform(-1, 0)
    fIntelligence = random.uniform(-3, 0)
    fCivilization = random.uniform(-2, 0)

    # L = np.random.uniform(2 , maxL)                         #loguniform

    # median = (maxL - 2) / 2 + 2  # polovica intervala
    # sigma = (median - 2) / 3  # tako, da je 3sigma cez cel obseg
    # L = np.random.normal(median, sigma)  # lognormal

    # L = math.log10(np.random.uniform(10 ** 2, 10 ** maxL))  # uniform

    sigmaHalfGauss = (10 ** maxL - 10 ** 2) / 6 # interval/2 je polovic in se /3 je tako da bo 3sigma cez cel interval
    L = np.log10(np.abs(np.random.normal(0, sigmaHalfGauss)) + 10 ** 2)

    # fLife = random.uniform(-2 , 0)
    # fLifeEks = fLife
    nStars = random.uniform(11, 11.60205999132)

    fLife = lifeDist(mean=0, sigma=50)
    fLifeEks = float(mp.log(fLife, 10))

    E3 = nStars + fPlanets + nEnvironment
    E4 = E3 + fLife
    E5 = E4 + fIntelligence

    resitev = RStarSample + fPlanets + nEnvironment + fLifeEks + fIntelligence + fCivilization + L  # calculates N

    # thresholds
    if (resitev < 0) or E4 < math.log(2, 10) or E3 < math.log(3, 10) or resitev > 5:
        # return getPoint(maxL)
        return False

    return resitev


# divide Lmax scale
numHorSec = 48  # on how many parts should we divide L - how many different Lmax should we take
noIterationsPerMaxL = 30000  # How many points N per each file/maxL - should be as big as possible  ##trenutno 1000, da jih hitreje generira
logPoints = np.linspace(2, 10, numHorSec)  # devide on numHorSec equal parts a scale from 2 to 10 -

# for each Lmax create a file with points
for maxL in logPoints:
    array = []
    for _ in range(0, noIterationsPerMaxL):
        point = getPoint(maxL)
        if type(point) != type(False):
            array.append(point)

    saveData(array, "/inf" + str(maxL))
    print("File: inf" + str(maxL) + ".txt created. Size: " + str(len(array)))

print('done')
