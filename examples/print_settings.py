"""
print_settings.py - illustrates how to print the devices current settins.
"""
from pyMightLED import LedController

port = '/dev/ttyUSB0'
dev = LedController(port)
dev.printSettings()
