import board
import digitalio
import neopixel
from my_extension import MyExtension

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC

# Direct key scanner to replace matrix scanner
from kmk.scanners.keypad import KeysScanner

print("Starting")

# GPIO to key mapping - each line is a new row.
# The switches are connected to these microcontroller pins through the PCB.
_KEY_CFG = [
    board.GP27, board.GP28, board.GP26
]

# Turn on internal NeoPixel
led = digitalio.DigitalInOut(board.GP11)
led.direction = digitalio.Direction.OUTPUT
led.value = True

# Keyboard implementation for direct pin connection (i.e. not a matrix)
class MyKeyboard(KMKKeyboard):
    def __init__(self):
        # create and register the scanner
        self.matrix = KeysScanner(
            pins=_KEY_CFG,
            value_when_pressed=False,
            pull=True,
            interval=0.02,  # Debounce time in floating point seconds
            max_events=64
        )


keyboard = MyKeyboard()

# Extensions let you add custom hooks to the firmware's event loop.
ext = MyExtension()
keyboard.extensions.append(ext)

# Change your keymap here
# Keycodes can be found on http://kmkfw.io/docs/keycodes
# Left to right, with the USB port facing right
keyboard.keymap = [
    [KC.LGUI, KC.C, KC.V]
]

if __name__ == '__main__':
    keyboard.go()
