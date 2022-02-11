import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input
from PIL import ImageFont, ImageDraw, Image
import cv2
import numpy as np
# import openpyxl
import matplotlib.pyplot as plt
import environ

env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env()


new_model = tf.keras.models.load_model(env('PROJECT_SRC')+'_models/punctuation/output.h5')
cars = ["(",",", "!", ".","!","?","-",'"', '"', ")"]


def preProcessing(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.equalizeHist(img)
    img = img/255
    return img

def image_resizing(image):
    ht, wd, cc = image.shape

    # create new image of desired size and color (blue) for padding
    ww = 250
    hh = 250
    color = (0, 0, 0)
    result = np.full((hh, ww, cc), 0, dtype=np.uint8)

    # compute center offset
    xx = (ww - wd) // 2
    yy = (hh - ht) // 2

    # copy img image into center of result image
    result[yy:yy + ht, xx:xx + wd] = image

    result = cv2.resize(result, (128, 128))
    return result







def punctuation_main(image2):
    result = image_resizing(image2)
    img = preProcessing(result)
    img_array = image.img_to_array(img)
    img_batch = np.expand_dims(img_array, axis=0)
    # img_preprocessed = preprocess_input(img_batch)

    prediction = new_model.predict(img_batch)

    pred = np.argmax(prediction[0], np.newaxis)
    pred_1 = np.amax(prediction)

    # print(np.amax(prediction) * 100)
    # print(pred)
    print(cars[pred])
    return cars[pred]

