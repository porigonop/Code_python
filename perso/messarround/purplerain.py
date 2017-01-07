from Tkinter import *
import time
import random
print("hello world")
i = 2
width = 1920
height = 1000
z = 100

def mapjs(value, min, max, newmin, newmax):
    return (value / (max - min))*(newmax-newmin)



class Drop:
    def __init__(self, canvas):
        self.x = random.random() * width
        self.y = random.random() * height
        self.z = random.random() * z
        
        
        
        self.yspeed = mapjs(self.z, 0, z, 10, 30)
        self.width = mapjs(self.z, 0, z, 2, 10)
        self.height = mapjs(self.z, 0, z, 10, 50)
        
        self.drop = canvas.create_line(50, 25, 50, 50 + self.height, fill="purple", width = self.width)
        
    def update(self, canvas):
        self.y += self.yspeed
        if self.y > height:
            self.y = -50
        canvas.coords(self.drop, (self.x, self.y, self.x, self.y + self.height))

def move():
    for elt in drops:
        elt.update(canvas)
    tk.after(10, move)




tk = Tk()
decay = 5
canvas = Canvas( tk, width = width, height = height, background = "white")
drops = []
for i in range(600):
    drops.append(Drop(canvas))
canvas.pack()
move()
tk.mainloop()

    
    
