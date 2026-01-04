import math

continuer = True

while continuer:

    print("\n ========Menu =========")
    print("1.Addition")
    print("2.Soustraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Modulo (reste de la division entière)")
    print("6.Puissance")
    print("7.Moyenne")
    print("8.Max")
    print("9.Min")
    print("10.Racine carré")
    print("11.Factoriel")
    print("0.Quitter")

    operation = int(input("Veuillez choisir une operation:"))

    if operation == 0:
        print("A bientot")
        break

    n=int (input("Combien de nombre vous voulez choisir ?"))
    Nombre=[]
    for i in range(1,n+1):
        nb=int(input(f"Veuillez entrez le nombre {i}:"))
        Nombre.append(nb)    #Stocker nb dans la liste Nombre

    if operation == 1: #Addition
        resultat = 0
        for nb in Nombre:
            resultat = resultat + nb
        print("Resultat = ",resultat)

    elif operation == 2:    #Soustraction
        resultat = Nombre[0]
        for nb in Nombre[1:]:
            resultat = resultat - nb
        print("Resultat = ",resultat)

    elif operation == 3:     #Multiplication
        resultat = 1
        for nb in Nombre:
            resultat = resultat * nb
        print("Resultat = ",resultat)

    elif operation == 4:      #Division
        resultat = Nombre[0]
        for nb in Nombre[1:]:
            if nb == 0:
                print("Erreur! Division par 0 n'existe pas")
                break
            resultat = resultat  / nb
        else:
            print("Resultat = ",resultat)

    elif operation == 5:    #Modulo
        resultat = Nombre[0]
        for nb in Nombre[1:]:
            if nb == 0:
                print("Erreur! Modulo par 0 n'existe pas")
                break
            resultat = resultat % nb
        else:
            print("Resultat = ",resultat)

    elif operation == 6:       #Puissance
        resultat = Nombre[0]
        for nb in Nombre[1:]:
            resultat = resultat ** nb
        print("Resultat = ",resultat)

    elif operation==7:   #Moyenne
        resultat = sum(Nombre) / len(Nombre)
        print("Resultat = ",resultat)


    elif operation ==  8:   #Max
        resultat = max(Nombre)
        print("Resultat = ",resultat)

    elif operation == 9:  #Min
        resultat = min(Nombre)
        print("Resultat = ",resultat)

    elif operation == 10:  #Racine carré
        if Nombre[0] < 0:
            print("Erreur! racine carré d'un nombre negative impossible")
        else:
            resultat = math.sqrt(Nombre[0])
            print("Resultat = ",resultat)

    elif operation == 11: #factoriel
        if  Nombre[0] < 0:
            print("Erreur! factoriel d'un nombre negative impossible")
        else:
            resultat = math.factorial(Nombre[0])
            print("Resultat = ",resultat)


    choix=input("Voulez-vous recalculer oui/non ?").lower()
    if choix != "oui":
        print("Wa Salam")
        break

