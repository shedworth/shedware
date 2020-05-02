#! /usr/bin/env python

import serial, time
import pyglet
    

tempo = 100
beat = int(tempo/3.7)
tempBeat = (60.0/tempo)

print tempBeat

def deltime(x):
    time.sleep(x*0.001)

def delInstant():
    time.sleep(0.01)

def del4Bar():
    time.sleep(tempBeat * 16)
    
def del1Bar():
    time.sleep(tempBeat * 4)

def del1Beat():
    time.sleep(tempBeat)

def delQuaver():
    time.sleep(tempBeat / 2)

def delSquaver():
    time.sleep(tempBeat/4)

def delSSquaver():
    time.sleep(tempBeat/8)

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

def flames(rate):
        shedMove(4,0,0,0,0,0,0,0,rate)


""" Define some lighting states"""

def sidesblack():
    sides(1,0,0,0,0,0,0,0)

def sides1():   # sides purple
    sides(1,150,0,150,0,0,0,0)    

def sides2():   # sides yellow
    sides(1,255,150,0,0,0,0,0)

def sides3():   #sides red
    sides(1,255,0,0,0,0,0,0)

def sides4():   # sides green
    sides(1,0,35,0,0,0,0,0)

def sides5():   # sides blue
    sides(1,0,0,255,0,0,0,0)


def sides_scan1():  # sides scan yellow
    sides(2,255,150,0,0,0,0,12)
    
    









        

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
        #print(str(self.fixture))
        #print(str(self.pattern))
        #print(str(self.colour1))
        #print(str(self.colour2))
        #print(str(self.rate))

        arduino.write(str(serialOut))
        #print(serialOut)


arduino = serial.Serial('/dev/ttyACM0', 19200, timeout=.5)

time.sleep(5) # wait for Arduino to get its shit together

sound = pyglet.media.load('Koan Sound - Mr Brown.wav', streaming=False)
sound.play()



""" MAIN SEQUENCE """

sides(1,255,150,0,0,0,0,0)      # yellow solid
window(1,255,150,0,0,0,0,0)

del1Beat()  # 1/1

sides(1,150,0,150,0,0,0,0)      # purple solid          1/2
window(1,0,0,0,0,0,0,0)

del1Beat()  # 1/2

del1Beat()  # 1/3

del1Beat()  # 1/4

del1Beat()  # 2/1

del1Beat()  # 2/2

del1Beat()  # 2/3

delQuaver() # 2/3.5

sides(2,255,150,0,0,0,0,12)     # yellow scan

delQuaver() # 2/4

delQuaver() # 3/1

delQuaver()

sides(1,150,0,150,0,0,0,0)      # purple solid      3/2

del1Beat()   # 3/2

del1Beat()   # 3/3

del1Beat()   # 3/4

del1Beat()   # 4/1

del1Beat()   # 4/2

del1Beat()   # 4/3

del1Beat()   # 4/4

sides(1,255,150,0,0,0,0,0)      # yellow solid
window(1,255,150,0,0,0,0,0)

delQuaver()  # 1/1

sides(1,150,0,150,0,0,0,0)      # purple solid          1/2
window(1,0,0,0,0,0,0,0)

delQuaver()

del1Beat()  # 1/2

del1Beat()  # 1/3

del1Beat()  # 1/4

del1Beat()  # 2/1

del1Beat()  # 2/2

del1Beat()  # 2/3

delQuaver() # 2/3.5

sides(2,255,150,0,0,0,0,12)     # yellow scan
window(1,0,0,0,0,0,0,0)

delQuaver() # 2/4

delQuaver() # 3/1

delQuaver()

sides(1,150,0,150,0,0,0,0)      # purple solid      3/2


del1Beat()   # 3/2

del1Beat()   # 3/3

del1Beat()   # 3/4

del1Beat()   # 4/1

del1Beat()   # 4/2

del1Beat()   # 4/3

del1Beat()   # 4/4


sides(1,255,150,0,0,0,0,0)      # yellow solid
window(1,255,150,0,0,0,0,0)

delQuaver()  # 1/1

sides(1,150,0,150,0,0,0,0)      # purple solid          1/2
window(1,0,0,35,0,0,0,0)

delQuaver()

del1Beat()  # 1/2

sides(1,255,0,0,0,0,0,0)  # 1/3  red solid

del1Beat()  # 1/3

sides(1,150,0,150,0,0,0,0)      # purple solid 1/4

del1Beat()  # 1/4

sides(1,255,0,0,0,0,0,0)  # 1/3  red solid

del1Beat()  # 1/1

sides(1,150,0,150,0,0,0,0)      # purple solid 1/4

del1Beat()  # 2/2

sides(1,255,0,0,0,0,0,0)  # 1/3  red solid

del1Beat()  # 1/3

sides(1,150,0,150,0,0,0,0)      # purple solid 1/4

delQuaver() # 2/3.5

sides(2,255,150,0,0,0,0,12)     # yellow scan
window(1,0,0,0,0,0,0,0)

delQuaver() # 2/4

delQuaver() # 2/4

delQuaver() # 2/4

sides(1,150,0,150,0,0,0,0)      # purple solid          1/2
window(1,0,0,35,0,0,0,0)

del1Beat()  # 1/2

sides(1,255,0,0,0,0,0,0)  # 1/3  red solid

del1Beat()  # 1/3

sides(1,150,0,150,0,0,0,0)      # purple solid 1/4

del1Beat()  # 1/2

sides(1,255,0,0,0,0,0,0)  # 1/3  red solid

del1Beat()  # 1/3

sides(1,150,0,150,0,0,0,0)      # purple solid 1/4

del1Beat()  # 2/2

sides(1,255,0,0,0,0,0,0)  # 1/3  red solid

del1Beat()  # 1/3

sides(1,150,0,150,0,0,0,0)      # purple solid 1/4

del1Beat() # 2/3.5












sides(1,255,150,0,0,0,0,0)      # yellow solid
window(1,255,150,0,0,0,0,0)

delQuaver()  # 1/1

sides(1,250,0,250,0,0,0,0)      # purple solid          1/2
window(1,0,0,35,0,0,0,0)

delQuaver()

del1Beat()  # 1/2

sides(1,255,0,0,0,0,0,0)  # 1/3  red solid

del1Beat()  # 1/3

sides(1,250,0,250,0,0,0,0)      # purple solid 1/4

del1Beat()  # 1/4

sides(1,255,0,0,0,0,0,0)  # 1/3  red solid

del1Beat()  # 1/1

sides(1,250,0,250,0,0,0,0)      # purple solid 1/4

del1Beat()  # 2/2

sides(1,255,0,0,0,0,0,0)  # 1/3  red solid

del1Beat()  # 1/3

sides(1,250,0,250,0,0,0,0)      # purple solid 1/4

delQuaver() # 2/3.5

