#
# Tensorflow 1.15.2
#
# Tutorial: https://www.tensorflow.org/tutorials/keras/classification
#

# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

print(tf.__version__)

# set up class names
class_names = ['bad_detection', 'stop', 'turn_left', 'turn_right', 'park']


# load data
## TODO


# preprocess the data
## Make sure that the pixel values are in range 0 to 1 before feeding them
##  to the neural network model.


# Build the model - layers

## TODO - change the input_shape and last layer to number of classes (10 atm)
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10)
])

# Build the model - compile
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])


# Train the model
model.fit(train_images, train_labels, epochs=10)

# Optional:  Evaluate accuracy
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

print('\nTest accuracy:', test_acc)



### USING MODEL ###

# make predictions
probability_model = tf.keras.Sequential([model, 
                                         tf.keras.layers.Softmax()])

predictions = probability_model.predict(test_images)

np.argmax(predictions[0])  # which item index

# use model
## Grab image
img = test_images[0]

print(img.shape)

## Add the image to a batch where it's the only member.
img = (np.expand_dims(img,0))

predictions_single = probability_model.predict(img)

print(predictions_single)

np.argmax(predictions_single[0])
