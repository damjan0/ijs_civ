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
    if fileNo:
        array = readData("/inf"+str(fileNo))
    #array = readData("/inf_lognormal_"+str(fileNo))
    #array = readData("/inf_loguni_"+str(fileNo))
    #array = readData("/inf_uni_"+str(fileNo))
        Z+=filter(lambda x: -8 < x < -6 , array)
       # Z+= array

Z = [10**i for i in Z]

#temp = list(filter(lambda x:  x < 4, Z))
#temp1 = list(filter(lambda x: x > 0 , temp))
#print("Probability that we are not alone: " + str(len(temp1)/len(temp)))

# for i in [0, -2, -4, -6, -8]:
#     temp = list(filter(lambda x: i < x < 4, Z))
#     temp1 = list(filter(lambda x: x > 0 , temp))
#     print("Cutting at: " + str(i) + ", probability that we are not alone: " + str(len(temp1)/len(temp)))

out, binsV, patchesV = plt.hist(Z, 1000)

#out = fl.gaussian_filter(nV, 2)

m = np.where(out == out.max())
m1 = binsV[m][0]

avg = sum(Z)/len(Z)

print('Največja verjetnost: N = '+ str(m1))
print("Povprečje: N = "+str(avg))
plt.cla()
plt.plot(binsV[0:-1], out,'red')
plt.ylabel('frequency')
plt.xlabel('N')
#plt.legend(loc=1)
plt.title('Loguniform distribution for L')
#plt.annotate('max', (m1, 0), annotation_clip=False)
plt.axvline(m1, color ='b', alpha = 0.5)
plt.axvline(avg, color='g', alpha=0.7)
plt.show()