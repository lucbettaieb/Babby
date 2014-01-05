#Module for controlling simple motors with PWM
#Andrew M. Blasius

'''Assumes we have a PWM pin hooked up to a PNP/NPN transistor as follows:
    Collector                   Emitter
        0 ------- PNP/NPN ---------0
                    |
                    |
                    |
            Pinout >0
                  Base
'''

import RPi.GPIO as GPIO
import time

class motor:
    def __init__(self,pin,cycle=0,freq=50): #Initially off with freq = 50Hz
        GPIO.setup(pin,GPIO.OUT)
        self.pin = GPIO.PWM(pin,freq)
        self.pin.start(cycle)
    
    def setSpeed(self,speed):
        #Speed should range from 0% to 100%
        try:
            self.pin.ChangeDutyCycle(speed)
        except:
            print 'Speed outside acceptable range'
            return
    
    def end(self)
        self.pin.stop()
        print 'PWM ended'
 
        
        