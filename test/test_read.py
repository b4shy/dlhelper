import pytest
from context import read


def test_read():
    imgs = read.read_images("data",1)
    assert len(imgs) == 1

