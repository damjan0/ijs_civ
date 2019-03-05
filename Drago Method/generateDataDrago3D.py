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

#Generate a point
def getPoint(maxL=10):
    RStarSample = random.uniform(0 , 2) #logaritmic
    fPlanets = random.uniform(-1 , 0)
    nEnvironment = random.uniform(-1 , 0)
    fInteligence = random.uniform(-3 , 0)
    fCivilization = random.uniform(-2 , 0)
    L = random.uniform(2 , maxL)
    #fLife = random.uniform(-2 , 0)
    #fLifeEks = fLife
    nStars = random.uniform(11, 11.60205999132)

    fLife = lifeDist(mean=0, sigma=50)
    fLifeEks = float(mp.log(fLife, 10))
    #fLifeEks = np.random.lognormal(-2 , 0)

    E3 = nStars + fPlanets + nEnvironment
    E4 = E3 + fLife
    E5 = E4 + fInteligence


    resitev = RStarSample + fPlanets + nEnvironment + fLifeEks + fInteligence + fCivilization + L   #calculates N

    #thresholds
    if (resitev<0) or E4 < math.log(2,10) or E3 < math.log(3,10) or resitev > 5:
        return getPoint(maxL)

    x.append(fLife) #for checking fLife
    return resitev

#devide Lmax scale
numHorSec = 48  #on how many parts should we devide L - how many different Lmax should we take
noIterationsPerMaxL = 1000     #How many points N per each file/maxL - should be as big as possible  ##trenutno 1000, da jih hitrej generira
logPoints = np.linspace(2,10,numHorSec) #devide on numHorSec equal parts a scale from 2 to 10 -
x = []  #for checking fLife

#for each Lmax create a file with points
for maxL in logPoints:
    array=[]
    for _ in range(0, noIterationsPerMaxL):
        array.append(getPoint(maxL))

    saveData(array,"/inf"+str(maxL))
    print("File: inf"+str(maxL)+".txt created")

#for checking fLife
x = np.array(x)
#print("Mean: " + str(np.mean(x)) + " Median: " + str(np.median(x)))
plt.hist(x,np.linspace(0,1,100),facecolor='blue',alpha=0.75)        #
#plt.show()

print('done')