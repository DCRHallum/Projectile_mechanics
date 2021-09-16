import math,time
from polynomial import Poly
from turtle import Turtle

def getNum(message,default):
        if default == None:
            while True:
                valStr = input(message)
                if valStr.lstrip('-').isdigit():
                    return float(valStr)
        else:
            valStr = input(message)
            if valStr.lstrip('-').isdigit():
                return float(valStr)
            elif valStr == '':
                return default

SCREENX = 768
SCREENY = 648
MPP = getNum('Enter width of area modelled in metres: ',10)/SCREENX # Metres represented by 1 pixel (metres per pixel), screen is 10m wide
#MPP = 0.0130208333333
global G
G = getNum('Gravitational field strength (in terms of g): ',1)*(-9.81/MPP)
#G = -9.81/MPP

def timeSince(start):
     return (time.time()-start)

class Cannon():
    def __init__(self,size):
        self.size = size

class Projectile():
    def __init__(self,size,x,y):
        self.trtle = Turtle()
        self.trtle.size = size
        self.trtle.shape('circle')
        #self.trtle.penup()
        self.trtle.goto(x,y)
    def shoot(self,initSpeed,initAngle): #angle: 0 is east, anti-clockwise
        initSpeed = initSpeed/MPP
        initVelX = math.cos(math.radians(initAngle)) * initSpeed
        initVelY = math.sin(math.radians(initAngle)) * initSpeed
        distX, distY = self.trtle.pos()
        xPoly = Poly([[initVelX,1]])
        yPoly = Poly([[initVelY,1],[0.5*G,2]])
        startTime = time.time()
        while distX > (SCREENX/-2) and distX < (SCREENX/2) and distY > (SCREENX/-2): #stays within screen, modelled as a box with no lid
            t = timeSince(startTime)
            distX = xPoly.calcY(t)
            distY = yPoly.calcY(t)
            print(t)
            self.trtle.goto(distX,distY)


ball = Projectile(10,0,0)
initVel = getNum('Enter initial velocity: ',None)
angle = getNum('Enter angle',None)
ball.shoot(initVel,angle)





