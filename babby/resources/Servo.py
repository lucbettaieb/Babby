#Servo Motor Module
#Andrew M. Blasius

'''
Servos Expect to receive a pulse every 20 ms => 50 times/sec => 50Hz
    -0 degrees corresponds to a pulse width of 1 ms => on for 5 % => DC = 5
    -90 degrees corresponds to a pulse width of 1.5ms => on for 7.5% => DC = 7.5
    -180 degrees corresponds to a pulse width of 2 ms => on for 10.0% => DC = 10.0
'''

import time
import RPi.GPIO as GPIO

class servo:
    def __init__(self,pin,degree,minPos,maxPos,freq = 50.0):
        '''minPos and maxPos are the pulse widths (in milliseconds)
        which correspond to 0 degrees and 180 degrees, respectively'''
        GPIO.setup(pin,GPIO.OUT)
        self.pulseTime = 1.0/freq * (10**3) #Total Pulse [milliseconds]
        self.lower = minPos / self.pulseTime
        self.upper = maxPos / self.pulseTime
        self.pin = GPIO.PWM(pin,freq)
        cycle = self.getCycle(degree)
        self.pin.start(cycle)
        
    def getCycle(self,degree):
        #Uses affine map to calculate duty cycle from lower limit, upper limit and position
        cycle = (self.lower*(1 - degree/180.0) + self.upper*(degree/180.0)) * 100
        return cycle
        
    def setPosition(self,degree):
        cycle = self.getCycle(degree)
        self.pin.ChangeDutyCycle(cycle)
    
    def end(self):
        self.pin.stop()
    
        
