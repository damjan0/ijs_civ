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

horSec = np.linspace(2,10,numHorSec)

for fileNo in horSec:
    array = readData("/inf"+str(fileNo))
    #array = readData("/inf_lognormal_"+str(fileNo))
    #array = readData("/inf_loguni_"+str(fileNo))
    #array = readData("/inf_uni_"+str(fileNo))
    Z+=array


nV, binsV, patchesV = plt.hist(Z, 200)

out = fl.gaussian_filter(nV, 2)

m = np.where(out == out.max())
m1 = binsV[m][0]

print('Največja verjetnost: N = '+ str(10**m1))
plt.cla()
plt.plot(binsV[0:-1], out,'red')
plt.ylabel('frequency')
plt.xlabel('Log(N)')
#plt.legend(loc=1)
plt.title('Loguniform distribution for L')
#plt.annotate('max', (m1, 0), annotation_clip=False)
plt.axvline(m1, color ='r', alpha = 0.5)
plt.show()