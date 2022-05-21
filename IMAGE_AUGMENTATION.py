




#import libraries
import matplotlib.pyplot as plt
import cv2
import numpy as num
import os

path=r"C:\Users\user\Desktop\img2.3"#location
filename="\img_" #any_name_you wanna give for you augmented image files


def augment(path,filename):
    
    c=0
    for img in os.listdir(path):

        new_path=os.path.join(path,img)
        image=cv2.imread(new_path,1)
        #rotate clockwise
        image_rot=cv2.rotate(image,cv2.cv2.ROTATE_90_CLOCKWISE)
        #rotate counter clockwise
        img_count_rot=cv2.rotate(image,cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)
        #flip
        img_flip=cv2.flip(image,0)
        c=c+1
        cv2.imwrite(path + filename +str(c)+".jpg",img_count_rot)
        c=c+1
        cv2.imwrite(path + filename +str(c)+".jpg",image_rot)
        c=c+1
        cv2.imwrite(path + filename + str(c)+".jpg",img_flip)
        
        






