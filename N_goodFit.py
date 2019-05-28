from libraries.IO import readData
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage.filters as fl
import math

numHorSec = 48
noBins = 50
bins = np.linspace(-13,20,noBins+1) #devide N scale
horSec = np.linspace(2,10,numHorSec)    #devide Lmax scale
Z = []    #no.hits 2D array - we draw this

nrIterations = 30000

for fileNo in horSec:
    array = readData("/inf"+str(fileNo))
    #array = readData("/inf_lognormal_"+str(fileNo))
    #array = readData("/inf_loguni_"+str(fileNo))
    #array = readData("/inf_uni_"+str(fileNo))
    Z.append(len(array)/nrIterations)


#nV, binsV, patchesV = plt.hist(Z, 200)

out = fl.gaussian_filter(Z, 2)

#m = Z.index(max(Z))

#avg = sum(Z)/len(Z)

#print('Največja verjetnost: N = '+ str(10**m))
#print("Povprečje: N = "+str(10**avg))
plt.cla()
plt.plot(horSec, out,'red')
plt.ylabel('frequency of good result')
plt.xlabel('log(L)')
#plt.legend(loc=1)
plt.title('Loguniform distribution for L')
#plt.annotate('max', (m1, 0), annotation_clip=False)
#plt.axvline(m1, color ='r', alpha = 0.5)
#plt.axvline(avg, color='r', alpha=0.7)
plt.show()