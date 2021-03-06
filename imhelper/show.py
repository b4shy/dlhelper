import matplotlib.pyplot as plt
import numpy as np
import logging

logger = logging.getLogger("Show")
logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)


def show_images(imgs, plot_no, labels=None, class_mapping_dict=None):

    if not type(plot_no) is tuple:
        logger.info("plot_no was no tuple! Creating tuple with (%i, %i)", plot_no, plot_no)
        plot_no = (plot_no, plot_no)

    fig, axis = _init_fig(plot_no)
    _show_image(plot_no, class_mapping_dict, axis, labels, imgs)


def _init_fig(plot_no):
    fig, axis = plt.subplots(plot_no[0], plot_no[1], squeeze=False)
    fig.set_figheight(10)
    fig.set_figwidth(10)
    return fig, axis


def _show_image(plot_no, class_mapping_dict, axis, labels, imgs):
    for i in range(plot_no[0]):
        for j in range(plot_no[1]):
            ind = np.random.randint(0, len(imgs))
            axis[i, j].imshow(imgs[ind])

            if labels and class_mapping_dict:
                axis[i, j].set_title(class_mapping_dict[labels[ind]])

            elif labels:
                axis[i, j].set_title(labels[ind])
    plt.show()

