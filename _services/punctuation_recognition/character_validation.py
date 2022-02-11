# import the necessary packages
from skimage.metrics import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2
import environ

env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env()


def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err


def compare_images(imageA, imageB):
    # compute the mean squared error and structural similarity
    # index for the images
    m = mse(imageA, imageB)
    s = ssim(imageA, imageB)
    return s


def check_punct(image):
    for x in range(2):
        image2 = cv2.imread(env('PROJECT_SRC') + "_services/punctuation_recognition/" + str(x) + ".png")
        original = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
        #contrast = cv2.cvtColor(cv2.resize(image, (64, 64)), cv2.COLOR_BGR2GRAY)
        comparision = compare_images(original,cv2.resize(image, (64, 64)))
        print(comparision)
        if comparision > 0.80:
            print("it bacame trueeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
            return True
        else:
            return False
