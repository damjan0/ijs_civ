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


# Generate a point
def getPoint(maxL=10):
    RStarSample = random.uniform(0, 2)  # logaritmic
    fPlanets = random.uniform(-1, 0)
    nEnvironment = random.uniform(-1, 0)
    fInteligence = random.uniform(-3, 0)
    fCivilization = random.uniform(-2, 0)
    L = random.uniform(2, maxL)
    # fLife = random.uniform(-2 , 0)
    # fLifeEks = fLife

    fLife = lifeDist(mean=0, sigma=50)
    fLifeEks = float(mp.log(fLife, 10))
    # fLifeEks = np.random.lognormal(-2 , 0)

    resitev = RStarSample + fPlanets + nEnvironment + fLifeEks + fInteligence + fCivilization + L  # calculates N

    # threshold if N values are very low
    #if (resitev < 0):
    #    return False

    resitev1 = int(round(10 ** resitev))  # rounded de-logarithmised solution

    koncnaResitev = 0

    # for i in range(resitev1):
    A = random.gauss(1, 0.5)
    v = random.gauss(0.016 * 300000, 2000)
    # L1 = random.uniform(2, maxL)
    L1 = L
    B = 0.004 * ((9.461 * 10 ** (-12)) ** 3)  # number density of stars as per Wikipedia
    R = v * random.uniform(0,
                           L)  # radius of inhabited zone, I assume they have been expanding since the became detectable, which is random
    #integral = integrate.quad(lambda r: r ** 2 * math.exp(-(R - r) / (v * 10 ** L1)), 0, R)
    integral = L1*v*(R**2 - 2*L1*R*v + 2*(1- math.e**(-R/(L1*v)))*L1**2*v**2)

    n = B * fPlanets * nEnvironment * 4 * math.pi * integral

    koncnaResitev = A * (n + 1) * resitev1

    return koncnaResitev


# devide Lmax scale
numHorSec = 48  # on how many parts should we devide L - how many different Lmax should we take
noIterationsPerMaxL = 30000  # How many points N per each file/maxL - should be as big as possible  ##trenutno 1000, da jih hitrej generira
logPoints = np.linspace(2, 10, numHorSec)  # devide on numHorSec equal parts a scale from 2 to 10 -

# for each Lmax create a file with points
for maxL in logPoints:
    array = []
    for _ in range(0, noIterationsPerMaxL):
        point = getPoint(maxL)
        if type(point) != type(False):
            array.append(point)

    saveData(array, "/inf" + str(maxL))
    print("File: inf" + str(maxL) + ".txt created")

print('done')
