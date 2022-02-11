import cv2
import numpy as np
from imutils import contours
from matplotlib import pyplot as plt


def get_vertical_projections(image):
    return np.sum(image, axis=0, dtype="int32")


def get_binarized_image(image):
    return image * (1 / 255)


def find_candidates_vertical(bins):
    regions = []

    for idx, count in enumerate(bins):
        if count > 5:
            regions.append(idx)

    # get_continuous=get_continuous_vertical(regions)
    # for i in get_continuous:
    #     image_cpy2[:,i[0]:i[1]] = 255
    #
    # cv2.imshow("letter",image_cpy2)
    return get_continuous_vertical(regions)


def get_continuous_vertical(arr):
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
        if len(i) > 10:
            candidate.append(i)

    limits = []

    for i in candidate:
        obj = [min(i), max(i)]
        limits.append(obj)
    return limits


def get_avg(arr):
    total=sum(arr)
    length=len(arr)
    return (total/length)


def identify_word_length(image,kernel):
    kernel_size = kernel
    kernel = np.ones((kernel_size, kernel_size), dtype="uint8")
    open_img = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    # cv2.imshow("open", open_img)

    contours = cv2.findContours(open_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

    words=[]
    for i, contour in enumerate(contours):
        [x, y, w, h] = cv2.boundingRect(contour)
        if w > 40:
            roi = image[y:y + h, x:x + w]
            # cv2.imshow("roi,"+str(i),roi)
            # mask=np.zeros((image_cpy2.shape[:2]),np.uint8)
            # cv2.drawContours(mask,[contour],-1,255,-1)
            # mask_roi=mask[y:y + h, x:x + w]
            # masked_image = cv2.bitwise_and(roi, roi, mask=mask_roi)
            words.append(roi)

    return len(words)


def identify_words(image,kernel):
    kernel_size = kernel
    kernel = np.ones((kernel_size, kernel_size), dtype="uint8")
    open_img = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    # cv2.imshow("open", open_img)

    contours = cv2.findContours(open_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

    words=[]
    for i, contour in enumerate(contours):
        [x, y, w, h] = cv2.boundingRect(contour)
        if w > 40:
            roi = image[y:y + h, x:x + w]
            # cv2.imshow("roi,"+str(i),roi)
            # mask=np.zeros((image_cpy2.shape[:2]),np.uint8)
            # cv2.drawContours(mask,[contour],-1,255,-1)
            # mask_roi=mask[y:y + h, x:x + w]
            # masked_image = cv2.bitwise_and(roi, roi, mask=mask_roi)
            words.append(roi)

    return words


def get_confident(arr):
    arr_len=len(arr)
    count=0
    for i in arr:
        if i>50:
            count=count+1

    avg=count/arr_len
    print(avg)
    return avg

def get_word_list(arr,image):
    last_first_element = arr[0][0] #last checked array element # but at first it is 0 index of the array
    last_second_element = arr[0][1]

    list = []

    max_val = last_first_element
    for idx, i in enumerate(arr[1:]):
        now_first_element = i[0]
        difference = (now_first_element - last_second_element)
        last_second_element=i[1]
        list.append(difference)

        if idx==0:
            max_val = difference

        elif difference>max_val:
            max_val=difference

    words_len=identify_word_length(image,35)
    if words_len==1:
        return [[arr[0][0],arr[len(arr)-1][1]]]
    else:
        array_of_candidates=[]
        half_of_max=int(max_val/2)
        for i in list:
            if i>half_of_max:
                array_of_candidates.append(i)

        word_array=[]
        last_index=0

        for index,j in enumerate(array_of_candidates):
            obj=[]
            idx=list.index(j)
            if index==0:
                obj.append(arr[0][0])
                obj.append(arr[idx][1])
                last_index=idx

            else:
                obj.append(arr[last_index + 1][0])
                obj.append(arr[idx][1])
                last_index = idx

            word_array.append(obj)

        obj=[]
        obj.append(arr[last_index + 1][0])
        obj.append(arr[len(arr) - 1][1])
        word_array.append(obj)

        if len(word_array)==words_len:
            return word_array
        else:
            words_len=identify_word_length(image,25)
            if len(word_array)==words_len:
                return word_array
            else:
                if get_confident(array_of_candidates)>0.99:
                    return word_array
                else:
                    return False


def word_segmentation(image):
    image_cpy = image.copy()
    image_cpy2 = image.copy()
    binarized = get_binarized_image(image_cpy)
    bins = get_vertical_projections(binarized)

    candidates=find_candidates_vertical(bins)

    word_list=get_word_list(candidates,image)

    if not word_list:
        return identify_words(image,35)

    for i in word_list:
        x1, x2 = i
        image_cpy[:,x1:x2] = 255

    contours = cv2.findContours(image_cpy, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

    countour_arr = []
    for i, contour in enumerate(contours):
        [x, y, w, h] = cv2.boundingRect(contour)
        countour_arr.append([x, y, w, h])

    sorter = lambda x: (x[0])
    sorted_region_list = sorted(countour_arr, key=sorter)

    words = []
    for i, contour in enumerate(sorted_region_list):
        [x, y, w, h] = contour
        if w > 0:
            roi = image_cpy2[y:y + h, x:x + w]

            words.append(roi)

    return words


def word_segmentation_preprocess(image_array):
    print("Word segmentation process started")
    words=[]
    for idx,image in enumerate(image_array):
        print("line: "+str(idx))
        words.append(word_segmentation(image))
    # words.append(word_segmentation(image_array[0]))
    print("word segmentation process done")
    print()
    print("#####################################")
    print()
    return words

# def get_word_list(arr):
#     length = len(arr) - 2
#     avg = get_avg(arr)
#
#     if avg>10:
#         last_first_element = arr[0][0]
#         last_second_element = arr[0][1]
#
#         list = []
#
#         obj = [last_first_element]
#
#         for idx, i in enumerate(arr[1:]):
#             now_first_element = i[0]
#             difference = (now_first_element - last_second_element)
#
#             if difference > avg:
#                 obj.append(last_second_element)
#                 list.append(obj)
#                 obj = [now_first_element]
#
#             if idx == length:
#                 obj.append(i[1])
#                 list.append(obj)
#
#             last_second_element = i[1]
#     else:
#         list=[[arr[0][0],arr[len(arr)-1][1]]]
#
#     return list
