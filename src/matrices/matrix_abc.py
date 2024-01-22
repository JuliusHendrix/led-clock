from abc import ABC
import numpy as np


class MatrixABC(ABC):
    def __init__(self, matrix_size: tuple[int, int]) -> None:
        super().__init__()

        self._matrix_size = matrix_size
        self._array_shape = (*self._matrix_size, 3)
        self._brightness = 0.01

    def get_matrix_size(self) -> tuple[int, int]:
        return self._matrix_size

    def set_brightness(self, brightness: float) -> None:
        if brightness >= 0.0 and brightness <= 1.0:
            self._brightness = brightness

    def display_array(self, array: np.ndarray) -> None:
        raise NotImplementedError()

    def clear(self) -> None:
        self.display_array(np.zeros(shape=self._array_shape))

    def _validate_array(self, array: np.ndarray) -> bool:
        if array.shape != self._array_shape:
            print("wrong array shape")
            return False

        if array.min() < 0 or array.max() > 255:
            print("array not within (0, 255)")
            return False

        return True

    def _scale_array_brightness(self, array: np.ndarray) -> np.ndarray:
        return (self._brightness * array).astype(int)
