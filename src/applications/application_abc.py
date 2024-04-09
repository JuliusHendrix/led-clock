from abc import ABC
from threading import Thread
import time


class ApplicationABC(ABC):
    def __init__(self, refresh_rate: float) -> None:
        super().__init__()

        self._period = 1 / refresh_rate
        self._thread = Thread(target=self._clock_loop)
        self._thread_running = False
        self._thread_stop_request = False

    def _clock_loop(self) -> None:
        next_call = time.time()
        stop_request = False
        while not self._thread_stop_request:
            self._update()
            next_call = next_call + self._period
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

        self._thread_stop_request = True

        self._thread.join()
        self._thread_stop_request = False

        return True

    def _update(self) -> None:
        raise NotImplementedError()
