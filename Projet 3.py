menu = ["Pizza", "Burger", "Tacos", "Salade", "Filet de boeuf", "Gateau", "Smookie", "Eau minérale"]

while True:
    print("\n================ Menu ===============\n")
    print("Bienvenue chez Hawaah'S FOOD, les bons saveurs au rendez-vous!")

 #Affiche le menu principal
    print("Que voulez-vous faire?")
    print("1:Afficher le menu")
    print("2:Ajouter un plat")
    print("3:Supprimer un plat")
    print("4:Modifier un plat")
    print("5.Quitter")


#Affiche le menu avec numero
    option=(input("Votre choix:"))
    if option == "1":
        if len(menu) == 0:
         print("Desolé, le menu est vide!")
        else:
            print("\n=== Menu du Restaurant ===")
            for i, plat in enumerate(menu, start=1):
                print(f"{i}. {plat}")


    elif option == "2":  #ajout plat
        nouveau_plat=input("Entrez le nom du plat à ajouter:")
        if nouveau_plat:   #si nouveau plat n'est âes vide
            menu.append(nouveau_plat)   #ajout le plat à la fin de la liste
            print(f"{nouveau_plat} a ete ajouté au menu")
            break


    elif option == "3":   #suppression d'un plat
        if len(menu) == 0:
            print("Le menu est vide rien a supprimer")
        else:
            for i, plat in enumerate(menu, start=1):
                print(f"{i}. {plat}")
            try:
                Num=int(input("Entrez le numero du plat à supprimer:"))
                if 1 <= Num <= len(menu):
                    plat_supprimer = menu.pop(Num - 1)  #supprime le plat correspond
                    print(f" {plat_supprimer} a ete supprimé")
                else:
                    print("Numero invalide")
            except ValueError:
                print("Veuillez entrer un nombre valide.")
                break

    elif option == "4":   #Modification d'un plat
        if len(menu) == 0:
            print("Le menu est vide rien a modifer")
        else:
            for i, plat in enumerate(menu, start=1):
                print(f"{i}. {plat}")
            try:
                Num = int(input("Entrez le numero du plat à modifier:"))
                if 1 <= Num <= len(menu):
                    nouveau_plat=input("Entrez le nouveau plat à modfier:")
                    if nouveau_plat:
                        ancien_plat = menu[Num - 1]
                        menu[Num - 1] = nouveau_plat
                        print(f"{ancien_plat} a ete remplacé par {nouveau_plat}")
                    else:
                        print("Nom invalide")
                else:
                        print("Numero invalide")
            except ValueError:
                print("Veuillez entrer un nombre valide")
                break

    elif option == "5":   #Quitter
        print("Thank you, seen you soon!")
        break












