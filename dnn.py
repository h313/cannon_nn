#!/usr/bin/env python3
"""The primary file that builds and trains the neural network.

This script assumes that convert.py has been run and Skott1.csv to
Skott20.csv are in training/ and Skott21.csv to Skott25.csv are in
test/
"""
from keras.models import Sequential
from keras.layers import Dense, Activation
import numpy as np
import scipy as sp

# Generate training dataset
data = np.genfromtxt('./training/Skott1.csv', delimiter=',')
data = np.swapaxes(data, 0, 1)
train_X = np.swapaxes(np.array([data[0], data[1], data[3]]), 0, 1)
train_y = np.array(data[4])

# Generate testing dataset
data1 = np.genfromtxt('./training/Skott2.csv', delimiter=',')
data1 = np.swapaxes(data1, 0, 1)
test_X = np.swapaxes(np.array([data1[0], data1[1], data1[3]]), 0, 1)
print(test_X)
test_y = np.array(data1[1])

model = Sequential([
    Dense(3, input_shape=(3,)),
    Activation('relu'),
    Dense(10),
    Activation('softmax'),
    Dense(10),
    Activation('softmax'),
    Dense(1),
    Activation('sigmoid'),
])

model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# fit network
model.fit(train_X, train_y, epochs=10, batch_size=32)
