#!/usr/bin/env python3
from Joueur import *

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
        self.finit = False
        self.perdant = ""
    def __repr__(self):
        """
redefinition de __repr__ qui va renvoyer la chaine de caractére 
représentant les dominos déja joué sur la table
        """
        return str(self.domino_poses)

    def affiche(self):
        """
affiche a l'aide de __repr__ les dominos déja joués
        """
        print(self.domino_poses)
        
    def ajoute_en_tete(self, domino, joueur):
        """ 
ajoute en tete le domino voulut, sans prendre en compte le sens
        """ 
        if self.domino_poses == []:
            self.domino_poses.insert(0, domino)
            return True
        else:
            if domino.droite == self.domino_poses[0].gauche:
                self.domino_poses.insert(0, joueur.joue(domino))
                return True
            else:
                domino.retourne()
                if domino.droite == self.domino_poses[0].gauche:
                    self.domino_poses.insert(0, joueur.joue(domino))
                    return True
        return False
    
    def ajoute_en_queue(self, domino, joueur):
        if self.domino_poses == []:
            self.domino_poses.append(joueur.joue(domino))
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
        return False
    
    def jouer(self, domino, joueur):
        if not self.ajoute_en_tete(domino, joueur):
            if not self.ajoute_en_queue(domino, joueur):
                print("Coup impossible, le domino", domino, "ne s'insére par correctement")
                return False
        return True
                
    def est_finit(self):
        for domino in 
    def gagnant(self):
        if self.est_finit():
            if self.joueur_1 == self.perdant:
                return self.joueur_2
            else:
                return self.joueur_1
    
if __name__ == "__main__":
    d1 = Domino(3,2)
    d2 = Domino(2,3)
    d3 = Domino(6,2)
    d4 = Domino(4,3)
    joueur1 = Joueur("Toto")
    joueur2 = Joueur("Titi")
    joueur1.ajoute_a_la_main(d1)
    joueur2.ajoute_a_la_main(d2)
    joueur1.ajoute_a_la_main(d3)
    joueur2.ajoute_a_la_main(d4)
    jeu = JeuDeDomino(joueur1, joueur2)
    jeu.affiche()
    jeu.ajoute_en_queue(d1, joueur1)
    jeu.affiche()
    jeu.ajoute_en_tete(d2, joueur2)
    jeu.affiche()
    jeu.jouer(d3, joueur1)
    jeu.affiche()
    jeu.jouer(d4, joueur2)
    print("Est-fini ?", jeu.est_finit())
    print("le gagnant ?", jeu.gagnant().nom)
