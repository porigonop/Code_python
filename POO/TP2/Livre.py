#!/usr/bin/env python3
class Livre:
    def __init__(self, titre = '', auteur = '', ISBN = ''):
        """contructeur de la classe Livre
        """
        self.titre = titre
        self.auteur = auteur
        self.ISBN = ISBN

    def __repr__(self):
        """permet de representer un livre comme demandé
        """
        return "Title : " + self.titre + "\nAuthor : " + self.auteur\
            + "\nISBN : " + self.ISBN

    def identique(self, livre):
        """demande si un livre est identique avec le livre sur lequel on fait la methode
        """
        if self.titre == livre.titre:
            if self.auteur == livre.auteur:
                if self.ISBN == livre.ISBN:
                    return True
        return False

class Roman(Livre):
    def __repr__(self):
        """redefinition du __repr__ afin de l'afficher différement
        """
        return "Roman \t----> Titre : "+self.titre +\
            "\n\t----> Autheur : "+ self.auteur+\
            "\n\t----> ISBN : " + self.ISBN
    
if __name__ == "__main__":
    livre_1 = Livre('Paul Klee', 'La pensée créative, vol. 1', '2-249-25012-X')
    roman = Roman('Jules Vernes', 'Vingt milles lieux sous les mers',\
                  '978−29542687−6−7')
    livre_2 = Livre('Paul Klee', 'La pensée créative, vol. 1', '2-249-25012-X')

    for document in [livre_1, roman, livre_2]:
        print(document)
