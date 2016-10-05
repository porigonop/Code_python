class CompteBancaire:
    """ Classe représentant un compte bancaire

    :Attribut titulaire: de type String, représentant le nom du titulaire du 
    compte
    :Attribut solde: de type float, représentant la somme disponible sur le 
    compte
    """

    def __init__(self, nom_titulaire = 'George_Charpak', solde_initial = 1000):
        """ Constructeur de la classe
        
        :Param nom_titulaire: de type String, sérvant à nommer le titulair ;
        par defaut, George_Charpack
        :Param solde_initial: de type float, sérvant à répresenter l'argent ;
        par défaut, 1000
        """
        self.titulaire = nom_titulaire
        self.solde = solde_initial

    def depot(self, somme):
        """ Param self: de type CompteBancaire, represente l'objet instancie
        Param somme: de type float, represente le montant ajoute au compte   
        """
        if somme > 0:
            self.solde += somme
        else: print("erreur de requete: votre depot est négatif")

    def retrait(self,somme):
        """ Param self: de type CompteBancaire, répresente l'objet instancie
        Param somme: de type float, répresente le montant retire au compte   
        """
        if somme > 0 and (self.solde - somme) > 0 : self.solde -= somme
        else: print("vous ne pouvez pas effectuer ce retrait") 

    def affiche(self):
        """ affiche le nom du compte bancaire ainsi que son montant
        Param: self
        """
        print("Le solde du compte bancaire de " + self.titulaire + " est de " \
              + str(self.solde))

    def virement(self, compte, somme):
        """permet d'effectuer un virement de
        somme du compte courant vers le compte"""
        self.retrait(somme)
        compte.depot(somme)


        
if __name__ == "__main__":
    compte1 = CompteBancaire("Institut_Villebon", 1000000.1)
    compte1.retrait(10000)
    compte1.affiche()
    compte2 = CompteBancaire()
    compte2.depot(9000)
    compte2.affiche()
    compte1.virement(compte2, 5000)
    compte1.affiche()
    compte2.affiche()
