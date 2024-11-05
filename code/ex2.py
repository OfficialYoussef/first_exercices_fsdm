try:
    # Demande à l'utilisateur de saisir cinq notes, séparées par des espaces
    note1, note2, note3, note4, note5 = input("Entrez les cinq notes séparées par des espaces : ").split()
    
    # Demande à l'utilisateur de saisir cinq coefficients, séparés par des espaces
    coefficients1, coefficients2, coefficients3, coefficients4, coefficients5 = input("Entrez les cinq coefficients séparés par des espaces : ").split()
    
    # Convertit les notes et les coefficients en nombres flottants
    note1, note2, note3, note4, note5 = float(note1), float(note2), float(note3), float(note4), float(note5)
    coefficients1, coefficients2, coefficients3, coefficients4, coefficients5 = float(coefficients1), float(coefficients2), float(coefficients3), float(coefficients4), float(coefficients5)
    
    # Calcule la moyenne pondérée en utilisant la formule : somme des (note * coefficient) / somme des coefficients
    moyenne = (note1 * coefficients1 + note2 * coefficients2 + note3 * coefficients3 + note4 * coefficients4 + note5 * coefficients5) / (coefficients1 + coefficients2 + coefficients3 + coefficients4 + coefficients5)
    
    # Affiche la moyenne pondérée
    print("La moyenne pondérée est :", moyenne)

except ValueError:
    # Affiche un message d'erreur si l'utilisateur n'entre pas exactement cinq notes et cinq coefficients
    print("Erreur : Vous devez entrer cinq notes et cinq coefficients.")
