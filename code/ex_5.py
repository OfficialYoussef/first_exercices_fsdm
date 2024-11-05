import math  # Importer la bibliothèque math pour les fonctions mathématiques

# Demande à l'utilisateur de saisir la valeur de ρ (distance du point à l'origine)
rho = float(input("Entrez la valeur de ρ : "))

# Demande à l'utilisateur de saisir la valeur de θ (angle azimutal)
theta = float(input("Entrez la valeur de θ (en radians) : "))

# Demande à l'utilisateur de saisir la valeur de φ (angle polaire)
phi = float(input("Entrez la valeur de φ (en radians) : "))

# Calcule les coordonnées cartésiennes (x, y, z) à partir des coordonnées sphériques (ρ, θ, φ)
x = rho * math.cos(phi) * math.cos(theta)  # Coordonnée x
y = rho * math.sin(phi) * math.sin(theta)  # Coordonnée y
z = rho * math.sin(phi)                     # Coordonnée z

# Vérifie si φ et θ sont dans les intervalles valides
if (-(math.pi / 2) <= phi <= (math.pi / 2)) and (-(math.pi) <= theta <= (math.pi)):
    # Affiche les coordonnées x, y, z si les angles sont valides
    print(f"Axe x : {x}, Axe y : {y}, Axe z : {z}")
else:
    # Affiche un message d'erreur si les angles sont en dehors des intervalles valides
    print("Erreur : θ ou φ est en dehors des intervalles valides.")
