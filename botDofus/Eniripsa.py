

class Eniripsa:
    def __init__(self, level, map_pos):
        self.level = level
        self.pos = [0, 0]
        self.map_pos = map_pos
        
    def change_map(self, direction):
        if direction == -1:
            print("monter")
            self.map_pos[1] -= 1
        elif direction == 1:
            print("aller en bas")
            self.map_pos[1] += 1
        elif direction == 2:
            print("aller a droite")
            self.map_pos[0] += 1
        elif direction == -2:
            print("aller a gauche")
            self.map_pos[0] -= 1
            
    def move_to_map(self, map_pos):
        while self.map_pos != map_pos:
            if map_pos[0] > self.map_pos[0]:
                self.change_map(2)
            elif map_pos[0] != self.map_pos[0]:
                self.change_map(-2)
            if map_pos[1] > self.map_pos[1]:
                self.change_map(1)
            elif map_pos[1] != self.map_pos[1]:
                self.change_map(-1)
    
    def look_around(self, radius):
        #a finir
        count = 1
        while radius > 0:
            self.change_map(2)
            for i in range(count):
                self.change_map(-1)
            for i in range(count):
                self.change_map(-2)
            for i in range(count):
                self.change_map(-1)
if __name__ == "__main__":
    perso = Eniripsa(31, [2, -17])
    perso.move_to_map((10, 10))
