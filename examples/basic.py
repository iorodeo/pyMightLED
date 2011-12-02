"""
basic.py

illustrates how to set the output current of a channel using normal mode.
"""
import time
from pyMightLED import LedController

port = '/dev/ttyUSB0'
chan = 1
imax = 1000 # Maximum allowed current

dev = LedController(port)

dev.setNormalModeParams(chan,imax,0)
dev.setMode(1,'normal')

for iset in [5,50,100,300,600]:
    print('iset: {0}mA'.format(iset))
    dev.setNormalModeCurrent(chan,iset)
    time.sleep(1.0)

dev.setMode(1,'disable')
dev.close()
