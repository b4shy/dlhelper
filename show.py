import matplotlib.pyplot as plt
import numpy as np
from read import read_images


class Show:

    def __init__(self, imgs, plot_no, labels=None, class_mapping_dict=None):
        self.imgs = imgs
        self.plot_no = plot_no
        self.labels = labels
        self.class_mapping_dict = class_mapping_dict
        self.show_samples()

    def show_samples(self):
        fig, axis = self.init_fig()
        self.show_image(axis)

    def init_fig(self):
        fig, axis = plt.subplots(self.plot_no[0], self.plot_no[1], squeeze=False)
        fig.set_figheight(10)
        fig.set_figwidth(10)
        return fig, axis

    def show_image(self, axis):
        for i in range(self.plot_no[0]):
            for j in range(self.plot_no[1]):
                ind = np.random.randint(0, len(self.imgs))
                axis[i, j].imshow(self.imgs[ind])

                if self.labels and self.class_mapping_dict:
                    axis[i, j].set_title(self.class_mapping_dict[self.labels[ind]])

                elif self.labels:
                    axis[i, j].set_title(self.labels[ind])
        plt.show()



imgs = read_images("data")
Show(imgs,(2,2))
