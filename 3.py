def addition(num1, num2):
    return num1 + num2

def soustraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2!= 0:
        return num1 / num2
    else:
        raise ValueError("Erreur : Division par zéro")
    

print("Bienvenue dans la calculatrice!")


# Boucle pour trois opérations
for _ in range(3):
    try:
        num = []
        # Demander à l'utilisateur d'entrer deux nombres
        nombre1 = float(input("Entrez le premier nombre : "))
        # Demander à l'utilisateur de choisir l'opération
        choix = input("Entrez l'opération souhaitée (+/-/*//) : ")
        nombre2 = float(input("Entrez le deuxième nombre : "))

        # Vérifier le choix de l'utilisateur et effectuer l'opération correspondante
        if choix == '+':
            resultat = addition(nombre1, nombre2)
        elif choix == '-':
            resultat = soustraction(nombre1, nombre2)
        elif choix == '*':
            resultat = multiplication(nombre1, nombre2)
        elif choix == '/':
            resultat = division(nombre1, nombre2)
        else:
            raise ValueError("Opération non valide")

        # Afficher le résultat
        print("Le résultat est :", resultat)
    except ValueError:
        print("Erreur: Valeur invalide.")

#__________________________________________________________ tout simple 
choix = input ("choisez [+,-,*,/]")

if choix == '*':
    num1 = int(input("Entrer le première nomber: "))
    num2 = int(input("Entrer le duxième nomber: "))      

    total = num1 * num2
    print(f"{num1} * {num2} = {total}")

elif choix == '-':
    num1 = int(input("Entrer le première nomber: "))
    num2 = int(input("Entrer le duxième nomber: "))      
    
    total = num1 - num2
    print(f"{num1} - {num2} = {total}")
elif choix == '+':
    num1 = int(input("Entrer le première nomber: "))
    num2 = int(input("Entrer le duxième nomber: "))      

    total = num1 + num2
    print(f"{num1} + {num2} = {total}")
elif choix == '/':
    num1 = int(input("Entrer le première nomber: "))
    num2 = int(input("Entrer le duxième nomber: "))      

    total = num1 / num2
    print(f"{num1} / {num2} = {total}")
else:
    print("erruer")  

num1 = int(input("Entrer le première nomber: "))
num2 = int(input("Entrer le duxième nomber: "))      

total = num1 + num2
print(f"{num1} + {num2} = {total}")


