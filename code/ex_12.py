# Demande à l'utilisateur de saisir le premier nombre
a = int(input("Entrez le nombre de a : "))

# Demande à l'utilisateur de saisir le deuxième nombre
b = int(input("Entrez le nombre de b : "))

# Affiche les options de calcul et demande à l'utilisateur de choisir une opération
c = input("""
Choisissez le type de calcul :
------------------------------
+ : addition
- : soustraction
* : multiplication
/ : division
------------------------------
Type :
""")

# Vérifie l'opération choisie et effectue le calcul correspondant
if c == '+':
    # Effectue l'addition
    print(a + b)
elif c == '-':
    # Effectue la soustraction
    print(a - b)
elif c == '*':
    # Effectue la multiplication
    print(a * b)
elif c == '/':
    # Vérifie si b est zéro pour éviter la division par zéro
    if b == 0:
        print("Division par zéro !")
    else:
        # Effectue la division
        print(a / b)
else:
    # Affiche un message si l'opération n'est pas reconnue
    print("Opération inconnue")
