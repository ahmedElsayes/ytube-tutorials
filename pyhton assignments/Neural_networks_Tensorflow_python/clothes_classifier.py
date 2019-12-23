# ahmed.elsayes@tuni.fi
from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
import numpy as np
import math
import matplotlib.pyplot as plt
import logging
import tensorflow_datasets as tfds
tfds.disable_progress_bar()

logger = tf.get_logger()
logger.setLevel(logging.ERROR)

# Loading the training set and test set of fashion_mnist
dataset, metadata = tfds.load('fashion_mnist', as_supervised=True, with_info=True)
train_dataset, test_dataset = dataset['train'], dataset['test']

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal',      'Shirt',   'Sneaker',  'Bag',   'Ankle boot']

# To explore the number of training set and data set
num_train_examples = metadata.splits['train'].num_examples
num_test_examples = metadata.splits['test'].num_examples
print("Number of training examples: {}".format(num_train_examples))
print("Number of test examples:     {}".format(num_test_examples))

# Every image has a resolution of (23*23) pixels. Every pixel takes a number in the range from (0 to 255).
# to pre-frocess the dataset by normalizing the pixels
# .......................................................
def normalize(images, labels):
    images = tf.cast(images, tf.float32)    # to reformat each element in the array to float type
    images /= 255       # TO MAKE EACH ELEMETN TAKE A VALUE BETWEEN 0 TO 1
    return images, labels

train_dataset = train_dataset.map(normalize)
test_dataset = test_dataset.map(normalize)
print('the images pixels are normalized')

# The first time you use the dataset, the images will be loaded from disk
# Caching will keep them in memory, making training faster
train_dataset = train_dataset.cache()
test_dataset = test_dataset.cache()

# .........................................................
# to take a single image and remove the color dimension by reshaping

# for image, label in test_dataset.take(1):
#     break
# image = image.numpy().reshape((28,28))
# # to plot the single image
# plt.figure()
# plt.imshow(image, cmap=plt.cm.binary)
# plt.colorbar()
# plt.grid(False)
# plt.show()

# .........................................................
# plt.figure(figsize=(10,10))
# i = 0
# for (image, label) in test_dataset.take(25):
#     image = image.numpy().reshape(28,28)
#     plt.subplot(5,5,i+1)
#     plt.xticks([])        # this is to disable the xticks
#     plt.yticks([])
#     plt.grid(False)
#     plt.imshow(image, cmap=plt.cm.binary)
#     plt.xlabel(class_names[label])
#     i += 1
# plt.show()

# .........................................................
# building the neural network
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28, 1)),
    tf.keras.layers.Dense(128, activation=tf.nn.relu),
    tf.keras.layers.Dense(10,  activation=tf.nn.softmax)
])

# compile the modil and setting the optemization parameter
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
# training the model
BATCH_SIZE = 32     # the idea from Batch size is to accelerate the training process by taking every 32 sample for training
train_dataset = train_dataset.repeat().shuffle(
    num_train_examples).batch(BATCH_SIZE)       # the idea from shuffle is to randomize the selection of the sample to get ultimately higher accuracy for predictions
test_dataset = test_dataset.batch(BATCH_SIZE)
model.fit(train_dataset, epochs=5, steps_per_epoch=math.ceil(
    num_train_examples/BATCH_SIZE))     # model.fit is to initiate the training process

# evaluate the accuracy by testing on the test_dataset
test_loss, test_accuracy = model.evaluate(test_dataset, steps=math.ceil(num_test_examples/32))      # evaluate is determining if the model was able to predict accurately the preknown images of the test_dataset
print('Accuracy on test dataset:', test_accuracy)
