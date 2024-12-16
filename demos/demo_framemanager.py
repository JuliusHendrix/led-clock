import os
from pathlib import Path
import sys
import time


# own modules
script_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = str(Path(script_dir).parents[0])
src_dir = os.path.join(root_dir, "src")

sys.path.append(src_dir)

from matrices.opencv_matrix import OpenCVMatrix
from frame_displayers.fading_frame_displayer import FadingFrameDisplayer
from applications.counting_application import CountingApplication


def main():
    frame_displayer = FadingFrameDisplayer(
        OpenCVMatrix(pixels_per_element=25, matrix_size=(16, 32)), decay_rate=0.9
    )
    time.sleep(0.1)

    refresh_rate = 10  # fps
    period = 1 / refresh_rate

    counting_app = CountingApplication(frame_displayer, counting_rate=1)
    counting_app.start()

    while True:
        frame_displayer.display_frame()
        time.sleep(period)


if __name__ == "__main__":
    main()
