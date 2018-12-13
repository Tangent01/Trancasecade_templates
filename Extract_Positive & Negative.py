import os
import random
import cv2 as cv


def images_rename(target_path, i):
    # i = 0
    file_list = os.listdir(target_path)    # 全部文件
    for file in file_list:
        i += 1
        old_dir = os.path.join(target_path, file)     # 原来的文件路径
        if os.path.isdir(old_dir):  # 若是文件夹则跳过
            continue
        # print(i)

        file_name = os.path.splitext(file)[0]   # 文件名
        file_type = os.path.splitext(file)[1]   # 扩展名
        new_dir = os.path.join(target_path, ' '+str(i)+file_type)  # 新文件路径 'neg'是重命名负样本时用的
        os.rename(old_dir, new_dir)


def images_rename_B(target_path, i):
    # i = 0
    file_list = os.listdir(target_path)    # 全部文件
    for file in file_list:
        i += 1
        old_dir = os.path.join(target_path, file)     # 原来的文件路径
        if os.path.isdir(old_dir):  # 若是文件夹则跳过
            continue
        # print(i)

        file_name = os.path.splitext(file)[0]   # 文件名
        file_type = os.path.splitext(file)[1]   # 扩展名
        new_dir = os.path.join(target_path, str(i)+file_type)  # 新文件路径 'neg'是重命名负样本时用的
        os.rename(old_dir, new_dir)

def positive_extract_roi(original_image_path, output_path):     # 使用函数前需要重命名
    i = 0
    image_list = os.listdir(original_image_path)
    for image in image_list:
        i += 1
        image = cv.imread(original_image_path + '\\' + image)     # 实在不行也可以用for
        roi = image[432:500, 860:940]
        cv.imwrite(output_path+'\\'+str(i)+r'.jpg', roi)
        print(int((float(i)/float(len(image_list)))*100))
    print('all done.')


def negative_extract_roi(original_image_path, output_path, i):
    image_list = os.listdir(original_image_path)
    for image in image_list:
        i += 1
        height_random = random.randint(0, 9)
        width_random = height_random + random.randint(0, 2)
        image = cv.imread(original_image_path + '\\' + image)
        # roi = image[280:500, 550:820]
        # 随机ROI的算法不完善
        roi = image[height_random*100 : (height_random*100 + 200 + random.randint(-50, 50)),
                    width_random*100 : (width_random*100 + 200 + random.randint(-50, 50))]

        print(height_random, width_random, i)
        cv.imwrite(output_path+'\\'+str(i)+r'.jpg', roi)


def sift_images(target_path):
    image_list = os.listdir(target_path)
    for image in image_list:
        src = cv.imread(target_path + '\\' + image)
        h = src.shape[0]
        w = src.shape[1]
        if abs(h-w) > 100:
            os.remove(target_path + '\\' + image)


def show_roi(path):         # 查看ROI区域效果
    image = cv.imread(path)
    roi = image[432:500, 860:940]  # 这一行直接拷贝到positive_extract_roi函数中
    cv.imshow('ROI', roi)
    cv.waitKey(0)
    cv.destroyAllWindows()


original_image_path = r'E:\Python\Project_PrimeRM\Model\Extract\Pos_Ori'
positive_roi_extract_path = r'E:\Python\Project_Box\Extracted_ROI\Pos'
negative_roi_extract_path = r'E:\Python\Project_Box\Extracted_ROI\Neg'

'''
image_list = os.listdir(original_image_path)
for file in image_list:
    print(type(file))
    print(file)
'''

# show_roi(r'E:\Python\Project_PrimeRM\Model\Extract\Pos_Ori\Rotate\2018102419251098410800.jpg')
# images_rename(r'E:\Python\Project_PrimeRM\Model\Rotate\File8\ROI')
# positive_extract_roi(r'E:\Python\Project_PrimeRM\Model\Extract\Pos_Ori\Rotate\File8',
                     # r'E:\Python\Project_PrimeRM\Model\Extract\Pos_Ori\Rotate\File8\ROI')


# 负样本的数量要正样本的三倍左右
# images_rename(r'E:\Python\Project_PrimeRM\Model\Extract\Neg_Ori')
# for i in range(3):
  #  negative_extract_roi(r'E:\Python\Project_PrimeRM\Model\Extract\Neg_Ori',
   #                     r'E:\Python\Project_PrimeRM\Model\Extract\Neg', 2051*i)


# 去除奇怪的宽高比
# sift_images(r'E:\Python\Project_Box\Extracted_ROI\Neg')

# 以下三行可以优化一下 (若以及有存在的名字则不能‘重命名’)--------------------
# images_rename(negative_roi_extract_path)  # 这里要把'neg'去掉   <---|
# images_rename(positive_roi_extract_path)    # 这里要加上'pos'   <---|
# images_rename(positive_roi_extract_path)                      <---|

'''------------------样本准备完毕---------------------'''
images_rename(r'E:\C++\ProjectBox\test_trainning\pos-new', 301)
images_rename_B(r'E:\C++\ProjectBox\test_trainning\pos-new', 301)
