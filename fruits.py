
def ajoute1(stock, fruit):
    """Ajoute 1 fruit au stock et renvoie le nouveau stock sans modifier l'original."""
    nouveau_stock = stock.copy()
    nouveau_stock[fruit] = nouveau_stock.get(fruit, 0) + 1
    return nouveau_stock

def enleve1(stock, fruit):
    """Enlève 1 fruit du stock si possible, sinon affiche une erreur."""
    if stock.get(fruit, 0) == 0:
        print(f"Erreur: Quantité insuffisante de {fruit}")
        return stock
    nouveau_stock = stock.copy()
    if nouveau_stock[fruit] == 1:
        del nouveau_stock[fruit]
    else:
        nouveau_stock[fruit] -= 1
    return nouveau_stock

def ajoute(stock, fruit, q):
    """Ajoute une quantité q du fruit au stock."""
    nouveau_stock = stock.copy()
    nouveau_stock[fruit] = nouveau_stock.get(fruit, 0) + q
    return nouveau_stock

def enleve(stock, fruit, q):
    """Enlève une quantité q du fruit du stock si possible, sinon affiche une erreur."""
    if stock.get(fruit, 0) < q:
        print(f"Erreur: Quantité insuffisante de {fruit}")
        return stock
    nouveau_stock = stock.copy()
    if nouveau_stock[fruit] == q:   
        del nouveau_stock[fruit]
    else:
        nouveau_stock[fruit] -= q
    return nouveau_stock

def apres_livraison(stock, livraison):
    """Met à jour le stock en ajoutant les quantités de la livraison."""
    nouveau_stock = stock.copy()
    for fruit, quantite in livraison.items():
        nouveau_stock[fruit] = nouveau_stock.get(fruit, 0) + quantite
    return nouveau_stock

def commande(stock, stock_voulu):
    """Renvoie la commande nécessaire pour atteindre le stock voulu."""
    return {fruit: stock_voulu[fruit] - stock.get(fruit, 0) 
            for fruit in stock_voulu 
            if stock.get(fruit, 0) < stock_voulu[fruit]}

def total(stock):
    """Renvoie le nombre total de fruits présents dans le stock."""
    return sum(stock.values())

def quantite(stock, fruits_a_compter):
    """Renvoie la quantité totale de fruits présents dans la liste fruits_a_compter."""
    return sum(stock.get(fruit, 0) for fruit in fruits_a_compter)

def quantite_agrumes(stock):
    """Renvoie la quantité totale d'agrumes présents dans le stock."""
    agrumes = {"orange", "citron", "mandarine", "clementine", "pamplemousse"}
    return sum(stock.get(fruit, 0) for fruit in agrumes)

if __name__=="__main__":

    # Exemple de stock
    stock = {'pomme': 2, 'banane': 6}

    # Test des fonctions

    # Ajouter un fruit
    print(ajoute1(stock, 'pomme'))  # {'pomme': 3, 'banane': 6}
    print(ajoute1(stock, 'poire'))  # {'pomme': 2, 'banane': 6, 'poire': 1}

    # Enlever un fruit
    print(enleve1(stock, 'pomme'))  # {'pomme': 1, 'banane': 6}
    print(enleve1(stock, 'poire'))  # Affiche "Erreur: quantité insuffisante de poire" et renvoie {'pomme': 2, 'banane': 6}

    # Ajouter une quantité de fruits
    print(ajoute(stock, 'pomme', 5))  # {'pomme': 7, 'banane': 6}
    print(ajoute(stock, 'poire', 4))  # {'pomme': 2, 'banane': 6, 'poire': 4}

    # Enlever une quantité de fruits
    print(enleve(stock, 'pomme', 2))  # {'banane': 6}
    print(enleve(stock, 'banane', 10))  # Affiche "Erreur: quantité insuffisante de banane" et renvoie {'pomme': 2, 'banane': 6}

    # Après une livraison
    print(apres_livraison(stock, {'peche': 4, 'pomme': 5}))  # {'pomme': 7, 'banane': 6, 'peche': 4}

    # Commande à passer
    print(commande(stock, {'pomme': 15, 'orange': 20}))  # {'pomme': 13, 'orange': 20}
    print(commande(stock, {'pomme': 10, 'banane': 4}))  # {'pomme': 8}

    # Total des fruits
    print(total(stock))  # 8

    # Quantité des fruits d'une liste
    print(quantite(stock, ['pomme', 'citron', 'poire']))  # 2

    # Quantité des agrumes
    stock_bis = {'pomme': 15, 'peche': 4, 'citron': 3, 'orange': 20}
    print(quantite_agrumes(stock_bis))  # 23