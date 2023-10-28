import board
import digitalio
import KMKMatrix
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import KMKMatrix
from kmk.matrix import DiodeOrientation


# Define your matrix configuration (2x4 matrix)
matrix = KMKMatrix(
    rows=[digitalio.DigitalInOut(pin) for pin in (board.GP2, board.GP3)],
    columns=[digitalio.DigitalInOut(pin) for pin in (board.GP4, board.GP5, board.GP6, board.GP7)],
    diode_orientation=DiodeOrientation.COLUMNS
)

keyboard = KMKKeyboard(matrix)

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
    keyboard.go()
