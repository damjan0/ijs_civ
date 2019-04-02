import mpmath as mp
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import random
import math
import time
from libraries.IO import saveData
from libraries.lifeDist import lifeDist, lifeDist2


def getPoint(maxN=10):
	#RStarSample = random.uniform(0, 2)   #loguniform
	RStarSample = math.log10(np.random.uniform(10 ** 0, 10 ** 2))  # uniform
	#sigmaHalfGauss = (10 ** 2 - 10 ** 0) / 6 # interval/2 je polovic in se /3 je tako da bo 3sigma cez cel interval
	#RStarSample = np.log10(np.abs(np.random.normal(0, sigmaHalfGauss)) + 10 ** 0) 	#gauss
	#median = (2 - 0) / 2 + 2  # polovica intervala
	#sigma = (median - 2) / 3  # tako, da je 3sigma cez cel obseg
	#RStarSample = np.random.normal(median, sigma)  # lognormal

	#fPlanets = random.uniform(-1, 0)
	fPlanets = math.log10(np.random.uniform(10 ** -1, 10 ** 0))  
	#sigmaHalfGauss = (10 ** 0 - 10 ** -1) / 6 # interval/2 je polovic in se /3 je tako da bo 3sigma cez cel interval
	#fPlanets = np.log10(np.abs(np.random.normal(0, sigmaHalfGauss)) + 10 ** (-1)) 
	#median = (0 - (-1)) / 2 + 2  # polovica intervala
	#sigma = (median - 2) / 3  # tako, da je 3sigma cez cel obseg
	#fPlanets = np.random.normal(median, sigma)  

	#nEnvironment = random.uniform(-1, 0)
	nEnvironment = math.log10(np.random.uniform(10 ** -1, 10 ** 0))  
	#sigmaHalfGauss = (10 ** 0 - 10 ** -1) / 6 # interval/2 je polovic in se /3 je tako da bo 3sigma cez cel interval
	#nEnvironment = np.log10(np.abs(np.random.normal(0, sigmaHalfGauss)) + 10 ** (-1)) 
	#median = (0 - (-1)) / 2 + 2  # polovica intervala
	#sigma = (median - 2) / 3  # tako, da je 3sigma cez cel obseg
	#nEnvironment = np.random.normal(median, sigma)  

	#fIntelligence = random.uniform(-3, 0)
	fIntelligence = math.log10(np.random.uniform(10 ** -3, 10 ** 0))  
	#sigmaHalfGauss = (10 ** 0 - 10 ** -3) / 6 # interval/2 je polovic in se /3 je tako da bo 3sigma cez cel interval
	#fIntelligence = np.log10(np.abs(np.random.normal(0, sigmaHalfGauss)) + 10 ** (-3)) 
	#median = (0 - (-3)) / 2 + 2  # polovica intervala
	#sigma = (median - 2) / 3  # tako, da je 3sigma cez cel obseg
	#fIntelligence = np.random.normal(median, sigma)  

	#fCivilization = random.uniform(-2, 0)
	fCivilization = math.log10(np.random.uniform(10 ** -2, 10 ** 0)) 
	#sigmaHalfGauss = (10 ** 0 - 10 ** -2) / 6 # interval/2 je polovic in se /3 je tako da bo 3sigma cez cel interval
	#fCivilization = np.log10(np.abs(np.random.normal(0, sigmaHalfGauss)) + 10 ** (-2)) 
	#median = (0 - (-2)) / 2 + 2  # polovica intervala
	#sigma = (median - 2) / 3  # tako, da je 3sigma cez cel obseg
	#fCivilization = np.random.normal(median, sigma)

	#N = np.random.uniform(0 , maxN)                         
	N = math.log10(np.random.uniform(10 ** 0, 10 ** maxN))  # uniform
	#sigmaHalfGauss = 10 ** maxN / 6  # /3 je tako da bo 3sigma cez cel interval
	#N = np.log10(np.abs(np.random.normal(0, sigmaHalfGauss)))
	#median = maxN / 2  # polovica intervala
	#sigma = median / 3  # tako, da je 3sigma cez cel obseg
	#N = np.random.normal(median, sigma)  # lognormal
    #N = math.log10(np.random.normal(10**0, 10**maxN))      # lognormal

	fLife = lifeDist(mean=0, sigma=50)
	fLifeEks = float(mp.log(fLife, 10))

	nStars = random.uniform(11, 11.60205999132)
	E3 = nStars + fPlanets + nEnvironment
	E4 = E3 + fLife
	E5 = E4 + fIntelligence

	# resitev = RStarSample + fPlanets + nEnvironment + fLifeEks + fInteligence + fCivilization + L
	L = N - (RStarSample + fPlanets + nEnvironment + fLifeEks + fIntelligence + fCivilization)

	# thresholds
	if (L < 2) or E4 < math.log(2, 10) or E3 < math.log(3,10) or L > 10.139879:  # maxL - age of the universe - if we are taking drake equation for this moment
		# return getPoint(maxN)
		return False

	return L


drawnPoints=0
numHorSec = 48
noIterationsPerMaxN = 30000
logPoints = np.linspace(0, 7, numHorSec)
allPoints=noIterationsPerMaxN*numHorSec

for maxN in logPoints:
	array = []
	for _ in range(0, noIterationsPerMaxN):
		point = getPoint(maxN)
		if type(point) != type(False):
			array.append(point)

	saveData(array, "inf" + str(maxN))
	print("File: inf" + str(maxN) + ".txt created. no of points:" + str(len(array)))
	drawnPoints=drawnPoints+len(array)
	pointFraction= (drawnPoints*100)/allPoints
print('done')
print('Drawn points: ' + str(drawnPoints) + '  Which is: ' + str(pointFraction)+'%')