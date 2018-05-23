rfid-hass-bridge

### Determining which device to expose to Docker
This project includes a handy container that you can run to determine which device is your RFID reader:
```
sudo docker container run --rm --privileged -v /dev/input/:/dev/input/ overloadut/rfid-hass-bridge:arm32v7 python list_devices.py
```

<details>
  <summary>Docker command breakdown</summary>

  * `docker container run`: Run a container
  * `--rm`: Remove the container after it exits
  * `--privileged`: Run the container with elevated permissions (this is necessary when binding host devices in /dev)
  * `-v /dev/input/:/dev/input/`: Make the host's `/dev/input/` directory available inside the container's filesystem at the same location
  * `overloadut/rfid-hass-bridge:arm32v7`: The image to use (pulls from Docker Hub if you don't have it locally), as well as the tag to use. `arm32v7` is for Raspberry Pi 3. If you are using a Raspberry Pi Zero, use `:arm32v6`
  * `python list_devices.py`: Override the normal CMD for this image with our own command. This is how we run the script that simply outputs all of the input devices.
</details>

The output of this command will be something like
```
List of input devices:
/dev/input/event1 "lircd-uinput"
/dev/input/event0 "Sycreader USB Reader"
```

In this case, you would want to use `/dev/input/event0`