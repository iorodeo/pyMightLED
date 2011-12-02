"""
Copyright 2010  IO Rodeo Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import led_controller

class PwmController(object):
    """
    Controls led intesity using pwm based on the strobe mode of  the
    mighex LED controllers.
    """

    def __init__(self,port,freq=1000,iset=[1000,1000,1000,1000]):
        self._createEnabledList()
        self.freq = float(freq)
        self.iset = iset
        self.ledController = led_controller.LedController(port)
        self.disableAll()
        self.setImaxAll(led_controller.MAX_CURRENT)
        self.setValueAll([0,0,0,0])

    def _createEnabledList(self):
        self.enabledList = []
        for i in range(led_controller.NUM_CHANNELS):
            self.enabledList.append(False)

    def enable(self,chan):
        self.ledController.setMode(chan,'strobe')
        self.enabledList[chan-1] = True

    def disable(self,chan):
        self.ledController.setMode(chan,'disable')
        self.enabledList[chan-1] = False

    def enableAll(self):
        for i in range(led_controller.NUM_CHANNELS):
            self.enable(i+1)

    def disableAll(self):
        for i in range(led_controller.NUM_CHANNELS):
            self.disable(i+1)

    def getPeriod(self):
        """
        Calculates the period in us 
        """
        period = 1.0/float(self.freq)
        period = period*1.0e6
        return int(period)

    def setValue(self,chan,value):
        """
        Set the output value for the given channel. 
        chan = channel number 1,2,3 or 4
        value = channel value (float between 0 and 1)
        """
        period = self.getPeriod()
        timeHigh = int(value*period)
        timeLow = period - timeHigh
        if timeHigh == 0:
            self.disable(chan)
        else:
            iset = self.iset[chan-1]
            self.ledController.setStrobeModeProfile(chan,0,iset,timeHigh)
            self.ledController.setStrobeModeProfile(chan,1,0,timeLow)
            if self.enabledList[chan-1]:
                self.enable(chan)

    def setValueAll(self,valueList):
        """
        Set the output values for all channels
        """
        for i,value in enumerate(valueList):
            self.setValue(i+1,value)

    def setImax(self,chan,imax):
        self.ledController.setStrobeModeParams(chan,imax,'forever')

    def setImaxAll(self,imax):
        for i in range(led_controller.NUM_CHANNELS):
            self.setImax(i+1,imax)

# -----------------------------------------------------------------------------
if __name__ == '__main__':
    import time

    dev = PwmController('/dev/ttyUSB0')
    dev.enable(1)
    dev.setValue(1,0.1)
    time.sleep(1)
    dev.disable(1)






