import sys
import cv2
import numpy as np
from pandas import *
from imutils import contours
from matplotlib import pyplot as plt


def get_binarized_image(image):
    height, width = image.shape[:2]
    for i in range(height):
        for j in range(width):
            if image[i,j]>0:
                image[i,j]=1

    return image


def character_segmentation(image, name):
    height, width = image.shape[:2]

    structure = np.zeros((height, width), dtype="uint16")

    current_label=1
    for i in range(height):
        for j in range(width):
            if image[i, j]==1:
                if j==0:
                    left=0
                else:
                    left=image[i,j-1]
                if i==0:
                    top=0
                else:
                    top=image[i-1,j]

                if left==0 and top==0:
                    structure[i,j]=current_label
                    current_label=current_label+1

                elif left==1 and top==0:
                    structure[i,j]=structure[i,j-1]

                elif left==0 and top==1:
                    structure[i,j]=structure[i-1,j]

                elif left==1 and top==1:

                    left_structure=structure[i,j-1]
                    top_structure =structure[i-1,j]

                    # if left_structure>0 and top_structure>0:

                    if left_structure<top_structure :
                        structure[i,j]=left_structure
                        structure=alternatives(structure,left_structure,top_structure)
                        # parent_child_structure.append([left_structure,top_structure])
                    elif left_structure>top_structure :
                        structure[i, j] = top_structure
                        structure = alternatives(structure, top_structure, left_structure)
                        # parent_child_structure.append([top_structure,left_structure])
                    elif left_structure==top_structure:
                        structure[i, j] = left_structure

    nums=[]
    for i in range(height):
        for j in range(width):
            val=structure[i, j]
            if val >0 and val not in nums:
                nums.append(val)

    empty_structure = np.full((height, width, 3), 0, dtype="uint8")

    value=1
    region_list=[]
    for num in nums:
        lowest_x=0
        lowest_y=0
        highest_x = 0
        highest_y = 0
        idx=0
        for i in range(height):
            for j in range(width):
                if structure[i, j] == num:
                    empty_structure[i,j]=color(value)
                    if idx==0:
                        lowest_x=j
                        lowest_y=i
                        highest_x = j
                        highest_y = i
                        idx=idx+1
                    else:
                        if j<lowest_x:
                            lowest_x=j
                        if i<lowest_y:
                            lowest_y=i
                        if j>highest_x:
                            highest_x=j
                        if i>highest_y:
                            highest_y=i+1


        value=value+1
        region_list.append([lowest_x,lowest_y,highest_x,highest_y,num])

    sorter = lambda x: (x[0])
    sorted_region_list = sorted(region_list, key=sorter)

    chars=[]
    for idx,region in enumerate(sorted_region_list):
        character_height=region[3]-region[1]
        character_width=region[2]-region[0]
        empty_character_structure = np.full((character_height, character_width), 0, dtype="uint8")
        char_i=0

        area=character_width*character_height
        if area>100:
            for i in range(region[1],region[3]):
                char_j=0
                for j in range(region[0],region[2]):
                    comparison = structure[i,j] == region[4]
                    equal_arrays = comparison.all()
                    if equal_arrays:
                        empty_character_structure[char_i,char_j]=255
                    char_j=char_j+1


                char_i=char_i+1

            # cv2.imshow(name+str(idx), empty_character_structure)
            chars.append(empty_character_structure)
            # cv2.imwrite(name + str(idx)+name + str(idx)+name+str(idx)+".jpeg", empty_character_structure)

    # arr_0=array_list[0]
    # roi = a[arr_0[1]:arr_0[3], arr_0[0]:arr_0[2]]
    # cv2.imshow("roi",roi)

    # cv2.imshow(name,empty_structure)
    return chars,empty_structure


def color(value):
    if value==1:
        rgb = [0, 0, 255]
    elif value==2:
        rgb=[0, 255, 0]
    elif value==3:
        rgb=[255, 0,0]
    elif value==4:
        rgb=[0, 255,255]
    elif value==5:
        rgb = [255, 0, 255]
    elif value == 6:
        rgb = [0, 180, 150]
    elif value == 7:
        rgb = [0, 150, 0]
    elif value == 8:
        rgb = [150, 0, 0]
    elif value == 9:
        rgb = [155, 155, 0]
    else :
        rgb = [255, 255, 255]

    return rgb


def alternatives(image,parent, child):
    height, width = image.shape[:2]
    for i in range(height):
        for j in range(width):
            if image[i, j] == child:
                image[i, j] = parent

    return image


def segmentation(words):
    print("Character segmentation process started")
    line_arr=[]
    word_structure_arr=[]
    for i,line in enumerate(words):
        word_arr=[]
        for j,word in enumerate(line):
            print("line: "+str(i)+" word: "+str(j))
            binarized_image = get_binarized_image(word)
            char_arr,word_structure=character_segmentation(binarized_image, (str(i) + "," + str(j)))
            word_arr.append(char_arr)
            word_structure_arr.append(word_structure)
        line_arr.append(word_arr)

    print("Character segmentation process done")
    print()
    print("#####################################")
    print()
    return line_arr,word_structure_arr


