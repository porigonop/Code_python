from Tkinter import *
import random
import time
import math

width = 1000
height = 1000
G = 10

def dist (planet, otherplanet):
    #print(planet, otherplanet)
    return math.sqrt((planet.x - otherplanet.x)**2 + (planet.y - otherplanet.y)**2)

def nearest_object(planet, list_of_planet):
    min = float("inf")
    for pl in list_of_planet:
        d = dist(pl, planet)
        if d < min and (str(pl) != str(planet)):
            min = d
            nearest = pl

    if not pl:
        pl = None
    return nearest, min



class Planet:
    def __init__(self, name, x, xspeed, y, yspeed, radius, mass, canvas):
        
        self.name = name
        
        self.x = x
        self.y = y
        
        self.xspeed = xspeed
        self.yspeed = yspeed
        
        self.radius = radius
        
        self.mass = mass
        
        self.planet = canvas.create_oval(x - radius,\
                                         y - radius,\
                                         x + radius,\
                                         y + radius)
        
    def Draw(self, canvas):
        nearest, d = nearest_object(self, Planets)
        print(self, nearest)
        if nearest:
            self.xspeed += (((G* nearest.mass * self.mass)/ (d**2) )* (nearest.y - self.y) / d) * self.mass 
            self.yspeed += (((G* nearest.mass * self.mass)/ (d**2) )* (nearest.x - self.x) / d) * self.mass 
            
        self.x += self.xspeed
        self.y += self.yspeed
        canvas.coords(self.planet,\
        self.x - self.radius,\
        self.y - self.radius,\
        self.x + self.radius,\
        self.y + self.radius )
     
    def __repr__(self):
        return self.name
        
def move():
    for elt in Planets:
        elt.Draw(canvas)
    tk.after(100, move)

tk = Tk()
decay = 5
canvas = Canvas( tk, width = width, height = height, background = "white")
Planets = []
Planets.append(Planet("sun", width/2, 0, height /2, 0, 50, 100, canvas ))
Planets.append(Planet("moon", 100, 100, 100, 0.5, 50, 5, canvas ))
canvas.pack()
move()
tk.mainloop()