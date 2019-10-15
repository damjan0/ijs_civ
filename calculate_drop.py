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
f = 0  # FROM this
to = (10 ** 6) + 1000  # to this
# to = 2500
years = 100  # tu nastaviš velikost binov

bins = np.linspace(f, to, int((to - f) / years))
horSec = [1, 10, 100, 1000, 10000]  # različni N-ji
# horSec = [1]
# horSec = [100, 1000]
Z = [None] * numHorSec
i = 0
for fileNo in horSec:
    graph = []
    plt.figure(i)
    plt.subplot(1, 2, 1)
    array = readData("inf_l_" + str(fileNo))
    # print(fileNo)
    # print(str(int(10 ** fileNo)) + " - " + str(bins[np.argmax(Z[i])]))
    array = [10 ** x for x in array]
    hist1, _ = np.histogram(array, bins)
    # hist1, _, _ = plt.hist(array, bins)
    #hist1 = gaussian_filter(hist1, sigma=8)
    # print(hist[0:10])
    # print('N= {} '.format(fileNo))
    suu = str(fileNo)
    max_cen = np.max(hist1) * 10

    #for x in [0, 10, 100, 1000, 10000]:
    for x in range(0, len(hist1-10)):
        filled = np.sum(hist1[x:x + 10])
        # print('filled ', filled)
        # whole = int(hist[x])*10
        # print(filled)
        # print(whole)
        # plt.plot(hist[x:x + 10])
        # plt.show()
        #suu = "{} & ${}$".format(suu, filled / max_cen)

        if (filled / max_cen) <= 0.01:
            suu = "{} & {}".format(suu, x * 100)
            break

    print(suu, "\\\\")
    '''
    grad = np.gradient(hist1) #Za računanje padca
    grad = [a / b for a, b in zip(grad, hist1)]
    rag = 100
    plt.plot(grad[:rag])
    print('N= ', fileNo)
    print([i * 100 for i, e in enumerate(grad) if e > -0.01])
    
    not_found = True
    for st in range(1, len(hist1)):
        # print(hist[st])
        if (hist1[st - 1] != 0):
            al = abs(hist1[st] / hist1[st - 1])
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
    plt.subplot(1, 2, 2)
    # plt.plot(bins[:rag], hist1[:rag])

    plt.title(fileNo)
    i += 1

# plt.show()
