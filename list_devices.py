from evdev import InputDevice, list_devices

devices = [InputDevice(fn) for fn in list_devices()]

if len(devices) > 0:
    print("List of input devices:")
    for dev in devices:
        print(dev.fn + ' "' + dev.name + '"')
else:
    print("No input devices found at /dev/input/ \nIf running inside a container, did you bind your host's input directory? (-v /dev/input/:/dev/input/)")
