import sys
sys.path.append("..")
from context import KerasFormatHelper
import os
import shutil

path = os.path.dirname(os.path.abspath(__file__))
test_path = os.path.join(path, "StructureTest")
cat_path = os.path.join(test_path, "cat")
dog_path = os.path.join(test_path, "dog")
class3_path = os.path.join(test_path, "class3")


# First delete folders
def del_directories():
    if os.path.isdir(cat_path):
        shutil.rmtree(cat_path)
    if os.path.isdir(dog_path):
        shutil.rmtree(dog_path)
    if os.path.isdir(class3_path):
        shutil.rmtree(class3_path)


def test_mkdir():
    del_directories()

    k = KerasFormatHelper(test_path, "train_imgs")
    k._mkdir("cat")

    assert "cat" in os.listdir(test_path)


def test_make_directories():
    del_directories()

    k = KerasFormatHelper(test_path, "train_imgs")
    class_list = ["cat", "dog", "class3"]
    k.make_directories(class_list)

    for i in class_list:
        assert i in os.listdir(test_path)


def test_move_files_according_to_label():
    del_directories()

    k = KerasFormatHelper(test_path, "train_imgs")
    class_list = ["cat", "dog"]
    k.make_directories(class_list)
    k.move_files_according_to_label(class_list)

    for i in class_list:
        assert any(i in x for x in os.listdir(os.path.join(test_path, i)))
