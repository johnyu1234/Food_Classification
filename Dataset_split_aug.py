import os
import numpy as np
import cv2
import imutils
import random
array = ["apple","banana","carrots","egg","fried chicken","green apple","noodles","rice","sausage","fried rice","shrimp"]
list_train = ["train_1", "train_2", "train_3", "train_4", "train_5"]
list_class = ["apple","banana","cheese","carrots","egg","fried chicken","green apple","noodles","rice","sausage","fried rice","shrimp"]
def gausian_blur(image,name,path):
    image = cv2.GaussianBlur(image,(5,5),cv2.BORDER_DEFAULT)
    cv2.imwrite(path+"/"+name+"GausianBLur-.jpg", image)
# define location
def main(file_dir, final_path):
        for root, _, files in os.walk(file_dir):
            print(root)
        for file in files:
            print(file)
            if("jpeg" not in file):
                name = file[:len(file)-4]
            else:
                name = file[:len(file)-5]
            image = cv2.imread(file_dir+"/"+file)
            print(image)
            resize =imutils.resize(image,width=112)
            gausian_blur(resize,name,final_path)
            bright = np.ones(resize.shape, dtype="uint8")
            image_bright = cv2.add(resize,bright)
            image_dim = cv2.subtract(resize,bright)
            image_h = cv2.flip(resize,flipCode=0) #a-xis flip
            image_v = cv2.flip(resize,flipCode=1)#y-axis flip
            cv2.imwrite(final_path+"/"+name+"hflip.jpg", image_h)
            cv2.imwrite(final_path+"/"+name+"vflip.jpg", image_v)
            cv2.imwrite(final_path + "/" + name + "dim.jpg", image_dim)
            cv2.imwrite(final_path + "/" + name + "bright.jpg",image_bright)
def train_test_val_split(file_dir):
    for root, _, files in os.walk(file_dir):
        print(os.path.basename(root))

        for file in files :
            if random.randint(1, 10)<= 2:
                new_root = root.replace("/train", "test")
                os.rename(root+"/"+file,new_root+"/"+file)
            elif 2 < random.randint(1,10) < 4:
                new_root = root.replace("train", "val")
                os.rename(root+"/"+file,new_root+"/"+file)
                print(file)
def train_test_val_split_online(file_dir):
    for root, _, files in os.walk(file_dir):
        print(os.path.basename(root))

        for file in files :
            if random.randint(1, 10)<= 2:
                new_root = root.replace("dataset/online", "test")
                os.rename(root+"/"+file,new_root+"/"+file)
            elif 2 < random.randint(1,10) < 4:
                new_root = root.replace("dataset/online", "val")
                os.rename(root+"/"+file,new_root+"/"+file)
                print(file)
def create_folder_list(location,class_list,type_list):
   for j in type_list:
        for i in class_list:
            if not os.path.exists(location+"/"+j+"/"+i):
                os.makedirs(location+"/"+j+"/"+i)    


if __name__ == '__main__':
    #for i in array:
    #    main("/Users/johns/Desktop/dataset/dataset/actual/"+i,"/Users/johns/Desktop/dataset/train/"+i)
    #train_test_val_split("/Users/johns/Desktop/dataset/train")
    #create_folder_list("/Users/johns/Desktop/dataset",list_class,type_list)

    train_test_val_split_online("/Users/johns/Desktop/dataset/dataset/online")
