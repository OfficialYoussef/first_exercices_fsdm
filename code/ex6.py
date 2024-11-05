# Demande à l'utilisateur de saisir un nombre réel
x = float(input("Entrez un nombre réel : "))

# Convertit le nombre réel en entier (troncature)
X = int(x)

# Vérifie si la partie décimale de x est supérieure ou égale à 0.5
if (x - X) >= 0.5:
    # Si oui, affiche le nombre entier arrondi vers le haut
    print("x =", X + 1)
else:
    # Sinon, affiche le nombre entier arrondi vers le bas
    print("x =", X)
