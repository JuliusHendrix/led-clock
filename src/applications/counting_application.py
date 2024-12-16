import os
from pathlib import Path
import sys
import numpy as np
from random import random

# own modules
script_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = str(Path(script_dir).parents[0])
sys.path.append(src_dir)

from .application_abc import ApplicationABC
from frame_displayers.frame_displayer_abc import FrameDisplayerABC
from patterns.string.string_converter import StringConverter
from patterns.string.fonts.clock_font import ClockFont


class CountingApplication(ApplicationABC):
    def __init__(
        self, frame_displayer: FrameDisplayerABC, counting_rate: float
    ) -> None:
        super().__init__(counting_rate)

        self.frame_displayer = frame_displayer
        self.string_converter = StringConverter(ClockFont())
        self.count = 0

    def _update(self) -> None:
        color = (
            int(random() * 255),
            int(random() * 255),
            int(random() * 255),
        )

        string_array = self.string_converter.get_string_array(f"{self.count}", color)
        self.count += 1

        full_array = np.zeros((16, 32, 3))
        _, width, _ = string_array.shape
        if width <= 32:
            full_array[1:15, :width, :] = string_array
        self.frame_displayer.queue_frame(full_array)
