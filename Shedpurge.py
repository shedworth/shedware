#! /usr/bin/env python

import serial, time
    

def serWrite():
    arduino.write((serialOut).encode())

def Colour(red, green, blue, white = 0):
    if white == 0 and red == 0 and green == 0 and blue ==0:
        return str("00000000")
    else:
        return ((str((white << 24) | (red << 16)| (green <<8) | blue)).zfill(8))

def sides(pattern, red1, green1, blue1, red2, green2, blue2, rate):
        shedMove(1,pattern,red1,green1,blue1,red2,green2,blue2,rate)
        shedMove(2,pattern,red1,green1,blue1,red2,green2,blue2,rate)
        
def window(pattern,red1,green1,blue1,red2,green2,blue2,rate):
        shedMove(3,pattern,red1,green1,blue1,red2,green2,blue2,rate)


class shedMove(object):
    
    def __init__(self, fixture = "0", pattern = "0", red1 = 0, green1 = 0, blue1 = 0, red2 = 0, green2 = 0, blue2 = 0, rate = "000"):
        self.fixture = fixture
        self.pattern = pattern
        self.colour1 = Colour(red1, green1, blue1)
        self.colour2 = Colour(red2, green2, blue2)
        self.rate = rate

        self.combine()

    def combine(self):
        self.rate = (str(self.rate).zfill(3))        
        serialOut = (str(self.fixture) + str(self.pattern) + str(self.colour1) + str(self.colour2) + str(self.rate) + "\n")
     

        arduino.write(str(serialOut))
   


arduino = serial.Serial('/dev/ttyACM0', 19200, timeout=.5)

time.sleep(5) # wait for Arduino to get its shit together




""" MAIN SEQUENCE """

shedMove(4,0,0,0,0,0,0,0,255)

