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

from matrices.opencv_matrix import OpenCVMatrix
from patterns.string.string_converter import StringConverter
from patterns.string.fonts.minecraft_font import MinecraftFont


def main():
    matrix = OpenCVMatrix(pixels_per_element=25, matrix_size=(16, 32))
    time.sleep(0.1)

    font = MinecraftFont()
    string_converter = StringConverter(font)

    test_string_array = string_converter.get_string_array("17:39", (255, 20, 147))

    frame = np.zeros(shape=(16, 32, 3))

    frame[4:11, 2:31, :] = test_string_array

    matrix.display_array(frame)
    time.sleep(5)

    # for _ in range(10):
    #     random_arr = np.random.randint(0, 256, size=(16, 32, 3))
    #     matrix.display_array(random_arr)
    #     time.sleep(1)


if __name__ == "__main__":
    main()
