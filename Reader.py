import os.path
import sys

from evdev import InputDevice, categorize, ecodes, list_devices
from select import select


class Reader:
    def __init__(self, device_name):
        self.keys = "X^1234567890XXXXqwertzuiopXXXXasdfghjklXXXXXyxcvbnmXXXXXXXXXXXXXXXXXXXXXXX"

        devices = [InputDevice(fn) for fn in list_devices()]
        for device in devices:
            print(device.name.strip(), device_name.strip())
            if device.name.strip() == device_name.strip():
                self.dev = device
                print(device)
                break
        try:
            self.dev
        except:
            sys.exit('Could not find the device %s\n. Make sure is connected' % device_name)

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
