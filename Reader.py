import sys
import os

from evdev import InputDevice, ecodes, list_devices


class Reader:
    def __init__(self):
        self.keys = "X^1234567890XXXXqwertzuiopXXXXasdfghjklXXXXXyxcvbnmXXXXXXXXXXXXXXXXXXXXXXX"

        devices = [InputDevice(fn) for fn in list_devices()]
        if len(devices) == 0:
            sys.exit('ERROR: No input devices detected.\n'
                     'If running inside Docker, be sure to use the `--device` parameter to expose the RFID reader to '
                     'the container')

        if len(devices) == 1:
            self.dev = devices[0]
            return

        if not 'RFID_READER_NAME' in os.environ:
            sys.exit('ERROR: More than one input device was detected. You have two options:\n'
                     '1. If running inside Docker, expose only a single input device using the `--device` parameter\n'
                     '2. If running outside Docker or exposing multiple input devices to the container, set the '
                     '"RFID_READER_NAME" to the NAME of the reader (not the filename). You can use the list_devices '
                     'script to view the names of all input devices on your system.')

        device_name = os.environ['RFID_READER_NAME']
        for device in devices:
            if device.name.strip().lower() == device_name.strip().lower():
                self.dev = device
                return

        sys.exit('ERROR: No input device named ' + device_name + ' was found.')

    def readCard(self):
        stri = ''
        key = ''
        while key != 'KEY_ENTER':
            for event in self.dev.read():
                if event.type == 1 and event.value == 1:
                    stri += self.keys[event.code]
                    key = ecodes.KEY[event.code]
        return stri[:-1]

