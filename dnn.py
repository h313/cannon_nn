#!/usr/bin/env python3
"""
The primary file that builds and trains the neural network.
"""
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import Nadam
import numpy as np

# Generate dataset
'''
The dataset is a .csv consisting of 5 variables - time, charge weight, shot weight, velocity, and r
Each of these variables are normalized, i.e. each value is divided by the largest of its value
This allows the neural network to work with the values using sigmoid activation.
'''
train_data = np.swapaxes(np.genfromtxt('./data.csv', delimiter=','), 0, 1)
# Remove the first line of the csv, which is used to convert the normalized variables back
multipliers = train_data[:, 0]
train_data = np.delete(train_data, 0, axis=1)
# Convert the training data into two arrays, one of input data and one of output data
train_X = np.swapaxes(np.array([train_data[0], train_data[1]]), 0, 1)
train_y = np.swapaxes(np.array([train_data[2], train_data[3], train_data[4]]), 0, 1)

# Define the neural network
model = Sequential()
'''
The neural network is a dense network consisting of three hidden layers of 10, 20, and 10 neurons respectively
Each of these networks use a Sigmoid activation function, 1/(1+e^(-x))
The input and output layers consist of two units, one for each input and output variable
'''
model.add(Dense(2, input_dim=2, kernel_initializer='zeros', activation='sigmoid'))
model.add(Dense(units=10, kernel_initializer='zeros', activation='sigmoid'))
model.add(Dense(units=20, kernel_initializer='zeros', activation='sigmoid'))
model.add(Dense(units=10, kernel_initializer='zeros', activation='sigmoid'))
model.add(Dense(units=3, kernel_initializer='zeros'))

# Compile the neural network
'''
The Adaptive Moment Estimation (Adam) optimizer with Nesterov momentum  was used to train the network, as RMSprop and 
SGD did not have the necessary momentum to overcome a local minima at loss=0.0350, and RMSprop converged faster than
SGD. Therefore, we decided that the Adam optimizer, which is essentially RMSprop with momentum, was the best choice for
this neural network.
Adam is a type of gradient descent optimizer, where for each neuron a gradient G is found where
G = -(E df/ds) * O
where E is the error of the entire network, df/ds is the derivative of the activation function (sigmoid in this
case), and O is the output of the node. The gradient can then be used along with momentum to change weights
to minimize error. Using Adam, our mean-squared-error during the verification phrase is on the power of 10^-4,
which for this specific excercise is practically 0.
MSE is used as the loss function as it is the most commonly used one in such networks.
'''
model.compile(optimizer=Nadam(),
              loss='mean_squared_error',
              metrics=['accuracy'])

# Train the neural network using cannon data
'''
The data is fitted one at a time, and repeats 10 times to attain a loss in the 4th decimal place
Each epoch (or iteration), the data is shuffled before being used in backpropogation
1% of the data is also randomly chosen per epoch to act as verification data
'''
model.fit(train_X, train_y, epochs=10, batch_size=1, verbose=1, shuffle=True, validation_split=0.01)

# Save the trained neural network to a hdf5 file
model.save('trained_model.h5')
