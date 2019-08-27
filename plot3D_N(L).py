from libraries.IO import readData
from libraries.IO import saveData
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
#import scipy.ndimage.filters as fl
#from libraries.StandardizeDistribution import StandardizeDistributionW

numHorSec = 20
noBins = 50

bins = np.linspace(-2,5,noBins+1) #devide N scale

horSec = np.linspace(2, 10, numHorSec)  # devide Lmax scale
Z = [None] * numHorSec  # no.hits 2D array - we draw this
i = 0

# go through the files
for fileNo in horSec:
    array = readData("/inf" + str(fileNo.round(11)))
    # array = array[0:4664]
    #array = list(filter(lambda x: 0 <= x < 4, array))
    Z[i], _ = np.histogram(array, bins)
    # Z[i] = np.multiply(Z[i], 2.0/float(fileNo), out=Z[i], casting="unsafe")    # decay factor is 2/fileNo = 2/maxL
    i += 1

X, Y = np.meshgrid(bins[0:-1], horSec)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X = np.array(X)
Y = np.array(Y)
Z = np.array(Z)

# saveData(Z, "no_hits")   old
print("Saved no. of hits")

# Plot the surface
ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, shade=True, color='b', alpha=0.8)

ax.set_xlabel("N")
ax.set_ylabel("log(maxL)")
ax.set_zlabel("no. hits")
plt.show()

print("done")
