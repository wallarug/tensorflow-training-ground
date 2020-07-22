#
# Script to rename and create data for TensorFlow
#

from os import listdir, rename, listdir
from os.path import isfile, join
from pathlib import Path

PATH = "/Users/cianb/Documents/repos/wallarug/tensorflow-training-ground/turn_signs_color_filtered/train/left"
FILE_NAME = "left"

"""
    Pre-Process Proceedure
    1.  Rename files to correct format
    2.  Flip Horizontal and put into correct directory
    3.  Split into train and validation (75/25)

"""


#train_dir = os.path.join(PATH, 'train')
#validation_dir = os.path.join(PATH, 'validation')


def folder_rename(path, name):
    # renames all files from 0 to x with format 'name{0}.jpg'
    for count, filename in enumerate(listdir(path)):
        # get extension
        ext = filename[-3:]
        
        # set up new file name
        dst = "{0}/{1}{2}.{3}".format(path, name, count, ext)

        # set up old file name
        src = "{0}/{1}".format(path, filename)

        if src == dst:
            print("file already exists")
            continue

        # rename files
        rename(src, dst)
        #print(src, dst)
        
        
folder_rename(Path(PATH),FILE_NAME)

