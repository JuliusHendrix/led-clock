from abc import ABC


class ApplicationABC(ABC):
    def start(self) -> bool:
        raise NotImplementedError()

    def stop(self) -> bool:
        raise NotImplementedError()
