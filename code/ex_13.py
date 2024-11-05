# Demande à l'utilisateur de saisir le nombre a
a = int(input("Entrez le nombre de a : "))

# Demande à l'utilisateur de saisir le nombre b
b = int(input("Entrez le nombre de b : "))

# Demande à l'utilisateur de saisir le nombre c
c = int(input("Entrez le nombre de c : "))

# Échange les valeurs de a, b et c
a, b, c = c, a, b

# Affiche les variables après l'échange
print("Variables échangées :", a, b, c)
