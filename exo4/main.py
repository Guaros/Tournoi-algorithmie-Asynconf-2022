import base64
import json
import sys


def saisir_message():

    """
    Demander à l'utilisateur de saisir le message secret 
    (une ligne vide marque la fin de la saisie)

    Retour:
        str : le message code

    Exemple : 
        saisir_message()
            > WwogICAgewogICAgICAgICJuYW1lIjogIlNpbG9wcCIsCiA
            > gICAgICAgInNpemUiOiAxNDkyNCwKICAgICAgICAiZGlzdG
            > FuY2VUb1N0YXIiOiA5MDI0ODQ1MiwKICAgICAgICAibWFzc
            > yI6IDE5NDUzMgogICAgfSwKICAgIHsKICAgICAgICAibmFt
            > ZSI6ICJBc3RyaW9uIiwKICAgICAgICAic2l6ZSI6IDE1MjA
            > wMCwKICAgICAgICAiZGlzdGFuY2VUb1N0YXIiOiAxNDkzMD
            > IsCiAgICAgICAgIm1hc3MiOiAyMTk0CiAgICB9LAogICAge
            > wogICAgICAgICJuYW1lIjogIlZhbGVudXMiLAogICAgICAg
            > ICJzaXplIjogMjkwNDUwLAogICAgICAgICJkaXN0YW5jZVR
            > vU3RhciI6IDIwOTQ4NTkzNDU1LAogICAgICAgICJtYXNzIj
            > ogMTk1MjkzCiAgICB9Cl0=
    """

    message = ""
    ligne_message = input("saisissez une ligne du message codé : ")

    while len(ligne_message):

        message += ligne_message
        ligne_message = input("saisissez une ligne du message codé : ")
    
    print(message)
    return message


# ------------------------------------------------------------------------------------------------------------------------


def decoder_message(message):

    """
    Converti le message codé en objet JSON

    Arguments:
        message : str : le message codé

    Retour:
        JSON : l'objet JSON
    """

    try:
        message_json = base64.b64decode(message)

    except base64.binascii.Error:
        print("Le texte est incomplet")
        sys.exit()

    except:
        print("Erreur inconnue")
        sys.exit()
    

    try:
        return json.loads(message_json)

    except json.decoder.JSONDecodeError:
        print("Le texte est vide")
        sys.exit()

    except: 
        print("Erreur inconnue")
        sys.exit()
    

# ------------------------------------------------------------------------------------------------------------------------
    

def remplir_gauche(planetes_fusionnee, planetes_gauche, indice_planetes_gauche):

    """
    Fonction intermédiaire du tri fusion 
    Ajoute à la liste triée, tous les éléments de la liste gauche plus grand
    que le dernier élément de la liste droite

    Arguments:
        planetes_fusionnee : list : la liste finale triée
        planetes_gauche : list : la liste gauche triée
        indice_planetes_gauche : int : L'indice à partir du quel les éléments de
        la liste gauche deviennent plus grand que le dernier élément de la liste droite
         
    Retour:
        planetes_fusionnee : la liste finale triée

    Exemple : 
        planetes_gauche = [2, 3, 7, 8]
        planetes_droite = [1, 2, 5]

        planetes_fusionnee = [1, 2, 2, 3, 5]
        
        remplir_gauche(planetes_fusionnee, planetes_gauche, 2)
            -> [1, 2, 2, 3, 5, 7, 8]
    """

    while indice_planetes_gauche < len(planetes_gauche):

        planetes_fusionnee.append(planetes_gauche[indice_planetes_gauche])
        indice_planetes_gauche += 1
    
    return planetes_fusionnee


# ------------------------------------------------------------------------------------------------------------------------


def remplir_droite(planetes_fusionnee, planetes_droite, indice_planetes_droite):

    """
    Fonction intermédiaire du tri fusion 
    Ajoute à la liste triée, tous les éléments de la liste droite plus grand
    que le dernier élément de la liste gauche

    Arguments:
        planetes_fusionnee : list : la liste finale triée
        planetes_droite : list : la liste droite triée
        indice_planetes_droite : int : L'indice à partir du quel les éléments de
        la liste droite deviennent plus grand que le dernier élément de la liste gauche
         
    Retour:
        planetes_fusionnee : la liste finale triée

    Exemple : 
        planetes_gauche = [1, 2, 5]
        planetes_droite = [2, 3, 7, 8]
        
        planetes_fusionnee = [1, 2, 2, 3, 5]
        
        remplir_gauche(planetes_fusionnee, planetes_droite, 2)
            -> [1, 2, 2, 3, 5, 7, 8]
    """

    while indice_planetes_droite < len(planetes_droite):

        planetes_fusionnee.append(planetes_droite[indice_planetes_droite])
        indice_planetes_droite += 1

    return planetes_fusionnee


# ------------------------------------------------------------------------------------------------------------------------


