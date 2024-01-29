import numpy as np
import cv2

from .matrix_abc import MatrixABC


class OpenCVMatrix(MatrixABC):
    def __init__(self, pixels_per_element: int, matrix_size: tuple[int, int]) -> None:
        super().__init__(matrix_size, 1)

        self._window_size = (
            matrix_size[1] * pixels_per_element,
            matrix_size[0] * pixels_per_element,
        )

    def display_array(self, array: np.ndarray) -> None:
        if not self._validate_array(array):
            return

        scaled_array = self._scale_array_brightness(array)

        im = cv2.resize(
            scaled_array[:, :, ::-1].astype(np.uint8),  # BGR to RGB
            self._window_size,
            interpolation=cv2.INTER_NEAREST,
        )

        cv2.imshow("OpenCV Matrix", im)
        cv2.waitKey(100)
