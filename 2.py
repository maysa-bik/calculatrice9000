# Demander le première nombre
num1 = float(input("Entrez le premier nombre: "))
# Demander le type d'opération
operation = input("Entrez le type d'opération (+, -, *, /): ")
# Demander le duxième nomber
num2 = float(input("Entrez le second nombre: "))



# Calculer le résultat
if operation == "+":
    resultat = num1 + num2
elif operation == "-":
    resultat = num1 - num2
elif operation == "*":
    resultat = num1 * num2
elif operation == "/":
    if num2 == 0:
        print("Erreur: Division par zéro.")
    else:
        resultat = num1 / num2
else:
    print("Erreur: Opération invalide.")

# Afficher le résultat
if operation in ["+", "-", "*", "/"]:
    print("Résultat: ", resultat)