#!/usr/bin/env python3
"""The primary file that builds and trains the neural network.

This script assumes that convert.py has been run and Skott1.csv to
Skott20.csv are in training/ and Skott21.csv to Skott25.csv are in
test/
"""
from keras.models import Sequential
from keras.layers import Dense, Activation, LSTM
import numpy as np
import scipy as sp

# Generate training dataset
data = np.genfromtxt('./training/Skott1.csv', delimiter=',')
data = np.swapaxes(data, 0, 1)
train_X = np.array([data[0], data[1], data[3]])
train_y = data[4]

# Generate testing dataset
data1 = np.genfromtxt('./training/Skott2.csv', delimiter=',')
data1 = np.swapaxes(data1, 0, 1)
test_X = np.array([data1[0], data1[1], data1[3]])
test_y = data1[1]

model = Sequential()
model.add(LSTM(50, input_shape=(train_X.shape[1], train_X.shape[2])))
model.add(Dense(1))
model.compile(loss='mae', optimizer='adam')
# fit network
history = model.fit(train_X, train_y, epochs=50, batch_size=72, validation_data=(test_X, test_y), verbose=2, shuffle=False)
