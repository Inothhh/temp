# Creation des classes et des objets en Python 

class Animal:
    def __init__(self, poids, taille):
        self.__poids = poids
        self.__taille = taille

    def Se_deplacer(self):
        print("L'Animal se déplace")

    def get_poids(self):
        return self.__poids
    
    def get_taille(self):
        return self.__taille
    
    def set_poids(self, poids):
        if poids > 0:
            self.__poids = poids
        else:
            print("Le poids doit être supérieur à 0")

    def set_taille(self, taille):
        if taille > 0:
            self.__taille = taille
        else:
            print("La taille doit être supérieure à 0")

    def __str__(self):
        return f"Poids : {self.__poids} kg, Taille : {self.__taille} m"
    
    def __gt__(self, other):
        return self.__poids > other.__poids
    
    def __lt__(self, other):
        return self.__poids < other.__poids
    
    def __eq__(self, other):
        return self.__poids == other.__poids
        


class Serpent(Animal):
    def __init__(self, poids, taille):
        super().__init__(poids, taille)

    def Se_deplacer(self):
        print("Le serpent se déplace en rampant")

class Oiseau(Animal):
    def __init__(self, poids, taille, altitude_max):
        super().__init__(poids, taille)
        self.altitude_max = altitude_max
    
    def Se_deplacer(self):
        print("L'Oiseau se déplace en volant")

    def Altitude_max(self):
        return self.altitude_max
    
    def set_altitude_max(self, altitude_max):
        if altitude_max > 0:
            self.altitude_max = altitude_max
        else:
            print("L'altitude doit être supérieure à 0")
    
    def get_altitude_max(self):
        return self.altitude_max
    

    

    
    
class Zoo:
    def __init__(self):
        self.liste_animaux = []
    
    def ajouter_animal(self, animal):
        self.liste_animaux.append(animal)

    def afficher_animaux(self):
        for animal in self.liste_animaux:
            print(animal)
    
    def suprimer_animal(self, animal):
        self.liste_animaux.remove(animal)

    def get_animaux(self):
        return self.liste_animaux
    
    def set_animaux(self, liste_animaux):
        self.liste_animaux = liste_animaux

    
    
    
# Programme principal
if __name__ == "__main__":
    # Animal1 = Animal(10, 1)
    # Animal1.Se_deplacer()
    # print("Taille de l'animal : ", Animal1.get_taille())
    # print("Poids de l'animal : ", Animal1.get_poids())
    # Serpent1 = Serpent(2, 0.5)  
    # Serpent1.Se_deplacer()
    # print("Taille du serpent : ", Serpent1.get_taille())
    # print("Poids du serpent : ", Serpent1.get_poids())
    # Oiseau1 = Oiseau(1, 0.1, 1000)
    # Oiseau1.Se_deplacer()
    # print("Taille de l'oiseau : ", Oiseau1.get_taille())
    # print("Poids de l'oiseau : ", Oiseau1.get_poids())
    # print("Altitude maximale de l'oiseau : ", Oiseau1.Altitude_max())
    # Animal1.set_poids(20)
    # print("Poids modifié de l'animal : ", Animal1.get_poids())
    # Serpent1.set_taille(1)
    # print("Taille modifié du serpent : ", Serpent1.get_taille())
    # Oiseau1.set_poids(2)
    # print("Poids modifié de l'oiseau : ", Oiseau1.get_poids())

    # Zoo1 = Zoo()
    # Zoo1.ajouter_animal(Animal1)
    # Zoo1.ajouter_animal(Serpent1)
    # Zoo1.ajouter_animal(Oiseau1)
    # Zoo1.afficher_animaux()
    # Zoo1.suprimer_animal(Animal1)
    # Zoo1.afficher_animaux()

    # Zoo1.ajouter_animal(Oiseau(2, 0.2, 2000))
    # Zoo1.ajouter_animal(Oiseau(3, 0.3, 3000))
    
    ani = Animal(10, 1)
    ser = Serpent(2, 0.5)
    ois = Oiseau(1, 0.1, 1000)
    ois2 = Oiseau(2, 0.2, 2000)
    Zoo1 = Zoo()
    Zoo1.ajouter_animal(ani)
    Zoo1.ajouter_animal(ser)
    Zoo1.ajouter_animal(ois)
    Zoo1.ajouter_animal(ois2)
    Zoo1.afficher_animaux()
    print("Comparaison de poids : ", ois > ois2)
    print("Comparaison de poids : ", ois < ois2)
    print("Comparaison de poids : ", ois == ois2)




