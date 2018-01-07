#!/usr/bin/env python3
"""
The primary file that builds and trains the neural network.
"""
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import Adam
import numpy as np

# Generate dataset
train_data = np.swapaxes(np.genfromtxt('./data.csv', delimiter=','), 0, 1)
multipliers = train_data[:, 0]
train_data = np.delete(train_data, 0, axis=1)
train_X = np.swapaxes(np.array([train_data[0], train_data[1]]), 0, 1)
train_y = np.swapaxes(np.array([train_data[3], train_data[4]]), 0, 1)

# Define the neural network
model = Sequential()

model.add(Dense(2, input_dim=2, kernel_initializer='zeros', activation='sigmoid'))
model.add(Dense(units=10, kernel_initializer='zeros', activation='sigmoid'))
model.add(Dense(units=20, kernel_initializer='zeros', activation='sigmoid'))
model.add(Dense(units=10, kernel_initializer='zeros', activation='sigmoid'))
model.add(Dense(units=2, kernel_initializer='zeros'))

# Compile the neural network
model.compile(optimizer=Adam(),
              loss='mean_squared_error',
              metrics=['accuracy'])

# Fit the neural network to data
model.fit(train_X, train_y, epochs=10, batch_size=1, verbose=1, shuffle=True, validation_split=0.01)

model.save('trained_model.h5')
