import math  # Importer la bibliothèque math pour utiliser la valeur de pi

# Demande à l'utilisateur de saisir les valeurs de a, b et c, séparées par des espaces
a, b, c = input("Entrez les valeurs de a, b et c, séparées par des espaces : ").split()

# Convertit les valeurs saisies en nombres flottants
a = float(a)
b = float(b)
c = float(c)

# Calcule le volume d'un ellipsoïde en utilisant la formule (4/3) * pi * a * b * c
print("Volume de l'ellipsoïde =", 4/3 * math.pi * a * b * c)

# Note : si vous souhaitez calculer le volume d'un cylindre, utilisez la formule : pi * r^2 * h
# où r est le rayon de la base et h est la hauteur du cylindre.