sides(2,255,150,0,0,0,0,12)     # yellow scan
window(1,0,0,0,0,0,0,0)

delQuaver() # 2/4

delQuaver() # 2/4

delQuaver() # 2/4

sides(1,250,0,250,0,0,0,0)      # purple solid          1/2
window(1,0,0,35,0,0,0,0)

del1Beat()  # 1/2

sides(1,255,0,0,0,0,0,0)  # 1/3  red solid

del1Beat()  # 1/3

sides(1,250,0,250,0,0,0,0)      # purple solid 1/4

del1Beat()  # 1/2

sides(1,255,0,0,0,0,0,0)  # 1/3  red solid

del1Beat()  # 1/3

sides(1,250,0,250,0,0,0,0)      # purple solid 1/4

del1Beat()  # 2/2

sides(1,255,0,0,0,0,0,0)  # 1/3  red solid

del1Beat()  # 1/3

sides(1,250,0,250,0,0,0,0)      # purple solid 1/4

del1Beat() # 2/3.5


sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,0,0,0,0,0,0)       

#del1Beat()

del4Bar()
del1Bar()
del1Bar()


#window(6,50,0,0,0,0,0,255)

del1Bar()
del1Bar()

sides(1,255,150,0,0,0,0,0)      # yellow solid          DROP!

window(1,255,150,0,0,0,0,0)

flames(40)

delQuaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,20,35,0,0,0,0)        # dim cyan


delQuaver() # 2/4               

sides4()    # Green     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)        

delSquaver()

sides4()   # Green     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides4()    # Green     womp

delSquaver()

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides4()   # Green     womp    

delSquaver() 

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides4()    # Green     womp

delSquaver() 

sides(1,0,0,0,0,0,0,0)

delSquaver()

window(1,0,0,0,0,0,0,0)     # Window blackout

sides(2,255,150,0,0,0,0,12) # Scan

delQuaver()

window(1,0,20,35,0,0,0,0)   # Window cyan

sides(1,0,0,0,0,0,0,0)

delQuaver()

sides4()    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides4()    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

sides4()    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides4()    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

sides4()    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides4()    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()
sides4()    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides4()    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

sides(1,255,150,0,0,0,0,0)      # yellow solid       BANG!

window(1,255,150,0,0,0,0,0)

flames(20)

delSquaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,0,0,0,0,0,0)

delSquaver()

sides(1,255,150,0,0,0,0,0)      # yellow solid          BANG!!

window(1,255,150,0,0,0,0,0)

flames(40)

delQuaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,20,35,0,0,0,0)        # dim cyan


delQuaver() # 2/4               

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)        

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver()

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp    

delSquaver() 

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver() 

sides(1,0,0,0,0,0,0,0)

delSquaver()

window(1,0,0,0,0,0,0,0)     # Window blackout

sides(2,255,150,0,0,0,0,12) # Scan

delQuaver()

window(1,0,20,35,0,0,0,0)   # Window cyan

sides(1,0,0,0,0,0,0,0)

delQuaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()
sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()
sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSquaver()


# SECOND SET OF WOMPS

sides(1,255,150,0,0,0,0,0)      # yellow solid          DROP!

window(1,255,150,0,0,0,0,0)

flames(40)

delQuaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,20,35,0,0,0,0)        # dim cyan


delQuaver() # 2/4               

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)        

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver()

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp    

delSquaver() 

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver() 

sides(1,0,0,0,0,0,0,0)

delSquaver()

window(1,0,0,0,0,0,0,0)     # Window blackout

sides(2,255,150,0,0,0,0,12) # Scan

delQuaver()

window(1,0,20,35,0,0,0,0)   # Window cyan

sides(1,0,0,0,0,0,0,0)

delQuaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()
sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

sides(1,255,150,0,0,0,0,0)      # yellow solid          BANG!

window(1,255,150,0,0,0,0,0)

flames(20)

delSquaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,0,0,0,0,0,0)

delSquaver()

sides(1,255,150,0,0,0,0,0)      # yellow solid          BANG!!

window(1,255,150,0,0,0,0,0)

flames(40)

delQuaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,20,35,0,0,0,0)        # dim cyan


delQuaver() # 2/4               

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)        

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver()

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp    

delSquaver() 

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver() 

sides(1,0,0,0,0,0,0,0)

delSquaver()

window(1,0,0,0,0,0,0,0)     # Window blackout

sides(2,255,150,0,0,0,0,12) # Scan

delQuaver()

window(1,0,20,35,0,0,0,0)   # Window cyan

sides(1,0,0,0,0,0,0,0)

delQuaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()
sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()
sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSquaver()
delSSquaver()

######## THIRD SET OF WOMPS

sides(1,255,150,0,0,0,0,0)      # yellow solid          DROP!

window(1,255,150,0,0,0,0,0)

flames(40)

delQuaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,20,35,0,0,0,0)        # dim cyan


delQuaver()                

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)        

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver()

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides3()    # Red     womp    

delSquaver() 

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides3()    # Red     womp 

delSquaver() 

sides(1,0,0,0,0,0,0,0)

delSquaver()

window(1,0,0,0,0,0,0,0)     # Window blackout

sides(2,255,150,0,0,0,0,12) # Scan

delQuaver()

window(1,0,20,35,0,0,0,0)   # Window cyan

sides(1,0,0,0,0,0,0,0)

delQuaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()
sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSSquaver()
deltime(50)

sides(1,255,150,0,0,0,0,0)      # yellow solid          BANG!

window(1,255,150,0,0,0,0,0)

flames(20)

delSquaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,0,0,0,0,0,0)

delSquaver()

sides(1,255,150,0,0,0,0,0)      # yellow solid          BANG!!

window(1,255,150,0,0,0,0,0)

flames(20)

delSquaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,0,0,0,0,0,0)

delSquaver()

sides2()                        # yellow solid          BANG!!
window(1,255,150,0,0,0,0,0)        # dim cyan
flames(40)

delSquaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,0,0,0,0,0,0)

delSquaver()

            

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)        

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver()

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides3()    # Red     womp   

delSquaver() 

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides3()    # Red     womp 

delSquaver() 

sides(1,0,0,0,0,0,0,0)

delSquaver()

window(1,0,0,0,0,0,0,0)     # Window blackout

sides(2,255,150,0,0,0,0,12) # Scan

delQuaver()

window(1,0,20,35,0,0,0,0)   # Window cyan


delSquaver()

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()
sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()
delSSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()
delSSquaver()


sides(1,255,150,0,0,0,0,0)      # yellow solid          DROP!

window(1,255,150,0,0,0,0,0)

flames(40)

delQuaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,20,35,0,0,0,0)        # dim cyan


delQuaver()                

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)        

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver()

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides3()    # Red     womp    

delSquaver() 

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides3()    # Red     womp 

