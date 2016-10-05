#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from Domino import *
from random import choice
class Joueur:
    """ Classe reprÃ©sentant un joueur

    :Attribut nom: String, représentant le nom du joueur
    :Attibut main: Domino[], représentant la main du joueur courant, ie
                   l'ensemble des dominos qu'il a à jouer
    """

    def __init__(self, nom):
        """ Constructeur de la classe

        :Param nom: String, servant à initialiser l'attribut nom 
        de la classe
        """

        self.nom = nom
        self.main = []
        self.adversaire = None


    def pioche(self, pioche):
        """ Methode permettant d'ajouter un domino à la main du joueur courant 
        """
        if pioche == []:
            return False
        domino = choice(pioche)
        if isinstance(domino, Domino):
            self.main.append(domino)
            pioche.remove(domino)
        return True


    def __repr__(self):
        """ Redéfinition de la méthode __repr__ pour la classe Domino"""
        return "Main du joueur " + self.nom + ' : ' + str(self.main)


    def est_le_meme_que(self, joueur):
        """ Méthode permettant de tester si le nom du joueur courant 
        (ie de self) et de joueur sont identiques
        :Param joueur: Joueur
        """

        return self.nom == joueur.nom


    def affiche(self):
        """ Méthode permettant d'afficher la main du joueur courant """

        print(self.__repr__())


    def joue(self, domino):
        """ Méthode permettant au joueur courant de jouer un domino.
        Cela n'est possible que si le domino en question est 
        effectivement dans la main du joueur.
        Lorsque l'action n'est pas possible, la méthode affiche 
        la main du joueur courant.

        :Param domino: Domino
        """

        for indice in range(len(self.main)):
            if domino.est_le_meme_que(self.main[indice]):
                return self.main.pop(indice)
        print("COUP IMPOSSIBLE : " + "main de "+ self.nom + " : " +\
              str(self.main))
        return None
if __name__ == '__main__':

    d1 = Domino(3,2)
    d2 = Domino(3,4)
    d3 = Domino(2,3)
    d4 = Domino(4,4)
    d5 = Domino(5,4)
    joueur = Joueur("toto")
    joueur.affiche()
    joueur.ajoute_a_la_main(d1)
    joueur.affiche()
    joueur.ajoute_a_la_main("3")
    joueur.affiche()
    joueur.ajoute_a_la_main(d2)
    joueur.ajoute_a_la_main(d3)
    joueur.ajoute_a_la_main(d4)
    joueur.ajoute_a_la_main(d5)
    joueur.affiche()
    joueur.joue(d2)
    joueur.affiche()
    d6 = Domino(1, 2)
    joueur.joue(d6)
    joueur_2 = Joueur("titi")
    joueur_3 = Joueur("toto")
    print(joueur.est_le_meme_que(joueur_2))
    print(joueur.est_le_meme_que(joueur_3))
