import cv2
import os
import numpy as np

def read_images(path, size=(224, 224)):
    imgs = []
    for i in os.listdir(path):
        img_path = os.path.join(path, i)
        img = cv2.imread(img_path)
        img = cv2.resize(img, size)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        imgs.append(img)
    return np.array(imgs)