delSquaver() 

sides(1,0,0,0,0,0,0,0)

delSquaver()

window(1,0,0,0,0,0,0,0)     # Window blackout

sides(2,255,150,0,0,0,0,12) # Scan

delQuaver()

window(1,0,20,35,0,0,0,0)   # Window cyan

sides(1,0,0,0,0,0,0,0)

delQuaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()
sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSSquaver()
deltime(50)

sides(1,255,150,0,0,0,0,0)      # yellow solid          BANG!

window(1,255,150,0,0,0,0,0)

flames(20)

delSquaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,0,0,0,0,0,0)

delSquaver()

sides(1,255,150,0,0,0,0,0)      # yellow solid          BANG!!

window(1,255,150,0,0,0,0,0)

flames(20)

delSquaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,0,0,0,0,0,0)

delSquaver()

sides2()                        # yellow solid          BANG!!
window(1,255,150,0,0,0,0,0)        # dim cyan
flames(40)

delSquaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,0,0,0,0,0,0)

delSquaver()

            

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)        

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver()

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides3()    # Red     womp   

delSquaver() 

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides3()    # Red     womp 

delSquaver() 

sides(1,0,0,0,0,0,0,0)

delSquaver()

window(1,0,0,0,0,0,0,0)     # Window blackout

sides(2,255,150,0,0,0,0,12) # Scan

delQuaver()

window(1,0,20,35,0,0,0,0)   # Window cyan

delSquaver()

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()
sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()
delSSquaver()


delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()
#delSSquaver()


# GREEN WOMPS AGAIN

sides(1,255,150,0,0,0,0,0)      # yellow solid          DROP!

window(1,255,150,0,0,0,0,0)

flames(40)

delQuaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,20,35,0,0,0,0)        # dim cyan


delQuaver() # 2/4               

sides4()    # Green     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)        

delSquaver()

sides4()   # Green     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides4()    # Green     womp

delSquaver()

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides4()   # Green     womp    

delSquaver() 

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides4()    # Green     womp

delSquaver() 

sides(1,0,0,0,0,0,0,0)

delSquaver()

window(1,0,0,0,0,0,0,0)     # Window blackout

sides(2,255,150,0,0,0,0,12) # Scan

delQuaver()

window(1,0,20,35,0,0,0,0)   # Window cyan

sides(1,0,0,0,0,0,0,0)

delQuaver()

sides4()    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides4()    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

sides4()    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides4()    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

sides4()    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides4()    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()
sides4()    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides4()    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

sides(1,255,150,0,0,0,0,0)      # yellow solid       BANG!

window(1,255,150,0,0,0,0,0)

flames(20)

delSquaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,0,0,0,0,0,0)

delSquaver()

sides(1,255,150,0,0,0,0,0)      # yellow solid          BANG!!

window(1,255,150,0,0,0,0,0)

flames(40)

delQuaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,20,35,0,0,0,0)        # dim cyan


delQuaver() # 2/4               

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)        

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver()

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp    

delSquaver() 

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver() 

sides(1,0,0,0,0,0,0,0)

delSquaver()

window(1,0,0,0,0,0,0,0)     # Window blackout

sides(2,255,150,0,0,0,0,12) # Scan

delQuaver()

window(1,0,20,35,0,0,0,0)   # Window cyan

delSquaver()

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()
sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()
sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSquaver()
deltime(50)


# SECOND SET OF WOMPS

sides(1,255,150,0,0,0,0,0)      # yellow solid          DROP!

window(1,255,150,0,0,0,0,0)

flames(40)

delQuaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,20,35,0,0,0,0)        # dim cyan


delQuaver() # 2/4               

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)        

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver()

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp    

delSquaver() 

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver() 

sides(1,0,0,0,0,0,0,0)

delSquaver()

window(1,0,0,0,0,0,0,0)     # Window blackout

sides(2,255,150,0,0,0,0,12) # Scan

delQuaver()

window(1,0,20,35,0,0,0,0)   # Window cyan

sides(1,0,0,0,0,0,0,0)

delQuaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()
sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

sides(1,255,150,0,0,0,0,0)      # yellow solid          BANG!

window(1,255,150,0,0,0,0,0)

flames(20)

delSquaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,0,0,0,0,0,0)

delSquaver()

sides(1,255,150,0,0,0,0,0)      # yellow solid          BANG!!

window(1,255,150,0,0,0,0,0)

flames(40)

delQuaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,20,35,0,0,0,0)        # dim cyan


delQuaver() # 2/4               

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)        

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver()

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp    

delSquaver() 

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver() 

sides(1,0,0,0,0,0,0,0)

delSquaver()

window(1,0,0,0,0,0,0,0)     # Window blackout

sides(2,255,150,0,0,0,0,12) # Scan

delQuaver()

window(1,0,20,35,0,0,0,0)   # Window cyan

sides(1,0,0,0,0,0,0,0)

delQuaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()
sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()
sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSquaver()
delSSquaver()


######## THIRD SET OF WOMPS

sides(1,255,150,0,0,0,0,0)      # yellow solid          DROP!

window(1,255,150,0,0,0,0,0)

flames(40)

delQuaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,20,35,0,0,0,0)        # dim cyan


delQuaver()                

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)        

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver()

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides3()    # Red     womp    

delSquaver() 

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides3()    # Red     womp 

delSquaver() 

sides(1,0,0,0,0,0,0,0)

delSquaver()

window(1,0,0,0,0,0,0,0)     # Window blackout

sides(2,255,150,0,0,0,0,12) # Scan

delQuaver()

window(1,0,20,35,0,0,0,0)   # Window cyan

sides(1,0,0,0,0,0,0,0)

delQuaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()
sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSSquaver()
deltime(50)

sides(1,255,150,0,0,0,0,0)      # yellow solid          BANG!

window(1,255,150,0,0,0,0,0)

flames(20)

delSquaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,0,0,0,0,0,0)

delSquaver()

sides(1,255,150,0,0,0,0,0)      # yellow solid          BANG!!

window(1,255,150,0,0,0,0,0)

flames(20)

delSquaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,0,0,0,0,0,0)

delSquaver()

sides2()                        # yellow solid          BANG!!
window(1,255,150,0,0,0,0,0)        # dim cyan
flames(40)

delSquaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,0,0,0,0,0,0)

delSquaver()

            

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)        

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver()

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides3()    # Red     womp   

delSquaver() 

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides3()    # Red     womp 

delSquaver() 

sides(1,0,0,0,0,0,0,0)

delSquaver()

window(1,0,0,0,0,0,0,0)     # Window blackout

sides(2,255,150,0,0,0,0,12) # Scan

delQuaver()

window(1,0,20,35,0,0,0,0)   # Window cyan

sides(1,0,0,0,0,0,0,0)

delQuaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()
sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()
delSSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()
delSSquaver()


sides(1,255,150,0,0,0,0,0)      # yellow solid          DROP!

window(1,255,150,0,0,0,0,0)

flames(40)

delQuaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,20,35,0,0,0,0)        # dim cyan


delQuaver()                

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)        

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver()

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides3()    # Red     womp    

delSquaver() 

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides3()    # Red     womp 

delSquaver() 

sides(1,0,0,0,0,0,0,0)

delSquaver()

window(1,0,0,0,0,0,0,0)     # Window blackout

sides(2,255,150,0,0,0,0,12) # Scan

delQuaver()

window(1,0,20,35,0,0,0,0)   # Window cyan

sides(1,0,0,0,0,0,0,0)

delQuaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()
sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSSquaver()
deltime(50)

sides(1,255,150,0,0,0,0,0)      # yellow solid          BANG!

window(1,255,150,0,0,0,0,0)

flames(20)

delSquaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,0,0,0,0,0,0)

delSquaver()

sides(1,255,150,0,0,0,0,0)      # yellow solid          BANG!!

window(1,255,150,0,0,0,0,0)

flames(20)

delSquaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,0,0,0,0,0,0)

delSquaver()

sides2()                        # yellow solid          BANG!!
window(1,255,150,0,0,0,0,0)        # yellow window
flames(40)

delSquaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,0,0,0,0,0,0)

delSquaver()

            

#sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver() # 2/4

#sides(1,0,0,0,0,0,0,0)        

delSquaver()

#sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver() # 2/4

#sides(1,0,0,0,0,0,0,0)

delSquaver()

#sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver()

#sides(1,0,0,0,0,0,0,0)

delSquaver()

#sides3()    # Red     womp   

delSquaver() 

#sides(1,0,0,0,0,0,0,0)

delSquaver()

#sides3()    # Red     womp 

delSquaver() 

#sides(1,0,0,0,0,0,0,0)

delSquaver()

window(1,0,0,0,0,0,0,0)     # Window blackout

sides(2,255,150,0,0,0,0,12) # Scan

delQuaver()

window(1,0,0,0,0,0,0,0)   # Window black
sides(2,0,150,255,0,0,0,50)                 # slow cyan scan



del1Beat()

del1Beat()

sides(2,150,0,150,0,0,0,50)                 # slow magenta scan

del1Beat()

del1Beat()


# RAINBOW

sides2()                        # yellow solid          BANG!!
window(1,255,150,0,0,0,0,0)        # yellow window
#flames(40)

delQuaver()
delSquaver()

sides(3,0,0,0,0,0,0,10)
window(3,0,0,0,0,0,0,10)

delSSquaver()
deltime(50)

del1Beat()

del1Beat()

del1Beat()

del1Beat()

del1Beat()

del1Beat()

delQuaver()

sides(1,255,150,0,0,0,0,0)      # yellow solid       BANG!

window(1,255,150,0,0,0,0,0)

#flames(20)

delSquaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,0,0,0,0,0,0)

delSquaver()

sides2()                        # yellow solid          BANG!!
window(1,255,150,0,0,0,0,0)        # yellow window
#flames(40)

delQuaver()
delSquaver()

sides(3,0,0,0,0,0,0,10)
window(3,0,0,0,0,0,0,10)

delSSquaver()
deltime(50)

del1Beat()

del1Beat()

del1Beat()

del1Beat()

del1Beat()

del1Beat()

del1Beat()


sides2()                        # yellow solid          BANG!!
window(1,255,150,0,0,0,0,0)        # yellow window
#flames(40)

delQuaver()
delSquaver()

sides(3,0,0,0,0,0,0,10)
window(3,0,0,0,0,0,0,10)

delSSquaver()
deltime(50)

del1Beat()

del1Beat()

del1Beat()

del1Beat()

del1Beat()

del1Beat()

delQuaver()

sides(1,255,150,0,0,0,0,0)      # yellow solid       BANG!

window(1,255,150,0,0,0,0,0)

#flames(20)

delSquaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,0,0,0,0,0,0)

delSquaver()

sides2()                        # yellow solid          BANG!!
window(1,255,150,0,0,0,0,0)        # yellow window
#flames(40)

delQuaver()
delSquaver()

sides(3,0,0,0,0,0,0,10)
window(3,0,0,0,0,0,0,10)

delSSquaver()
deltime(50)

del1Beat()

del1Beat()

del1Beat()

del1Beat()

del1Beat()

del1Beat()

del1Beat()
#delSSquaver()       # makeup delay
deltime(50)


# CLANGING

sides2()                        # yellow solid          BANG!!
window(1,255,150,0,0,0,0,0)        # yellow window
flames(40)

delQuaver()


sidesblack()
window(1,0,0,0,0,0,0,0)

#delSquaver()

sides(6,255,0,0,0,0,255,150)        # red/blue police

del1Beat()

del1Beat()

del1Beat()

sides(2,0,150,250,0,0,0,27)

del1Beat()

sides4()    # Green     womp
window(1,0,20,35,0,0,0,0)

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides4()    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

sides4()    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides4()    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

sides4()    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides4()    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()
sides4()    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides4()    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

sides(1,255,150,0,0,0,0,0)      # yellow solid       BANG!

window(1,255,150,0,0,0,0,0)

flames(20)

delSquaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,0,0,0,0,0,0)

delSquaver()

sides(1,255,150,0,0,0,0,0)      # yellow solid          BANG!!

window(1,255,150,0,0,0,0,0)

flames(20)

delSquaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,255,150,0,0,0,0,0)       


delSquaver()

sides(1,255,150,0,0,0,0,0)      # yellow solid          BANG!!

window(1,255,150,0,0,0,0,0)

flames(40)

#delSquaver()

#sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,20,35,0,0,0,0)        # dim cyan

#delSquaver()



sides(6,255,0,0,0,0,255,150)        # red/blue police

del1Beat()

del1Beat()

del1Beat()

sides(2,0,150,250,0,0,0,27)


del1Beat()
#delQuaver()

sides4()    # Green     womp
window(1,0,20,35,0,0,0,0)

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides4()    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides4()    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides4()    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()
delSquaver()


sides4()    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides4()    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides4()    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()
delSquaver()

sides4()    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()


sides4()    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

sides4()    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

# CLANGING (REPEAT)

sides2()                        # yellow solid          BANG!!
window(1,255,150,0,0,0,0,0)        # yellow window
flames(40)

delQuaver()


sidesblack()
window(1,0,0,0,0,0,0,0)

#delSquaver()

sides(6,255,0,0,0,0,255,150)        # red/blue police

del1Beat()

del1Beat()

del1Beat()

sides(2,0,150,250,0,0,0,27)

del1Beat()

