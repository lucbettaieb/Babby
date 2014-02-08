#Main file for babby
#Andrew M. Blasius

from math import abs,cos,acos,radians
from resources import Map,Servo,Motor,Angle
from Map import search,initMap
from Servo import servo
from Motor import motor
from Angle import switchAngle,convert
import RPi.GPIO as GPIO

class babby:
    def __init__(self,speed,maxspeed,legdistance,baseHeight,strutHeight
                 s1,s2,s3,s4,m1,m2,m3,m4,
                 minPulseTime,maxPulseTime,initAngle=90,
                 serPort='/dev/ttyAMA0',baud=9600,tolerance=.01):
        ''' speed should be given in units [distance]/sec and legdistance should be consistent. 
            s1 through s4 (as inputs) are the pin numbers of the pins controlling the servo motors. (INT)
            m1 through m4 (as inputs) are the pin numbers of the pins controlling the DC motors. (INT)
            speed is the initial speed of Babby (given in units of {distance}/sec). (FLOAT)
            maxspeed is the maximum speed of the motors. This is used to calculate the duty cycle of the PWM output. (FLOAT)
            legdistance is the distance between Babby's Legs. (FLOAT)
            baseHeight is the height returned by the ARDUINO when measuring ground with a slope m=0. (FLOAT)
            strutHeight is the height (not length) of the static strut. (FLOAT)
            minPulseTime is the minimum angular position (in degrees) to which the servos can sweep (INT)
            maxPulseTime is the maximum angular position (in degrees) to which the servos can sweep (INT)
            initAngle is the initial position of the servo motors. (INT)
            serPort is a string representing the address of the Rasperry Pi's serial port (STR)
            baud is the baudrate for the Raspberry Pi's serial port (INT)
            tolerance is the error allowed in computing the movement of babby's legs (FLOAT)
        '''
            
        #Servo Setup    
        self.s1 = servo(s1,initAngle,minPulseTime,maxPulseTime)
        self.s2 = servo(s2,initAngle,minPulseTime,maxPulseTime)
        self.s3 = servo(s3,initAngle,minPulseTime,maxPulseTime)
        self.s4 = servo(s4,initAngle,minPulseTime,maxPulseTime)
        
        self.maxSpeed = maxspeed
        self.speed = speed
        self.dt = dt
        self.timeSeparation = float(legdistance)/self.speed #Calculate the initial time separation
        
        #DC Motor Setup
        self.cycle = (float(speed)/maxspeed) * 100
        self.m1 = motor(m1,cycle=self.cycle)
        self.m2 = motor(m2,cycle=self.cycle)
        self.m3 = motor(m3,cycle=self.cycle)
        self.m4 = motor(m4,cycle=self.cycle)
        
        #Serial Setup
        self.ser = serial.begin(serPort,baud) #Should add something to initialize handshaking
        
        #Map Setup
        self.map = initMap(timeSeparation,dt)
        self.heightSum = 0
        self.baseHeight= baseHeight
        self.frontHeight = 0
        self.backHeight = 0
        self.tol = tolerance
        
        #Leg x-coordinate setup
        self.frontX = 0
        self.backX = -legSeparation
        
        #Constant, intrinsic babby properties
        self.L = strutHeight
        
        #Handshake with ARDUINO 
        self.handshake()
        

    def handshake(self):
        '''Checks to make sure that we're connected to the ARDUINO, and sends our timestep dt'''
        print 'Handshaking in progress...'
        self.ser.write('!')
        print 'Sent character:\'!\'\nAwaiting response...'
        recByte = ser.readline()
        if recByte == '!':
            print 'Response received! Ready to proceed!\nSending dt'
            self.ser.write(str(dt))
            print 'Waiting for response...'
            recByte = ser.readline()
            if recByte == '!':
                print 'Ready to go!'
                return
    
    
    def getHeights(self):
        self.dx = self.dt * self.speed
        self.frontX += self.dx
        self.backX += self.dx
        
        #Getting back height
        if self.backX <= 0:
            self.backHeight = 0 + self.L * cos(radians(self.angle)) #ANGLE NEEDS TO BE FIXED
        else:
            height = map.search(self.map,self.backX,self.tol)
            self.backHeight = height + self.L * cos(radians(self.angle)) #ANGLE NEEDS TO BE FIXED
        
        #Getting front height
        reading = self.ser.readline()
        self.heightSum += self.dx * reading
        self.map.appendright((self.frontX,self.heightSum)) 
        self.frontHeight = self.heightSum
   
   
    def moveLegs(self):
        '''Needs Revision!'''
        difference = self.FrontHeight - self.BackHeight
        if abs(difference) < self.tol:
            pass
        try:
            s1.angle = acos(cos( radians(self.s3.angle) ) - difference/self.L) #ANGLE NEEDS TO BE FIXED
            s2.angle = self.switchAngle(self.s1.angle)
        except:
            try:
                s3.angle = acos(cos( radians(s1.angle) ) + difference/self.L) #ANGLE NEEDS TO BE FIXED
                s4.angle = self.convertAngle(self.s3.angle)
            except:
                print 'Can\'t move legs!'
                raise 
       
            
    def run(self):
        while True:
            self.getHeights()
            self.moveLegs()
        
        
    def end(self):
        '''Closes up open ports.'''
        #Close servos
        self.s1.end()
        self.s2.end()
        self.s3.end()
        self.s4.end()
        
        #Close DC motors
        self.m1.end()
        self.m2.end()
        self.m3.end()
        self.m4.end()
        
        #Close serial and cleanup
        self.ser.close()
        GPIO.cleanup()
        
    
if __name__ == '__main__':
    GPIO.setmode(GPIO.BOARD)
    initSpeed = #
    maxSpeed = #Set by motor specs
    legDistance = #
    baseHeight = #
    strutHeight = #
    s1 = #
    s2 = #
    s3 = #
    s4 = #
    m1 = #
    m2 = #
    m3 = #
    m4 = #
    minPulseTime = #Set by servo specs
    maxPulseTime = #Set by servo specs
    tolerance = #
    Babby = babby(initSpeed,maxSpeed,legDistance,baseHeight,strutHeight
                 s1,s2,s3,s4,m1,m2,m3,m4,
                 minPulseTime,maxPulseTime,tolerance)
    Babby.run()
    Babby.end()
