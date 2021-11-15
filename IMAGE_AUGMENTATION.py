#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import libraries
import matplotlib.pyplot as plt
import cv2
import numpy as num
import os
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


path=r"C:\Users\user\Desktop\img2.3"#location
filename="\img_" #any_name_you wanna give for you augmented image files


# In[5]:


c=0
for img in os.listdir(path):
    new_path=os.path.join(path,img)
    print(new_path)
    image=cv2.imread(new_path,1)
    print(image.shape)
    image_rot=cv2.rotate(image,cv2.cv2.ROTATE_90_CLOCKWISE)
    img_count_rot=cv2.rotate(image,cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)
    plt.imshow(img_count_rot)
    plt.show()
    img_flip=cv2.flip(image,0)
    plt.imshow(img_flip)
    plt.show()
    plt.imshow(image)
    plt.imshow(image_rot)
    plt.show()
    c=c+1
    cv2.imwrite(path + filename +str(c)+".jpg",img_count_rot)

    plt.show()
    c=c+1
    cv2.imwrite(path + filename +str(c)+".jpg",image_rot)
    c=c+1
    cv2.imwrite(path + filename + str(c)+".jpg",img_flip)


# In[ ]:




