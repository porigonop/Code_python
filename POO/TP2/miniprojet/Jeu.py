#!/usr/bin/env python3
from Grille import Grille
from Joueur import Joueur
#initialisation du jeu
nom1 = input("nom joueur 1 :")
nom2 = input("nom joueur 2 : ")
taille = input("taille du morpion : ")
#definition des joueurs
joueur_1 = Joueur(nom1)
joueur_2 = Joueur(nom2)
#définition des piéce de chaque joueur
joueur_1.piece = "x"
joueur_2.piece = "0"
#définition de la grille
grille = Grille(int(taille))
#mise en place du joueur actuel
joueur_actuel = joueur_1
#tant que ce n'est pas finie : rappel grille.fini() rennvoie False
#si elle n'est pas fini
while not grille.fini():
    print(grille)
    print(joueur_actuel())
    if grille.changer(joueur_actuel.joue(), joueur_actuel.piece):
        if joueur_actuel == joueur_1:
            joueur_actuel = joueur_2
        else:
            joueur_actuel = joueur_1
    else:
        print("impossible de joueur ici")
    
        
    
