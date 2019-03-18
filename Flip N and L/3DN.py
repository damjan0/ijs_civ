from IO import readData
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import scipy.ndimage.filters as fl
from StandardizeDistribution import StandardizeDistributionW

numHorSec = 9
noBins = 60
bins = np.linspace(-1, 15, noBins + 1)
#horSec = np.linspace(0, 10, numHorSec)
horSec = range(1, 11)
Z = [None] * numHorSec
i = 0

for fileNo in horSec:
    array = readData("linN/lin" + str(fileNo))
    Z[i], _ = np.histogram(array, bins)
    # Z[i] = np.multiply(Z[i], 2.0/float(fileNo), out=Z[i], casting="unsafe")    # decay factor is 2/fileNo = 2/maxL
    print('N'+str(fileNo)+' max at L='+str(bins[Z[i].argmax()]))
    i += 1

X, Y = np.meshgrid(bins[0:-1], horSec)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X = np.array(X)
Y = np.array(Y)
Z = np.array(Z)

# Plot the surface
ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, shade=True, color='b', alpha=0.8)

ax.set_xlabel("log(L)")
ax.set_ylabel("fixed N")
ax.set_zlabel("no. hits")
plt.show()

print("done")