sides4()    # Green     womp
window(1,0,20,35,0,0,0,0)

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides4()    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

sides4()    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides4()    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

sides4()    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides4()    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()
sides4()    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides4()    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

sides(1,255,150,0,0,0,0,0)      # yellow solid       BANG!

window(1,255,150,0,0,0,0,0)

flames(20)

delSquaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,0,0,0,0,0,0)

delSquaver()

sides(1,255,150,0,0,0,0,0)      # yellow solid          BANG!!

window(1,255,150,0,0,0,0,0)

flames(20)

delSquaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,255,150,0,0,0,0,0)       


delSquaver()

sides(1,255,150,0,0,0,0,0)      # yellow solid          BANG!!

window(1,255,150,0,0,0,0,0)

flames(40)

#delSquaver()

#sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,20,35,0,0,0,0)        # dim cyan

#delSquaver()



sides(6,255,0,0,0,0,255,150)        # red/blue police

del1Beat()

del1Beat()

del1Beat()

sides(2,0,150,250,0,0,0,27)


del1Beat()
#delQuaver()

sides4()    # Green     womp
window(1,0,20,35,0,0,0,0)

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides4()    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides4()    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides4()    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()
delSquaver()


sides4()    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides4()    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides4()    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()
delSquaver()

sides4()    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()


sides4()    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

sides4()    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()


# BREAKDOWN

sidesblack()
window(1,0,0,0,0,0,0,0)

del1Bar()

shedMove(1,2,255,150,0,0,0,0,75)    # 1 yellow  slow

deltime(1000)

shedMove(2,2,150,0,150,0,0,0,50)    # 2 purple  med

deltime(800)

shedMove(3,2,150,150,150,0,0,0,100) # win white slow

deltime(1000)

shedMove(1,2,150,150,150,0,0,0,75)  # 1 white   slow

deltime(1400)

shedMove(2,2,255,150,0,0,0,0,20)    # 2 yellow  fast

deltime(500)

shedMove(2,2,150,0,150,0,0,0,75)    # 2 purple  slow

deltime(500)

shedMove(3,2,150,0,150,0,0,0,100)   # win purple slow

deltime(800)

shedMove(1,1,0,0,0,0,0,0,0)          # 1    black

deltime(500)

shedMove(2,2,150,150,150,0,0,0,20)    # 2 white  fast

deltime(1200)

shedMove(1,2,255,150,0,0,0,0,35)    # 1 yellow med

deltime(500)

shedMove(3,1,0,0,0,0,0,0,0)   # win black


shedMove(1,2,150,150,150,0,0,0,75)    # 1 white slow

shedMove(2,2,150,150,150,0,0,0,100)    # 2 white  slow

deltime(2000)

shedMove(1,2,255,150,0,0,0,0,50)    # 1 yellow  med

deltime(1000)

shedMove(3,2,150,150,150,0,0,0,100)   # win white slow

deltime(1500)

shedMove(1,1,0,0,0,0,0,0,0)    # 1 yellow  black

deltime(1000)

shedMove(2,2,150,0,150,0,0,0,50)    # 2 purple  med

deltime(800)

shedMove(3,2,255,150,0,0,0,0,75)    # win yellow slow

deltime(1000)

shedMove(1,2,150,150,150,0,0,0,75)  # 1 white   slow

deltime(1400)

shedMove(2,2,255,150,0,0,0,0,20)    # 2 yellow  fast




# QUIET

sidesblack()
window(1,0,0,0,0,0,0,0)

del4Bar()

del1Bar()

del1Bar()









sides(5,255,0,0,0,0,0,210)      # Red buildup

del1Bar()

del1Beat()
del1Beat()
del1Beat()
delQuaver()
#delSquaver()
delSSquaver()
deltime(50)

# Second Drop

sides(1,255,150,0,0,0,0,0)      # yellow solid          BANG!!

window(1,255,150,0,0,0,0,0)

flames(40)

delSSquaver()
deltime(50)
delSSquaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,20,35,0,0,0,0)        # dim cyan

delSSquaver()



sides(6,255,0,0,0,0,255,150)        # red/blue police
window(6,255,0,0,0,0,255,150)        # red/blue police

del1Beat()

del1Beat()

del1Beat()

delQuaver()

window(1,0,20,35,0,0,0,0)        # dim cyan
sides3()    # Red     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)        

delSquaver()

sides5()    # Blue     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides3()    # Red     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)        

delSquaver()

sides5()    # Blue     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides3()    # Red     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)        

delSquaver()

sides3()    # Red     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides5()    # Blue     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides3()    # Red     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)        

delSquaver()

sides(1,255,150,0,0,0,0,0)      # yellow solid          BANG!!

window(1,255,150,0,0,0,0,0)

flames(40)

delSquaver()
delSSquaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,20,35,0,0,0,0)        # dim cyan

delSSquaver()



sides(6,255,0,0,0,0,255,150)        # red/blue police
window(6,255,0,0,0,0,255,150)        # red/blue police

del1Beat()

del1Beat()

del1Beat()

delQuaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,20,35,0,0,0,0)        # dim cyan

delQuaver()



sides5()    # Blue     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides5()    # Blue     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()
delSquaver()


sides5()    # Blue     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides5()    # Blue     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()
delSquaver()

sides5()    # Blue     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides3()    # Red     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()
delSquaver()


sides5()    # Blue     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides5()    # Blue     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()
delSquaver()

sides(2,255,150,0,0,0,0,12)     # yellow scan
window(1,0,0,0,0,0,0,0)


delQuaver() # 2/4


# Second Drop (repeat)

sides(1,255,150,0,0,0,0,0)      # yellow solid          BANG!!

window(1,255,150,0,0,0,0,0)

flames(40)

delSquaver()
delSSquaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,20,35,0,0,0,0)        # dim cyan

delSSquaver()



sides(6,255,0,0,0,0,255,150)        # red/blue police
window(6,255,0,0,0,0,255,150)        # red/blue police

del1Beat()

del1Beat()

del1Beat()

delQuaver()

window(1,0,20,35,0,0,0,0)        # dim cyan
sides3()    # Red     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)        

delSquaver()

sides5()    # Blue     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides3()    # Red     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)        

delSquaver()

sides5()    # Blue     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides3()    # Red     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)        

delSquaver()

sides3()    # Red     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides5()    # Blue     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)

delSSquaver()
deltime(50)

sides(1,255,150,0,0,0,0,0)      # yellow solid          BANG!!

window(1,255,150,0,0,0,0,0)

flames(20)

delSquaver()
delSSquaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,20,35,0,0,0,0)        # dim cyan

delSSquaver()

sides(1,255,150,0,0,0,0,0)      # yellow solid          BANG!!

window(1,255,150,0,0,0,0,0)

flames(40)

delSquaver()
delSSquaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,20,35,0,0,0,0)        # dim cyan

