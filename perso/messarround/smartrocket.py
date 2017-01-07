#smart rocket
import random
from Tkinter import *
import math
from pprint import pprint
import time
nb = 1000
WIDTH = 700
HEIGHT = 700
radius = 1
iteration = 0
thrust = 0.1
mutation_rate = 0.01
scale = 5000000
nb_rocket = 5002
nb_obs = 300
touch_target = 0.2
touch_obs = 0.1
FPS = 1000
SCALE = 7

nb_secteur = 10

def delete_liste(lst1, lst2):
    ln1 = len(lst1)
    cp1 = list(lst1)
    cp2 = list(lst2)
    for elt in range(-1,-ln1 -1, -1):
        item = lst1.pop(ln1 + elt)
        if item in lst1:
            cp1.pop(ln1 + elt)
            cp2.pop(ln1 + elt)
            lst2.pop(len(lst1) + elt)
    ln2 = len(lst2)
    for elt in range(-1,-ln2 -1, -1):
        item = lst2.pop(ln2 + elt)
        if item in lst1:
            cp1.pop(ln2 + elt)
            cp2.pop(ln2 + elt)
    return cp1, cp2

def mapjs(value, min, max, newmin, newmax):
    return (value / (max - min))*(newmax-newmin)

def dist (rocket, target):
    return (rocket.x - target.x)**2 + (rocket.y - target.y)**2

def collide(item, lst = []):
    if item.x > WIDTH or item.x < 0 or item.y > HEIGHT + 100 or item.y < 0:
        return True
    elif list == []:
        return False
        
    for obs in secteurs[lst[0]][lst[1]]:
        if item.x < obs.x + obs.len and item.x > obs.x - obs.len \
            and item.y < obs.y + obs.height and item.y > obs.y - obs.height:
            if obs.col == '':
                obs.col = 'red'
                canvas.delete(obs.obs)
                obs.obs = canvas.create_rectangle(obs.x - obs.len,
                                                    obs.y - obs.height,
                                                    obs.x + obs.len,
                                                    obs.y + obs.height,
                                                    fill = obs.col)
            return True

    return False
    
def succed(rocket):
    dis = 1/dist(rocket, population.target)
    if rocket.x > WIDTH or rocket.x < 0 or rocket.y > HEIGHT + 100 or rocket.y < 0:
        dis *= 0.8 
    if rocket.crashed:
        dis *= touch_obs
    if rocket.goal:
        dis *= touch_target
        dis /= mapjs(rocket.iter, 0, nb, 0, 100) + 0.1
    return int(dis * scale)
        
class Target():
    def __init__(self):
        self.x = WIDTH / 2
        self.y = HEIGHT / 8
        
        self.target = canvas.create_oval(self.x - 10,\
                                         self.y - 10,\
                                         self.x + 10,\
                                         self.y + 10)
                                         
    def move(self, x, y):
        canvas.move(self.target, -self.x, -self.y)
        canvas.move(self.target, x, y)
        self.x = x
        self.y = y

x_rocket =  WIDTH / 2
y_rocket = HEIGHT + 50
class Rocket():
    
    def __init__(self, genes = False, mut = random.random() * 0.1):
        if genes:
            self.genes = genes
        else:
            self.genes = []
            for i in range(nb):
                self.genes.append((random.randint(-1, 1), random.randint(-1, 1)))
        self.x = x_rocket
        self.y = y_rocket
        self.xspeed = 0
        self.yspeed = 0
        self.mutation_rate = mut
        self.rocket = canvas.create_oval(self.x - radius,\
                                         self.y - radius,\
                                         self.x + radius,\
                                         self.y + radius)
        self.crashed = False
        self.goal = False
        self.iter = nb
        
    def move(self):
        if self.y > HEIGHT:
            pass
        elif collide(self, [int(mapjs(self.x, 0, WIDTH, 0, nb_secteur-1)),\
                        int(mapjs(self.y, 0, HEIGHT, 0, nb_secteur-1))]):
            self.crashed = True
        if dist(self, population.target) < (10 + radius) **2 and not self.goal:
            self.goal = True
            self.iter = iteration
        if not self.crashed and not self.goal:
            self.xspeed += self.genes[iteration][0] * thrust
            self.yspeed += self.genes[iteration][1] * thrust
            self.x += self.xspeed
            self.y += self.yspeed 
        canvas.coords(self.rocket,\
                    self.x - radius,\
                    self.y - radius,\
                    self.x + radius,\
                    self.y + radius )
                    
        
    def crossover(self, otherrocket):
        mid = random.random() * nb
        new_genes = []
        for i in range(nb):
            if i > mid:
                new_genes.append(otherrocket.genes[i])
            else:
                new_genes.append(self.genes[i])
        if random.random() > 0.5:
            mut = self.mutation_rate
        else:
            mut = otherrocket.mutation_rate
        
        return Rocket(self.mutate(new_genes), mut)

    def mutate(self, genes):

        for i in range(len(genes)):
            if random.random() < self.mutation_rate:
                genes[i] = (random.randint(-1, 1), random.randint(-1, 1))
        if random.random() < mutation_rate:
            self.mutation_rate = random.random() * 0.1
        return genes
        
    def __del__(self):
        try:
            canvas.delete(self.rocket)
        except:
            pass
        
