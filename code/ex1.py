import math
# Demande à l'utilisateur de saisir la valeur de a et la convertit en nombre à virgule flottante
a = float(input("Entrez la valeur de a :"))

# Demande à l'utilisateur de saisir la valeur de b et la convertit en nombre à virgule flottante
b = float(input("Entrez la valeur de b :"))

# Demande à l'utilisateur de saisir la valeur de r et la convertit en nombre à virgule flottante
r = float(input("Entrez la valeur de r :"))

# Calcule le périmètre du rectangle en utilisant les valeurs de a et b
print("Le périmètre du rectangle de côtés a et b est :", 2 * (a + b))

# Calcule la circonférence du cercle en utilisant la valeur de r
print("\nLa circonférence du cercle de rayon r est :", 2 * math.pi * r)
