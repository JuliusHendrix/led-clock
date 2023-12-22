from abc import ABC


class ApplicationABC(ABC):
    def start(self) -> None:
        raise NotImplementedError()

    def stop(self) -> None:
        raise NotImplementedError()
