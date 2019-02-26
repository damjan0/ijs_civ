from IO import readData
import matplotlib.pyplot as plt
import scipy.ndimage.filters as fl

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
over = parametersDict.copy()
valid = parametersDict.copy()

parameters = {"nStars", "fPlanets", "nEnviroment", "fLife", "fIntelligence", "fContact", "RStarSample", "L"}

no=1
for key in parameters:
#for key in {"nStars"}:  

    plt.figure(no)
    no=no+1
    under[key] = readData("Bokal/under_"+key)
    valid[key] = readData("Bokal/valid_"+key)
    over[key] = readData("Bokal/over_"+key)
    
    nU, binsU, patchesU = plt.hist(under[key], 200, facecolor='red', alpha=0.75)
    nV, binsV, patchesV = plt.hist(valid[key], 200, facecolor='green', alpha=0.75)
    nO, binsO, patchesO = plt.hist(over[key], 200, facecolor='blue', alpha=0.75)
    
    sigma = 3
    nU = fl.gaussian_filter(nU, sigma)
    nV = fl.gaussian_filter(nV, sigma)
    nO = fl.gaussian_filter(nO, sigma)
           
    #plt.xscale("log")
    plt.cla()
    plt.plot(binsU[0:-1], nU,'red',label='under')
    plt.plot(binsV[0:-1], nV,'green',label='valid')
    plt.plot(binsO[0:-1], nO,'blue',label='over')
    plt.ylabel('relative frequency')
    plt.xlabel('Log('+str(key)+')')
    plt.legend(loc=1)
    plt.title(key)
plt.show()
