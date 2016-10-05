#!/usr/bin/env python3
from Moteur import Moteur
class Plateau:
    def __init__(self, x_max, y_max):
        """constructeur du plateau, demande les maximum ou i peux se 
        déplacer
        """
        self.moteur_x = Moteur(0, x_max)
        self.moteur_y = Moteur(0, y_max)

    def __repr__(self):
        return "\nposition x : " + str(self.moteur_x.pos)+\
            "\nposition y : " + str(self.moteur_y.pos) + "\n\n"
         
        
    def aller_a(self, x, y):
        """
        permet de déplacer a une position en x et y.
        """
        if not self.moteur_x.bouge_en(x):
            print("déplacement impossible en x")
        if not self.moteur_y.bouge_en(y):
            print("déplacement impossible en y")

if __name__ == "__main__":
    plateau = Plateau(100, 100)
    plateau.aller_a(5,3)
    print(plateau)
    plateau.aller_a(60, 30)
    print(plateau)
    plateau.aller_a(102,10)
    print(plateau)
    plateau.aller_a(20, 108)
    print(plateau)
