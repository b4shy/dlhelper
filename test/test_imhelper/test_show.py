import pytest
import os
import sys
sys.path.append("..")
from context import *
import matplotlib.pyplot as plt
path = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(path, "data")
imgs = read_images(path)


# def test_show():
#     show_images(imgs, (2,2))


# def test_no_tuple():
#     show_images(imgs, 3)
