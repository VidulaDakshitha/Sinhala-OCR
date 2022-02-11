import numpy as np
import cv2
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input
from _services.Handwritten.string_builder import string_CompuWa0
from _services.Handwritten.string_builder import string_CompuWa1
from _services.Handwritten.string_builder import string_CompuWa2
from _services.Handwritten.string_builder import string_CompuWa3
from _services.Handwritten.string_builder import is_suppotiveLetter

import cv2
from PIL import Image
import uuid

import matplotlib.pyplot as plt
import environ
from _services.Handwritten.handwritten_constants import PADDING_VALUE
from _services.Handwritten.handwritten_constants import R_VALUE
from _services.Handwritten.handwritten_constants import CLASS_INDICES
from _services.Handwritten.handwritten_constants import TRUE_LABEL

env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env()
import tensorflow as tf

sinhala_model = tf.keras.models.load_model(env('PROJECT_SRC') + '_models/Handwritten/model_new.h5')

#IT18045840
#S.D.S.L Diaaanayake


def padding_add(img, padding):
    ht, wd, cc = img.shape

    hh = ht + 2 * padding
    ww = wd + 2 * padding

    color = (cc, cc, cc)
    result = np.full((hh, ww, cc), color, dtype=np.uint8)

    # compute center offset
    xx = (ww - wd) // 2
    yy = (hh - ht) // 2

    # copy img image into center of result image
    result[yy:yy + ht, xx:xx + wd] = img
    return result


def get_class_id(val):
    key_list = list(CLASS_INDICES.keys())
    val_list = list(CLASS_INDICES.values())

    ind = val_list.index(val)
    return key_list[ind]


def gethandwritten_prediction(letter):
    character_image = change_shape(letter)
    ress = aspectratio_change(R_VALUE, character_image)

    # optimal padding value define hear
    image_padded = padding_add(ress, PADDING_VALUE)
    character_image_gray = cv2.cvtColor(image_padded, cv2.COLOR_RGB2GRAY)

    character_image_resize = cv2.resize(character_image_gray, (80, 80), interpolation=cv2.INTER_AREA)

    # unique_filename = str(uuid.uuid4())
    # cv2.imwrite("C:/Users/sathira/OneDrive/Desktop/new_segmetaion/output/" + unique_filename + ".jpg", character_image_resize)

    character_elemet = image.img_to_array(character_image_resize)
    character_elemet_expanded_dims = np.expand_dims(character_elemet, axis=0)

    predictions = sinhala_model.predict(character_elemet_expanded_dims)
    sinhala_prediction = TRUE_LABEL[int(get_class_id(np.argmax(predictions))) - 1]

    return sinhala_prediction


# word builder
def word_builder(word_array):
    print('word_array', word_array)
    n = len(word_array)

    ress0 = string_CompuWa2(word_array)
    ress1 = string_CompuWa1(ress0)
    ress2 = string_CompuWa0(ress1)
    ress3 = string_CompuWa3(ress2)

    ress4 = is_suppotiveLetter(ress3)

    return ress4



def change_shape(img):
    ht, wd, cc = img.shape
    max = 0
    dx = 0
    if ht < wd:
        dx = wd - ht
        hh = ht + dx
        ww = wd
    else:
        dx = ht - wd
        ww = wd + dx
        hh = ht

    color = (cc, cc, cc)
    result = np.full((hh, ww, cc), color, dtype=np.uint8)

    # compute center offset
    xx = (ww - wd) // 2
    yy = (hh - ht) // 2

    # copy img image into center of result image
    result[yy:yy + ht, xx:xx + wd] = img
    return result


def aspectratio_change(scale_percent, img):
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)

    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    return resized
