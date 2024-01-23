import os
from pathlib import Path
import sys
import numpy as np
from datetime import datetime


# own modules
script_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = str(Path(script_dir).parents[0])
src_dir = os.path.join(root_dir, "src")

sys.path.append(src_dir)

from .application_abc import ApplicationABC
from matrices.frame_manager import FrameManager
from patterns.string.string_converter import StringConverter
from patterns.string.fonts.clock_font import ClockFont


class ClockApplication(ApplicationABC):
    def __init__(self, frame_manager: FrameManager) -> None:
        super().__init__(2)

        self.frame_manager = frame_manager
        self.string_converter = StringConverter(ClockFont())

    def _update(self) -> None:
        current_time_string = datetime.now().strftime("%H:%M")

        print(current_time_string)

        time_string_array = self.string_converter.get_string_array(
            current_time_string, (255, 255, 255)
        )

        full_array = np.zeros((16, 32, 3))
        full_array[1:15, :, :] = time_string_array

        self.frame_manager.queue_frame(full_array)
