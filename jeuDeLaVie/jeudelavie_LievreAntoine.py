#!/usr/bin/env python3
"""
Simulateur du jeu de la vie de John Horton Conway
utilisation : dans un terminal unix, avec python 3 d'installer ainsi que le module complementaire PyQt5,
taper : ./jeudelavie.py [nom_du_fichier] [nombre_de_génération]
avec [nom_du_fichier] est le nom a ouvrir, un fichier texte contenant
- "." pour les cellules morte.
- "*" pour les celllules vivante
- "#[...]" un commentaire qui ne sera pas lu par le programme.
"""
# taille maxi de la grille d'entré
TAILLE_X = 300
TAILLE_Y = 300
import sys
from pprint import *
# Chargement des bibliothèques Qt5
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import QRect
# Le tableau ‘vivante‘ booléen dit si la cellule (x,y) est vivante
# il est initialisé vide
vivante = [
[False, False, False, False],
[False, False, False, False],
[False, False, False, False],
[False, False, False, False]]
def dessiner_grille(qp):
    """
dessine la grille de l’automate cellulaire sur le QPainter qp
    """
    #definition des variables
    # L = longueur en x des cellules
    # l = longueur en y des cellules
    L = 30
    l = 30
    # b et a sont des compteur pour avoir la position ou l'on se trouve dans le dessin.
    b = 0
    a = 0
    # noir est la couleur noir
    noir = QColor(0,0,0)
    qp.setPen(noir) # on dessine en noir
    for ligne in vivante:
        b += 1
        for elt in ligne:
            a += 1
            # on dessine toujours la grille de cellule vide
            qp.drawRect(QRect(a*L,b*l,L,l))
            if elt: # si elle est vivante on remplit la grille
                qp.fillRect(QRect(a*L,b*l,L,l), noir)                
        a = 0 
    return
class FenetreDessin(QWidget):
    """
Notre classe fenêtre qui permettra d’afficher l’état de l’automate
cellulaire
    """
    def paintEvent(self, event):
        """
    paintEvent est appelée chaque fois qu’il faut redessiner la fenêtre
        """
        qp = QPainter(self)
        dessiner_grille(qp)

#-----------decoder les lignes----------#
def decodage_ligne(ligne):
    """
cette fonction permet de décoder une ligne renvoyant une liste avec 
- "." = False
- "*" = True
- "#" = renvoie tout les elements precedement lu
    """
    tab = []
    for elt in ligne:
        if elt ==".":
            tab.append(False)
        elif elt == "*":
            tab.append(True)
        elif elt == "#":
            return tab
        elif elt == "\n":
            return tab
        else:
            print("----------------------------------")
            print("erreur lors de la lecture de ligne")
            print("----------------------------------")
            return []
    return tab
#------------decoder un fichier----------#
def initialiser_depuis_fichier(fichier):
    """
cette fonction initialise le tableau vivante depuis le nom de fichier
    """
    fi = open(fichier)

    fic = []# tableau final contenant tout les elements du fichier
    
    #lecture du fichier
    for ligne in fi:
        tab = [] # celui ci contient les lignes du fichier une a une
        for elt in ligne:
            tab.append(elt)
        fic.append(tab)
    fi.close()
    
    #enregistrer dans une liste dont chaque elt est une liste.
    #test pour voir si le tableau est correct.
    nb_ligne = 0
    nb_car_defaut = 0
    for elt in fic:
        nb_car = 0
        for elt1 in elt:
            if (elt1 == "." or elt1 == "*") and elt1 != "#":
                nb_car += 1 # compteur de caractere
            elif elt1 == "#":
# compteur de ligne pour compenser avec l'addition en fin de lecture
                nb_ligne -= -1
                break
            elif elt1 == "\n":
                break#sortir de la boucle pour ligne suivante
            else:
                print("-----------------------------------------------")
                print("erreur lors de la lecture,caractere non reconnu")
                print("-----------------------------------------------")
                return -1
            if nb_car == TAILLE_X:
                print("-----------------------------------")
                print("erreur, trop de caractere par ligne")
                print("-----------------------------------")
                return -2
        if nb_car != 0 and nb_car_defaut == 0:
            nb_car_defaut = nb_car
        if nb_car != nb_car_defaut:
            print("------------------------------------")
            print("erreur nombre de caractére different")
            print("------------------------------------")
            return -4
        nb_ligne += 1
        if nb_ligne == TAILLE_Y:
            print("----------------------")
            print("erreur, trop de lignes")
            print("----------------------")
            return -3
        
    #ajout des ligne decoder a table        
    table = []
    for elt in fic:
        a = decodage_ligne(elt)
        if a != []: # liste vide est quand on as un commentaire en début de ligne
            table.append(a)
    
    return table

