import numpy as np
import cv2

def getAnswerMask(image):
    mask = np.ones(image.shape, dtype=np.uint8) * 255
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    cnts = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    for c in cnts:
        area = cv2.contourArea(c)
        # finding the strings and keeping only them in the mask image
        if area < 11000:
            x, y, w, h = cv2.boundingRect(c)
            mask[y:y + h, x:x + w] = image[y:y + h, x:x + w]
    return mask

def getAnswerAreaContour(image):
    count = 1
    mask = getAnswerMask(image)
    # subtract the mask from original image to keep only the box areas
    answer_area = cv2.subtract(mask, image)
    imgBlur = cv2.GaussianBlur(answer_area, (9, 9), 2)
    gray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)
    contours_answer, h = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cont_return = []
    for cnt in contours_answer:
        if not cnt is None:
            area = cv2.contourArea(cnt)
            if area > 40000:
                x, y, w, h = cv2.boundingRect(cnt)
                cont_return.append([x, y, w, h])
    length = len(cont_return)
    # cont_return[length - 1] = None
    return cont_return

def getStringContours(image):
    # horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 1))
    # detected_lines = cv2.morphologyEx(image, cv2.MORPH_OPEN, horizontal_kernel, iterations=2)
    # cnts = cv2.findContours(detected_lines, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    # for c in cnts:
    #     cv2.drawContours(image, [c], -1, (0, 0, 0), 2)
    #
    # vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 10))
    # detected_lines = cv2.morphologyEx(image, cv2.MORPH_OPEN, vertical_kernel, iterations=2)
    # cnts = cv2.findContours(detected_lines, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    # for c in cnts:
    #     cv2.drawContours(image, [c], -1, (0, 0, 0), 2)
    mask = np.ones(image.shape, dtype=np.uint8) * 255
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    cnts = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    for c in cnts:
        area = cv2.contourArea(c)
        if area < 11000:
            x, y, w, h = cv2.boundingRect(c)
            mask[y:y + h, x:x + w] = image[y:y + h, x:x + w]
    gray_mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    gray_mask = cv2.medianBlur(gray_mask, 5)
    thresh_mask = cv2.adaptiveThreshold(gray_mask, 255, 1, 1, 11, 2)
    thresh_mask = cv2.dilate(thresh_mask, None, iterations=15)
    thresh_mask = cv2.erode(thresh_mask, None, iterations=15)
    contours, hierarchy = cv2.findContours(thresh_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    string_cont = []

    for cnt in contours:
        if not cnt is None:
            x, y, w, h = cv2.boundingRect(cnt)
            string_cont.append([x,y,w,h])

    return string_cont

def clearImage(image):
    # getting only the strings
    got_contours = getStringContours(image)

    mask = np.ones(image.shape, dtype=np.uint8) * 255
    for c in got_contours:
        x, y, w, h = c[0], c[1], c[2], c[3]
        mask[y:y + h, x:x + w] = image[y:y + h, x:x + w]
    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    return mask