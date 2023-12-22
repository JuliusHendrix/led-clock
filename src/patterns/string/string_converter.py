import numpy as np

from .fonts.font_abc import FontABC


class StringConverter:
    def __init__(self, font: FontABC) -> None:
        self.font = font
        self.font_height = font.get_font_height()

    def get_character_array(
        self, character: str, color: tuple[int, int, int]
    ) -> np.ndarray:
        if min(color) < 0 or max(color) > 255:
            return np.zeros(shape=(self.font_height, 1))

        if len(character) != 1:
            return np.zeros(shape=(self.font_height, 1))

        (succes, bool_character) = self.font.get_bool_character(character)

        if not succes:
            return np.zeros(shape=(self.font_height, 1))

        led_character = bool_character[:, :, None] * np.array(color)[None, None, :]

        return led_character

    def get_string_array(self, string: str, color: tuple[int, int, int]) -> np.ndarray:
        if min(color) < 0 or max(color) > 255:
            return np.zeros(shape=(self.font_height, 1))

        # create boolean string
        bool_string = np.zeros(shape=(self.font_height, 1))
        for character in string:
            (succes, bool_character) = self.font.get_bool_character(character)

            if not succes:
                continue

            bool_string = np.concatenate((bool_string, bool_character), axis=1)
            bool_string = np.concatenate(
                (bool_string, np.zeros(shape=(self.font_height, 1))), axis=1
            )

        # convert bool to color string
        led_string = bool_string[:, :, None] * np.array(color)[None, None, :]

        return led_string
