Backup of Michael Shedworth project

Full software for building a miniature, head-worn shed complete with audio playback, three WS2182B pixel strips and roof-mounted flamethrower.

A Raspberry Pi running a Python script does the following:
- Plays back audio over the onboard soundcard
- Periodically sends a string over the USB port to an Arduino, containing various instructions
- Allows remote control of the shed over VNC

An Arduino does the following:
- Waits to receive a control string from the Raspberry Pi and unpacks it
- Controls the shed's various peripherals according to commands contained within the control string
- Interfaces with 3 x WS2182B pixel strips and a 5V DC solenoid inline with a butane supply via a custom-build circuit board
