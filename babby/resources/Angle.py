#Angular conversion for babby

def switchAngle(angle):
    '''Switches angle from servo to servo
    ie. an angle of 100 degrees at one servo (s1)
    will correspond to an angle of 80 degrees at the opposite servo (s2)
    '''
    return 180 - angle
    
def convert(angle):
    '''Converts the angle fed into the servo into an angle that works with
    the cosine calculation'''
    return angle - 90 