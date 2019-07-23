#from libraries.IO import readData
import numpy as np
import matplotlib.pyplot as plt
#import scipy.ndimage.filters as fl
import math


def readData(filename):
    file = open('data/' + filename + '.txt', 'r')
    lines = file.readlines()
    size = len(lines)
    y = [0] * size

    for i in range(0, size):
        y[i] = float(lines[i][0:-1])

    file.close()
    return y

numHorSec = 48
noBins = 50
bins = np.linspace(-13,20,noBins+1) #devide N scale
horSec = np.linspace(2,10,numHorSec)    #devide Lmax scale
Z = []    #no.hits 2D array - we draw this

horSec = np.linspace(2,10,numHorSec)

#for fileNo in horSec:
array = readData("/inf"+str(horSec[-1]))
#     #array = readData("/inf_lognormal_"+str(fileNo))
#     #array = readData("/inf_loguni_"+str(fileNo))
#     #array = readData("/inf_uni_"+str(fileNo))
array1 = list(filter(lambda x: -6 < x < 4, array))
Z+=array1
# fileNo = 10
# array = readData("/inf"+str(fileNo))
# Z = array

median = 10**np.median(Z)

print("Median: " + str(median))

nV, binsV, patchesV = plt.hist(Z, 200)

#out = fl.gaussian_filter(nV, 2)

m = np.where(nV == nV.max())
m1 = binsV[m][0]
Z1 = [10**i for i in Z]
avg = sum(Z1)/len(Z1)

print("Najvecja verjetnost: N = "+ str(10**m1))
print("Povprecje: N = "+str(avg))
plt.cla()
plt.plot(binsV[0:-1], nV ,'red')
plt.ylabel('frequency')
plt.xlabel('Log(N)')
#plt.legend(loc=1)
plt.title('Model 1, no cut. Median: {0}, average: {1}'.format(round(median,2), round(avg,2)))
#plt.annotate('max', (m1, 0), annotation_clip=False)
#plt.axvline(m1, color ='r', alpha = 0.5)
#plt.axvline(avg, color='r', alpha=0.7)
plt.show()