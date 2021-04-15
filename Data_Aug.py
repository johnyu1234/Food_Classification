import os
import numpy as np
import cv2
import imutils
import random
from imgaug import augmenters as iaa
array = ["apple","banana","cheese","egg","fried chicken","green apple","noodles","rice","sausage"]

def gausian_blur(image,name,path):
    image = cv2.GaussianBlur(image,(5,5),cv2.BORDER_DEFAULT)
    cv2.imwrite(path+"\\"+name+"GausianBLur-.jpg", image)
# define location
def main(file_dir, final_path):
        for root, _, files in os.walk(file_dir):
            print(root)
        for file in files:
            print(file)
            name = file[:len(file)-4]
            image = cv2.imread(file_dir+"\\"+file)
            resize =imutils.resize(image,width=112)
            gausian_blur(resize,name,final_path)
            image_h = cv2.flip(resize,flipCode=0) #a-xis flip
            image_v = cv2.flip(resize,flipCode=1)#y-axis flip
            translater = iaa.Affine(translate_px={"x": -16})
            image_a = translater.augment_image(resize)
            scaler = iaa.Affine(scale={"y":(0.8,1.2)})
            image_s = scaler.augment_image(resize)

            #image_light = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)
            cv2.imwrite(final_path+"\\"+name+"hflip.jpg", image_h)
            cv2.imwrite(final_path+"\\"+name+"vflip.jpg", image_v)
            cv2.imwrite(final_path + "\\" + name + "trans.jpg", image_a)
            cv2.imwrite(final_path + "\\" + name + "scale.jpg", image_s)
            #cv2.imwrite(final_path+"\\"+name+"light.jpg", image_light)


if __name__ == '__main__':
    #for i in array:
     #   main(r"B:\DATASET\train"+"\\"+i,r"B:\DATASET\train"+"\\"+i)
    main(r"B:\ji\hi",r"B:\ji\hi")
