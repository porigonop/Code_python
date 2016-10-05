#!/usr/bin/env python3
import math
class DronePolaire:
    """décrit l'obje DronePolaire quie est un drone se déplaceant dans l'éspace
    x, y, z, peux monter descendre avancer et tourner sur lui-même
    """
    def __init__(self):
        """initialisation des parametre, inchangeable au debut
        """
        self.x = 0
        self.y = 0
        self.z = 0
        self.direction = 0
        
    def affiche(self):
        """permet d'afficher la position du drone en x, y, z ainsi que sa 
        direction
        """
        print("( x = " + str(self.x) +\
              " y = " + str(self.y)+\
              " z = " +str(self.z)+\
              " direction : "+str(self.direction)+ ")")
        
    def rotate(self, rotation):
        """permet une rotation du drone dans le sens anti-horaire avec 
        rotation en radian uniquement si le drone vole
        """
        if self.z > 0:
            self.direction = round(self.direction + rotation, 2)

            return True
        print("Voyons, je suis déjà au sol...")
        return False

    def avance(self, distance):
        """permet de faire avancer le drone d'une distance positive 
        et si il vole
        """
        if distance > 0:
            if self.z > 0:
                self.x += round(distance * math.cos(self.direction), 2)
                self.y += round(distance * math.sin(self.direction), 2)
                return True
            print("je ne peux pas bouger au sol")
            return False
        print("A mon avis une disance se devrait d'être positive...")
        return False

    def monte(self, altitude):
        """permet de faire monter le drone d'une altitude positive
        """
        if altitude > 0:
            self.z += round(altitude, 2)
            return True
        print("Descendre et monter sont deux actions différente...")
        return False
    
    def descend(self, altitude):
        """permet de faire descendre le drone d'une distance positive, 
        le drone le peux pas se crasher
        """
        if altitude > 0:
            if self.z - altitude >= 0:
                self.z -= round(altitude, 2)
                return True
            print("Non... je refuse de m'écraser !!!")
            return False
        print("Descendre et monter sont deux actions différente...")
        return False

if __name__ == "__main__":
    monDrone = DronePolaire()
    monDrone.affiche()
    monDrone.rotate(math.pi / 2)
    monDrone.monte(-3)
    monDrone.monte(3)
    monDrone.rotate(math.pi / 2)
    monDrone.avance(-10);
    monDrone.avance(10);
    monDrone.affiche()
    monDrone.descend(-3);
    monDrone.descend(4);
    monDrone.descend(2);
    monDrone.rotate(- math.pi / 4);
    monDrone.affiche()
