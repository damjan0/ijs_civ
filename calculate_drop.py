from libraries.IO import readData
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import scipy.ndimage.filters as fl
from libraries.StandardizeDistribution import StandardizeDistributionW
from numpy.random import randn
from scipy.ndimage import gaussian_filter

numHorSec = 48
# numHorSec = 5
noBins = 60
# bins = np.linspace(-2, 13, noBins + 1)
f = 100  # FROM this
to = (10 ** 6) * 2  # to this
years = 1000  # tu nastaviš velikost binov

bins = np.linspace(f, to, to / years)
# print(bins)
horSec = [1, 10, 100, 1000, 10000] #različni N-ji
# horSec = [1]
Z = [None] * numHorSec
i = 0
for fileNo in horSec:
    plt.figure(i)
    # plt.subplot(1, 2, 1)
    array = readData("inf_l_" + str(fileNo))
    # print(fileNo)
    # print(str(int(10 ** fileNo)) + " - " + str(bins[np.argmax(Z[i])]))
    array = [10 ** x for x in array]
    hist, _ = np.histogram(array, bins)
    hist = gaussian_filter(hist, sigma=20)
    print('N= {} '.format(fileNo))
    suu = ""
    for x in [0, 1, 10, 100, 1000]:
        suu = "{} & ${:.3f}$".format(suu, hist[x] / 165742) #To ja za izpis, še sem normalizirau na roko z deljenjm
    print(suu, "\\")
    # grad = np.gradient(hist) #Za računanje padca
    # grad = [a / b for a, b in zip(grad, hist)]
    # plt.plot(grad)
    # print('N= ', fileNo)
    # print([i * 100 for i, e in enumerate(grad) if e > -0.01])
    '''
    not_found = True
    for st in range(1, len(hist)):
        # print(hist[st])
        if (hist[st - 1] != 0):
            al = abs(hist[st] / hist[st - 1])
            #print(al)
            graph.append(al)
            if (al > 0.99) and not_found:
                not_found = False
                print(bins[st])
            # print(hist[st] / hist[st - 1])
    '''

    # graph = gaussian_filter(graph, sigma=20)

    # plt.hist(array, bins=bins)

    # plt.plot(graph[f:400])
    # plt.subplot(1, 2, 2)
    plt.plot(hist, bins[:-1])
    graph = []
    plt.title(fileNo)
    i += 1

plt.show()
