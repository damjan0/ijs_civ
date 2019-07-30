from libraries.IO import saveData,readData
from libraries.lifeDist import lifeDist, lifeDist2
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import scipy.ndimage.filters as fl
#from StandardizeDistribution import StandardizeDistributionW
import sys
def printf(format, *args):
    sys.stdout.write(format % args)


numHorSec = 48
noBins = 50
bins = np.linspace(0,2,noBins+1) #devide N scale
horSec = np.linspace(2,10,numHorSec)    #devide Lmax scale
Z = [None]*numHorSec    #no.hits 2D array - we draw this
i=0

#go through the files
for fileNo in horSec:
    try:
        type_dist = "loguniform"
        array = readData("/inf_"+ type_dist + "_" +str(fileNo))
        array = [np.log10(i) for i in array]
        array = list(filter(lambda x : x <=4, array))
    except FileNotFoundError: array = 0
    Z[i],_ = np.histogram(array, bins)
    #Z[i] = np.multiply(Z[i], 2.0/float(fileNo), out=Z[i], casting="unsafe")    # decay factor is 2/fileNo = 2/maxL
    printf("L %.2f - N %.2f\n",fileNo,np.log10(np.average(array)))
    i+=1

X, Y = np.meshgrid(bins[0:-1],horSec)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X = np.array(X)
Y = np.array(Y)
Z = np.array(Z)

#PRINT Z aka no_hits table used for other programs
#np.savetxt('no_hits.txt', Z, fmt='%.0f')
#saveData(Z, "no_hits")   old
print("Saved no. of hits")

# Plot the surface
ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,shade=True,color='b',alpha=0.8)

ax.set_xlabel("log(N)")
ax.set_ylabel("log(maxL)")
ax.set_zlabel("no. hits")
plt.show()

print("done")