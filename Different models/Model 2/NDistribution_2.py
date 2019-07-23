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
    array = list(filter(lambda x: x < 4, array))
    Z+=array


median = 10**np.median(Z)

print("Median: " + str(median))

nV, binsV, patchesV = plt.hist(Z, 200)

#out = fl.gaussian_filter(nV, 2)

m = np.where(nV == nV.max())
m1 = binsV[m][0]
Z1 = [10**i for i in Z]
avg = sum(Z1)/len(Z1)

print('Največja verjetnost: N = '+ str(10**m1))
print("Povprečje: N = "+str(avg))
plt.cla()
plt.plot(binsV[0:-1], nV,'red')
plt.ylabel('frequency')
plt.xlabel('Log(N)')
#plt.legend(loc=1)
plt.title('Model 2, no cut. Median: {0}, average: {1}'.format(round(median,2), round(avg,2)))
#plt.annotate('max', (m1, 0), annotation_clip=False)
#plt.axvline(m1, color ='r', alpha = 0.5)
#plt.axvline(avg, color='r', alpha=0.5)
plt.show()