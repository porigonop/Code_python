#!/usr/bin/env python3
import math
class Turtle:
    """Classe modélisant une tortue graphique"""
    stepSize = 5
    def __init__(self, color, position, rotation):
        
        self.color = color
        self.position = position
        self.rotation = rotation

    def __repr__(self):
        return "turtle : " + str(self.color) + "," + \
              str(self.position) + "," + str(self.rotation)
    @staticmethod
    def degToRad(degree):
        return degree / 180*math.pi
    
    def readPosition(self):
        return self.position
    
    def readAngle(self):
        return self.rotation

    def turn(self, angle):
        self.rotation += angle

    def advance(self):
        x, y = self.position
        rads = Turtle.degToRad(self.rotation)
        x += math.cos(rads) * Turtle.stepSize
        y += math.sin(rads) * Turtle.stepSize
        self.position = (x, y)
        
if __name__ == "__main__":
    turtle = []
    for i in range(0,10):
        turtle.append(Turtle('red', (i*3,i*2), i*10))
        
    print(turtle[1].color, turtle[1].position, turtle[1].rotation)
    turtle[1].advance()
    turtle[1].turn(50)
    print(turtle[1])
