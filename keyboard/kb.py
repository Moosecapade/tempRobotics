import board  # Importing the board module for hardware interface

from kmk.extensions.LED import LED  # Importing the LED class from the kmk.extensions module
from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard  # Importing the KMKKeyboard class as _KMKKeyboard from kmk.kmk_keyboard module
from kmk.scanners import DiodeOrientation  # Importing the DiodeOrientation class from kmk.scanners module

# Defining a custom class KMKKeyboard that extends _KMKKeyboard
class KMKKeyboard(_KMKKeyboard):

    # Defining column pins for the keyboard matrix
    col_pins = (
        board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5,
        board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11,
        board.GP12, board.GP13, board.GP14, board.GP15, board.GP16, board.GP17,
    )

    # Defining row pins for the keyboard matrix
    row_pins = (
        board.GP18, board.GP19, board.GP20, board.GP21, board.GP22, board.GP26,
    )

    # Specifying the diode orientation (assumes diodes are in columns)
    diode_orientation = DiodeOrientation.COLUMNS

    # Setting up LEDs for the keyboard
    leds = LED(led_pin=[board.GP27, board.GP28])
    
    # Appending the LEDs extension to the extensions list
    _KMKKeyboard.extensions.append(leds)
