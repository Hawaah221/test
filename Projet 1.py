import random
while True:

    facile="1"
    dificile="2"
    choix=input("Entrez votre choix:")
    if choix=="1":
        limite_max=30
        nbre_essai=7
    else:
        limite_max=100
        nbre_essai=5
    nombre_mystere= random.randint(0,limite_max)
    point = 0

    for i in range(0,nbre_essai-1):
        nombre = int(input("Entrez un nombre:"))
        if nombre > nombre_mystere:
            print("Trop grand")
        elif nombre < nombre_mystere:
            print("Trop petit")
        else:
            point = nbre_essai-1 - i
            print(f"BRAVO vous avez trouvé ! vous avez {point} point")
            break

        if i == 3 and nombre != nombre_mystere:
            if nombre_mystere % 2 == 0:
                print("Indice:Le nombre est pair")
            else:
                print("Indice: Le nombre est impair")

    else:
        print("Perdu! le nombre etait " ,nombre_mystere)


    Rejouer=input("Voulez-vous rejouer oui/non ?").lower()
    if Rejouer == "non":
        print("Merci d'avoir joué !")
        break

