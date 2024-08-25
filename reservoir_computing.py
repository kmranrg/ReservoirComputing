# -*- coding: utf-8 -*-
"""Reservoir_Computing.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tfY1buqmR0yKcMp4sndNNlWqViWlIdU_
"""

# installing the module
!pip install reservoirpy

# importing the libraries
import numpy as np
import matplotlib.pyplot as plt
from reservoirpy.nodes import Reservoir, Ridge
from reservoirpy.datasets import mackey_glass
from sklearn.metrics import mean_squared_error

# loading the Mackey-Glass time series data
data = mackey_glass(n_timesteps=2000)

# printing the data
print("First 10 values of data:")
print(data[:10])
print("\nLast 10 values of data:")
print(data[-10:])

# splitting the data into training and testing sets
train_data, test_data = data[:1500], data[1500:]

# creating a reservoir with 100 units and a spectral radius of 0.9
reservoir = Reservoir(100, sr=0.9)

# collecting reservoir states by running the training data through the reservoir
states = reservoir.run(train_data[:-1])

# training the output layer using the Ridge regression from reservoirpy
readout = Ridge()
readout = readout.fit(states, train_data[1:])

# using the model to make predictions
test_states = reservoir.run(test_data[:-1])
predicted = readout.run(test_states)

# plotting the results
plt.figure(figsize=(10, 6))
plt.plot(test_data[1:], label="True Data")
plt.plot(predicted, label="Predicted Data")
plt.legend()
plt.title("Mackey-Glass Time Series Prediction")
plt.show()

# calculating the Mean Squared Error
mse = mean_squared_error(test_data[1:], predicted)
print(f"Mean Squared Error: {mse}")