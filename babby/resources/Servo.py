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
import gc

class servo:
    
    def __init__(self,pin,initalAngle,minPulseTime,maxPulseTime,freq=50.0,angularOffset=0):
        '''minPulseTime and maxPulseTime are the pulse widths (in milliseconds)
        which correspond to 0 degrees and 180 degrees, respectively
        ANGLES SHOULD BE KEPT IN DEGREES'''
        
        GPIO.setup(pin,GPIO.OUT)
        self.pulseTime = 1.0/freq * (10**3) #Total Pulse [milliseconds]
        
        self.lower = minPulseTime / self.pulseTime
        self.upper = maxPulseTime / self.pulseTime
        
        self.angularOffset = angularOffset
        
        self.pin = GPIO.PWM(pin,freq)         #Declare PWM pin

        #Initialization
        self.cycle = getCycle(initialAngle)
        self.angle = initialAngle
        self.pin.start( self.cycle )            
        
        gc.collect() #Collect Garbage
    
    
    def getCycle(self,angle):
        #Uses affine map to calculate duty cycle from lower limit, upper limit and position
        cycle = 100 * ( self.lower + (self.upper - self.lower) * self.angle / 180.0 ) / self.pulseTime 
        gc.collect() #Collect Garbage
        return cycle
    
    
    def setPosition(self,angle):
        if (degree < self.lower) or (degree > self.upper):
            print 'Position outside of range'
            return
        else:
            self.angle = angle - self.angularOffset
            self.cycle = self.getCycle(angle)
            self.pin.ChangeDutyCycle(self.cycle)
   
    
    def end(self):
        self.pin.stop()
        gc.collect() #Collect Garbage
        
