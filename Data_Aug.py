import os
import numpy as np
import cv2
import imutils
import random
# define location
location = r"C:\Users\johny\OneDrive\Desktop\Fall 2021\Project\dataset\test\rice"
def main(file_dir, output_path):
        for root, _, files in os.walk(file_dir):
            print(root)
        for file in files:
            print(file)
            if((file.find("hflip")==-1)and(file.find("vflip")==-1)and(file.find("light")==-1)):
                image = cv2.imread(file_dir+"\\"+file)
                resize =imutils.resize(image,width=100)
                image_h = cv2.flip(resize,flipCode=0) #a-xis flip
                image_v = cv2.flip(resize,flipCode=1)#y-axis flip
                saturation=150
                image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

                v = image[:, :, 2]
                v = np.where(v <= 255 + saturation, v - saturation, 255)
                image[:, :, 2] = v

                image_light = cv2.cvtColor(image, cv2.COLOR_HSV2BGRR)
                name = file[:len(file)-4]
                cv2.imwrite(location+"\\"+name+"hflip.jpg",image_h)
                cv2.imwrite(location+"\\"+name+"vflip.jpg",image_v)
                cv2.imwrite(location+"\\"+name+"light.jpg",image_light)
            else:
                print("augmentation has been done before")



main(location,location)