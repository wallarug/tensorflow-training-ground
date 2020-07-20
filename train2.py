#
# Tensorflow 1.15.2
#
# Tutorial: https://www.tensorflow.org/tutorials/images/classification
#


from os import listdir
from os.path import isfile, join

# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

print(tf.__version__)

PATH = ''

train_dir = os.path.join(PATH, 'train')
validation_dir = os.path.join(PATH, 'validation')

train_right_dir = os.path.join(train_dir, 'right')  # directory with our training cat pictures
train_left_dir = os.path.join(train_dir, 'left')  # directory with our training dog pictures
validation_right_dir = os.path.join(validation_dir, 'right')  # directory with our validation cat pictures
validation_left_dir = os.path.join(validation_dir, 'left')  # directory with our validation dog pictures

num_right_tr = len(os.listdir(train_right_dir))
num_left_tr = len(os.listdir(train_left_dir))

num_right_val = len(os.listdir(validation_right_dir))
num_left_val = len(os.listdir(validation_left_dir))

total_train = num_right_tr + num_left_tr
total_val = num_right_val + num_left_val

print('total training right images:', num_right_tr)
print('total training left images:', num_left_tr)

print('total validation right images:', num_right_val)
print('total validation left images:', num_left_val)
print("--")
print("Total training images:", total_train)
print("Total validation images:", total_val)

train_image_generator = ImageDataGenerator(rescale=1./255) # Generator for our training data
validation_image_generator = ImageDataGenerator(rescale=1./255) # Generator for our validation data

# variables
batch_size = 128
epochs = 15
IMG_HEIGHT = 40
IMG_WIDTH = 40

train_data_gen = train_image_generator.flow_from_directory(batch_size=batch_size,
                                                           directory=train_dir,
                                                           shuffle=True,
                                                           target_size=(IMG_HEIGHT, IMG_WIDTH),
                                                           class_mode='binary')

val_data_gen = validation_image_generator.flow_from_directory(batch_size=batch_size,
                                                              directory=validation_dir,
                                                              target_size=(IMG_HEIGHT, IMG_WIDTH),
                                                              class_mode='binary')


# train the model
model = Sequential([
    Conv2D(16, 3, padding='same', activation='relu', input_shape=(IMG_HEIGHT, IMG_WIDTH ,3)),
    MaxPooling2D(),
    Conv2D(32, 3, padding='same', activation='relu'),
    MaxPooling2D(),
    Conv2D(64, 3, padding='same', activation='relu'),
    MaxPooling2D(),
    Flatten(),
    Dense(512, activation='relu'),
    Dense(1)
])

model.compile(optimizer='adam',
              loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
              metrics=['accuracy'])


history = model.fit_generator(
    train_data_gen,
    steps_per_epoch=total_train // batch_size,
    epochs=epochs,
    validation_data=val_data_gen,
    validation_steps=total_val // batch_size
)
