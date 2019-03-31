import pytest
import os
from context import read


def test_read_up_to():
    imgs = read.read_images("data", 1)
    assert len(imgs) == 1


def test_read_all_imgs():
    imgs = read.read_images("data")
    assert len(imgs) == len(os.listdir("data"))


def test_read_all_imgs_negative_img_number():
    imgs = read.read_images("data",-2)
    assert len(imgs) == len(os.listdir("data"))


def test_read_all_imgs_2():
    imgs = read.read_images("data",2)
    assert len(imgs) == 2


def test_read_all_imgs_with_size():
    imgs = read.read_images("data", size=(299,299))
    assert imgs.shape[1:-1] == (299,299)

