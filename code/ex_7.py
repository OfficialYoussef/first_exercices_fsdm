# Demande à l'utilisateur de saisir quatre nombres a, b, c et d, séparés par des espaces
x_1, x_2, x_3, x_4 = input("Écrivez un nombre a, b, c et d : ").split()

# Convertit les valeurs saisies en flottants
x_1, x_2, x_3, x_4 = float(x_1), float(x_2), float(x_3), float(x_4)

# Calcule la valeur maximale parmi les quatre nombres
max_valeur = max(x_1, x_2, x_3, x_4)

# Calcule la valeur minimale parmi les quatre nombres
min_valeur = min(x_1, x_2, x_3, x_4)

# Affiche la valeur maximale et la valeur minimale
print("Maximum : {}\nMinimum : {}".format(max_valeur, min_valeur))
