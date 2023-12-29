import numpy as np

from .matrix_abc import MatrixABC


class FrameManager:
    def __init__(self, matrix: MatrixABC, queue_size: int = 10) -> None:
        self.matrix = matrix
        self.array_queue = []
        self.queue_size = queue_size

    def queue_frame(self, array: np.ndarray) -> None:
        if len(self.array_queue) == self.queue_size:
            self.array_queue.pop(0)
        self.array_queue.append(array)

    def show_next_frame(self) -> None:
        if len(self.array_queue) > 0:
            self.matrix.display_array(self.array_queue.pop(0))
