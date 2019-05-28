from libraries.IO import readData
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage.filters as fl
import math

def draw_L(type_dist):
    numHorSec = 48
    noBins = 50
    bins = np.linspace(-13,20,noBins+1) #devide N scale
    logPoints = np.linspace(0, 4, numHorSec)    #devide Lmax scale
    Z = []    #no.hits 2D array - we draw this

    horSec = np.linspace(0, 4, numHorSec)

    for fileNo in horSec:

        array = readData("inf"+str(fileNo))
        Z+=array

    #out = fl.gaussian_filter(Z, 1)

    nV, binsV, patchesV = plt.hist(Z, 200)

    out = fl.gaussian_filter(nV, 2)

    m = np.where(out == out.max())
    m1 = binsV[m][0]

    avg = sum(Z) / len(Z)

    print('Največja verjetnost: L = '+ str(10**m1))
    print("Povprečje: L = " + str(10 ** avg))
    plt.cla()
    plt.plot(binsV[0:-1], out,'red')
    plt.ylabel('frequency')
    plt.xlabel('Log(L)')
    #plt.legend(loc=1)
    plt.title('{} distribution for N'.format(type_dist))
    #plt.annotate('max', (m1, 0), annotation_clip=False)
    plt.axvline(m1, color ='r', alpha = 0.5)
    plt.axvline(avg, color='r', alpha=0.5)
    plt.show()
    
# distributions = ["loguniform", "uniform", "halfgauss", "lognormal"]
#
# for d in distributions:
draw_L("loguniform")
#
# print("REALLY DONE!")