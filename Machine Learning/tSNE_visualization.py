'''''
tSNE visualization
'''''

import csv
import numpy as np
import time
import math

from sklearn.preprocessing import MinMaxScaler
#from sklearn.preprocessing import normalize
from sklearn.manifold import TSNE
#from sklearn.decomposition import PCA

import matplotlib.pyplot as plt
import matplotlib.patheffects as PathEffects

file = 'points4.csv'

x_train = []    #every parameter a new dim
y_train = []    #labels are N

#store each parameter to its own variable array
x_1 = []
x_2 = []
x_3 = []
x_4 = []
x_5 = []
x_6 = []
x_7 = []
x_8 = []

'''''
## Normalize
'''''

def minMaxNormalization(a):
    maxInAllColumns = np.max(a, axis=0) #find max values in the whole column
    minInAllColumns = np.min(a, axis=0)

    for i in range(len(maxInAllColumns)):   #take every column
        maxInThisCol = maxInAllColumns[i]   #note min and max
        minInThisCol = minInAllColumns[i]
        for j in range(len(a)):
            x = a[j][i]
            a[j][i] = (float(x-minInThisCol)/(maxInThisCol-minInThisCol))
    return a


'''''
## Loads csv data
'''''
print("Loading data...")
with open(file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
            vector = []  # empty 8D vector to store all parameters from one line
            for i in range(0,9):    #vključi vse parametre
                parameter = row[i]
                vector.append(float(parameter))
            x_train.append(vector)
            y_train.append(math.log(float(row[0])))  #N
            ''' #Logarithmic parameters
            x_1.append(math.log(float(row[1])))      #rStar
            x_2.append(math.log(float(row[2])))      #fPlanets
            x_3.append(math.log(float(row[3])))    #nEnvironment
            x_4.append(math.log(float(row[4])))      #fLife
            x_5.append(math.log(float(row[5])))      #fIntelligence
            x_6.append(math.log(float(row[6])))      #fCivilization
            x_7.append(math.log(float(row[7])))     #Longevity
            x_8.append(math.log(float(row[8])))     #Max Longevity
            ''' #Normal paramters
            x_1.append(float(row[1]))      #rStar
            x_2.append(float(row[2]))      #fPlanets
            x_3.append(float(row[3]))      #nEnvironment
            x_4.append(float(row[4]))      #fLife
            x_5.append(float(row[5]))      #fIntelligence
            x_6.append(float(row[6]))      #fCivilization
            x_7.append(float(row[7]))      #Longevity
            x_8.append(float(row[8]))      #Max Longevity
            #x_1 = x_train[:,1]  #take second column of x_train
            line_count += 1

print(f'Processed {line_count} lines.')

#how many rows are should we use
howManyTest = 150000  #how many rows should be considered an input at t-SNE function
howManyShow = howManyTest  #how many rows should be printed out

#make it numpy
x_train = np.array(x_train)
y_train = np.array(y_train)
x_1 = np.array(x_1)
x_2 = np.array(x_2)
x_3 = np.array(x_3)
x_4 = np.array(x_4)
x_5 = np.array(x_5)
x_6 = np.array(x_6)
x_7 = np.array(x_7)
x_8 = np.array(x_8)

#normalize
minMaxNormalization(x_train)

#optimizacija
x_train = x_train[:howManyTest]
y_train = y_train[:howManyTest]
x_1 = x_1[:howManyTest]
x_2 = x_2[:howManyTest]
x_3 = x_3[:howManyTest]
x_4 = x_4[:howManyTest]
x_5 = x_5[:howManyTest]
x_6 = x_6[:howManyTest]
x_7 = x_7[:howManyTest]
x_8 = x_8[:howManyTest]

'''''
#normalize it using MinMaxScaler
scaler = MinMaxScaler()
scaler.fit(x_train)
scaler.data_max_
x_train = scaler.transform(x_train)
'''''
#normalize it using normalize
#https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.normalize.html


'''''
## tSNE magic
'''''
print("Initializing t-SNE...")

time_start = time.time()
#tsne = TSNE(n_components=2, verbose=1, perplexity=40, n_iter=300)
tsne = TSNE(n_components=2, verbose=1, perplexity=1000, n_iter=1000)
tsne_results = tsne.fit_transform(x_train)

print('t-SNE done! Time elapsed: {} seconds'.format(time.time()-time_start))


'''''
## Visualization
'''''
print("Drawing points...")

#get x and y coordinates of all our points
vis_x = tsne_results[:, 0]
vis_y = tsne_results[:, 1]

#Show N
#plt.figure(figsize=(12, 10))
plt.figure(figsize=(19.2, 10.8))
plt.scatter(vis_x[:howManyShow], vis_y[:howManyShow], c=y_train[:howManyShow])
plt.colorbar()
plt.title("Color: log(N)")
plt.savefig("points_tSNE_N.png", dpi=100)
#plt.show()
#Show rStar
plt.figure(figsize=(19.2, 10.8))
plt.scatter(vis_x[:howManyShow], vis_y[:howManyShow], c=x_1[:howManyShow])
plt.colorbar()
plt.title("Color: rStar")
plt.savefig("points_tSNE_x1.png", dpi=100)
#plt.show()
#Show fPlanets
plt.figure(figsize=(19.2, 10.8))
plt.scatter(vis_x[:howManyShow], vis_y[:howManyShow], c=x_2[:howManyShow])
plt.colorbar()
plt.title("Color: fPlanets")
plt.savefig("points_tSNE_x2.png", dpi=100)
#plt.show()
#Show nEnvironment
plt.figure(figsize=(19.2, 10.8))
plt.scatter(vis_x[:howManyShow], vis_y[:howManyShow], c=x_3[:howManyShow])
plt.colorbar()
plt.title("Color: nEnvironment")
plt.savefig("points_tSNE_x3.png", dpi=100)
#plt.show()
#Show fLife
plt.figure(figsize=(19.2, 10.8))
plt.scatter(vis_x[:howManyShow], vis_y[:howManyShow], c=x_4[:howManyShow])
plt.colorbar()
plt.title("Color: fLife")
plt.savefig("points_tSNE_x4.png", dpi=100)
#plt.show()
#Show fIntelligence
plt.figure(figsize=(19.2, 10.8))
plt.scatter(vis_x[:howManyShow], vis_y[:howManyShow], c=x_5[:howManyShow])
plt.colorbar()
plt.title("Color: fIntelligence")
plt.savefig("points_tSNE_x5.png", dpi=100)
#plt.show()
#Show fCivilization
plt.figure(figsize=(19.2, 10.8))
plt.scatter(vis_x[:howManyShow], vis_y[:howManyShow], c=x_6[:howManyShow])
plt.colorbar()
plt.title("Color: fCivilization")
plt.savefig("points_tSNE_x6.png", dpi=100)
#plt.show()
#Show Longevity
plt.figure(figsize=(19.2, 10.8))
plt.scatter(vis_x[:howManyShow], vis_y[:howManyShow], c=x_7[:howManyShow])
plt.colorbar()
plt.title("Color: Longevity")
plt.savefig("points_tSNE_x7_L.png", dpi=100)
#plt.show()
#Show Max Longevity
plt.figure(figsize=(19.2, 10.8))
plt.scatter(vis_x[:howManyShow], vis_y[:howManyShow], c=x_8[:howManyShow])
plt.colorbar()
plt.title("Color: Max Longevity")
plt.savefig("points_tSNE_x8_Lmax.png", dpi=100)
#plt.show()

print("Points drawn and saved...")