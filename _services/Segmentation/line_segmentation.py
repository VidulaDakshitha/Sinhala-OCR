import cv2
import numpy as np
from imutils import contours
from matplotlib import pyplot as plt


def get_horizontal_projections(image):
    return np.sum(image, axis=1, dtype="int32")


def get_binarized_image(image):
    return image * (1 / 255)


def get_continuous_horizontal(arr):
    before = arr[0]
    regions = []
    obj = [before]
    for idx, i in enumerate(arr[1:]):
        next = before + 1
        if i == next:
            obj.append(i)
            before = i
        else:
            regions.append(obj)
            obj = []
            obj.append(i)
            before = i

    regions.append(obj)

    candidate = []
    for i in regions:
        if len(i) > 25:
            candidate.append(i)

    limits = []

    for i in candidate:
        obj = [min(i), max(i)]
        limits.append(obj)

    return limits


def find_candidates_horizontal(bins):
    regions = []

    non_zero_bins=[i for i in bins if i>0]

    threshold=np.median(non_zero_bins)

    for idx, count in enumerate(bins):
        if count > threshold:
            regions.append(idx)

    return get_continuous_horizontal(regions)


def line_segmentation(image):
    print()
    print("line segmentation process started")
    height, width = image.shape[:2]
    image_cpy = image.copy()
    image_cpy2 = image.copy()

    binarized = get_binarized_image(image_cpy)

    bins = get_horizontal_projections(binarized)

    candidates = find_candidates_horizontal(bins)

    for i in candidates:
        image_cpy[i[0]:i[1], :] = 255


    contours = cv2.findContours(image_cpy, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

    lines = []
    # mask = np.zeros_like(image_cpy2)
    for i, contour in enumerate(contours):
        [x, y, w, h] = cv2.boundingRect(contour)
        if w == width:
            roi = image_cpy2[y:y + h, x:x + w]
            mask=np.zeros((image_cpy2.shape[:2]),np.uint8)
            cv2.drawContours(mask,[contour],-1,255,-1)
            mask_roi=mask[y:y + h, x:x + w]
            masked_image = cv2.bitwise_and(roi, roi, mask=mask_roi)
            lines.append(masked_image)

    print("line segmentation process done")
    print()
    print("#####################################")
    print()
    return reversed(lines),image,image_cpy