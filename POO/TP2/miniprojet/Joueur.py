#!/usr/bin/env python3
class Joueur:
    def __init__(self, nom):
        """constructeur de la classe joueur
        """
        try:
            self.nom = str(nom)
        except:
            print("errreur pas de nom, vous serez nommé toto")
            self.nom = "toto"
        self.piece = None
        
    def joue(self):
        """renvoie une postion x, y et la demande tant qu'elle n'est pas bonne exit pour quitter.
        """
        while 1:
            try:
                a =input("quelle position jouer ? x x ")
                #condition pour quitter le jeu
                if a == 'exit':
                    return None
                #separer les deux partis du domino
                a = a.split(" ")
                for i in range(len(a)):
                    a[i] = int(a[i])
                
                return a
            except:
                print("veuillez entrer une position valide")
    def __repr__(self):
        """represent le joueur avec son nom.
        """
        return "joueur : " + self.nom
