#!/usr/bin/env python3
import sys
from random import *
from pprint import *
from time import *
# le code n'est pas le plus beau possible, je l'ai écris vite pour aller
#le plus loin possible.
TAILLE_X = 300
TAILLE_Y = 300
vivante = []
# Chargement des bibliothèques Qt5
from PyQt5.QtCore import QTimer, pyqtSlot, QPoint
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QGridLayout, QDialog, QInputDialog, QLabel
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import QRect

#plusieur variable global
fenetre = None #la fenetre ou se trouve l'affichage
nb_gene = 0 # nombre de generation 
pourcent = 0 # pourcentage d'avancement de la bar de chargement
#elle est global pour enregistrer l'ancienne position de la bar
#entre les stop etc...
charg = False # si oui ou non la bar de chargement doit avancer
positionA = 0 #position de la bar de chargement, idem pour positionB
positionB = 10
taille = 0#taille de la bar
pinceau = 0 #pinceau utiliser, rouge ou blanc
@pyqtSlot()
def suivant():
    """
fait acancer d'une génération
    """
    global vivante
    global nb_gene
    global LabelGenen #nombre de generation, affiché en haut a gauche
    nb_gene += 1
    vivante = recalculer_grille()
    labelGene.setText(str(nb_gene))
    fenetre.repaint()
@pyqtSlot()
def start():
    """
lance le QtTimer qui va actualiser a l'aide de suivant tout les 50ms
et lancer la bar de chargement
    """
    global charg
    charg = True
    timer.start(50)
@pyqtSlot()
def stop():
    """
arréte le timer et la bar de chargement
    """
    global charg
    charg = False
    fenetre.repaint()
    timer.stop()
@pyqtSlot()
def quitter():
    """
quitter le programe et donne en console le nombre de génération passé
    """
    print("nombre de generation : ", nb_gene)
    exit()
@pyqtSlot()
def avance(nb):
    """
avance d'un nombre nb de génération tout en augmentant la bar de 
chargement assigné a cette fonction, differente de celle du timer
    """
    global vivante
    global nb_gene
    global pourcent
    nb_gene += nb
    b = nb // 100
    for i in range(nb):
        vivante = recalculer_grille()
        pourcent = i+b
        fenetre.repaint()
    pourcent = 0
    fenetre.repaint()

@pyqtSlot()
def effacer():
    """
efface tout le tableau vivante
    """
    global vivante
    for i in range(len(vivante)):
        for y in range(len(vivante[i])):
            vivante[i][y] = False
    fenetre.repaint()
@pyqtSlot()
def pinceau():
    """
selection un pinceau
    """
    global pinceau
    item, ok = QInputDialog.getItem(fenetre, "liste","choissisez votre pinceau",["rouge","blanc"])
    if item == "rouge":
        pinceau = 1
    else:
        pinceau = 0    
def chargement(qp):
    """
bar de chargement de avance
    """
    noir = QColor(0,0,0)
    rouge = QColor(255,0,0)
    qp.setPen(noir)
    qp.drawRect(QRect(520,20,100,10))
    qp.fillRect(QRect(520,20,pourcent,10), noir)
    
def chargwin(qp):
    """
bar de chargement du timer, glitch legerement à la fin
    """
    if charg:
        noir = QColor(0,0,0)
        rouge = QColor(255,0,0)
        qp.setPen(noir)
        qp.drawRect(QRect(300,20,100,10))
        global positionA
        global positionB
        global taille
        if positionA == 100:
            positionA = 0
        positionA += 1
        if positionA <= 10:
            taille += 1
            qp.fillRect(QRect(300, 20, taille, 10), noir)
        elif positionA > 90:
            taille -= 1
            qp.fillRect(QRect(300 + positionA-taille, 20, taille, 10), noir)
        else:
            qp.fillRect(QRect(300 + positionA-taille, 20, taille, 10), noir)
            

