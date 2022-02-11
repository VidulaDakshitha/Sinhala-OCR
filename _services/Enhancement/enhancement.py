#malidi wageesha
#IT18194272
from imutils.perspective import four_point_transform
import cv2
from skimage.filters import threshold_sauvola, threshold_niblack
from skimage import img_as_ubyte
from scipy.spatial import distance as dist
from skimage import io
import numpy as np
import imutils


def sauvola(gray):
    window_size = 95
    thresh_sauvola = threshold_sauvola(gray, window_size=window_size)
    binary_sauvola = gray > thresh_sauvola
    th = img_as_ubyte(binary_sauvola)
    return th


def findCorrectedContours(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    # Find contours and sort for largest contour
    cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
    displayCnt = None

    for c in cnts:
        # Perform contour approximation
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        if len(approx) == 4:
            displayCnt = approx
            break

    # Obtain birds' eye view of image
    warped = four_point_transform(image, displayCnt.reshape(4, 2))
    return warped;


def rotate(img, angle):
    rows, cols = img.shape
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
    dst = cv2.warpAffine(img, M, (cols, rows))
    return dst


def detect_angle(image, pixel_type):
    mask = np.zeros(image.shape, dtype=np.uint8)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 0)
    adaptive = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15, 4)

    cnts = cv2.findContours(adaptive, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    for c in cnts:
        area = cv2.contourArea(c)
        if area < 45000 and area > 20:
            cv2.drawContours(mask, [c], -1, (255, 255, 255), -1)

    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

    h, w = mask.shape

    # Horizontal
    if w > h:
        left = mask[0:h, 0:0 + w // 8]
        right = mask[0:h, (w // 8) * 7:]

        left_pixels = cv2.countNonZero(left)
        right_pixels = cv2.countNonZero(right)

        if pixel_type:
            return 90 if left_pixels >= right_pixels else 270
        else:
            return 270 if left_pixels >= right_pixels else 90
    # Vertical
    else:
        top = mask[0:h // 8, 0:w]
        bottom = mask[(h // 8) * 7:, 0:w]
        top_pixels = cv2.countNonZero(top)
        bottom_pixels = cv2.countNonZero(bottom)

        if pixel_type:
            return 180 if bottom_pixels >= top_pixels else 0
        else:
            return 0 if bottom_pixels >= top_pixels else 180


def unsharp_mask(image, kernel_size=(5, 5), sigma=1.0, amount=1.0, threshold=0):
    """Return a sharpened version of the image, using an unsharp mask."""
    blurred = cv2.GaussianBlur(image, kernel_size, sigma)
    sharpened = float(amount + 1) * image - float(amount) * blurred
    sharpened = np.maximum(sharpened, np.zeros(sharpened.shape))
    sharpened = np.minimum(sharpened, 255 * np.ones(sharpened.shape))
    sharpened = sharpened.round().astype(np.uint8)
    if threshold > 0:
        low_contrast_mask = np.absolute(image - blurred) < threshold
        np.copyto(sharpened, image, where=low_contrast_mask)
    return sharpened


def threshold_image(image):
    # image = cv2.imread("Test11/warped.png",0)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    return thresh


def detect_template_angle(image):
    mask = np.zeros(image.shape, dtype=np.uint8)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 0)
    thresh2 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    adaptive = cv2.adaptiveThreshold(thresh2, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15, 4)

    cnts = cv2.findContours(adaptive, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    for c in cnts:
        area = cv2.contourArea(c)
        if area < 45000 and area > 20:
            cv2.drawContours(mask, [c], -1, (255, 255, 255), -1)

    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

    h, w = mask.shape

    left = mask[0:h, 0:0 + w // 8]
    right = mask[0:h, w // 8:]
    top = mask[0:h // 8, 0:w]
    bottom = mask[(h // 8) * 7:, 0:w]

    top_pixels = cv2.countNonZero(top)
    bottom_pixels = cv2.countNonZero(bottom)
    if top_pixels > bottom_pixels:
        return True
    else:
        return False
#Main function
def image_main(image,template):
    result = findCorrectedContours(image)
    # Load image, grayscale, Gaussian blur, Otsu's threshold

    image2 = result

    angle = detect_angle(result, detect_template_angle(template))
    rotate_img = imutils.rotate_bound(image2, angle)
    sharpened_image = unsharp_mask(rotate_img)
    img = threshold_image(sharpened_image)
    return img


