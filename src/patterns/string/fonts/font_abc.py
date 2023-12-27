from abc import ABC
import numpy as np


class FontABC(ABC):
    characters = {}

    def get_bool_character(self, character: str) -> tuple[bool, np.ndarray]:
        if len(character) != 1:
            return (False, np.array([]))
        if not character in self.characters:
            return (False, np.array([]))
        return (True, self.characters[character])

    def get_font_height(self) -> int:
        raise NotImplementedError()
