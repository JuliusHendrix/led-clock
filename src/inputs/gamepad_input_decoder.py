import hid
from dataclasses import dataclass
from enum import Enum


# code based on: https://blog.thea.codes/talking-to-gamepads-without-pygame/
class GamepadInputDecoder:
    DEVICE_VENDOR_ID = 0x081F
    DEVICE_PRODUCT_ID = 0xE401

    class GamepadButtons(Enum):
        A = 0
        B = 1
        X = 2
        Y = 3
        LB = 4
        RB = 5
        START = 6
        SELECT = 7
        UP = 8
        DOWN = 9
        LEFT = 10
        RIGHT = 11

    @dataclass
    class ButtonBitmap:
        index: int
        bitmap: int

    button_bitmaps = {
        GamepadButtons.A: ButtonBitmap(5, 0b00100000),
        GamepadButtons.B: ButtonBitmap(5, 0b01000000),
        GamepadButtons.X: ButtonBitmap(5, 0b00010000),
        GamepadButtons.Y: ButtonBitmap(5, 0b10000000),
        GamepadButtons.LB: ButtonBitmap(6, 0b00000001),
        GamepadButtons.RB: ButtonBitmap(6, 0b00000010),
        GamepadButtons.START: ButtonBitmap(6, 0b00100000),
        GamepadButtons.SELECT: ButtonBitmap(6, 0b00010000),
    }

    d_pad_bitmaps = {
        GamepadButtons.UP: ButtonBitmap(1, 0),
        GamepadButtons.DOWN: ButtonBitmap(1, 255),
        GamepadButtons.LEFT: ButtonBitmap(1, 255),
        GamepadButtons.RIGHT: ButtonBitmap(1, 255),
    }

    def __init__(self) -> None:
        for device in hid.enumerate():
            print(
                f"0x{device['vendor_id']:04x}:0x{device['product_id']:04x} {device['product_string']}"
            )
        self.gamepad = hid.device()
        self.gamepad.open(self.DEVICE_VENDOR_ID, self.DEVICE_PRODUCT_ID)
        self.gamepad.set_nonblocking(True)

    def get_inputs(self) -> list[GamepadButtons]:
        report = self.gamepad.read(64)

        if not report:
            return []

        buttons_pressed = []

        # buttons
        for button, bitmap in self.button_bitmaps.items():
            if report[bitmap.index] & bitmap.bitmap:
                buttons_pressed.append(button)

        # d-pad
        for direction, bitmap in self.d_pad_bitmaps.items():
            if report[bitmap.index] == bitmap.bitmap:
                buttons_pressed.append(direction)

        return buttons_pressed
