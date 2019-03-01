import random
from IO import saveData
from lifeDist import lifeDist, lifeDist2
import math
import time

parametersDict = {
    "nStars" : [],
    "fPlanets" : [],
    "nEnviroment" : [],
    "fLife" : [],
    "fIntelligence" : [],
    "fContact" : [],
    "RStarSample" : [],
    "L" : []
    }

under = parametersDict.copy()
#over = parametersDict.copy()
#valid = parametersDict.copy()

over = {
    "nStars" : [],
    "fPlanets" : [],
    "nEnviroment" : [],
    "fLife" : [],
    "fIntelligence" : [],
    "fContact" : [],
    "RStarSample" : [],
    "L" : []
    }

valid = {
    "nStars" : [],
    "fPlanets" : [],
    "nEnviroment" : [],
    "fLife" : [],
    "fIntelligence" : [],
    "fContact" : [],
    "RStarSample" : [],
    "L" : []
    }

def updateParams(d,params):
    nStars,fPlanets,nEnviroment,fLife,fIntelligence,fContact,RStarSample,L = params
    d["nStars"].append(nStars)
    d["fPlanets"].append(fPlanets)
    d["nEnviroment"].append(nEnviroment)
    d["fLife"].append(fLife)
    d["fIntelligence"].append(fIntelligence)
    d["fContact"].append(fContact)
    d["RStarSample"].append(RStarSample)
    d["L"].append(L)


noIterations =109999


startTime = time.time()

for i in range(0, noIterations):
    if i%1000==0:
        totalTime = 300
        print((time.time()-startTime)/totalTime)
        if time.time()-startTime>totalTime:
                break
    nStars = random.uniform(11, 11.60205999132)     # current number of stars in our galaxy (log uniform distibution)

    fPlanets = random.uniform(-1 , 0)
    nEnvironment = random.uniform(-1 , 0)
    fLife = float(lifeDist(mean=0, sigma=50))
    fIntelligence = random.uniform(-3 , 0)
    fContact = random.uniform(-2 , 0)
    RStarSample = random.uniform(0 , 2)
    L = random.uniform(2 , 10)
    parameters = [nStars,fPlanets,nEnvironment,fLife,fIntelligence,fContact,RStarSample,L]

    E3 = nStars + fPlanets + nEnvironment
    E4 = E3 + fLife
    E5 = E4 + fIntelligence
    E6 = E5 + fContact      #This is the result of Sandberg method, for adding new methods just this E-s are replaced

    E7 = RStarSample + fPlanets + nEnvironment + fLife + fIntelligence + fContact + L;

    if E7 < math.log(1,10) or E4 < math.log(2,10) or E3 < math.log(3,10) : #underestimations
        updateParams(under,parameters)
    elif E7 > 5: #oversetimation
        updateParams(over,parameters)
    else:
        updateParams(valid,parameters)
    
for key in under:
    saveData(under[key],"Bokal/under_"+key)
for key in over:
    saveData(over[key],"Bokal/over_"+key)
for key in under:
    saveData(valid[key],"Bokal/valid_"+key)
print('done')


    