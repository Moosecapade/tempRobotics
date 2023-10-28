import board  # Importing the board module for hardware interface
import digitalio  # Importing the digitalio module for digital input/output control
import KMKMatrix  # Importing KMKMatrix for handling keyboard matrix
from kmk.kmk_keyboard import KMKKeyboard  # Importing the KMKKeyboard class
from kmk.keys import KC  # Importing keycodes (KC) for defining key mappings
from kmk.matrix import KMKMatrix  # Importing KMKMatrix for defining matrix configuration
from kmk.matrix import DiodeOrientation  # Importing DiodeOrientation for specifying diode orientation

# Define your matrix configuration (2x4 matrix)
matrix = KMKMatrix(
    rows=[digitalio.DigitalInOut(pin) for pin in (board.GP2, board.GP3)],
    columns=[digitalio.DigitalInOut(pin) for pin in (board.GP4, board.GP5, board.GP6, board.GP7)],
    diode_orientation=DiodeOrientation.COLUMNS
)

keyboard = KMKKeyboard(matrix)  # Creating an instance of the KMKKeyboard with the defined matrix

# Define key mappings to send the respective letter
keyboard.keymap = {
    (0, 0): KC.A,
    (0, 1): KC.B,
    (0, 2): KC.C,
    (0, 3): KC.D,
    (1, 0): KC.E,
    (1, 1): KC.F,
    (1, 2): KC.G,
    (1, 3): KC.H,
}

if __name__ == '__main__':
    keyboard.go()  # Start the keyboard
