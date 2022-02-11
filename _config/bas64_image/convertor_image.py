import io
import cv2
import base64
import cv2
import numpy as np
from PIL import Image
# Image.MAX_IMAGE_PIXELS = None
from django.core.files.base import ContentFile
# Take in base64 string and return PIL image
def stringToImage(base64_string):
    format, img_str = base64_string.split(';base64,')
    ext = format.split('/')[-1]
    imgdata = base64.b64decode(img_str)

    return Image.open(io.BytesIO(imgdata))

# convert PIL Image to an RGB image( technically a numpy array ) that's compatible with opencv
def toRGB(image):
    return cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)


def RGBtoGray(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def GraytoRGB(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)