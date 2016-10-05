#!/usr/bin/env python3
class ID:
    #numero maximal de tout les IDs permet de savoir le plus haut ID donné
    numero_max = 0
    
    def __init__(self):
        """constructeur de la classe ID à l'aide du numero max
        """
        ID.numero_max += 1
        self.ID = ID.numero_max
    def getId(self):
        """methode permettant d'afficher l'ID de la personne
        """
        print(self.ID)
        
    def getIdMax(self):
        """methode permettant de récupérer l'ID max attribué
        """
        print(ID.numero_max)
        
if __name__ == "__main__":
    id_1 = ID()
    id_1.getId()
    id_2 = ID()
    id_3 = ID()
    id_2.getIdMax()
