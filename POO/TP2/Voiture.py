#!/usr/bin/env python3
class Voiture:
    """
    Objet représentant une voiture avec :
    une marque qui est un string
    une couleur, un string également
    un pilote qui est une string
    et une vitesse qui est un float
    """
    def __init__(self, marque = 'Lamborghini', couleur = 'rouge'):
        self.marque = marque
        self.couleur = couleur
        self.pilote = None
        self.vitesse = 0
        
    def __repr__(self):
        pilote = self.pilote
        if self.pilote == None:
            pilote = "nobody"
        return str(self.marque +" " + self.couleur +\
            "\nconducteur actuel : "+ pilote +\
                   "\nVitesse actuelle : "+str(self.vitesse) + " km/h")
    
    def affiche(self):
        """ affiche en console le déscriptif de la voiture"""
        print(self.__repr__())
        
    def choix_conducteur(self, conducteur):
        """ change le pilote avec le nouveau conducteur"""
        self.pilote = conducteur
        
    def accelerer(self, valeur_acceleration, duree):
        """permet d'accelerer de x km/h durant x duré avec un pilote
        """
        if self.pilote == None:
            print("il n'y as pas de pilote")
            return False
        self.vitesse += valeur_acceleration * duree
        return True
    
if __name__ == "__main__":
    voiture = Voiture("McLaren", "Rouge")
    voiture.accelerer(1.8, 12)
    voiture.affiche()
    voiture.choix_conducteur('Ayrton Senna')
    voiture.accelerer(1.8, 12)
    voiture.affiche()
#fini