def fusionner(planetes_gauche, planetes_droite):

    """
    Fonction intermédiaire du tri fusion
    concatène deux listes triées dans une troisième liste triée

    Arguments:
        planetes_gauche : list : la chaine de gauche
        planetes_droite : list : la liste de droite

    Retour:
        list : la liste triée

    Exemple : 
        fusionner([1, 2, 5], [2, 3, 7, 8])
            -> [1, 2, 2, 3, 5, 7, 8]
    """

    planetes_fusionnee = []
    indice_planetes_gauche = 0
    indice_planetes_droite = 0
    
    while indice_planetes_gauche < len(planetes_gauche) and indice_planetes_droite < len(planetes_droite):

        planete_gauche = planetes_gauche[indice_planetes_gauche]
        planete_droite = planetes_droite[indice_planetes_droite]

        if (planete_gauche["distanceToStar"] < planete_droite["distanceToStar"]):

            planetes_fusionnee.append(planete_gauche)
            indice_planetes_gauche += 1

        else:

            planetes_fusionnee.append(planete_droite)
            indice_planetes_droite += 1

    planetes_fusionnee = remplir_gauche(planetes_fusionnee, planetes_gauche, indice_planetes_gauche)
    planetes_fusionnee = remplir_droite(planetes_fusionnee, planetes_droite, indice_planetes_droite)

    return planetes_fusionnee


# ------------------------------------------------------------------------------------------------------------------------
   
            
def tri_fusion(planetes):

    """
    Tri une liste en appliquant l'algorithme de tri-fusion

    Arguments:
        planetes : list : liste non triée

    Retour:
        list : liste triée

    Exemple : 
        tri_fusion([7, 3, 5, 2, 1, 8, 2])
           -> [1, 2, 2, 3, 5, 7, 8]
    """

    if (len(planetes) > 1):

        milieu = len(planetes) // 2
        planetes_gauche = planetes[0:milieu]
        planetes_droite = planetes[milieu:len(planetes)]

        return fusionner(planetes_gauche, planetes_droite)

    else:
        return planetes


# ------------------------------------------------------------------------------------------------------------------------


def afficher_planetes(planetes):

    """
    Affiche l'objet JSON avec un format lisible pour l'être humain

    Arguments:
        planetes : JSON : le message au format JSON

    Exemple :
        objet_json =  [{"name": "Silopp","size": 14924,"distanceToStar": 90248452,
        "mass": 194532},{"name": "Astrion","size": 152000,"distanceToStar": 149302,
        "mass": 2194}, {"name": "Valenus","size": 290450,"distanceToStar": 20948593455,
        "mass": 195293}]
    """

    for planete in planetes:
        
        nom = planete["name"]
        taille = str(planete["size"])
        masse = str(planete["mass"])
        distance_etoile = str(planete["distanceToStar"])

        print(f"Nom : {nom}")
        print(f"Taille : {taille}km")
        print(f"Masse : {masse} tonnes")
        print(f"Distance à l'étoile : {distance_etoile} km\n")


# ------------------------------------------------------------------------------------------------------------------------


def main():

    """
    Programme principal

    Exemple : 
        main()
            > WwogICAgewogICAgICAgICJuYW1lIjogIlNpbG9wcCIsCiA
            > gICAgICAgInNpemUiOiAxNDkyNCwKICAgICAgICAiZGlzdG
            > FuY2VUb1N0YXIiOiA5MDI0ODQ1MiwKICAgICAgICAibWFzc
            > yI6IDE5NDUzMgogICAgfSwKICAgIHsKICAgICAgICAibmFt
            > ZSI6ICJBc3RyaW9uIiwKICAgICAgICAic2l6ZSI6IDE1MjA
            > wMCwKICAgICAgICAiZGlzdGFuY2VUb1N0YXIiOiAxNDkzMD
            > IsCiAgICAgICAgIm1hc3MiOiAyMTk0CiAgICB9LAogICAge
            > wogICAgICAgICJuYW1lIjogIlZhbGVudXMiLAogICAgICAg
            > ICJzaXplIjogMjkwNDUwLAogICAgICAgICJkaXN0YW5jZVR
            > vU3RhciI6IDIwOTQ4NTkzNDU1LAogICAgICAgICJtYXNzIj
            > ogMTk1MjkzCiAgICB9Cl0=

            -> Nom : Astrion
               Taille : 152000km
               Masse : 2194 tonnes
               Distance à l’étoile : 149302km

               Nom : Silopp
               Taille : 14924km
               Masse : 194532 tonnes
               Distance à l’étoile : 90248452km

               Nom : Valenus
               Taille : 290450km
               Masse : 195293 tonnes
               Distance à l’étoile : 20948593455km
    """
    
    message_code = saisir_message()
    planetes = decoder_message(message_code)
    planetes_triees = tri_fusion(planetes)
    
    afficher_planetes(planetes_triees)


# ------------------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()