#
# Script to rename and create data for TensorFlow
#
# Tutorial: https://www.tensorflow.org/tutorials/images/classification
#


from os import listdir, rename
from os.path import isfile, join



PATH = ''

train_dir = os.path.join(PATH, 'train')
validation_dir = os.path.join(PATH, 'validation')

train_right_dir = os.path.join(train_dir, 'right')  # directory with our training cat pictures
train_left_dir = os.path.join(train_dir, 'left')  # directory with our training dog pictures
validation_right_dir = os.path.join(validation_dir, 'right')  # directory with our validation cat pictures
validation_left_dir = os.path.join(validation_dir, 'left')  # directory with our validation dog pictures


def folder_rename(path, name):
    # renames all files from 0 to x with format 'name{0}.jpg'
    for count, filename in enumerate(os.listdir(path)):
        # get extension
        ext = filename[-3:]
        
        # set up new file name
        dst = "{0}/{1}{2}.{3}".format(path, name, count-1, ext)

        # set up old file name
        src = "{0}/{1}".format(path, filename)

        # rename files
        rename()
        
        
