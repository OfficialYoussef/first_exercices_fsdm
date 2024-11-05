# Demande à l'utilisateur de saisir le premier nombre
x = float(input("Entrez le nombre : "))

# Demande à l'utilisateur de saisir le deuxième nombre
y = float(input("Entrez le nombre 2 : "))

# Calcule la somme des deux nombres
maxsi = x + y

# Vérifie si l'un des nombres est zéro
if (x == 0) or (y == 0):
    print("Les nombres doivent être différents de zéro, il y a null.")
# Vérifie si la somme est positive et si l'un des nombres est positif
elif (maxsi >= 0) and ((x == abs(x)) or (y == abs(y))):
    print("Les nombres sont positifs.")
else:
    # Si aucune des conditions ci-dessus n'est remplie, les nombres sont négatifs
    print("Les nombres sont négatifs.")
