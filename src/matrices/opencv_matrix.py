import numpy as np
import cv2

from .matrix_abc import MatrixABC


class OpenCVMatrix(MatrixABC):
    def __init__(self, pixels_per_element: int, matrix_size: tuple[int, int]) -> None:
        super().__init__()

        self.matrix_size = matrix_size
        self.array_shape = (*self.matrix_size, 3)

        self.window_size = (
            matrix_size[1] * pixels_per_element,
            matrix_size[0] * pixels_per_element,
        )

        # create black window
        self.queued_array = np.zeros(self.array_shape)

    def get_matrix_size(self) -> tuple[int, int]:
        return self.matrix_size

    def queue_array(self, array: np.ndarray) -> bool:
        if array.shape != self.array_shape:
            print("wrong array shape")
            return False

        if array.min() < 0 or array.max() > 255:
            print("array not within (0, 255)")
            return False

        self.queued_array = cv2.resize(
            array[:, :, ::-1].astype(np.uint8),  # BGR to RGB
            self.window_size,
            interpolation=cv2.INTER_NEAREST,
        )

        return True

    def show_queued_array(self) -> None:
        print("show")
        cv2.imshow("OpenCV Matrix", self.queued_array)
        cv2.waitKey(100)
