from libraries.IO import readData
from libraries.IO import saveData
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import scipy.ndimage.filters as fl
from libraries.StandardizeDistribution import StandardizeDistributionW

# from functools import map

if True:
    bin_no = 100
    start = 0
    end = 10000

    fixed_n = [1, 10, 100, 1000, 10000]
    colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple']

    bounds = [500000,
              50000,
              500000,
              5000000,
              50000000]

    bounds = list(map(lambda x: x / 2, bounds))

    bins = np.linspace(start, end, bin_no)

    for i, maxN in enumerate(fixed_n):
        array = readData("inf_l_" + str(maxN))
        array = list(map(lambda x: 10 ** x, array))
        med = np.median(array)
        std = np.std(array)
        title = 'N = {:5}, median = {:8.0f}'.format(fixed_n[i], med)
        # plt.figure(title)
        plt.subplot(2, 3, i + 1)
        plt.title(title)
        bins = np.linspace(0, bounds[i], bin_no)
        # y, bins = np.histogram(array, )
        y, bins = np.histogram(array, bins=bins)
        #y = plt.hist(array, bins=bins, color=colors[i])
        y = y / max(y)
        # adj_bins = bins + (bins[1] - bins[0]) / 2
        # ax = plt.subplot(111)
        plt.plot(bins[:-1], y, colors[i])
        print(title, 'min: {:3.0f}, max: {:10.0f}'.format(min(array), max(array)))
        plt.xlabel("Expected civilization longevity in years")
        plt.ylabel("Relative probability")
        # ax.axes.get_yaxis().set_ticklabels(["Probability"])

        # plt.legend(loc=4)

    plt.show()

a = 1
if a == 2:
    bin_no = 100
    start = 0
    end = 10000

    fixed_n = [1, 10, 100, 1000, 10000]
    colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple']

    bounds = [5000,
              50000,
              500000,
              5000000,
              50000000]

    bounds = list(map(lambda x: np.log(x / 2), bounds))

    bins = np.linspace(start, end, bin_no)

    for i, maxN in enumerate(fixed_n):
        array = readData("inf_l_" + str(maxN))
        # array = list(map(lambda x: 10 ** x, array))
        med = np.median(array)
        std = np.std(array)
        title = 'N = {:5}, median = {:10.2f}'.format(fixed_n[i], 10 ** med)
        # plt.figure(title)
        # plt.subplot(2, 3, i + 1)
        plt.title(title)
        bins = np.linspace(0, 12, bin_no)
        # y, bins = np.histogram(array, )
        # y = plt.hist(array, bins=bins, color=colors[i])
        # adj_bins = bins + (bins[1] - bins[0]) / 2
        # ax = plt.subplot(111)
        y, bins = np.histogram(array, bins=bins)
        y = y / max(y)
        plt.plot(bins[:-1], y, colors[i], label='N={}'.format(maxN))
        print(title, 'min: {:3.0f}, max: {:10.0f}'.format(min(array), max(array)))
        plt.xlabel("Expected civilization longevity in log(years)")
        plt.ylabel("Relative probability")
        # ax.axes.get_yaxis().set_ticklabels(["Probability"])

    plt.legend(loc=1)
    plt.show()
