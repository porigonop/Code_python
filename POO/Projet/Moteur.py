#!/usr/bin/env python3
class Moteur:
    def __init__(self, pos_min, pos_max):
        """constructeur de Moteur, depart a la position mminimale dans une 
        direction et demande une position a ne pas dépassez.
        """
        self.pos_min = pos_min
        self.pos_max = pos_max
        self.pos = pos_min
        self.direction = True # True = un direction, False = une autre

    def __repr__(self):
        """une représentation du Moteur, avec sa position et sa 
        direction
        """
        return "\n\nposition : " + str(self.pos) + \
            "\ndirection : " + str(self.direction)
    
    def change_direction(self):
        """permet de changer la direction dans laquelle va le moteur
        """
        if self.direction:
            self.direction = False
        else:
            self.direction = True
        return True

    def avance(self, nombre):
        """avance le moteur ne nombre cran. ajouter ici le code de 
        control moteur
        """
        if self.pos + nombre > self.pos_max and self.direction:
            return False
        if self.pos - nombre < self.pos_min and not self.direction:
            return False
        
        for i in range(0, nombre):
            if self.direction:
                self.pos += 1
                #ici pour avancer
            else:
                self.pos -= 1
                #ici pour reculer
        return True

    def bouge_en(self, pos):
        """permet d'envoyer le moteur a une position
        """
        pos_init = self.pos
        if pos_init < pos:
            if self.direction:
                return self.avance(pos - pos_init)
            
            else:
                self.change_direction()
                return self.avance(pos - pos_init)

            
        else:
            if not self.direction:
                return self.avance(pos_init - pos)
            
            else:
                self.change_direction()
                return self.avance(pos_init - pos)


if __name__ == "__main__":
    moteur = Moteur(0, 100)
    moteur.bouge_en(3)
    print(moteur)
    moteur.bouge_en(1)
    print(moteur)
    moteur.bouge_en(30)
    print(moteur)
    moteur.bouge_en(102)
    print(moteur)
