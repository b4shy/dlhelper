import cv2
import os
import numpy as np
import logging

logger = logging.getLogger("READ")
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)


def read_images(path, img_no=-1, size=(224, 224)):

    if img_no < 0:
        logger.info("Imread all images from %s", path)
    else:
        logger.info("Read %i image(s) from %s", img_no, path)
    imgs = []

    for counter, i in enumerate(os.listdir(path)):

        if counter == img_no:
            logger.info("Done")
            break

        if ".png" in i or ".jpg" in i:
            img_path = os.path.join(path, i)
            img = cv2.imread(img_path)
            img = cv2.resize(img, size)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            imgs.append(img)

        else:
            logger.warning("%s is not a valid image file", i)
            raise TypeError("{} is not a valid image file".format(i))

    return np.array(imgs)

