import numpy as np
import os
import cv2


class ImageReader:
    def __init__(self) -> None:
        pass

    def binary_image_to_bool_array(self, path: str) -> tuple[bool, np.ndarray]:
        if not os.path.isfile(path):
            return (False, np.array([]))

        if not path[-3:] == "png":
            return (False, np.array([]))

        im = cv2.imread(path)
        im_2d = im.sum(axis=2)
        bool_array = np.where(im_2d == 0, 0, 1)

        return (True, bool_array)
