from libraries.IO import readData
from libraries.IO import saveData
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import scipy.ndimage.filters as fl
from libraries.StandardizeDistribution import StandardizeDistributionW

numHorSec = 48
noBins = 100
bins = np.linspace(100,1000,noBins+1) #divide N scale
horSec = np.linspace(2, 10, numHorSec)  # divide Lmax scale
Z = [None] * numHorSec  # no.hits 2D array - we draw this
i = 0

# go through the files
for fileNo in horSec:
    array = readData("/inf" + str(fileNo))
    # array = array[0:4664]
    array = [10**i for i in array]
    Z[i], _ = np.histogram(array, bins)
    # Z[i] = np.multiply(Z[i], 2.0/float(fileNo), out=Z[i], casting="unsafe")    # decay factor is 2/fileNo = 2/maxL
    i += 1

X, Y = np.meshgrid(bins[0:-1], horSec)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X = np.array(X)
Y = np.array(Y)
Z = np.array(Z)

# PRINT Z aka no_hits table used for other programs
np.savetxt('no_hits.txt', Z, fmt='%.0f')
# saveData(Z, "no_hits")   old
print("Saved no. of hits")

# Plot the surface
ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, shade=True, color='b', alpha=0.8)

ax.set_xlabel("N")
ax.set_ylabel("log(maxL)")
ax.set_zlabel("no. hits")
plt.show()

print("done")
