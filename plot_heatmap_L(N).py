from libraries.IO import readData
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import scipy.ndimage.filters as fl
from libraries.StandardizeDistribution import StandardizeDistributionW
from numpy.random import randn

numHorSec = 48
# numHorSec = 5
noBins = 60
#bins = np.linspace(-2, 13, noBins + 1)
bins = np.linspace(0,10**5,noBins+1)
horSec = np.linspace(0, 4, numHorSec)
Z = [None] * numHorSec
i = 0

for fileNo in horSec:
    array = readData("inf_l_" + str(fileNo))

    Z[i], _ = np.histogram(array, bins)
    Z[i] = [10**x for x in Z[i]]
    print(str(int(10 ** fileNo)) + " - " + str(bins[np.argmax(Z[i])]))
    i += 1


X, Y = np.meshgrid(bins[0:-1], horSec)
X = np.array(X)
Y = np.array(Y)
Z = np.array(Z)


#Z = np.flip(Z, 0)
#horSec = horSec[::-1]
# fig = plt.figure()

# p = plt.imshow(Z, cmap=cm.coolwarm)

fig, ax = plt.subplots()

# data = np.clip(randn(250, 250), -1, 1)

cax = ax.contourf(X,Y, Z, cmap=cm.coolwarm, levels=100)
#ax.set_title('Expected number of civilization Longevity based on N')

plt.xlabel("log(L)")
plt.ylabel("log(N)")

cbar = fig.colorbar(cax, ticks=[0, np.amax(Z)], orientation='horizontal')
cbar.ax.set_xticklabels(['Low',  'High'])

#slice_range_x = 8
#slice_range_y = 6
#plt.xticks(range(noBins + 1)[0:-1:slice_range_x], np.around(bins[0:-1:slice_range_x], 1))
#plt.yticks(range(numHorSec)[0:-1:slice_range_y], np.around(horSec[0:-1:slice_range_y], 1))

plt.show()

print("done")
