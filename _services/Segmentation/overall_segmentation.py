import sys
import cv2
import numpy as np
from imutils import contours
from matplotlib import pyplot as plt

from _services.Segmentation.character_segmentation import segmentation
from _services.Segmentation.line_segmentation import line_segmentation
from _services.Segmentation.word_segmentation import word_segmentation_preprocess
import environ

env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env()


def preprocessing(image,height_val):
    height, width = image.shape[:2]
    h_ = height_val
    w_ = int((h_ * width) / height)
    image = cv2.resize(image, (w_, h_), interpolation=cv2.INTER_AREA)

    de_noise_image = cv2.fastNlMeansDenoising(image, None, 10, 7, 21)

    thresh = cv2.threshold(de_noise_image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    return thresh


def mainFunc(image,height):
    #var = 'sinhala1.jpg'
    #image = cv2.imread(var, 0)

    # do preprocessing
    thresh = preprocessing(image,height)

    # line segmentation
    lines, original, labeled = line_segmentation(thresh)

    # cv2.imshow("Line labeled", labeled)
    # # # show segmented lines
    # for i, image in enumerate(lines):
    #     cv2.imshow(str(i), image)
    #     cv2.waitKey()
    #     cv2.destroyAllWindows()

    # word segmentation
    words=word_segmentation_preprocess(lines)

    # for i,line in enumerate(words):
    #     for j,word in enumerate(line):
    #         cv2.imshow(str(i)+str(j),word)
    #         cv2.waitKey()
    #         cv2.destroyAllWindows()

    # character segmentation
    chars,words_structure=segmentation(words)

    result_line=[]
    result_word = []
    result_char = []
    for i, line in enumerate(chars):
        result_word = []
        for j, word in enumerate(line):
            result_char = []
            for k, char in enumerate(word):
                # cv2.imwrite(env('PROJECT_SRC')+'_services/Segmentation/questions/'+str(i) + "," + str(j) + "," + str(k)+'.png', char)
                result_char.append(char)
            result_word.append(result_char)
        result_line.append(result_word)
    return result_line;



