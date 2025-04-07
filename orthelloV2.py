import numpy as np

# ==============================
# Classe du plateau de jeu (Grid)
# ==============================
class Grid:
    def initialiser_matrice(self):
        # Plateau 8x8 vide (cases représentées par '🟩')
        matrice = np.full((8, 8), '🟩', dtype=str)

        # Position initiale selon les règles du jeu Othello
        matrice[3][3] = '⚪'
        matrice[3][4] = '⚫'
        matrice[4][3] = '⚫'
        matrice[4][4] = '⚪'

        return matrice 
    
    def afficher_matrice(self, matrice):
        numeros_colonnes = "  " + " ".join(["0️⃣", "1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣"])
        print(numeros_colonnes)
        
        for i in range(8):
            print(f"{i}️⃣", end=" ")
            for j in range(8):
                print(matrice[i][j], end="")
            print()

# ==============================
# Classe Pion
# ==============================
class Pion:
    def __init__(self, couleur):
        self.couleur = couleur

    def get_couleur(self):
        return self.couleur

    def set_couleur(self, couleur):
        self.couleur = couleur

    def retourner(self):
        if self.couleur == '⚫':
            self.couleur = '⚪'
        else:
            self.couleur = '⚫'

# ==============================
# Classe Partie (Logique du jeu)
# ==============================
class Partie:
    # Directions possibles (8 directions)
    DIRECTIONS = [
        (-1, 0), (1, 0),  # Haut, Bas
        (0, -1), (0, 1),  # Gauche, Droite
        (-1, -1), (-1, 1), # Diagonale Haut-Gauche, Haut-Droite
        (1, -1), (1, 1)    # Diagonale Bas-Gauche, Bas-Droite
    ]

    def __init__(self):
        self.joueur = '⚫'  # Joueur noir commence
        self.fin = False
        self.grille = Grid()
        self.matrice = self.grille.initialiser_matrice()
        self.grille.afficher_matrice(self.matrice)

    # Vérifie si un coup est possible
    def coup_possible(self, x, y):
        return self.matrice[x][y] == '🟩'

    # Vérifie si un coup est valide (avec prise en sandwich)
    def coup_valide(self, x, y):
        if not self.coup_possible(x, y):
            return False

        adversaire = '⚪' if self.joueur == '⚫' else '⚫'

        for dx, dy in self.DIRECTIONS:
            i, j = x + dx, y + dy
            if 0 <= i < 8 and 0 <= j < 8 and self.matrice[i][j] == adversaire:
                while 0 <= i < 8 and 0 <= j < 8:
                    i += dx
                    j += dy
                    if not (0 <= i < 8 and 0 <= j < 8):
                        break
                    if self.matrice[i][j] == '🟩':
                        break
                    if self.matrice[i][j] == self.joueur:
                        return True
        return False

    # Retourne les pions adverses pris en sandwich
    def retourner_pions(self, x, y):
        adversaire = '⚪' if self.joueur == '⚫' else '⚫'
        for dx, dy in self.DIRECTIONS:
            temp_positions = []
            i, j = x + dx, y + dy
            while 0 <= i < 8 and 0 <= j < 8 and self.matrice[i][j] == adversaire:
                temp_positions.append((i, j))
                i += dx
                j += dy
            if 0 <= i < 8 and 0 <= j < 8 and self.matrice[i][j] == self.joueur:
                for (a, b) in temp_positions:
                    self.matrice[a][b] = self.joueur

    # Vérifie si la partie est terminée
    def partie_finie(self):
        for i in range(8):
            for j in range(8):
                if self.matrice[i][j] == '🟩' and (self.coup_valide(i, j)):
                    return False
        return True

    # Vérifie si la partie est nulle (plateau plein)
    def partie_nulle(self):
        return '🟩' not in self.matrice

    # Affiche le score
    def afficher_score(self):
        score_noir = np.count_nonzero(self.matrice == '⚫')
        score_blanc = np.count_nonzero(self.matrice == '⚪')
        print(f"⚫ Score Noir : {score_noir} | ⚪ Score Blanc : {score_blanc}")

    # Jouer un tour
    def jouer(self):
        while not self.fin:
            print(f"\n🎯 C'est au tour du joueur {self.joueur}")
            try:
                x = int(input("Entrez la ligne : "))
                y = int(input("Entrez la colonne : "))

                if self.coup_valide(x, y):
                    self.matrice[x][y] = self.joueur
                    self.retourner_pions(x, y)
                    self.grille.afficher_matrice(self.matrice)
                    self.joueur = '⚪' if self.joueur == '⚫' else '⚫'
                else:
                    print("❌ Coup invalide, réessayez.")
            except ValueError:
                print("❌ Entrée invalide, veuillez entrer des nombres.")
            except IndexError:
                print("❌ Les coordonnées sont hors limites.")

            # Vérifier les conditions de fin de partie
            if self.partie_finie():
                print("\n🏁 La partie est terminée !")
                self.afficher_score()
                self.fin = True
            elif self.partie_nulle():
                print("\n🔷 La partie est nulle, plateau plein !")
                self.afficher_score()
                self.fin = True


# ==============================
# Programme principal
# ==============================
if __name__ == "__main__":
    partie = Partie()
    partie.jouer()
