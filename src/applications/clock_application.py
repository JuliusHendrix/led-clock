import os
from pathlib import Path
import sys
import numpy as np
import time


# own modules
script_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = str(Path(script_dir).parents[0])
src_dir = os.path.join(root_dir, "src")

sys.path.append(src_dir)

from application_abc import ApplicationABC
from matrices.matrix_abc import MatrixABC
from patterns.string.string_converter import StringConverter
from patterns.string.fonts.minecraft_font import MinecraftFont


class ClockApplication(ApplicationABC):
    def __init__(self, matrix: MatrixABC) -> None:
        super().__init__()

        self.matrix = matrix
        self.string_converter = StringConverter(MinecraftFont())
