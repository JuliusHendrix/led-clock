import time

from src.matrices.led_matrix import LEDMatrix
from frame_displayers.basic_frame_displayer import BasicFrameDisplayer
from src.applications.clock_application import ClockApplication


def main():
    led_matrix = LEDMatrix()
    frame_manager = BasicFrameDisplayer(led_matrix)
    clock_app = ClockApplication(frame_manager)

    frame_period = 0.5  # s

    clock_app.start()
    while True:
        frame_manager.display_frame()
        time.sleep(frame_period)


if __name__ == "__main__":
    main()