def dessiner_grille(qp):
    """
dessine la grille de l’automate cellulaire sur le QPainter qp
    """
    dx = 100
    dy = 100
    L = 5
    l = 5
    b = 0
    a = 0
    noir = QColor(0,0,0)
    rouge = QColor(255,0,0)
    qp.setPen(noir)
    for ligne in vivante:
        b += 1
        for elt in ligne:
            a += 1
            #qp.drawRect(QRect(a*L + dx ,b*l + dy,L,l))
            if elt:
                qp.fillRect(QRect(a*L + dx,b*l + dy,L,l), rouge)                
        a = 0 
    return

class FenetreDessin(QWidget):
    """
    Notre classe fenêtre qui permettra d’afficher l’état de l’automate
    cellulaire
    """
    def mousePressEvent(self, QMouseEvent):
        """
permet de savoir quand l'utilisateur appui sur la souris à une position
        """
        x, y = QMouseEvent.x()-105, QMouseEvent.y()-105
        x1 = ( x // 5 )
        y1 = ( y // 5 )
        if pinceau == 1:
            try:
                vivante[y1][x1] = True
            except:
                pass
        else:
            vivante[y1][x1] = False
        fenetre.setMouseTracking(True)
        fenetre.repaint()
    def mouseMoveEvent(self, QMouseEvent):
        """
enregistre le deplacement de la souris.
        """
        x, y = QMouseEvent.x()-105, QMouseEvent.y()-105
        x1 = ( x // 5 )
        y1 = ( y // 5 )
        if pinceau == 1:
            try:
                vivante[y1][x1] = True
            except:
                pass
        else:
            try:
                vivante[y1][x1] = False
            except:
                pass
        fenetre.repaint()
    def mouseReleaseEvent(self, QMouseEvent):
        """
quand on arrète d'appuyer sur la souris
        """
        fenetre.setMouseTracking(False)
    def paintEvent(self, event):
        """
paintEvent est appelée chaque fois qu’il faut redessiner la fenêtre
        """
        qp = QPainter(self)
        dessiner_grille(qp)
        chargement(qp)
        chargwin(qp)

#-----------decoder les lignes----------#
def decodage_ligne(ligne):
    """
décode une ligne de caractére type str
    """
    tab = []
    for elt in ligne:
        if elt == ".":
            tab.append(False)
        elif elt == "*":
            tab.append(True)
        elif elt == "#":
            return tab
        elif elt == "\n":
            return tab
        else:
            print("erreur lors de la lecture de ligne")
            return []
    return tab
#------------decoder un fichier----------#
def initialiser_depuis_fichier(fichier):
    """
initialise depuis une chaine de caractére qui est un fichier
    """
    fi = open(fichier)
    fic = []
    #lecture du fichier
    for ligne in fi:
        tab = []
        for elt in ligne:
            tab.append(elt)
        fic.append(tab)
    fi.close()
    #enregistrer dans un tableau dont chaque elt est un tableau.
    #test pour voir si le tableau est correct.
    j = 0
    for elt in fic:
        i = 0
        for elt1 in elt:
            if (elt1 == "." or elt1 == "*") and elt1 != "#":
                i += 1
            elif elt1 == "#":
                j -= -1
                break
            elif elt1 == "\n":
                break
            else:
                print("erreur lors de la lecture,caractere non reconnu")
                break
            if i == TAILLE_X:
                print("erreur, trop de caractere par ligne")
                return
        j += 1
        if j == TAILLE_Y:
            print("erreur, trop de lignes")
            return
    #ajout des ligne decoder a table        
    table = []
    for elt in fic:
        a = decodage_ligne(elt)
        if a != []:
            table.append(a)
        else:
            pass
    return table

#----------nombre de voisin a la position x, y-----------#
def nombre_de_voisin(x,y):
    """
compte le nombre de voisin a la position x, y
    """
    voisin = 0
    for k in range(-1,2):
        if y+k >= 0 and y+k < len(vivante):
            for l in range(-1,2):
                if l == k and k == 0:
                    pass
                else:
                    if x + l >= 0  and x+l < len(vivante[1]):
                        if vivante[y+k][x+l]:
                            voisin += 1
                        else:
                            pass
        else:
            pass
    return voisin
#--------etat suivant au position x, y-------#
def etat_suivant(x, y):
    """
renvoie True ou False de la cellule a la position x, y
    """
    etat = vivante[y][x]
    voisin = nombre_de_voisin(x, y)
    if voisin <= 1  or voisin > 3:
        etat = False
    elif voisin == 3:
        etat = True
    return etat
#--------------------changer de generation------------#
def recalculer_grille():
    """
recalcul la grille entiére vivante
    """
    tab = []
    for i in range(0,len(vivante)):
        t = []
        for j in range(0,len(vivante[i])):
            t.append(etat_suivant(j,i))
        tab.append(t)
    return tab


#--créé un fichier de caractere aléatoire pour le jeu de la vie --#
def creefic(nom):
    """
crée un fichier de 100*100 nommer nom avec des . et des * aléatoirement
    """
    liste = ['.','*']
    fic = open(nom,"w")
    for i in range(0,100):
        for j in range(0,100):
            fic.write(choice(liste))
        fic.write('\n')
        
if __name__ == "__main__":
    creefic("aleatoire")#crée un fichier aléatoire si on veux l'utiliser
    if sys.argv[1] !="__vide__":
        vivante = initialiser_depuis_fichier(sys.argv[1])
    else:
        for i in range(int(sys.argv[2])):
            tab = []
            for i in range(int(sys.argv[3])):
                tab.append(False)
            vivante.append(tab)
    #il manque un gestion d'erreur dans mon code.

    #definition de l'affichage.
    app = QApplication(sys.argv)
    
    fenetre = FenetreDessin()
    fenetre.setWindowTitle("le jeu de la vie")
    fenetre.setGeometry(300,300, 1000, 1000)
    fenetre.show()


    btnQuitter = QPushButton('quitter',fenetre)
    btnQuitter.clicked.connect(quitter)
    btnQuitter.resize(btnQuitter.sizeHint())
    btnQuitter.setGeometry(100, 0, 100, 20)
    btnQuitter.show()
        
    btnSuivant = QPushButton('suivant', fenetre)
    btnSuivant.clicked.connect(suivant)
    btnSuivant.resize(btnSuivant.sizeHint())
    btnSuivant.setGeometry(200,0,100,20)
    btnSuivant.show()
        
    btnStart = QPushButton('Start',fenetre)
    btnStart.clicked.connect(start)
    btnStart.resize(btnStart.sizeHint())
    btnStart.setGeometry(300,0,100,20)
    btnStart.show()
        
    btnStop = QPushButton('Stop', fenetre)
    btnStop.clicked.connect(stop)
    btnStop.resize(btnStop.sizeHint())
    btnStop.setGeometry(400,0,100,20)
    btnStop.show()
    
    btnAvance = QPushButton('avancer de 100', fenetre)
    btnAvance.clicked.connect((lambda : avance(100)))
    btnAvance.resize(btnAvance.sizeHint())
    btnAvance.setGeometry(500,0,150,20)
    btnAvance.show()

    btnEffacer = QPushButton('effacer', fenetre)
    btnEffacer.clicked.connect(effacer)
    btnEffacer.setGeometry(650,0,100,20)
    btnEffacer.show()

    btnPinceau = QPushButton('pinceau', fenetre)
    btnPinceau.clicked.connect(pinceau)
    btnPinceau.setGeometry(750,0,100,20)
    btnPinceau.show()
    
    labelGene = QLabel(str(nb_gene), fenetre)
    labelGene.setGeometry(0,20,500,20)
    labelGene.show()
    
    timer = QTimer()
    timer.timeout.connect(suivant)

    app.exec_()
