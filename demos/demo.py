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
from matrices.frame_manager import FrameManager
from applications.clock_application import ClockApplication
from inputs.gamepad_input_decoder import GamepadInputDecoder


def main():
    gamepad_input_manager = GamepadInputDecoder()

    for _ in range(1000):
        gamepad_input_manager.check_input()

        inputs = gamepad_input_manager.get_inputs()
        print(inputs)

        time.sleep(0.01)

    # frame_manager = FrameManager(
    #     OpenCVMatrix(pixels_per_element=25, matrix_size=(16, 32)), queue_size=10
    # )
    # time.sleep(0.1)

    # clock_app = ClockApplication(frame_manager)
    # clock_app.start()

    # for _ in range(120):
    #     frame_manager.show_next_frame()
    #     time.sleep(1)

    # clock_app.stop()

    # time.sleep(1)


if __name__ == "__main__":
    main()