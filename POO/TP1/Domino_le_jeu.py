#!/usr/bin/env python3
from JeuDeDominoV2 import *
# initialisation
joueur1 = Joueur(input("nom du premier joueur : "))
joueur2 = Joueur(input("nom du second joueur : "))
jeu = JeuDeDomino(joueur1, joueur2)
# début du jeu
while not jeu.est_finit():
    jeu.joueur_courant.affiche()
    jeu.affiche()
    try:
        a =input("quelle domino jouer ? x x ")
        #condition pour quitter le jeu
        if a == 'exit':
            break
        #separer les deux partis du domino
        a = a.split(" ")
        for i in range(len(a)):
            a[i] = int(a[i])
        jeu.jouer(Domino(a[0], a[1]))
        #si l'input n'est pas bonne n'est pas bonne
    except:
        print("veuiller entrer un domino correcte")
if a == 'exit':
    sys.exit()
print("le gagnant est : ", jeu.gagnant().nom)
