import pytest
import os
from context import read

path = myPath = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(path, "data")


def test_read_up_to():
    imgs = read.read_images(path, 1)
    assert len(imgs) == 1


def test_read_all_imgs():
    imgs = read.read_images(path)
    assert len(imgs) == len(os.listdir(path))


def test_read_all_imgs_negative_img_number():
    imgs = read.read_images(path, -2)
    assert len(imgs) == len(os.listdir(path))


def test_read_all_imgs_2():
    imgs = read.read_images(path, 2)
    assert len(imgs) == 2


def test_read_all_imgs_with_size():
    imgs = read.read_images(path, size=(299, 299))
    assert imgs.shape[1:-1] == (299, 299)


def test_wrong_file_name():
    with pytest.raises(TypeError):
        read.read_images(".")