delSSquaver()



sides(6,255,0,0,0,0,255,150)        # red/blue police
window(6,255,0,0,0,0,255,150)        # red/blue police

del1Beat()

del1Beat()

del1Beat()

delQuaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,20,35,0,0,0,0)        # dim cyan

delQuaver()



sides5()    # Blue     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides5()    # Blue     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()
delSquaver()


sides5()    # Blue     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides5()    # Blue     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()
delSquaver()

sides5()    # Blue     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides3()    # Red     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()
delSquaver()


sides5()    # Blue     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides5()    # Blue     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()
delSquaver()

sides5()    # Blue     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()
delSquaver()

 

# Second drop 2

sides(1,255,150,0,0,0,0,0)      # yellow solid          DROP!

window(1,255,150,0,0,0,0,0)

flames(40)

delQuaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,20,35,0,0,0,0)        # dim cyan


delQuaver()                

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)        

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver()

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides3()    # Red     womp    

delSquaver() 

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides3()    # Red     womp 

delSquaver() 

sides(1,0,0,0,0,0,0,0)

delSquaver()

window(1,0,0,0,0,0,0,0)     # Window blackout

sides(2,255,150,0,0,0,0,12) # Scan

delQuaver()

window(1,0,20,35,0,0,0,0)   # Window cyan

sides(1,0,0,0,0,0,0,0)

delQuaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()
sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSSquaver()
deltime(30)

sides(1,255,150,0,0,0,0,0)      # yellow solid          BANG!

window(1,255,150,0,0,0,0,0)

flames(20)

delSquaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,0,0,0,0,0,0)

delSquaver()

sides(1,255,150,0,0,0,0,0)      # yellow solid          BANG!!

window(1,255,150,0,0,0,0,0)

flames(20)

delSquaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,0,0,0,0,0,0)

delSquaver()

sides2()                        # yellow solid          BANG!!
window(1,255,150,0,0,0,0,0)        # dim cyan
flames(40)

delSquaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,0,0,0,0,0,0)

delSquaver()

            

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)        

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver()

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides3()    # Red     womp   

delSquaver() 

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides3()    # Red     womp 

delSquaver() 

sides(1,0,0,0,0,0,0,0)

delSquaver()

window(1,0,0,0,0,0,0,0)     # Window blackout

sides(2,255,150,0,0,0,0,12) # Scan

delQuaver()

window(1,0,20,35,0,0,0,0)   # Window cyan


delSquaver()

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()
sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()
delSSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()
delSSquaver()


sides(1,255,150,0,0,0,0,0)      # yellow solid          DROP!

window(1,255,150,0,0,0,0,0)

flames(40)

delQuaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,20,35,0,0,0,0)        # dim cyan


delQuaver()                

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)        

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver()

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides3()    # Red     womp    

delSquaver() 

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides3()    # Red     womp 

delSquaver() 

sides(1,0,0,0,0,0,0,0)

delSquaver()

window(1,0,0,0,0,0,0,0)     # Window blackout

sides(2,255,150,0,0,0,0,12) # Scan

delQuaver()

window(1,0,20,35,0,0,0,0)   # Window cyan

sides(1,0,0,0,0,0,0,0)

delQuaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()
sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

#delSSquaver()

delSSquaver()
deltime(60)

sides(1,255,150,0,0,0,0,0)      # yellow solid          BANG!

window(1,255,150,0,0,0,0,0)

flames(20)

delSquaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,0,0,0,0,0,0)

delSquaver()

sides(1,255,150,0,0,0,0,0)      # yellow solid          BANG!!

window(1,255,150,0,0,0,0,0)

flames(20)

delSquaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,0,0,0,0,0,0)

delSquaver()

sides2()                        # yellow solid          BANG!!
window(1,255,150,0,0,0,0,0)        # dim cyan
flames(40)

delSquaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,0,0,0,0,0,0)

delSquaver()

            

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)        

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver()

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides3()    # Red     womp   

delSquaver() 

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides3()    # Red     womp 

delSquaver() 

sides(1,0,0,0,0,0,0,0)

delSquaver()

window(1,0,0,0,0,0,0,0)     # Window blackout

sides(2,255,150,0,0,0,0,12) # Scan

delQuaver()

window(1,0,20,35,0,0,0,0)   # Window cyan

delSquaver()

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()
sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()
delSSquaver()


delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()
deltime(50)

#delSSquaver()

# Second drop again

sides(1,255,150,0,0,0,0,0)      # yellow solid          BANG!!

window(1,255,150,0,0,0,0,0)

flames(40)

delSSquaver()
deltime(50)
delSSquaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,20,35,0,0,0,0)        # dim cyan

delSSquaver()



sides(6,255,0,0,0,0,255,150)        # red/blue police
window(6,255,0,0,0,0,255,150)        # red/blue police

del1Beat()

del1Beat()

del1Beat()

delQuaver()

window(1,0,20,35,0,0,0,0)        # dim cyan
sides3()    # Red     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)        

delSquaver()

sides5()    # Blue     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides3()    # Red     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)        

delSquaver()

sides5()    # Blue     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides3()    # Red     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)        

delSquaver()

sides3()    # Red     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides5()    # Blue     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides(1,255,150,0,0,0,0,0)      # yellow solid          BANG!!

window(1,255,150,0,0,0,0,0)

flames(20)

delSquaver()
delSSquaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,20,35,0,0,0,0)        # dim cyan

delSSquaver()

sides(1,255,150,0,0,0,0,0)      # yellow solid          BANG!!

window(1,255,150,0,0,0,0,0)

flames(40)

delSquaver()
delSSquaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,20,35,0,0,0,0)        # dim cyan

delSSquaver()



sides(6,255,0,0,0,0,255,150)        # red/blue police
window(6,255,0,0,0,0,255,150)        # red/blue police

del1Beat()

del1Beat()

del1Beat()

delQuaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,20,35,0,0,0,0)        # dim cyan

delQuaver()



sides5()    # Blue     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides5()    # Blue     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()
delSquaver()


sides5()    # Blue     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides5()    # Blue     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()
delSquaver()

sides5()    # Blue     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides3()    # Red     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()
delSquaver()


sides5()    # Blue     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides5()    # Blue     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()
delSquaver()

sides5()    # Blue     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()
delSquaver()

sides(1,255,150,0,0,0,0,0)      # yellow solid          BANG!!

window(1,255,150,0,0,0,0,0)

flames(40)

delSSquaver()
deltime(50)
delSSquaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,20,35,0,0,0,0)        # dim cyan

delSSquaver()



sides(6,255,0,0,0,0,255,150)        # red/blue police
window(6,255,0,0,0,0,255,150)        # red/blue police

del1Beat()

del1Beat()

del1Beat()

