import os
import cv2 as cv


positive_path = r'E:\C++\ProjectBox\test_trainning\Pos'
negative_path = r'E:\C++\ProjectBox\test_trainning\Neg'


def generate_source_file_positive():
    image_list = os.listdir(positive_path)
    with open(r'E:\C++\ProjectBox\test_trainning\Pos.txt', 'w+') as file:
        for image in image_list:
            print(image)
            print(type(image))
            file.write('Pos\\' + image + ' 1 0 0 25 25\n')


def generate_source_file_negative():
    image_list = os.listdir(negative_path)
    with open(r'E:\C++\ProjectBox\test_trainning\Neg.txt', 'w+') as file:
        for image in image_list:
            print(image)
            print(type(image))
            file.write('Neg\\' + image + '\n')

'''
def gray():
    image_list = os.listdir(positive_path)
    for image in image_list:
        src = cv.imread(positive_path + '\\' + image)
        gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
        cv.imwrite(positive_path + '\\' + image, gray)
'''

generate_source_file_positive()
generate_source_file_negative()

