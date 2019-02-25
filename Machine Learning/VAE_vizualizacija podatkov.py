'''
Original code: https://github.com/keras-team/keras/blob/master/examples/variational_autoencoder.py

The VAE has a modular design. The encoder, decoder and VAE
are 3 models that share weights. After training the VAE model,
the encoder can be used to  generate latent vectors.
The decoder can be used to generate MNIST digits by sampling the
latent vector from a Gaussian distribution with mean=0 and std=1.
'''

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from keras.layers import Lambda, Input, Dense
from keras.models import Model
from keras.datasets import mnist
from keras.losses import mse, binary_crossentropy, mean_squared_error, mean_squared_logarithmic_error
from keras.utils import plot_model
from keras import backend as K

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
## Nek magic trik
'''''
# reparameterization trick
# instead of sampling from Q(z|X), sample eps = N(0,I)
# z = z_mean + sqrt(var)*eps
def sampling(args):
    """Reparameterization trick by sampling fr an isotropic unit Gaussian.
    # Arguments:
        args (tensor): mean and log of variance of Q(z|X)
    # Returns:
        z (tensor): sampled latent vector
    """

    z_mean, z_log_var = args
    batch = K.shape(z_mean)[0]
    dim = K.int_shape(z_mean)[1]
    # by default, random_normal has mean=0 and std=1.0
    epsilon = K.random_normal(shape=(batch, dim))
    return z_mean + K.exp(0.5 * z_log_var) * epsilon

'''''
## Setting ML parameters
'''''

original_dim = 9
batch_size = 2500       #size of no. of vectors going through the ML at one time

input_shape = (original_dim, )
intermediate_dim = 5
latent_dim = 2
epochs = 80             #how many types repeat ML learning with data

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
## Building encoder and decoder for VAE model
'''''
# VAE model = encoder + decoder

# build encoder model
inputs = Input(shape=input_shape, name='encoder_input')
x = Dense(intermediate_dim, activation='relu')(inputs)
z_mean = Dense(latent_dim, name='z_mean')(x)
z_log_var = Dense(latent_dim, name='z_log_var')(x)

# use reparameterization trick to push the sampling out as input
# note that "output_shape" isn't necessary with the TensorFlow backend
z = Lambda(sampling, output_shape=(latent_dim,), name='z')([z_mean, z_log_var])

# instantiate encoder model
encoder = Model(inputs, [z_mean, z_log_var, z], name='encoder')
encoder.summary()
#plot_model(encoder, to_file='vae_mlp_encoder.png', show_shapes=True)

# build decoder model
latent_inputs = Input(shape=(latent_dim,), name='z_sampling')
x = Dense(intermediate_dim, activation='relu')(latent_inputs)
outputs = Dense(original_dim, activation='sigmoid')(x)

# instantiate decoder model
decoder = Model(latent_inputs, outputs, name='decoder')
decoder.summary()
#plot_model(decoder, to_file='vae_mlp_decoder.png', show_shapes=True)

# instantiate VAE model
outputs = decoder(encoder(inputs)[2])
vae = Model(inputs, outputs, name='vae_mlp')


'''''
## Some magic stuff
'''''
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    help_ = "Load h5 model trained weights"
    parser.add_argument("-w", "--weights", help=help_)
    help_ = "Use mse loss instead of binary cross entropy (default)"
    parser.add_argument("-m",
                        "--mse",
                        help=help_, action='store_true')
    args = parser.parse_args()
    models = (encoder, decoder)
    data = (x_train, y_train)

    # VAE loss = mse_loss or xent_loss + kl_loss

    #reconstruction_loss = mean_squared_logarithmic_error(inputs, outputs)
    #reconstruction_loss = binary_crossentropy(inputs, outputs)
    reconstruction_loss = mean_squared_error(inputs, outputs)
    #reconstruction_loss = mse(inputs, outputs)
    '''
    if args.mse:
        reconstruction_loss = mse(inputs, outputs)
    else:
        reconstruction_loss = binary_crossentropy(inputs, outputs)
     '''

    reconstruction_loss *= original_dim
    kl_loss = 1 + z_log_var - K.square(z_mean) - K.exp(z_log_var)
    kl_loss = K.sum(kl_loss, axis=-1)
    kl_loss *= -0.5
    vae_loss = K.mean(reconstruction_loss + kl_loss)
    vae.add_loss(vae_loss)
    vae.compile(optimizer='adam')
    vae.summary()
    #plot_model(vae, to_file='vae_mlp.png', show_shapes=True)