delQuaver()

window(1,0,20,35,0,0,0,0)        # dim cyan
sides3()    # Red     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)        

delSquaver()

sides5()    # Blue     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides3()    # Red     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)        

delSquaver()

sides5()    # Blue     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides3()    # Red     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)        

delSquaver()

sides3()    # Red     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides5()    # Blue     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides(1,255,150,0,0,0,0,0)      # yellow solid          BANG!!

window(1,255,150,0,0,0,0,0)

flames(20)

delSquaver()
delSSquaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,20,35,0,0,0,0)        # dim cyan

delSSquaver()

sides(1,255,150,0,0,0,0,0)      # yellow solid          BANG!!

window(1,255,150,0,0,0,0,0)

flames(40)

delSquaver()
delSSquaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,20,35,0,0,0,0)        # dim cyan

delSSquaver()



sides(6,255,0,0,0,0,255,150)        # red/blue police
window(6,255,0,0,0,0,255,150)        # red/blue police

del1Beat()

del1Beat()

del1Beat()

delQuaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,20,35,0,0,0,0)        # dim cyan

delQuaver()



sides5()    # Blue     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides5()    # Blue     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()
delSquaver()


sides5()    # Blue     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides5()    # Blue     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()
delSquaver()

sides5()    # Blue     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides3()    # Red     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()
delSquaver()


sides5()    # Blue     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides5()    # Blue     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()
delSquaver()

sides5()    # Blue     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()
delSquaver()

sides(1,255,150,0,0,0,0,0)      # yellow solid          DROP!

window(1,255,150,0,0,0,0,0)

flames(40)

delQuaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,20,35,0,0,0,0)        # dim cyan


delQuaver()                

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)        

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver()

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides3()    # Red     womp    

delSquaver() 

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides3()    # Red     womp 

delSquaver() 

sides(1,0,0,0,0,0,0,0)

delSquaver()

window(1,0,0,0,0,0,0,0)     # Window blackout

sides(2,255,150,0,0,0,0,12) # Scan

delQuaver()

window(1,0,20,35,0,0,0,0)   # Window cyan

sides(1,0,0,0,0,0,0,0)

delQuaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()
sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

#delSSquaver()

delSquaver()
deltime(30)

sides(1,255,150,0,0,0,0,0)      # yellow solid          BANG!

window(1,255,150,0,0,0,0,0)

flames(20)

delSquaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,0,0,0,0,0,0)

delSquaver()

sides(1,255,150,0,0,0,0,0)      # yellow solid          BANG!!

window(1,255,150,0,0,0,0,0)

flames(20)

delSquaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,0,0,0,0,0,0)

delSquaver()

sides2()                        # yellow solid          BANG!!
window(1,255,150,0,0,0,0,0)        # dim cyan
flames(40)

delSquaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,0,0,0,0,0,0)

delSquaver()

            

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)        

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver()

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides3()    # Red     womp   

delSquaver() 

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides3()    # Red     womp 

delSquaver() 

sides(1,0,0,0,0,0,0,0)

delSquaver()

window(1,0,0,0,0,0,0,0)     # Window blackout

sides(2,255,150,0,0,0,0,12) # Scan

delQuaver()

window(1,0,20,35,0,0,0,0)   # Window cyan

sides(1,0,0,0,0,0,0,0)

delQuaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()
sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()
delSSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()
delSSquaver()


sides(1,255,150,0,0,0,0,0)      # yellow solid          DROP!

window(1,255,150,0,0,0,0,0)

flames(40)

delQuaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,20,35,0,0,0,0)        # dim cyan


delQuaver()                

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)        

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver() # 2/4

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver()

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides3()    # Red     womp    

delSquaver() 

sides(1,0,0,0,0,0,0,0)

delSquaver()

sides3()    # Red     womp 

delSquaver() 

sides(1,0,0,0,0,0,0,0)

delSquaver()

window(1,0,0,0,0,0,0,0)     # Window blackout

sides(2,255,150,0,0,0,0,12) # Scan

delQuaver()

window(1,0,20,35,0,0,0,0)   # Window cyan

sides(1,0,0,0,0,0,0,0)

delQuaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides3()    # Red     womp 

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()
sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides(1,0,35,0,0,0,0,0)    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()
#deltime(20)

sides(1,255,150,0,0,0,0,0)      # yellow solid          BANG!

window(1,255,150,0,0,0,0,0)

flames(20)

delSquaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,0,0,0,0,0,0)

delSquaver()

sides(1,255,150,0,0,0,0,0)      # yellow solid          BANG!!

window(1,255,150,0,0,0,0,0)

flames(20)

delSquaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,0,0,0,0,0,0)

delSquaver()

sides2()                        # yellow solid          BANG!!
window(1,255,150,0,0,0,0,0)        # yellow window
flames(40)

delSquaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,0,0,0,0,0,0)

delSquaver()

            

#sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver() # 2/4

#sides(1,0,0,0,0,0,0,0)        

delSquaver()

#sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver() # 2/4

#sides(1,0,0,0,0,0,0,0)

delSquaver()

#sides(1,0,35,0,0,0,0,0)    # Green     womp

delSquaver()

#sides(1,0,0,0,0,0,0,0)

delSquaver()

#sides3()    # Red     womp   

delSquaver() 

#sides(1,0,0,0,0,0,0,0)

delSquaver()

#sides3()    # Red     womp 

delSquaver() 

#sides(1,0,0,0,0,0,0,0)

delSquaver()

window(1,0,0,0,0,0,0,0)     # Window blackout

sides(2,255,150,0,0,0,0,12) # Scan

delQuaver()

window(1,0,0,0,0,0,0,0)   # Window black
sides(2,0,150,255,0,0,0,50)                 # slow cyan scan



del1Beat()

del1Beat()

sides(2,150,0,150,0,0,0,50)                 # slow magenta scan

del1Beat()

del1Beat()

deltime(20)

# RAINBOW

sides2()                        # yellow solid          BANG!!
window(1,255,150,0,0,0,0,0)        # yellow window
flames(40)

delQuaver()
delSquaver()

sides(3,0,0,0,0,0,0,10)
window(3,0,0,0,0,0,0,10)

delSquaver()

del1Beat()

del1Beat()

del1Beat()

del1Beat()

del1Beat()

del1Beat()

delQuaver()
deltime(20)

sides(1,255,150,0,0,0,0,0)      # yellow solid       BANG!

window(1,255,150,0,0,0,0,0)

flames(20)

delSquaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,0,0,0,0,0,0)

delSquaver()

sides2()                        # yellow solid          BANG!!
window(1,255,150,0,0,0,0,0)        # yellow window
flames(40)

delQuaver()
delSquaver()

sides(3,0,0,0,0,0,0,10)
window(3,0,0,0,0,0,0,10)