#----------nombre de voisin a la position x, y-----------#
def nombre_de_voisin(x,y):
    """
calcul du nombre de voisin pour la position x, y avec le 0 en haut 
à gauche, le x est horizontal et y vertical
    """
    voisin = 0
    for k in range(-1,2):
        if y+k >= 0 and y+k < len(vivante): # verifictaion que l'on ne dépasse pas la longueur du tableau en y
            for l in range(-1,2):
                if not( l == k and k == 0):# dans tous les cas ou ce n'est pas vrai cad que la cellule regardée n'est pas elle même
                    if x + l >= 0  and x+l < len(vivante[1]):# on test en x de la même facon que pour y
                        if vivante[y+k][x+l]:
                            voisin += 1
    return voisin
#--------etat suivant au position x, y-------#
def etat_suivant(x, y):
    """
renvoi la valuer du prochain état de la cellule x, y, suivant les 
régle du jeu de la vie
    """
    etat = vivante[y][x] # dans les listes, x et y sont inversé
    voisin = nombre_de_voisin(x, y)
    if voisin <= 1  or voisin > 3:
        etat = False
    elif voisin == 3:
        etat = True
    return etat# on ne gére pas le cas de 2 voisins car cela ne change pas la valeur
#--------------------changer de generation------------#
def recalculer_grille():
    """
cette fonction utilise la variable global vivante pour passer de l'étape t à t + 1 
elle change la valeur du tableau vivante
    """
    tab = []
    for i in range(0,len(vivante)):
        t = []
        for j in range(0,len(vivante[i])):
            t.append(etat_suivant(j,i))
        tab.append(t)
    return tab

#--------------------faire avancer de plusieur génération -------------#
def passer_gene(nb_gene):
    """
cette fonction n'etait pas donné dans l'ennoncé du TP, elle permet de passer de la generation 
n a la génération n + nb_gene
    """
    global vivante
    for i in range(0,nb_gene):
        vivante = recalculer_grille()
    return
#----------tester si le fichier est utilisable--------#
def test_parametre(fichier, nb_gene):
    """
cette fonction n'est pas donné dans le TP elle verifie les parametres 
du terminal sont valides, elle fait de la gestion d'erreur
    """
    if type(fichier) != str:
        print("---------------------------------------------------")
        print("erreur, veuiller entrer un nom de fichier correcte.")
        print("---------------------------------------------------")
    try :
        open(fichier)
    except:
        print("-------------------------------")
        print("erreur à l'ouverture du fichier")
        print("-------------------------------")
        return -1
    try:
        nb_gene = int(nb_gene)
    except:
        print("-------------------------------------------------")
        print("veuiller entrer le nombre de generation à avancer")
        print("-------------------------------------------------")
        return -1
    return 0
if __name__ == '__main__':
    #ceci ne s'éxécute que quand le fichier sont éxécuté par le shell
    try:
        # on récupere les arguments donnés en entrée
        fichier = sys.argv[1]
        nb_gene = sys.argv[2]
    except:
        print("veuiller entrer deux paramêtre en entré")
    testeur = test_parametre(fichier, nb_gene)# on test les paramêtres
    
    while testeur != 0:
        print("veuiller entrer de nouvelle valeur")
        print("----------------------------------")
        fichier = input("fichier a ouvrir : ")
        nb_gene = input("nombre de génération à passer : ")
        testeur = test_parametre(fichier, nb_gene)
    nb_gene = int(nb_gene)
    vivante = initialiser_depuis_fichier(fichier)
    passer_gene(nb_gene)
    
    
    app = QApplication(sys.argv)
    
    fenetre = FenetreDessin()
    fenetre.setWindowTitle("le jeu de la vie")
    fenetre.setGeometry(100,100, 300, 200)
    fenetre.show()    

    app.exec_()
