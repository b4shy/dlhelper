import os
import shutil

class KerasFormatHelper:
    def __init__(self, path_to_image_folder, name_of_img_folder):
        self.path = path_to_image_folder
        self.class_list = []
        self.files = os.listdir(os.path.join(self.path, name_of_img_folder))

    def make_directories(self, class_list):
        self.class_list = class_list
        for i in class_list:
            self._mkdir(i)

    def move_files_according_to_label(self, format_string):
        for img in self.files:
            for c, i in enumerate(format_string):
                if i in img:
                    shutil.copy(os.path.join(self.path, img), os.path.join(self.path, self.class_list[c]))

    def _mkdir(self, dirname):
        path_to_dir = os.path.join(self.path, dirname)
        if not os.path.isdir(path_to_dir):
            os.mkdir(path_to_dir)

