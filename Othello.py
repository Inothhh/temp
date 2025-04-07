

# Jeu de Othello


import numpy as np

class grid : 
    def initialiser_matrice(self):
        # Plateau 8x8 vide (cases représentées par '-')
        matrice = np.full((8, 8), '🟩', dtype=str)

        matrice[3][3] = '⚪'
        matrice[3][4] = '⚫'
        matrice[4][3] = '⚫'
        matrice[4][4] = '⚪'

        return matrice 
    

    def afficher_matrice(self, matrice):
        for i in range(8):
            for j in range(8):
                print(matrice[i][j], end=" ")
            print()

class pion:
    def __init__(self, couleur):
        self.couleur = couleur

    def get_couleur(self):
        return self.couleur

    def set_couleur(self, couleur):
        self.couleur = couleur

    def __str__(self):
        return self.couleur

    def __repr__(self):
        return self.couleur
    
    def retourner(self):
        if self.couleur == '⚫':
            self.couleur = '⚪'
        else:
            self.couleur = '⚫'

class partie:
    # Initialisation de la partie
    # Joeur noir commence
    def __init__(self):
        self.joueur = '⚫'
        self.fin = False
        self.grille = grid()
        self.matrice = self.grille.initialiser_matrice()
        self.grille.afficher_matrice(self.matrice)

    def jouer(self):
        while not self.fin:
            print("C'est au tour du joueur", self.joueur)
            x = int(input("Entrez la ligne : "))
            y = int(input("Entrez la colonne : "))
            self.matrice[x][y] = self.joueur
            self.grille.afficher_matrice(self.matrice)
            self.joueur = '⚪' if self.joueur == '⚫' else '⚫'

    # verifier si un coup est possible
    def coup_possible(self, x, y):
        if self.matrice[x][y] == '🟩':
            return True
        return False
    
    # verifier si un coup est valide
    def coup_valide(self, x, y):
        if self.coup_possible(x, y):
            return True
        return False
    
    # verifier si un coup est gagnant
    def coup_gagnant(self):
        pass

    # verifier si la partie est finie
    def partie_finie(self):
        pass

    # verifier si la partie est nulle
    def partie_nulle(self):
        pass

    # verifier si un coup est valide
    def coup_valide(self):
        pass
    






# Programme principal
