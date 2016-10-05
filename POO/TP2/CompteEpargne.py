#!/usr/bin/env python3
from CompteBancaire import *
class CompteEpargne(CompteBancaire):
    """permet de representer un compte epargne a partire d'un compte bancaire
    """
    def __init__(self, nom_titulaire, solde_initial = 1000, \
                 interet = 0.3):
        """on initialise a l'aide de l'interet mensuel et des anciennes 
        valeur de compte bancaire
        """
        CompteBancaire.__init__(self, nom_titulaire, solde_initial)
        self.interet_mensuel = interet
        
    def changeTaux(self, valeur):
        """permet de changer le taux mensuel du compte
        """
        self.interet_mensuel = valeur
        
    def capitalisation(self, nombreMois):
        """permet de faire monter le solde bancaire en fonction de 
        l'interet mensuel et du nombre de mois
        """
        print("Capitalisation sur "+ str(nombreMois)+\
              " mois au taux mensuel de "+str(self.interet_mensuel)+\
              "% effectuée : ")
        interet = self.solde*(self.interet_mensuel/100)*nombreMois
        self.solde += interet
        print("intérêt = " + str(interet)+"euro")
        
if __name__ == "__main__":
    compte = CompteEpargne("Antoine")
    compte.depot(1000)
    compte.affiche()
    compte.capitalisation(12)
    compte.affiche()
    compte.changeTaux(2)
    compte.capitalisation(6)
    compte.affiche()


