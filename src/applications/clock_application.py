import os
from pathlib import Path
import sys
import numpy as np
from datetime import datetime


# own modules
script_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = str(Path(script_dir).parents[0])
sys.path.append(src_dir)

from .application_abc import ApplicationABC
from frame_displayers.frame_displayer_abc import FrameDisplayerABC
from patterns.string.string_converter import StringConverter
from patterns.string.fonts.clock_font import ClockFont


class ClockApplication(ApplicationABC):
    def __init__(self, frame_displayer: FrameDisplayerABC) -> None:
        super().__init__(2)

        self.frame_displayer = frame_displayer
        self.string_converter = StringConverter(ClockFont())

        self.morning_color = (255, 103, 0)
        self.day_color = (255, 167, 0)
        self.evening_color = (255, 103, 0)
        self.night_color = (255, 0, 0)

        self.morning_start = "07:00"
        self.day_start = "09:00"
        self.evening_start = "18:00"
        self.night_start = "20:00"

        self.color = self.day_color

    @staticmethod
    def _is_it_later_than(time_now: str, time_to_compare_to: str) -> bool:
        if float(time_now[:2]) > float(time_to_compare_to[:2]):
            return True
        elif float(time_now[:2]) == float(time_to_compare_to[:2]):
            if float(time_now[3:]) >= float(time_to_compare_to[3:]):
                return True
        return False

    def set_color_from_time(self, time: str) -> None:
        if self._is_it_later_than(time, self.night_start):
            self.color = self.night_color
        elif self._is_it_later_than(time, self.evening_start):
            self.color = self.evening_color
        elif self._is_it_later_than(time, self.day_start):
            self.color = self.day_color
        elif self._is_it_later_than(time, self.morning_start):
            self.color = self.morning_color
        else:
            self.color = self.night_color

    def _update(self) -> None:
        current_time_string = datetime.now().strftime("%H:%M")

        self.set_color_from_time(current_time_string)

        time_string_array = self.string_converter.get_string_array(
            current_time_string, self.color
        )

        full_array = np.zeros((16, 32, 3))
        full_array[1:15, :, :] = time_string_array

        self.frame_displayer.queue_frame(full_array)