delSquaver()

del1Beat()

del1Beat()

del1Beat()

del1Beat()

del1Beat()

del1Beat()

del1Beat()


sides2()                        # yellow solid          BANG!!
window(1,255,150,0,0,0,0,0)        # yellow window
flames(40)

delQuaver()
delSquaver()

sides(3,0,0,0,0,0,0,10)
window(3,0,0,0,0,0,0,10)

delSquaver()

del1Beat()

del1Beat()

del1Beat()

del1Beat()

del1Beat()

del1Beat()

delQuaver()

sides(1,255,150,0,0,0,0,0)      # yellow solid       BANG!

window(1,255,150,0,0,0,0,0)

flames(20)

delSquaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,0,0,0,0,0,0)

delSquaver()

sides2()                        # yellow solid          BANG!!
window(1,255,150,0,0,0,0,0)        # yellow window
flames(40)

delQuaver()
delSquaver()

sides(3,0,0,0,0,0,0,10)
window(3,0,0,0,0,0,0,10)

delSquaver()

del1Beat()

del1Beat()

del1Beat()

del1Beat()

del1Beat()

del1Beat()

del1Beat()
deltime(10)      # makeup delay

# CLANGING

sides2()                        # yellow solid          BANG!!
window(1,255,150,0,0,0,0,0)        # yellow window
#flames(40)

delQuaver()


sidesblack()
window(1,0,0,0,0,0,0,0)

#delSquaver()

sides(6,255,0,0,0,0,255,150)        # red/blue police

del1Beat()

del1Beat()

del1Beat()

sides(2,0,150,250,0,0,0,27)

del1Beat()
sidesblack()

del1Beat()
del1Beat()
del1Beat()
deltime(10)

sides(1,255,150,0,0,0,0,0)      # yellow solid       BANG!

window(1,255,150,0,0,0,0,0)

#flames(20)

delSquaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,0,0,0,0,0,0)

delSquaver()

sides(1,255,150,0,0,0,0,0)      # yellow solid          BANG!!

window(1,255,150,0,0,0,0,0)

#flames(20)

delSquaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,255,150,0,0,0,0,0)       


delSquaver()

sides(1,255,150,0,0,0,0,0)      # yellow solid          BANG!!

window(1,255,150,0,0,0,0,0)

#flames(40)

#delSquaver()

#sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,20,35,0,0,0,0)        # dim cyan

#delSquaver()



sides(6,255,0,0,0,0,255,150)        # red/blue police

del1Beat()

del1Beat()

del1Beat()

sides(2,0,150,250,0,0,0,27)


del1Beat()
#delQuaver()
sidesblack()


del1Beat()
del1Beat()
del1Beat()
delQuaver()


# Clanging (repeat)

sides2()                        # yellow solid          BANG!!
window(1,255,150,0,0,0,0,0)        # yellow window
#flames(40)

delQuaver()


sidesblack()
window(1,0,0,0,0,0,0,0)

#delSquaver()

sides(6,255,0,0,0,0,255,150)        # red/blue police

del1Beat()

del1Beat()

del1Beat()

sides(2,0,150,250,0,0,0,27)

del1Beat()

sidesblack()

del1Beat()
del1Beat()
del1Beat()
deltime(25)

sides(1,255,150,0,0,0,0,0)      # yellow solid       BANG!

window(1,255,150,0,0,0,0,0)

#flames(20)

delSquaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,0,0,0,0,0,0)

delSquaver()

sides(1,255,150,0,0,0,0,0)      # yellow solid          BANG!!

window(1,255,150,0,0,0,0,0)

#flames(20)

delSquaver()

sides(1,0,0,0,0,0,0,0)          # blackout
window(1,255,150,0,0,0,0,0)       


delSquaver()

sides(1,255,150,0,0,0,0,0)      # yellow solid          BANG!!

window(1,255,150,0,0,0,0,0)

#flames(40)

#delSquaver()

#sides(1,0,0,0,0,0,0,0)          # blackout
window(1,0,20,35,0,0,0,0)        # dim cyan

#delSquaver()



sides(6,255,0,0,0,0,255,150)        # red/blue police

del1Beat()

del1Beat()

del1Beat()

sides(2,0,150,250,0,0,0,27)


del1Beat()
#delQuaver()

sides4()    # Green     womp
window(1,0,20,35,0,0,0,0)

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides4()    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides4()    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides4()    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()
delSquaver()


sides4()    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides4()    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

sides4()    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()
delSquaver()

sides4()    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()


sides4()    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()

sides4()    # Green     womp

delSSquaver()

sides(1,0,0,0,0,0,0,0)

delSSquaver()

delSquaver()













# Outro

sidesblack()
window(1,0,0,0,0,0,0,0)

del1Bar()

shedMove(1,2,255,150,0,0,0,0,75)    # 1 yellow  slow

deltime(1000)

shedMove(2,2,150,0,150,0,0,0,50)    # 2 purple  med

deltime(800)

shedMove(3,2,150,150,150,0,0,0,100) # win white slow

deltime(1000)

shedMove(1,2,150,150,150,0,0,0,75)  # 1 white   slow

deltime(1400)

shedMove(2,2,255,150,0,0,0,0,20)    # 2 yellow  fast

deltime(500)

shedMove(2,2,150,0,150,0,0,0,75)    # 2 purple  slow

deltime(500)

shedMove(3,2,150,0,150,0,0,0,100)   # win purple slow

deltime(800)

shedMove(1,1,0,0,0,0,0,0,0)          # 1    black

deltime(500)

shedMove(2,2,150,150,150,0,0,0,20)    # 2 white  fast

deltime(1200)

shedMove(1,2,255,150,0,0,0,0,35)    # 1 yellow med

deltime(500)

shedMove(3,1,0,0,0,0,0,0,0)   # win black


shedMove(1,2,150,150,150,0,0,0,75)    # 1 white slow

shedMove(2,2,150,150,150,0,0,0,100)    # 2 white  slow

deltime(2000)

shedMove(1,2,255,150,0,0,0,0,50)    # 1 yellow  med

deltime(1000)

shedMove(3,2,150,150,150,0,0,0,100)   # win white slow

deltime(1500)

shedMove(1,1,0,0,0,0,0,0,0)    # 1 yellow  black

deltime(1000)

shedMove(2,2,150,0,150,0,0,0,50)    # 2 purple  med

deltime(800)

shedMove(3,2,255,150,0,0,0,0,75)    # win yellow slow

deltime(1000)

shedMove(1,2,150,150,150,0,0,0,75)  # 1 white   slow

deltime(1400)

shedMove(2,2,255,150,0,0,0,0,20)    # 2 yellow  fast

window(1,0,20,30,0,0,0,0)
sidesblack()

del4Bar()
del4Bar()
window(1,0,0,0,0,0,0,0)
