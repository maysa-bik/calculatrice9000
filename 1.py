def evaluer_expression(operateur, nombre):
    if operateur == '+':
        return resultat + nombre
    elif operateur == '-':
        return resultat - nombre
    elif operateur == '*':
        return resultat * nombre
    elif operateur == '/':
        if nombre != 0:
            return resultat / nombre
        else:
            raise ValueError("Erreur : Division par zéro")
    else:
        raise ValueError("Opérateur non valide")

resultat = 0

while True:
    try:
        operateur = input("Entrez l'opérateur (+/-/*//) ou 'quit' pour quitter : ")
        if operateur.lower() == 'quit':
            break

        nombre = float(input("Entrez le nombre : "))
        resultat = evaluer_expression(operateur, nombre)

        print(f"Le résultat est : {resultat}")

    except ValueError as e:
        print(f"Erreur : {e}")
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")
