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
from scipy import integrate

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

    fLife = lifeDist(mean=0, sigma=50)
    fLifeEks = float(mp.log(fLife, 10))
    #fLifeEks = np.random.lognormal(-2 , 0)


    resitev = RStarSample + fPlanets + nEnvironment + fLifeEks + fInteligence + fCivilization + L   #calculates N

    #threshold if N values are very low
    if (resitev<-6):
        return getPoint(maxL)

    x.append(fLife) #for checking fLife

    resitev1 = int(round(10**resitev)) #rounded de-logarithmised solution

    koncnaResitev = 0

    for i in range(resitev1):
        A = random.gauss(1, 0.5)
        v = random.gauss(0.016*300000, 2000)
        L1 = random.uniform(2, maxL)
        B = 0.004*((9.461*10**(-12))**3) #number density of stars as per Wikipedia
        R = v*random.uniform(0, L) #radius of inhabited zone, I assume they have been expanding since the became detectable, which is random
        integral = integrate.quad(lambda r: r**2*math.exp(-(R-r)/(v*10**L1)), 0, R)

        n = B*fPlanets*nEnvironment*4*math.pi*integral[0]

        koncnaResitev+=A*(n+1)

    return koncnaResitev

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