'''''
## Training Autoencoder
'''''
if args.weights:
    vae.load_weights(args.weights)
else:
    # train the autoencoder
    vae.fit(x_train,
            epochs=epochs,
            batch_size=batch_size)
    vae.save_weights('vae_mlp_mnist.h5')

'''''
## Draw results
'''''
print("Drawing points...")

z_mean, _, _ = encoder.predict(x_train, batch_size=batch_size)

#Show N
#plt.figure(figsize=(12, 10))
plt.figure(figsize=(19.2, 10.8))
plt.scatter(z_mean[:, 0], z_mean[:, 1], c=y_train)
plt.colorbar()
plt.xlabel("z[0]")
plt.ylabel("z[1]")
plt.title("Color: log(N)")
plt.savefig("points_VAE_N.png", dpi=100)
plt.show()
#Show rStar
plt.figure(figsize=(19.2, 10.8))
plt.scatter(z_mean[:, 0], z_mean[:, 1], c=x_1)
plt.colorbar()
plt.xlabel("z[0]")
plt.ylabel("z[1]")
plt.title("Color: rStar")
plt.savefig("points_VAE_x1.png", dpi=100)
#plt.show()
#Show fPlanets
plt.figure(figsize=(19.2, 10.8))
plt.scatter(z_mean[:, 0], z_mean[:, 1], c=x_2)
plt.colorbar()
plt.xlabel("z[0]")
plt.ylabel("z[1]")
plt.title("Color: fPlanets")
plt.savefig("points_VAE_x2.png", dpi=100)
#plt.show()
#Show nEnvironment
plt.figure(figsize=(19.2, 10.8))
plt.scatter(z_mean[:, 0], z_mean[:, 1], c=x_3)
plt.colorbar()
plt.xlabel("z[0]")
plt.ylabel("z[1]")
plt.title("Color: nEnvironment")
plt.savefig("points_VAE_x3.png", dpi=100)
#plt.show()
#Show fLife
plt.figure(figsize=(19.2, 10.8))
plt.scatter(z_mean[:, 0], z_mean[:, 1], c=x_4)
plt.colorbar()
plt.xlabel("z[0]")
plt.ylabel("z[1]")
plt.title("Color: fLife")
plt.savefig("points_VAE_x4.png", dpi=100)
#plt.show()
#Show fIntelligence
plt.figure(figsize=(19.2, 10.8))
plt.scatter(z_mean[:, 0], z_mean[:, 1], c=x_5)
plt.colorbar()
plt.xlabel("z[0]")
plt.ylabel("z[1]")
plt.title("Color: fIntelligence")
plt.savefig("points_VAE_x5.png", dpi=100)
#plt.show()
#Show fCivilization
plt.figure(figsize=(19.2, 10.8))
plt.scatter(z_mean[:, 0], z_mean[:, 1], c=x_6)
plt.colorbar()
plt.xlabel("z[0]")
plt.ylabel("z[1]")
plt.title("Color: fCivilization")
plt.savefig("points_VAE_x6.png", dpi=100)
#plt.show()
#Show Longevity
plt.figure(figsize=(19.2, 10.8))
plt.scatter(z_mean[:, 0], z_mean[:, 1], c=x_7)
plt.colorbar()
plt.xlabel("z[0]")
plt.ylabel("z[1]")
plt.title("Color: Longevity")
plt.savefig("points_VAE_x7_L.png", dpi=100)
#plt.show()
#Show Max Longevity
plt.figure(figsize=(19.2, 10.8))
plt.scatter(z_mean[:, 0], z_mean[:, 1], c=x_8)
plt.colorbar()
plt.xlabel("z[0]")
plt.ylabel("z[1]")
plt.title("Color: Max Longevity")
plt.savefig("points_VAE_x8_Lmax.png", dpi=100)
#plt.show()
print("Points drawn and saved...")