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
from applications.clock_application import ClockApplication


def main():
    matrix = OpenCVMatrix(pixels_per_element=25, matrix_size=(16, 32))
    time.sleep(0.1)

    clock_app = ClockApplication(matrix)
    clock_app.start()

    for _ in range(120):
        matrix.show_queued_array()
        time.sleep(1)

    clock_app.stop()

    time.sleep(1)


if __name__ == "__main__":
    main()
