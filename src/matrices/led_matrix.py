import board
import neopixel
import numpy as np
import atexit

from .matrix_abc import MatrixABC

PIN = board.D18
MATRIX_SHAPE = (16, 32)


class LEDMatrix(MatrixABC):
    def __init__(self) -> None:
        super().__init__(MATRIX_SHAPE)

        self._number_of_pixels = np.prod(MATRIX_SHAPE)
        self._pixels = neopixel.NeoPixel(PIN, self._number_of_pixels)
        self._indices_to_flip = np.arange(1, MATRIX_SHAPE[1], 2)

        atexit.register(
            self.clear
        )  # TODO: memory leak? "swig/python detected a memory leak of type 'ws2811_t *', no destructor found."

    def _array_to_strip(self, array: np.ndarray) -> np.ndarray:
        # flip every even column
        flipped_array = array
        flipped_array[:, self._indices_to_flip] = array[::-1, self._indices_to_flip]
        # flatten column-major order
        return flipped_array.reshape(self._number_of_pixels, 3, order="F")

    def display_array(self, array: np.ndarray) -> None:
        if not self._validate_array(array):
            return

        scaled_array = self._scale_array_brightness(array)
        strip = self._array_to_strip(scaled_array)
        print(f"{strip.dtype = }")
        self._pixels[:] = strip
