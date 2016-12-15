import simplegui
import math
import random
WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
time = 0

class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)

ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# alternative upbeat soundtrack by composer and former IIPP student Emiel Stopler
# please do not redistribute without permission from Emiel at http://www.filmcomposer.nl
#soundtrack = simplegui.load_sound("https://storage.googleapis.com/codeskulptor-assets/ricerocks_theme.mp3")

# helper functions to handle transformations
def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)


class SpaceShip:
    def __init__(self, pos, vel, angle, sound, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.sound = sound
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.friction = 0.1
        
    def Update(self):
        self.angle += self.angle_vel
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT
        
        self.vel[0] *= (1-self.friction)
        self.vel[1] *= (1-self.friction)
        
        forward = [math.cos(self.angle), math.sin(self.angle)]
        if self.thrust:
            self.vel[0] += forward[0]
            self.vel[1] += forward[1]
    
    def PlaySound(self):
        self.sound.play()
        
    def StopSound(self):
        self.sound.pause()
        self.sound.rewind()
        
    def KeyDown(self, key):
        
        if key == simplegui.KEY_MAP["up"]:
            self.thrust = True
            
        if key == simplegui.KEY_MAP["left"]:
            self.angle_vel -= 0.1
        
        if key == simplegui.KEY_MAP["right"]:
            self.angle_vel += 0.1
            
    def KeyUp(self, key):
        
        if key == simplegui.KEY_MAP["up"]:
            self.thrust = False
        if key == simplegui.KEY_MAP["left"]:
            self.angle_vel += 0.1
            
        if key == simplegui.KEY_MAP["right"]:
            self.angle_vel -= 0.1
            
    def Draw(self, canvas):
        if self.thrust:  
            self.image_center[0]=135  
        else:  
            self.image_center[0]=45  
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size,self.angle)  
  
        canvas.draw_image(self.image,\
                          self.image_center,\
                          self.image_size,\
                          self.pos,\
                          self.image_size,\
                          self.angle)

    
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
   
    def Draw(self, canvas):
        canvas.draw_image(self.image,\
                          self.image_center,\
                          self.image_size,\
                          self.pos,\
                          self.image_size,\
                          self.angle)
    
    def Update(self):
        self.angle += self.angle_vel
        self.pos[0] = (self.pos[0] + self.vel[0])
        self.pos[1] = (self.pos[1] + self.vel[1])
        
        

def rock_spawner():
    global a_rock
    
    a_rock = Sprite([random.random() * WIDTH, random.random() * HEIGHT],\
                    [random.random() * random.choice((-1, 1)), random.random() * random.choice((-1, 1))],\
                    random.random(),\
                    random.random()*0.1,\
                    asteroid_image,\
                    asteroid_info)
        
def Draw(canvas):
    global time
    
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))

    spaceship.Draw(canvas)
    a_rock.Draw(canvas)
    
    if spaceship.thrust:
        spaceship.PlaySound()
    else:
        spaceship.StopSound()
            
    spaceship.Update()
    a_rock.Update()
    
def KeyDown(key):
    spaceship.KeyDown(key)
    
def KeyUp(key):
    spaceship.KeyUp(key)


    
    
    
a_rock = Sprite([random.random() * WIDTH, random.random() * HEIGHT],\
                    [random.random() * random.choice((-1, 1)), random.random() * random.choice((-1, 1))],\
                    random.random(),\
                    random.random(),\
                    asteroid_image,\
                    asteroid_info)
spaceship = SpaceShip([0, 0], [0, 0], 0, ship_thrust_sound, ship_image, ship_info)        
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

frame.set_draw_handler(Draw)
frame.set_keydown_handler(KeyDown)
frame.set_keyup_handler(KeyUp)
timer = simplegui.create_timer(1000, rock_spawner)

frame.start()
timer.start()
