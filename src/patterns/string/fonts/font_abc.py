from abc import ABC
import numpy as np


class FontABC(ABC):
    def get_font_height(self) -> int:
        raise NotImplementedError()

    def get_bool_character(self, character: str) -> tuple[bool, np.ndarray]:
        raise NotImplementedError()
