import math  # Importer la bibliothèque math pour les fonctions mathématiques

# Demande à l'utilisateur de saisir la valeur de R (rayon)
R = float(input("Donnez la valeur de R : "))

# Demande à l'utilisateur de saisir la valeur de θ en degrés
t = float(input("Donnez la valeur de θ (en degrés) : "))

# Demande à l'utilisateur de saisir la valeur de Z (coordonnée en Z)
Z = float(input("Donnez la valeur de Z : "))

# Convertit θ de degrés en radians
t_rand = math.radians(t)

# Boucle pour vérifier la validité de l'angle θ
while True:
    # Demande à l'utilisateur de saisir un angle en radians pour θ
    teatha = float(input("Entrez l'angle θ en radians : "))

    # Vérifie si l'angle θ est dans la plage valide (0, 2π)
    if (teatha <= 0) or (teatha >= 2 * math.pi):
        # Affiche un message d'erreur si θ n'est pas dans la plage [0, 2π]
        print(f"""Erreur : θ doit être dans l'intervalle [0, 2π]
Les coordonnées du point sont : x = {R * math.cos(t_rand)}, y = {R * math.sin(t_rand)}, z = {Z}
""")
