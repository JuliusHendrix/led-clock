from abc import ABC
import os
from pathlib import Path
import sys
from threading import Thread, Lock
import time

# own modules
script_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = str(Path(script_dir).parents[0])
src_dir = os.path.join(root_dir, "src")

sys.path.append(src_dir)

from matrices.frame_manager import FrameManager


class ApplicationABC(ABC):
    def __init__(self, refresh_rate: float) -> None:
        super().__init__()

        self._period = 1 / refresh_rate
        self._thread = Thread(target=self._clock_loop)
        self._thread_running = False
        self._thread_stop_request = False
        self._thread_mutex = Lock()

    def _clock_loop(self) -> None:
        next_call = time.time()
        stop_request = False
        while not stop_request:
            with self._thread_mutex:
                stop_request = self._thread_stop_request
            self._update()
            next_call = next_call + self._period
            print(next_call)
            time.sleep(next_call - time.time())

    def start(self) -> bool:
        if self._thread_running:
            return False

        self._thread.start()
        self._thread_running = True

        return True

    def stop(self) -> bool:
        if not self._thread_running:
            return False

        with self._thread_mutex:
            self._thread_stop_request = True

        self._thread.join()
        self._thread_stop_request = False

        return True

    def _update(self) -> None:
        raise NotImplementedError()
