#!/usr/bin/env python3
"""
The primary file that builds and trains the neural network.
"""
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import RMSprop
import numpy as np

# Generate dataset
train_data = np.swapaxes(np.genfromtxt('./data.csv', delimiter=','), 0, 1)
train_X = np.swapaxes(np.array([train_data[0], train_data[1]]), 0, 1)
train_y = np.swapaxes(np.array([train_data[2], train_data[3]]), 0, 1)

# Define the neural network
model = Sequential()

model.add(Dense(20, input_dim=2, kernel_initializer='zeros', activation='relu'))
model.add(Dense(units=10, kernel_initializer='zeros', activation='relu'))
model.add(Dense(units=2, kernel_initializer='zeros'))

# Compile the neural network
model.compile(optimizer=RMSprop(lr=0.0001), loss='mean_squared_error', metrics=['binary_accuracy'])

# Fit the neural network to data
model.fit(train_X, train_y, epochs=1, batch_size=1, verbose=1, shuffle=True, validation_split=0.01)

print(model.predict(np.array([[0.0, 0.0], [780.0, 0.7]]), verbose=1))
