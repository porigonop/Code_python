#!/usr/bin/env python3



class Domino:
    """ Classe representant un domino

    :Attribut gauche: de type int, representant le nb de point a gauche
    :Attribut droite: de type int, representant le nb de point a droite
    """

    def __init__(self, gauche, droite):
        """ constructeur, il possede 2 parametres (plus le self)
        cette classe possede 2 attributs, ils representent les deux
        parties du domino et ils sont només "gauche" et "droite"
        ---------------
        | *  * | *  * |
        |gauche|droite|
        | *  * | *  * |
        ---------------
        ici gauche = 4 et droite = 4

        :Param gauche: de type int, servant à savoir le nombre de point
        à gauche
        :Param droite: de type int, servant à savoir le nombre de point
        à droite
        """

        self.gauche = gauche
        self.droite = droite


    def __repr__(self):
        """ 
        cette methode permet de récupérer la chaine de caractére 
        représentant le domino
        """

        return str(self.gauche) + "|" + str(self.droite)


    def affiche(self):
        """ 
        cette fonction permet d'afficher le domino, ne faisant que 
        l'afficher, et ne permet pas de le récupérer
        """

        print(self.__repr__())


    def retourne(self):
        """ 
        retourne permet d'inverser le coter droite et gauche du domino,
        visuellement, cela reviens a retourner le domino.
        """

        tmp = self.droite
        self.droite = self.gauche
        self.gauche = tmp

    def est_le_meme_que(self, domino):
        """ 
        
        :Param un domino: de type domino
        est_le_même_que permet de voir si le domino que l'ont observe 
        est le même que le domino mis en entré, si il a été retourné 
        ou non.
        """

        sans_retournement = self.gauche == domino.gauche and self.droite == \
                            domino.droite
        avec_retournement = self.gauche == domino.droite and self.droite == \
                            domino.gauche
        if avec_retournement:
            domino.retourne()
        return sans_retournement or avec_retournement

#Exercice 2 :
#1/ ce programe crée un domino, il nous montre qu'il l'as bien crée
#puis le retourne pour ensuite l'afficher et nous montrer qu'il est
#bien retourné
#2/
if __name__ == "__main__":
    D_1 = Domino(3,6)
    D_1.affiche()
    print("Domino 1 :", D_1)
    D_2 = Domino(1,6)
    D_2.affiche()
    D_2.retourne()
    print("le domino 2 a été retourne")
    D_2.affiche()
    D_3 = Domino(3,6)
    print("domino 3 : ", D_3)
    print(D_1.est_le_meme_que(D_3))
    #Exercice 3 :
    print(help(Domino))
    # 2/ self represente le domino lui même, il n'est pas obligatoire
    # et si il n'est pas présent on appelle la methode une méthode
    #static
    
