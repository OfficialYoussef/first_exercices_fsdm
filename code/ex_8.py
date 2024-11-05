# Demande à l'utilisateur de saisir une note
note = float(input("Écrivez la note : "))

# Vérifie si la note est dans la plage valide de 0 à 20
if (note >= 0) and (note <= 20):
    # Si la note est supérieure ou égale à 10, elle est considérée comme valide
    if note >= 10:
        print("La note est valide.")
    else:
        # Si la note est inférieure à 10, elle est considérée comme non valide
        print("La note n'est pas valide.")
else:
    # Si la note n'est pas dans la plage de 0 à 20, affiche un message d'erreur
    print("La note doit être entre 0 et 20.")
