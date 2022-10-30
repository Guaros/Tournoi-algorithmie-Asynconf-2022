def saisie_etapes():

    """
    Renvoit toutes les étapes saisies par l'utilisateur 
    (Une ligne vide marque la dernière étape)

    Retour:
        list : la liste des etapes

    Exemple : 
        saisie_etapes()
            > "Jupiter"
            > "Terre"

            -> ["Jupiter", "Terre"]
    """
    
    etapes = []
    etape = "."
    while etape.strip():

        etape = input("saisissez une étape : ")
        etapes.append(etape.strip())
    
    etapes.remove("")
    return etapes


# -----------------------------------------------------------------------------------------------------


def codes_lettres_etapes(etapes): 

    """
    Renvoit toutes les lettres du code final

    Arguments:
        etapes : list : la liste des étapes

    Retour:
        list : la liste des lettres du code final

    Exemple : 
        codes_lettres_etapes(["Jupiter", "Terre"])
            -> ["J", "T"]
    """

    codes_lettres = []
    compteur_lettre = 1
   
    for etape in etapes:

        while (etape[0:compteur_lettre] in codes_lettres):

            compteur_lettre += 1
            
        codes_lettres.append(etape[0:compteur_lettre])
        compteur_lettre = 1

    return codes_lettres


# -----------------------------------------------------------------------------------------------------


def codes_chiffre_etapes(etapes, codes_lettres):

    """
    Renvoit tous les chiffres du code final

    Arguments:
        etapes : list : la liste des étapes
        codes_lettres : list : la liste des lettres du code finam

    Retour:
        list : la liste des chiffres du code final

    Exemple : 
        codes_lettres_etapes(["Jupiter", "Terre"], ["J", "T"])
            -> [6, 4]
    """

    codes_chiffre = []
    
    for numero_etape, etape in enumerate(etapes):

        codes_chiffre.append(len(etape) - len(codes_lettres[numero_etape]))

    return codes_chiffre


# -----------------------------------------------------------------------------------------------------


def assembler_code(codes_lettres_chiffre):

    """
    Renvoit le code final 

    Arguments:
        codes_lettres_chiffres : generateur : chaque couple (lettre;chiffre) du code final

    Retour:
        str : le code final

    Exemple : 
        codes_lettres_chiffre = zip(codes_lettres, codes_chiffre)
        assembler_code(codes_lettres_chiffre)
            -> "J6T4"
    """

    code_mission = ""

    for lettres, chiffre in codes_lettres_chiffre:

        chiffre = str(chiffre)
        code_mission += f"{lettres}{chiffre}"

    return code_mission


# -----------------------------------------------------------------------------------------------------


def main():
    
    """
    Programme principal 

    Exemple : 
        main()
            > "Jupiter"
            > "Terre

            -> "J6T4"
    """

    etapes = saisie_etapes()

    codes_lettres = codes_lettres_etapes(etapes)
    codes_chiffre = codes_chiffre_etapes(etapes, codes_lettres)

    codes_lettres_chiffre = zip(codes_lettres, codes_chiffre)
    code_mission = assembler_code(codes_lettres_chiffre)
    
    print(code_mission)


# -----------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()