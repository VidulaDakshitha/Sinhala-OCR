import cv2
import numpy as np
# Authored by Kevin Gomez to detect string areas in a blank form

def getQuestionMask(image):
    # creating a new array
    mask = np.ones(image.shape, dtype=np.uint8) * 255
    # making image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # thresholding the gray image, then white => black, black => white
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    # getting the contours of dilate image
    cnts = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    # getting the boundaries of rectangle
    for c in cnts:
        area = cv2.contourArea(c)
        if area < 80000:
            x, y, w, h = cv2.boundingRect(c)
            mask[y:y + h, x:x + w] = image[y:y + h, x:x + w]

    # returning final mask
    return mask

def getQuestionContours(image):
    mask = getQuestionMask(image)
    # converting the mask into grayscale and smoothing it
    gray_mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    gray_mask = cv2.medianBlur(gray_mask, 5)
    # a bit sharpening and thresholding
    thresh_mask = cv2.adaptiveThreshold(gray_mask, 255, 1, 1, 11, 2)
    # closing operation to detect the area of questions
    thresh_mask = cv2.dilate(thresh_mask, None, iterations=15)
    thresh_mask = cv2.erode(thresh_mask, None, iterations=15)
    # finding the contours of questions
    contours, hierarchy = cv2.findContours(thresh_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    length = len(contours)
    contours[length - 1] = None
    contours[length - 2] = None

    return contours

def reorderImages(imageList):
    new_list = []
    count = 0
    for a in reversed(imageList):
        new_list.append(a)
        count = count + 1
    return new_list