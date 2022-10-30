import sys


def recuperer_caracteristiques(caracteristiques):

    """
    Extrait la vitesse et le prix de déplacement du vaisseau de la chaine de caractéristiques

    Arguments:
        caracteristiques : str : la chaine des caractéristiques

    Retour:
        tuple : la vitesse et le prix de déplacement du vaisseau

    Exemple : 
        recuperer_caracteristiques("name=Crystal;speed=20000km/h;price=400/km")
            -> (20000, 400)
    """

    liste_caracteristiques = caracteristiques.split(";")

    try:
        vitesse_kmh = liste_caracteristiques[1].replace("speed=", "")
        prix_km = liste_caracteristiques[2].replace("price=", "")

        vitesse = vitesse_kmh.replace("km/h", "")
        prix = prix_km.replace("/km", "")

    except IndexError:
        print("La chaine saisie n'a pas le bon format")
        sys.exit()

    except:
        print("Erreur inconnue")
        sys.exit()

    return (int(vitesse), int(prix))


# -----------------------------------------------------------------------------------------------------


def cout_trajet(caracteristiques, temps_jours):

    """
    Calcule le coût du trajet 

    Arguments:
        caracteristiques : tuple : la vitesse et le prix de déplacement du vausseau
        temps_jours : int : le nombre de jours pendant lesquels le vaisseau se déplace

    Retour:
        int : le prix total du trajet

    Exemple : 
        cout_trajet((20000, 400), 10)
            -> 1920000000
    """
    

    temps_heures = temps_jours * 24

    distance = temps_heures * caracteristiques[0]
    prix_trajet = distance * caracteristiques[1]

    return prix_trajet


# -----------------------------------------------------------------------------------------------------


def main():
    
    """
    Programme principal

    Exemple : 
        main()
            > name=Crystal;speed=20000km/h;price=400/km
            > 10

            -> 1920000000€
    """

    caracteristiques_vaisseau = input("saisissez les caractéristiques du vaisseau : ")
    if not caracteristiques_vaisseau:
        print("Aucune caracteristique n'a été saisie")
        sys.exit()

    try:
        temps_jours = int(input("saisissez le temps de trajet : "))

    except ValueError:
        print("La valeur saisie doit être un nombre")
        sys.exit()

    except:
        print("erreur inconnue")
        sys.exit()

    caracteristiques = recuperer_caracteristiques(caracteristiques_vaisseau)

    cout = cout_trajet(caracteristiques, temps_jours)
    
    print(f"{cout}€")


# -----------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()