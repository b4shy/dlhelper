import pytest
import os
from context import *
path = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(path, "data")
imgs = read_images(path)

# def test_show():
#     show_images(imgs, (2,2))


def test_no_tuple():
    with pytest.raises(TypeError):
        show_images(imgs, 2)

