import os
from pathlib import Path
import sys
import numpy as np
import time


# own modules
script_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = str(Path(script_dir).parents[0])
src_dir = os.path.join(root_dir, "src")

sys.path.append(src_dir)

from inputs.gamepad_input_decoder import GamepadInputDecoder


def main():
    gamepad_input_manager = GamepadInputDecoder()
    gamepad_input_manager.start()

    for _ in range(1000):
        print(
            gamepad_input_manager.pressed_buttons[GamepadInputDecoder.GamepadButtons.A]
        )
        time.sleep(0.02)

    gamepad_input_manager.stop()


if __name__ == "__main__":
    main()
