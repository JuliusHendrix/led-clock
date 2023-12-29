import os
from pathlib import Path
import sys
import numpy as np
from datetime import datetime
from threading import Thread, Lock
import time


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
        super().__init__()

        self.frame_manager = frame_manager
        self.string_converter = StringConverter(ClockFont())

        self.refresh_rate = 1  # Hz
        self.clock_thread = Thread(target=self.clock_loop)
        self.thread_running = False
        self.thread_stop_request = False
        self.thread_mutex = Lock()

    def update_time(self) -> None:
        current_time_string = datetime.now().strftime("%H:%M")

        print(current_time_string)

        time_string_array = self.string_converter.get_string_array(
            current_time_string, (255, 255, 255)
        )

        full_array = np.zeros((16, 32, 3))
        full_array[1:15, :, :] = time_string_array

        self.frame_manager.queue_frame(full_array)

    def clock_loop(self) -> None:
        next_call = time.time()
        stop_request = False
        while not stop_request:
            with self.thread_mutex:
                stop_request = self.thread_stop_request
            self.update_time()
            next_call = next_call + 1
            print(next_call)
            time.sleep(next_call - time.time())

    def start(self) -> bool:
        if self.thread_running:
            return False

        self.clock_thread.start()
        self.thread_running = True

        return True

    def stop(self) -> bool:
        if not self.thread_running:
            return False

        with self.thread_mutex:
            self.thread_stop_request = True

        self.clock_thread.join()
        self.thread_stop_request = False

        return True
