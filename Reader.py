import sys

from evdev import InputDevice, ecodes, list_devices
from select import select


class Reader:
    def __init__(self):
        self.keys = "X^1234567890XXXXqwertzuiopXXXXasdfghjklXXXXXyxcvbnmXXXXXXXXXXXXXXXXXXXXXXX"

        devices = [InputDevice(fn) for fn in list_devices()]
        if len(devices) == 0:
            sys.exit('No input devices detected.' % device_name)

        self.dev = devices[0]

    def readCard(self):
        stri = ''
        key = ''
        while key != 'KEY_ENTER':
            r, w, x = select([self.dev], [], [])
            for event in self.dev.read():
                if event.type == 1 and event.value == 1:
                    stri += self.keys[event.code]
                    key = ecodes.KEY[event.code]
        return stri[:-1]
