import os
import random
import cv2 as cv


def images_rename(target_path):
    i = 0
    file_list = os.listdir(target_path)    # 全部文件
    for file in file_list:
        i += 1
        old_dir = os.path.join(target_path, file)     # 原来的文件路径
        if os.path.isdir(old_dir):  # 若是文件夹则跳过
            continue
        # print(i)

        file_name = os.path.splitext(file)[0]   # 文件名
        file_type = os.path.splitext(file)[1]   # 扩展名
        new_dir = os.path.join(target_path, 'neg' + str(i)+file_type)  # 新文件路径 'neg'是重命名负样本时用的
        os.rename(old_dir, new_dir)


def re_extract_roi(input_path, output_path, i):
    image_list = os.listdir(input_path)
    for image in image_list:
        i += 1
        image = cv.imread(input_path + '\\' + image)
        roi = image[0:33, 4:37]                            # <- #1
        # cv.imshow('ROI', image)
        cv.imwrite(output_path+'\\'+str(i)+r'.jpg', roi)


def show_roi(path):           # 查看ROI区域效果
    image = cv.imread(path)
    roi = image[0:33, 4:37]   # 这一行直接拷贝到------------------>#1
    cv.imshow('ROI', roi)
    cv.waitKey(0)
    cv.destroyAllWindows()


input_path_Left = r'E:\Python\Project_Box\Extracted_ROI\Pos\Done\Left'
input_path_Right = r'E:\Python\Project_Box\Extracted_ROI\Pos\Done\Right'
input_path_Medium = r'E:\Python\Project_Box\Extracted_ROI\Pos\Done\Medium'
output = r'E:\Python\Project_Box\Extracted_ROI\Pos\Done\Recut_Done'

# show_roi(r'E:\Python\Project_Box\Extracted_ROI\Pos\Done\Medium\72.jpg')
re_extract_roi(input_path_Medium, output, 239)
