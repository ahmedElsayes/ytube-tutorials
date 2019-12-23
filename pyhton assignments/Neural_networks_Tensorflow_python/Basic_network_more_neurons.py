# ahmed.elsayes@tuni.fi
from __future__ import absolute_import, division, print_function, unicode_literals
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import logging
logger = tf.get_logger()
logger.setLevel(logging.ERROR)

celcius = np.array([-40, -10,  0,  8, 15, 22,  38], dtype=float)
fehrenhiet = np.array([-40,  14, 32, 46, 59, 72, 100], dtype=float)
# create network layers
l0 = tf.keras.layers.Dense(units=4, input_shape=[1])
l1 = tf.keras.layers.Dense(units=4)
l2 = tf.keras.layers.Dense(units=1)

# assemble the layers
model = tf.keras.Sequential([l0, l1, l2])

# compile and set the optimization parameters
model.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.Adam(0.1))

# Train the network
model.fit(celcius, fehrenhiet, epochs=500, verbose=False)
print("Finished training the model")
print(model.predict([100.0]))
print("Model predicts that 100 degrees Celsius is: {} degrees Fahrenheit".format(model.predict([100.0])))
print("These are the l0 variables: {}".format(l0.get_weights()))
print("These are the l1 variables: {}".format(l1.get_weights()))
print("These are the l2 variables: {}".format(l2.get_weights()))
