import time

from src.matrices.led_matrix import LEDMatrix
from src.matrices.frame_manager import FrameManager
from src.applications.clock_application import ClockApplication


def main():
    led_matrix = LEDMatrix()
    frame_manager = FrameManager(led_matrix)
    clock_app = ClockApplication(frame_manager)

    frame_period = 0.5  # s
    duration = 24  # h

    clock_app.start()
    num_periods = duration * 60 * 60 / frame_period
    for _ in range(int(num_periods)):
        frame_manager.show_next_frame()
        time.sleep(frame_period)

    clock_app.stop()


if __name__ == "__main__":
    main()
