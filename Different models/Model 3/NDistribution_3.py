from libraries.IO import readData
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage.filters as fl
import mpmath as mp
import math

numHorSec = 48
noBins = 50
bins = np.linspace(-13,20,noBins+1) #divide N scale
horSec = np.linspace(2,10,numHorSec)    #divide Lmax scale
Z = []    #no.hits 2D array - we draw this

horSec = np.linspace(2,10,numHorSec)

maximum = mp.log10(511805)

#fileNo = min(horSec, key=lambda x:abs(x-maximum))

# for fileNo in horSec:
#      array = readData("inf_loguniform_"+str(fileNo))
#      Z+=array

fileNo = horSec[23]
W = readData("inf_loguniform_"+str(fileNo))
glajenje = 0.2
#Z1= readData("inf_loguniform_settlements_"+str(fileNo))
#Z = [np.log10(i) for i in Z]
#Z1 = list(filter(lambda x: 0 <= x <= 11.6, Z1))
#Z2 = [10**W[i]/Z1[i] for i in range(len(W))]
W = list(filter(lambda x: x <= np.random.normal(3.5, glajenje), W))

# epsilon = 0.1
# Z = []
# for i in range(len(Z1)):
#     if 1 -  epsilon <= Z2[i] <= 1 + epsilon:
#         Z.append(Z1[i])
#

nV, binsV, patchesV = plt.hist(W, 200)

out = fl.gaussian_filter(nV, 2)

m = np.where(out == out.max())
m1 = binsV[m][0]
Z = [10**x for x in W]
avg = sum(Z) / len(Z)
mediana = np.median(Z)

#print('Največja verjetnost: N = '+ str(10**m1))
#print("Povprečje: N = "+str(10**avg))
plt.cla()
plt.plot(binsV[0:-1], out,'red')
plt.ylabel('frequency')
#plt.xlabel('Number of settlements if number of civilizations = 1')
plt.xlabel('log(N)')
#plt.legend(loc=1)
plt.title('Model 3, middle slice, median: '+str(np.round(mediana,2))+" avg: "+str(np.round(avg,2)))
#plt.annotate('max', (m1, 0), annotation_clip=False)
#plt.axvline(m1, color ='r', alpha = 0.5)
#plt.axvline(avg, color='m', alpha=0.5, label='average')
#plt.axvline(mediana, color='g', alpha=0.5, label='median')
plt.show()