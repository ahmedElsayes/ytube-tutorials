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
for i, e in enumerate(fehrenhiet):
    print('{} degree celcius = {} degree fehrenhiet'.format(celcius[i], e))

# the training network should have features(inputs), labels(outputs), number of neurons per layer, number of hidden layers

# 1- building the network layers
NW = tf.keras.layers.Dense(units=1, input_shape=[1]) # the network is composed of only one layer

# 2- building the model to assemble the layers
model = tf. keras.Sequential([NW])

# 3- compiling the model by defining the loss function and the optimization parameters
# 0.1 is the learning rate usually it is value in range from 0.001 to 0.1
model.compile(loss='mean_squared_error',
              optimizer=tf.keras.optimizers.Adam(0.1))

# 4- training the model
history = model.fit(celcius, fehrenhiet, epochs=500, verbose=False)
print('the model has been trained')

# matplot for ploting the results
plt.xlabel('Epoch Number')
plt.ylabel("Loss Magnitude")
plt.plot(history.history['loss'])
plt.show()
# plt.savefig('loss.png')
# testing the trained network by feeding an new input
print('the predicted output for input = 100 is ', model.predict([100.0]))


