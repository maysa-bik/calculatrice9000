print("Bienvenue dans la calculatrice!")

historique = []

# Demander à l'utilisateur combien d'opérations il veut effectuer
n_operations = int(input("Entrez le nombre  que vous souhaitez effectuer (1 ou plus) : "))

# Vérifier que le nombre d'opérations est valide
if n_operations < 1:
    print("Erreur:  Le nombre d'opérations doit être au moins 1.")
else:
    # Demander à l'utilisateur d'entrer un nombre pour chaque opération
    nums = [float(input(f"Entrez le nombre {i+1} : ")) for i in range(n_operations)]

    # Demander à l'utilisateur de choisir l'opération pour chaque nombre
    operations = []
    for i in range(n_operations-1):
        operation = input(f"Entrez l'opération souhaitée pour le nombre {i+1} et le nombre {i+2} (+/-/*//) : ")
        operations.append(operation)

    # Effectuer les opérations et afficher le résultat
    try:
        resultat = nums[0]
        for i in range(1, n_operations):
            if operations[i-1] == '+':
                resultat += nums[i]
            elif operations[i-1] == '-':
                resultat -= nums[i]
            elif operations[i-1] == '*':
                resultat *= nums[i]
            elif operations[i-1] == '/':
                if nums[i] != 0:
                    resultat /= nums[i]
                else:
                    raise ValueError("Erreur : Division par zéro")
            else:
                raise ValueError("Opération non valide")
            
            # Stocker l'opération et le résultat dans l'historique
            historique.append(f"{nums[i-1]} {operations[i-1]} {nums[i]} = {resultat}")
        print("Le résultat est :", resultat)

        # Afficher l'historique 
        print("\nHistorique des opérations :")
        for operation in historique:
            print(operation)
    except ValueError:
        print("Erreur: Valeur invalide.")