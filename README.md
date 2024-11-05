# first_exercices_fsdm
### first page
![WhatsApp Image 2024-11-05 at 16 40 45](https://github.com/user-attachments/assets/f25ab364-06d5-47a1-b9e2-f4a17313c6d2)
### second page
![WhatsApp Image 2024-11-05 at 16 43 53](https://github.com/user-attachments/assets/57b7cdcf-cec7-4c7d-94ef-07d405120652)
### third page
![WhatsApp Image 2024-11-05 at 16 36 29(2)](https://github.com/user-attachments/assets/1b66ff8e-8ee2-467b-be53-c92453ccbe3a)
# Exercice 1: Calculer le périmètre d'un rectangle et d'un cercle
1. Demander à l'utilisateur d'entrer la valeur de `a`.
2. Demander à l'utilisateur d'entrer la valeur de `b`.
3. Demander à l'utilisateur d'entrer la valeur de `r`.
4. Calculer le périmètre du rectangle : `P_rectangle = 2 * (a + b)`.
5. Calculer le périmètre du cercle : `P_cercle = 2 * π * r`.
6. Afficher `P_rectangle` et `P_cercle`.

# Exercice 2: Calculer la moyenne pondérée des notes
1. Demander à l'utilisateur d'entrer cinq notes et leurs coefficients respectifs.
2. Convertir les entrées en nombres flottants.
3. Calculer la moyenne pondérée : 
   \[
   \text{moyenne} = \frac{(note1 \times coefficient1) + (note2 \times coefficient2) + ... + (note5 \times coefficient5)}{coefficient1 + coefficient2 + ... + coefficient5}
   \]
4. Afficher la moyenne.
5. Gérer les erreurs de saisie en affichant un message d'erreur si nécessaire.

# Exercice 3: Calculer le volume d'un ellipsoïde
1. Demander à l'utilisateur d'entrer les valeurs de `a`, `b` et `c`.
2. Calculer le volume : 
   \[
   \text{volume} = \frac{4}{3} \times π \times a \times b \times c
   \]
3. Afficher le volume.

# Exercice 4: Coordonnées d'un point en coordonnées cylindriques
1. Demander à l'utilisateur d'entrer la valeur de `R`, `theta` et `Z`.
2. Convertir `theta` en radians.
3. Utiliser une boucle pour demander une longueur `teatha`.
4. Vérifier si `teatha` est dans l'intervalle `[0, 2π]` :
   - Si non, afficher les coordonnées : 
     \[
     (R \times \cos(t), R \times \sin(t), Z)
     \]

# Exercice 5: Conversion des coordonnées sphériques en coordonnées cartésiennes
1. Demander à l'utilisateur d'entrer `rho`, `theta`, et `phi`.
2. Calculer les coordonnées cartésiennes :
   \[
   x = \rho \times \cos(\phi) \times \cos(\theta)
   \]
   \[
   y = \rho \times \sin(\phi) \times \sin(\theta)
   \]
   \[
   z = \rho \times \sin(\phi)
   \]
3. Vérifier que `phi` et `theta` sont dans les intervalles valides et afficher les résultats.

# Exercice 6: Arrondir un nombre
1. Demander à l'utilisateur d'entrer un nombre réel `x`.
2. Convertir `x` en entier `X`.
3. Vérifier si la partie décimale de `x` est supérieure ou égale à 0.5 :
   - Si oui, afficher `X + 1`.
   - Sinon, afficher `X`.

# Exercice 7: Trouver le maximum et le minimum parmi quatre nombres
1. Demander à l'utilisateur d'entrer quatre nombres.
2. Convertir les entrées en nombres flottants.
3. Calculer le maximum et le minimum.
4. Afficher les résultats.

# Exercice 8: Validation d'une note
1. Demander à l'utilisateur d'entrer une note.
2. Vérifier si la note est entre 0 et 20 :
   - Si oui et >= 10, afficher que la note est valide.
   - Sinon, afficher que la note n'est pas valide.

# Exercice 9: Calculer la valeur absolue de deux nombres
1. Demander à l'utilisateur d'entrer deux nombres réels.
2. Calculer et afficher la valeur absolue de chaque nombre.

# Exercice 10: Analyser deux nombres
1. Demander à l'utilisateur d'entrer deux nombres.
2. Calculer la somme des deux nombres.
3. Vérifier si l'un des nombres est égal à zéro et afficher un message approprié.
4. Vérifier si les deux nombres sont positifs et afficher un message.

# Exercice 11: Conversion de secondes en heures, minutes et secondes
1. Demander à l'utilisateur d'entrer un nombre de secondes.
2. Calculer les heures, minutes et secondes.
3. Afficher le résultat.

# Exercice 12: Calcul de base
1. Demander à l'utilisateur d'entrer deux nombres `a` et `b`.
2. Demander à l'utilisateur de choisir une opération (addition, soustraction, multiplication, division).
3. Exécuter l'opération choisie et afficher le résultat, en gérant les erreurs de division par zéro.

# Exercice 13: Échanger les valeurs de trois variables
1. Demander à l'utilisateur d'entrer trois nombres `a`, `b`, `c`.
2. Échanger les valeurs : `a`, `b`, `c` deviennent respectivement `c`, `a`, `b`.
3. Afficher les valeurs échangées.

