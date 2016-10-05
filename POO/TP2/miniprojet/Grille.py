#!/usr/bin/env python3
class Grille:
    def __init__(self, taille):
        """constructeur de la classe Grille
        """
        self.grille = []
        self.taille = taille
        for i in range(0,taille):
            a = []
            for j in range(0,taille):
                a.append(".")
            self.grille.append(a)
            
    def __repr__(self):
        """represente la grille en console
        """
        bord = "-"*self.taille*2
        grille = [bord]
        for i in range(0,self.taille):
            a = ["|"]
            for j in range(0,self.taille):
                a.append(self.grille[i][j])
                a.append("|")
            grille.append("".join(a))
        grille.append(bord)
        return "\n".join(grille)

    def changer(self, liste, piece):
        """permet de jouer a une position donner en argument 
        liste = [x, y]
        et la piece que veux placer le joueur,
        o ou x
        ne joue pas si deja placer
        """
        piece = str(piece)
        x = liste[0]
        y = liste[1]
        if x >= self.taille or x < 0 or y >= self.taille or y < 0:
            return False
        
        if self.grille[x][y]== ".":
            self.grille[x][y] = piece
            return True
        return False

    def fini(self):
        """methode pour savoir si la grille est gagner
        """
        #gestion ligne et colonne :
        for i in range(0,self.taille):
            colonne = []
            ligne = []
            compt_colonne = 0
            compt_ligne = 0
            compt_diag1 = 0
            compt_diag2 = 0
            for j in range(0,self.taille):
                colonne.append(self.grille[j][i])
                ligne.append(self.grille[i][j])
            for a in range(0, self.taille -1):
                if colonne[a] == colonne[a + 1]\
                   and colonne[0] != ".":
                    compt_colonne += 1
                if ligne[a] == ligne[a + 1]\
                   and ligne[0] != ".":
                    compt_ligne += 1
            #si on a compter autant que la taille de la grille c'est
            #gagné le -1 est unn équilibre avec le -1 du comptage.
            if compt_colonne ==self.taille -1:
                return colonne[0]
            if compt_ligne == self.taille-1:
                return ligne[0]
        #diagonale de haut gauche a bas droite :
        
        for i in range(0, self.taille-1):
            for j in range(0, self.taille-1):
                
                if i == j:
                    if self.grille[i][j] == self.grille[i+1][j+1]\
                       and self.grille[0][0] != ".":
                        compt_diag1 += 1
        #diagonale de haut droit a bas gauche :
        inverse = self.taille-1
        for i in range(0, self.taille-1):
            if self.grille[inverse][i] == self.grille[inverse-1][i+1]\
               and self.grille[self.taille-1][0] != ".":
                compt_diag2 += 1
            inverse -= 1
        #ideme que pour ligne et colonne
        if compt_diag1 == self.taille - 1:
            return self.grille[0][0]    
        if compt_diag2 == self.taille -1:
            return self.grille[0][self.taille-1]    
        return False

            

if __name__ == "__main__":
    grille = Grille(4)
    grille.changer(1,1,"o")
    grille.changer(2,0,"o")
    grille.changer(0,2,"o")
    print(grille)
    print(grille.fini())
