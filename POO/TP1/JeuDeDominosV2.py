#!/usr/bin/env python3
from JoueurV2 import *
from random import *
import sys
class JeuDeDomino:
    """
representation du jeu de domino
    """
    def __init__(self, joueur_1, joueur_2):
        """
constructeur du jeu, prend les differents objets joueurs en entré
        """
        self.domino_poses = []
        self.joueur_1 = joueur_1
        self.joueur_2 = joueur_2
        self.joueur_1.adversaire = self.joueur_2
        self.joueur_2.adversaire = self.joueur_2
        self.joueur_courant = self.joueur_1
        self.pioche = []
        for i in range(20):
            self.pioche.append(Domino(randrange(1,6,1),
                                      randrange(1,6,1)))
        for i in range(0,7):
            self.joueur_1.pioche(self.pioche)
            self.joueur_2.pioche(self.pioche)
        

    def __repr__(self):
        """
redefinition de __repr__ qui va renvoyer la chaine de caractére 
représentant les dominos déja joué sur la table
        """
        return "le jeu : " + str(self.domino_poses)

    def affiche(self):
        """
affiche a l'aide de __repr__ les dominos déja joués
        """
        print(self.__repr__())
        
    def ajoute_en_tete(self, domino):
        """ 
ajoute en tete le domino voulut, sans prendre en compte le sens
        """
        tmp = self.joueur_courant.joue(domino)
        if tmp != None:
            if self.domino_poses == []:
                self.domino_poses.insert(0, domino)
                return True
            else:
                if domino.droite == self.domino_poses[0].gauche:
                    self.domino_poses.insert(0, domino)
                    return True
                else:
                    domino.retourne()
                    if domino.droite == self.domino_poses[0].gauche:
                        self.domino_poses.insert(0, domino)
                        return True
        self.joueur_courant.pioche([tmp])
        return False
    
    def ajoute_en_queue(self, domino):
        tmp = self.joueur_courant.joue(domino)
        if tmp != None:
            if self.domino_poses == []:
                self.domino_poses.append(domino)
                return True
            else:
                if domino.gauche == self.domino_poses[-1].droite:
                    self.domino_poses.append(domino)
                    return True
                else:
                    domino.retourne()
                    if domino.gauche == self.domino_poses[-1].droite:
                        self.domino_poses.append(domino)
                        return True
        self.joueur_courant.pioche([tmp])
        return False
    
    def jouer(self, domino):
        if not self.ajoute_en_tete(domino):
            if not self.ajoute_en_queue(domino):
                print("Coup impossible, le domino", domino, \
                      "ne s'insére par correctement")
                return False
        self.joueur_courant.pioche(self.pioche)
        if self.joueur_courant == self.joueur_1:
            self.joueur_courant = self.joueur_2
        else:
            self.joueur_courant = self.joueur_1
        return True
        
    def peux_jouer(self, domino):
        if self.domino_poses == []:
                return True
        else:
            if domino.gauche == self.domino_poses[-1].droite:
                return True
            else:
                domino.retourne()
                if domino.gauche == self.domino_poses[-1].droite:
                    return True
                domino.retourne()
        if domino.droite == self.domino_poses[0].gauche:
            return True
        else:
            domino.retourne()
            if domino.droite == self.domino_poses[0].gauche:
                return True
            domino.retourne()
        return False
    def est_finit(self):
        for domino in self.joueur_courant.main:
            if self.peux_jouer(domino):
                return False
        return True
    def gagnant(self):
        if self.joueur_courant.main == []:
            return self.joueur_courant
        if self.joueur_courant == self.joueur_1:
            return self.joueur_2
        else:
            return self.joueur_1
