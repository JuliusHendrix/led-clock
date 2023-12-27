from .font_abc import FontABC
import os
from pathlib import Path
import sys
import numpy as np

# own modules
script_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = str(Path(script_dir).parents[3])
src_dir = os.path.join(root_dir, "src")

sys.path.append(src_dir)

from patterns.image_reader import ImageReader


class ClockFont(FontABC):
    def __init__(self) -> None:
        imageReader = ImageReader()

        script_dir = os.path.dirname(os.path.abspath(__file__))
        font_dir = os.path.join(script_dir, "clock_font")

        characters_to_read = {
            "0": os.path.join(font_dir, "0.png"),
            "1": os.path.join(font_dir, "1.png"),
            "2": os.path.join(font_dir, "2.png"),
            "3": os.path.join(font_dir, "3.png"),
            "4": os.path.join(font_dir, "4.png"),
            "5": os.path.join(font_dir, "5.png"),
            "6": os.path.join(font_dir, "6.png"),
            "7": os.path.join(font_dir, "7.png"),
            "8": os.path.join(font_dir, "8.png"),
            "9": os.path.join(font_dir, "9.png"),
            ":": os.path.join(font_dir, ":.png"),
        }

        for character, path in characters_to_read.items():
            (success, bool_array) = imageReader.binary_image_to_bool_array(path)

            if success:
                self.characters[character] = bool_array

    def get_font_height(self) -> int:
        return 14
