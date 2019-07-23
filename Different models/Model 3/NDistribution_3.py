from libraries.IO import readData
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage.filters as fl
import math

numHorSec = 48
noBins = 50
bins = np.linspace(-13,20,noBins+1) #divide N scale
horSec = np.linspace(2,10,numHorSec)    #divide Lmax scale
Z = []    #no.hits 2D array - we draw this

horSec = np.linspace(2,10,numHorSec)
'''
for fileNo in horSec:
    array = readData("inf_loguniform_"+str(fileNo))
    Z+=array
'''
fileNo = horSec[-1]
Z = readData("inf_loguniform_"+str(fileNo))

nV, binsV, patchesV = plt.hist(Z, 200)

out = fl.gaussian_filter(nV, 2)

m = np.where(out == out.max())
m1 = binsV[m][0]
Z = [10**x for x in Z]
avg = sum(Z) / len(Z)
mediana = np.median(Z)

#print('Največja verjetnost: N = '+ str(10**m1))
#print("Povprečje: N = "+str(10**avg))
plt.cla()
plt.plot(binsV[0:-1], out,'red')
plt.ylabel('frequency')
plt.xlabel('Log(N)')
plt.legend(loc=1)
plt.title('Model 3 no cut, median: '+str(np.round(mediana,2))+" avg: "+str(np.round(avg,2)))
#plt.annotate('max', (m1, 0), annotation_clip=False)
#plt.axvline(m1, color ='r', alpha = 0.5)
#plt.axvline(avg, color='m', alpha=0.5, label='average')
#plt.axvline(mediana, color='g', alpha=0.5, label='median')
plt.show()