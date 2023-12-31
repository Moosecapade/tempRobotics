import board  # Importing the board module for hardware interface

from kb import KMKKeyboard  # Importing the KMKKeyboard class from the kb module

# Importing specific components/extensions from the KMK library
from kmk.extensions.lock_status import LockStatus
from kmk.extensions.stringy_keymaps import StringyKeymaps
from kmk.keys import KC
from kmk.modules.layers import Layers

# Creating an instance of the KMKKeyboard named Pico87
Pico87 = KMKKeyboard()

# Defining a custom class LEDLockStatus that extends LockStatus
class LEDLockStatus(LockStatus):
    def set_lock_leds(self):
        # Setting caps lock LED brightness
        if self.get_caps_lock():
            Pico87.leds.set_brightness(50, leds=[0])
        else:
            Pico87.leds.set_brightness(0, leds=[0])

        # Setting scroll lock LED brightness
        if self.get_scroll_lock():
            Pico87.leds.set_brightness(50, leds=[1])
        else:
            Pico87.leds.set_brightness(0, leds=[1])

    def after_hid_send(self, sandbox):
        super().after_hid_send(sandbox)  # Calling parent class method (LockStatus)
        
        # If lock status report was updated, update LED status
        if self.report_updated:
            self.set_lock_leds()

# Adding a Layers module to the keyboard
Pico87.modules.append(Layers())

# Adding the custom LEDLockStatus extension to the keyboard
Pico87.extensions.append(LEDLockStatus())

# Adding the StringyKeymaps extension to the keyboard
Pico87.extensions.append(StringyKeymaps())

# Defining a special key code MOLYR using the MO function from the KC module
MOLYR = KC.MO(1)

# Placeholder for a key (value is 'NO')
______ = 'NO'

# Defining the keymap for the keyboard
Pico87.keymap = [
    # Layer 0 QWERTY
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
    [
        # Layer 1
        'ESC', ______, 'F1', 'F2', 'F3', 'F4', ______, 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'PSCR', 'SLCK', 'PAUS',
        'GRV', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'N8', 'N9', 'N0', 'MINS', 'EQL', ______, 'BSPC', 'INS', 'HOME', 'PGUP',
        'TAB', ______, 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'LBRC', 'RBRC', 'BSLS', 'DEL', 'END', 'PGDN',
        'CAPS', ______, 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'SCLN', 'QUOT', 'ENT', ______, ______, ______, ______,
        ______, 'LSFT', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', 'COMM', 'DOT', 'SLSH', ______, 'RSFT', ______, ______, 'UP', ______,
        'LCTL', 'LGUI', ______, 'LALT', ______, ______, 'SPC', ______, ______, ______, 'RALT', 'RGUI', ______, MOLYR, 'RCTL', 'LEFT', 'DOWN', 'RGHT',
    ]
]

# Check if this script is run directly
if __name__ == '__main__':
    Pico87.go()  # Start the keyboard
