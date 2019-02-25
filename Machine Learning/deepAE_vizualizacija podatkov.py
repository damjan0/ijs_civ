from keras.layers import Input, Dense
from keras.models import Model, Sequential
from keras.losses import mean_squared_error, mean_squared_logarithmic_error

import numpy as np
import matplotlib.pyplot as plt
import argparse
import os
import math
import csv


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
## Setting ML parameters
'''''

original_dim = 9
batch_size = 2500       #size of no. of vectors going through the ML at one time

input_shape = Input(shape=(original_dim,))

intermediate_dim = 6
intermediate_dim_2 = 4
encoded_dim = 2
epochs = 100            #how many types repeat ML learning with data

'''''
## Load our DATASET from .csv
'''''
file = 'points4.csv'

x_train = []
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


'''''
## Building encoder and decoder
'''''

print("1...")
encoded = Dense(intermediate_dim, activation='relu')(input_shape)
encoded = Dense(intermediate_dim_2, activation='relu')(encoded)
encoded = Dense(encoded_dim, activation='relu')(encoded)
'''''
encoded = Dense(encoded_dim, activation='relu')(input_shape)
'''''
print("2...")

decoded = Dense(intermediate_dim_2, activation='relu')(encoded)
decoded = Dense(intermediate_dim, activation='relu')(decoded)
decoded = Dense(original_dim, activation='sigmoid')(decoded)

autoencoder = Model(input_shape, decoded)
#autoencoder.compile(optimizer='adam', loss='binary_crossentropy')
autoencoder.compile(optimizer='adam', loss='mean_squared_error')
autoencoder.summary()
encoder = Model(input_shape, encoded)
#encoder.compile(optimizer='adadelta', loss='binary_crossentropy')
encoder.compile(optimizer='adam', loss='mean_squared_error')
encoder.summary()
print("3...")
'''''
## Some magic stuff
'''''


'''''
## Training Autoencoder
'''''
print("Training deep autoencoder...")
autoencoder.fit(x_train,x_train,
               epochs=epochs,
                batch_size=batch_size,
                shuffle=True)

'''''
## Draw results
'''''
print("Drawing points...")

a = encoder.predict(x_train, batch_size=batch_size)
a1 = a[:, 0]
a2 = a[:, 1]
#print(a)
#print(a1)
#print(a2)
#Show N
#plt.figure(figsize=(12, 10))
plt.figure(figsize=(19.2, 10.8))
plt.scatter(a1, a2, c=y_train)
plt.colorbar()
plt.title("Color: log(N)")
plt.savefig("points_deepAE_N.png", dpi=100)
#plt.show()
#Show rStar
plt.figure(figsize=(19.2, 10.8))
plt.scatter(a1, a2, c=x_1)
plt.colorbar()
plt.title("Color: rStar")
plt.savefig("points_deepAE_x1.png", dpi=100)
#plt.show()

#Show fPlanets
plt.figure(figsize=(19.2, 10.8))
plt.scatter(a1, a2, c=x_2)
plt.colorbar()
plt.title("Color: fPlanets")
plt.savefig("points_deepAE_x2.png", dpi=100)
#plt.show()
#Show nEnvironment
plt.figure(figsize=(19.2, 10.8))
plt.scatter(a1, a2, c=x_3)
plt.colorbar()
plt.title("Color: nEnvironment")
plt.savefig("points_deepAE_x3.png", dpi=100)
#plt.show()
#Show fLife
plt.figure(figsize=(19.2, 10.8))
plt.scatter(a1, a2, c=x_4)
plt.colorbar()
plt.title("Color: fLife")
plt.savefig("points_deepAE_x4.png", dpi=100)
#plt.show()
#Show fIntelligence
plt.figure(figsize=(19.2, 10.8))
plt.scatter(a1, a2, c=x_5)
plt.colorbar()
plt.title("Color: fIntelligence")
plt.savefig("points_deepAE_x5.png", dpi=100)
#plt.show()
#Show fCivilization
plt.figure(figsize=(19.2, 10.8))
plt.scatter(a1, a2, c=x_6)
plt.colorbar()
plt.title("Color: fCivilization")
plt.savefig("points_deepAE_x6.png", dpi=100)
#plt.show()
#Show Longevity
plt.figure(figsize=(19.2, 10.8))
plt.scatter(a1, a2, c=x_7)
plt.colorbar()
plt.title("Color: Longevity")
plt.savefig("points_deepAE_x7_L.png", dpi=100)
#plt.show()
#Show Max Longevity
plt.figure(figsize=(19.2, 10.8))
plt.scatter(a1, a2, c=x_8)
plt.colorbar()
plt.title("Color: Max Longevity")
plt.savefig("points_deepAE_x8_Lmax.png", dpi=100)
#plt.show()
print("Points drawn and saved...")
