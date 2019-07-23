from libraries.IO import readData
from libraries.IO import saveData
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import scipy.ndimage.filters as fl
from libraries.StandardizeDistribution import StandardizeDistributionW

numHorSec = 20
start = 0
end = -4
noBins = 100
range_bin = (start, 10 ** end)


array = readData("/N_Sandberg_no_cut")

# val, edges = np.histogram(array, bins, range)
n, bins, patches = plt.hist(array, noBins, range_bin)


plt.title("No cut, range: "+str(start) + " - " + str(10**end) + " bin size: "+str(bins[1]-bins[0]))
plt.xlabel("N")
plt.ylabel("log(maxL)")
plt.show()

print("done")
