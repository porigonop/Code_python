#!/usr/bin/env python3
#Lievre Antoine
class SacADos:
    """ Classe représentant un sac à dos

    :Attribut poids_maximum: de type float, représente le 
    poids maximum supporté par le sac en kilogrammes.

    :Attribut nombre_maximum: de type int, représente le nombre 
    maximum d'items pouvant être ajoutés dans le sac.

    :Attribut poids_actuel: de type float, représente le poids actuel 
    contenu par le sac en kilogrammes.

    :Attribut nombre_actuel: de type int, représente le nombre 
    d'items actuellement dans le sac.
    """

    def __init__(self, poids_maximum=1000.0, nombre_maximum=10):
        """ Constructeur de la classe
        
        :Param poids_maximum: de type float, servant à connaitre 
        le poids maximum que le sac peux transporter

        :Param nombre_maximum: de type int, servant à connaitre 
        le nombre d'item maximum que le sac peux transporter
        """
        self.poids_maximum = poids_maximum
        self.nombre_maximum = nombre_maximum

        self.poids_actuel = 0.0
        self.nombre_actuel = 0
        
    def incrementer_nombre(self):
        """
        ajoute un item au nombre actuel d'item
        """
        self.nombre_actuel += 1
        
    def ajouter_item(self, poids):
        """ Ajoute un item pesant 'poids' kilogrammes au contenu du sac.

            Retourne le booléen True si l'ajout est effectif
            Retourne le booléen False si l'ajout est impossible
        """
        if self.nombre_actuel != self.nombre_maximum \
           and self.poids_actuel+poids <= self.poids_maximum:
            
            self.incrementer_nombre()
            self.poids_actuel += poids
            return True
        
        return False
    
    def __repr__(self):
        """ donne une representation du sac avec le nombre d'item
            contenue ainsi que le poids de tous les items
        """
        return "le sac contient " +str(self.nombre_actuel) + \
            " et pèse " + str(self.poids_actuel) + " kilogrammes."

    def plus_lourd_que(self, sac_2):
        """
        permet de comparer la sac actuel et le sac mis en argument, 
        si le sac actuel est plus lours, renvoie True, 
        sinon renvoie False
        """
        if self.poids_actuel > sac_2.poids_actuel:
            return True
        return False
    
if __name__ == "__main__":
    sac_1 = SacADos(500.0, 10)
    sac_1.ajouter_item(100.1)
    sac_1.ajouter_item(50.5)
    sac_1.ajouter_item(300.0)
    sac_2 = SacADos(600.0, 10)
    sac_2.ajouter_item(300.52)
    print(sac_2.plus_lourd_que(sac_1))
    print(sac_1.plus_lourd_que(sac_2))
    print(sac_1.plus_lourd_que(sac_1))
    
    print(sac_1) # pareil que print(sac_1.__repr__())
