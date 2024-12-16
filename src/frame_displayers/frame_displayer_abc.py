from abc import ABC
import numpy as np
import os
from pathlib import Path
import sys

# own modules
script_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = str(Path(script_dir).parents[0])
sys.path.append(src_dir)

from matrices.matrix_abc import MatrixABC


# TODO: move framerate here?
class FrameDisplayerABC(ABC):
    def __init__(self, matrix: MatrixABC) -> None:
        super().__init__()
        self.matrix = matrix
        self.new_frame = False
        self.frame = np.zeros((*matrix.get_matrix_size(), 3))

    def queue_frame(self, frame: np.ndarray) -> None:
        self.new_frame = True
        self.frame = frame

    def display_frame(self) -> None:
        display_frame = self._get_display_frame(self.frame)
        self.matrix.display_array(display_frame)
        self.new_frame = False

    def _get_display_frame(self, frame: np.ndarray) -> np.ndarray:
        raise NotImplementedError
