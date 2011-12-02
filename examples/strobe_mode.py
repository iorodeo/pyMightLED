"""
strobe_mode.py - illustrates how to use strobe mode
"""
from pyMightLED import LedController

port = '/dev/ttyUSB0'
chan = 1
imax = 1000 # Maximum allowed current

dev = LedController(port)

# Set strobe mode parameters
imax = 1000 # max current in mA
repeat = 20 # repeat count (integer or string 'forever')
dev.setStrobeModeParams(chan,imax, repeat)

# Set the strobe mode profile
# Profile step 0
step = 0      # profile step number
iset = 200    # setpt current in mA
tset = 50000  # setpt time in us
dev.setStrobeModeProfile(chan,step,iset,tset)

# Profile step 1
step = 1       # profile step number
iset = 10      # setpt current in mA 
tset = 70000  # setpt time in us 
dev.setStrobeModeProfile(chan,step,iset,tset)

# Start the strobe output
dev.setMode(chan,'strobe')

