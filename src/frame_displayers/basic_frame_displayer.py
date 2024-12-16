import numpy as np

import os
from pathlib import Path
import sys

# own modules
script_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = str(Path(script_dir).parents[0])
sys.path.append(src_dir)

from .frame_displayer_abc import FrameDisplayerABC
from matrices.matrix_abc import MatrixABC


class BasicFrameDisplayer(FrameDisplayerABC):
    def __init__(self, matrix: MatrixABC) -> None:
        super().__init__(matrix)

    def _get_display_frame(self, frame: np.ndarray) -> np.ndarray:
        return frame
