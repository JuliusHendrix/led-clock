from abc import ABC
import numpy as np


class MatrixABC(ABC):
    def get_matrix_size(self) -> tuple[int, int]:
        raise NotImplementedError()

    def display_array(self, array: np.ndarray) -> None:
        raise NotImplementedError()