class Population():
    def __init__(self):
        self.rockets = []
        self.target = Target()
        for i in range(nb_rocket):
            self.rockets.append(Rocket())
    def Draw(self):

        for rocket in self.rockets:
            rocket.move()
        
    def new_pop(self):
        breedingpool = []
        for rocket in self.rockets:
            
            for i in range(succed(rocket)):
                breedingpool.append(rocket)
        np = []
        for i in range(nb_rocket):

            parentA = random.choice(breedingpool)
            parentB = random.choice(breedingpool)
            np.append(parentA.crossover(parentB))
            del(parentA)
            del(parentB)
        self.rockets = np
        
class Obstacle():
    def __init__(self, x, y, len, height):
        self.x = x
        self.y = y 
        self.len = len
        self.height = height
        self.col = ''
        self.obs = canvas.create_rectangle(self.x - self.len,
                                            self.y - self.height,
                                            self.x + self.len,
                                            self.y + self.height)

                                            
nbr = 1/FPS                                            
def Draw():
    global iteration
    global timeur
    while True:
        timeur = time.time()
        population.Draw()
        iteration += 1
        if iteration >= nb:
            iteration = 0
            population.new_pop()
                
        if iteration % 10 ==1:
            tk.update()
        #a = nbr - (time.time() - timeur )
        #time.sleep(a if a>0 else 0)

def pointeur(event):
    population.target.move(event.x, event.y)
tk = Tk()
decay = 5
timeur = time.time()
canvas = Canvas( tk, width = WIDTH, height = HEIGHT, background = "white")
population = Population()
secteurs = []             
obstacle = []               
for i in range(nb_secteur):
    secteurs.append([])
    for j in range(nb_secteur):
        secteurs[i].append([])
        for k in range(int(nb_obs / nb_secteur ** 2)):
            pos_x = random.random() *   WIDTH / nb_secteur + WIDTH * i / nb_secteur
            pos_y = random.random() *   HEIGHT / nb_secteur + HEIGHT * j/nb_secteur
            lengh = random.random() *   SCALE
            height = random.random() *   SCALE
            
            obstacle.append(Obstacle(pos_x,\
                               pos_y,\
                               lengh,\
                               height))
            
            
for obs in obstacle:
    x_al = []
    y_al = []
    
    x1 = int(mapjs(obs.x - obs.len, 0 - SCALE, WIDTH + SCALE, 0, nb_secteur-1))
    y1 = int(mapjs(obs.y - obs.height, 0 - SCALE, WIDTH + SCALE, 0, nb_secteur-1))
    x_al.append(x1)
    y_al.append(y1)
    
    x2 = int(mapjs(obs.x - obs.len, 0 - SCALE, WIDTH + SCALE, 0, nb_secteur-1))
    y2 = int(mapjs(obs.y + obs.height, 0 - SCALE, WIDTH + SCALE, 0, nb_secteur-1))
    x_al.append(x2)
    y_al.append(y2)
    
    x3 = int(mapjs(obs.x + obs.len, 0 - SCALE, WIDTH + SCALE, 0, nb_secteur-1))
    y3 = int(mapjs(obs.y + obs.height, 0 - SCALE, WIDTH + SCALE, 0, nb_secteur-1))
    x_al.append(x3)
    y_al.append(y3)
    
    x4 = int(mapjs(obs.x + obs.len, 0 - SCALE, WIDTH + SCALE, 0, nb_secteur-1))
    y4 = int(mapjs(obs.y - obs.height, 0 - SCALE, WIDTH + SCALE, 0, nb_secteur-1))
    x_al.append(x4)
    y_al.append(y4)
    
    x_al, y_al = delete_liste(x_al, y_al)
    for i in x_al:
        for j in y_al:
            secteurs[i][j].append(obs)
    
    
canvas.bind("<Button-1>", pointeur)
canvas.pack()
Draw()
tk.mainloop()