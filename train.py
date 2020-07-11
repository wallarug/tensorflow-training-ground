#
# Tensorflow 1.15.2
#
#
#

# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

print(tf.__version__)


class_names = ['bad_detection', 'stop', 'turn_left', 'turn_right', 'park']
