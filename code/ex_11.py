# Demande à l'utilisateur de saisir une valeur en secondes
valeur = int(input("Écrire le nombre de secondes : "))

# Calcule le nombre de minutes à partir des secondes
min = valeur // 60  # Division entière pour obtenir les minutes
sec = valeur % 60   # Reste de la division pour obtenir les secondes

# Calcule le nombre d'heures à partir des minutes
hr = min // 60      # Division entière pour obtenir les heures
min = min % 60      # Reste de la division pour obtenir les minutes restantes

# Affiche le résultat au format heures, minutes et secondes
print(f"Heures : {hr} hr\nMinutes : {min} min\nSecondes : {sec} sec")
