import os
import shutil


class KerasFormatHelper:
    '''
    Keep in mind that for move files the format string has to be in the same order as the class list
    '''
    def __init__(self, path_to_image_folder, name_of_img_folder):
        self.path = path_to_image_folder
        self.img_path = os.path.join(self.path, name_of_img_folder)
        self.files = os.listdir(self.img_path)
        self.class_list = []

    def make_directories(self, class_list):
        self.class_list = class_list
        for i in class_list:
            self._mkdir(i)

    def move_files_according_to_label(self, format_string):
        for img in self.files:
            for c, i in enumerate(format_string):
                if i in img:
                    shutil.copy(os.path.join(self.img_path, img), os.path.join(self.path, self.class_list[c]))

    def _mkdir(self, dirname):
        path_to_dir = os.path.join(self.path, dirname)
        if not os.path.isdir(path_to_dir):
            os.mkdir(path_to_dir)


