
"""
Mapping the pyautogui to the keyboard
"""

import pyautogui

from pybat.codec.ecc import OnebyteReedSolomonEcc, EmptyEcc
from pybat.communication import SoundReceiver


# table of letter and keycode
command = {"n": "down", "b": "up"}


def operate_keyboard_if_necessary(data_string):
    candidates = [k for k in command.keys() if k in data_string]
    if len(candidates) > 0:
        pyautogui.press(command[candidates[0]])


def launch_receiver(coder=EmptyEcc()):
    print("Listening to Ultrasonic sound ......")
    receiver = SoundReceiver(debug=False, coder=coder)
    while True:
        data = receiver.receive()
        if len(data) > 0:
            data_string = receiver.convert_data_to_ascii_string(data)
            print("Decoded Decimal: %s" % [int(d) for d in data])
            print("Decoded Binary : %s" % [format(int(d), 'b') for d in data])
            print("Decoded String : %s" % data_string)
            operate_keyboard_if_necessary(data_string)


if __name__ == "__main__":
    # Launch a sound receiver with Reedsolomon
    launch_receiver(OnebyteReedSolomonEcc())
