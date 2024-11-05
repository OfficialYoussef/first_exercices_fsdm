# Demande à l'utilisateur de saisir un premier nombre réel
number = float(input("Entrez un nombre réel 1 : "))

# Demande à l'utilisateur de saisir un deuxième nombre réel
number_2 = float(input("Entrez un nombre réel 2 : "))

# Calcule la valeur absolue du premier nombre
absolute_value = abs(number)

# Calcule la valeur absolue du deuxième nombre
absolute_value_1 = abs(number_2)

# Affiche les valeurs absolues des deux nombres
print("La valeur absolue de {} est : {}\nLa valeur absolue de {} est : {}".format(number, absolute_value, number_2, absolute_value_1))
