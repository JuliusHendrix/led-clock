import numpy as np
import copy

import os
from pathlib import Path
import sys

# own modules
script_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = str(Path(script_dir).parents[0])
sys.path.append(src_dir)

from .frame_displayer_abc import FrameDisplayerABC
from matrices.matrix_abc import MatrixABC


class FadingFrameDisplayer(FrameDisplayerABC):
    def __init__(self, matrix: MatrixABC, decay_rate: float) -> None:
        super().__init__(matrix)
        self.decay_rate = decay_rate

        self.last_keyframe = self.frame
        self.effected_frame = self.frame

    def _get_display_frame(self, frame: np.ndarray) -> np.ndarray:
        if self.new_frame:
            self.last_keyframe = copy.deepcopy(frame)
            self.effected_frame = copy.deepcopy(frame)
        else:
            self.effected_frame *= self.decay_rate
        return self.effected_frame
