from abc import ABC
import numpy as np


class MatrixABC(ABC):
    def get_matrix_size(self) -> tuple[int, int]:
        raise NotImplementedError()

    def queue_array(self, array: np.ndarray) -> bool:
        raise NotImplementedError()
