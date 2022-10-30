import collections
import string
import sys


def demander_plan():

    """
    Demande à l'utilisateur de saisir le plan

    Retour:
        list : le plan saisi

    Exemple : 
        demander_plan()
            > X___OO__O___O
            > __O__OOOO____
            > OO_O__OO__O__
            > _OO_O____OO_O
            > __O_O__O_OOVO

            -> ["X___OO__O___O", "__O__OOOO____", "OO_O__OO__O__", "_OO_O____OO_O", "__O_O__O_OOVO"]
    """

    plan = []
    ligne_plan = input("saisissez une ligne : ")

    while len(ligne_plan):

        plan.append(ligne_plan)
        ligne_plan = input("saisissez une ligne : ")
    
    return plan


# ------------------------------------------------------------------------------------------------------------------------


def verifier_plan(plan):

    """
    Verifie si un plan est valide 
        - la taille des lignes est inférieure à 27 
        - chaque ligne a la même taille
    

    Arguments:
        plan : list : le plan a vérifier

    Exemple : 
        verifier_plan(["X___OO__O___O", "__O__OOOO____", "OO_O__OO__O__", "_OO_O____OO_O", "__O_O__O_OOVO"])
    """

    nb_elements_ligne = len(plan[0])

    if nb_elements_ligne > 26:

        print("Le nombre de caractères par ligne doit être strictement inférieur à 27")
        sys.exit()

    else:

        for ligne in plan:
            if len(ligne) != nb_elements_ligne:

               print("Le nombre de caractères doit être le même pour chaque ligne")
               sys.exit() 


# ------------------------------------------------------------------------------------------------------------------------


def depart_arrivee(plan):

    """
    Renvoit un dictionnaire avec les coordonnéés du point de départ (X) et du point d'arrivée (V)

    Arguments:
        plan : list : le plan

    Retour:
        dict : les coordonnées du point de départ et du point d'arrivée

    Exemple : 
        depart_arrivee(["X___OO__O___O", "__O__OOOO____", "OO_O__OO__O__", "_OO_O____OO_O", "__O_O__O_OOVO"])
            -> {"depart":(0, 0), "arrivee":(4, 11)}
    """

    coordonnees = {}

    for indice_ligne, ligne in enumerate(plan):
        for indice_colonne, elem in enumerate(ligne):

            if elem == "V":
                coordonnees["arrivee"] = (indice_ligne, indice_colonne)

            elif elem == "X":
                coordonnees["depart"] = (indice_ligne, indice_colonne)
    
    return coordonnees


# ------------------------------------------------------------------------------------------------------------------------


def ajouter_voisins_predecesseur(plan, position, plan_visites, file_a_visiter, predecesseurs):

    """
    Fonction intermédiaire de predecesseurs 
    Ajoute un point précis au dictionnaire des prédécésseurs
    
    Arguments:
        plan : list : le plan
        position : tuple : les coordonnées du point actuel 
        plan_visites : list : copie du plan mais avec des valeurs booléennes. chaque element vaut
        True si on est déjà passé par le point (dans le dictionnaire des prédécesseurs) et False sinon
        file_a_visiter : collections.deque : file d'attente de tous les points sur lesquels on doit encore passer 
        predecesseurs : dict : dictionnaires des prédécesseurs


    Retour:
        dict : dictionnaires des prédécesseurs

    Exemple : 
        plan = ["X___OO__O___O", "__O__OOOO____", "OO_O__OO__O__", "_OO_O____OO_O", "__O_O__O_OOVO"]
        position = (0, 0)
        plan_visites = [[False for j in plan[0]] for i in plan]
        file_a_visiter
        predecesseurs = {"position"[], "precedents":[]}
  
        ajouter_voisins_predecesseur(plan, position, plan_visites, file_a_visiter, predecesseurs)
            -> predecesseurs = {"position"[(1, 0), (0, 1)], "precedents":[(0, 0), (0, 0)]}
    """

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for direction in directions:
        voisin = (position[0] + direction[0], position[1] + direction[1])

        if voisin[0] >= 0 and voisin[0] < len(plan) and voisin[1] >= 0 and voisin[1] < len(plan[0]):

            if plan[voisin[0]][voisin[1]] != "O":

                if not plan_visites[voisin[0]][voisin[1]]:

                    plan_visites[voisin[0]][voisin[1]] = True
                    voisin_precesseur = (voisin) 
                    file_a_visiter.append(voisin_precesseur)

                    predecesseurs["position"].append(voisin)
                    predecesseurs["precedent"].append(position)
       
    return predecesseurs


# ------------------------------------------------------------------------------------------------------------------------


def predecesseurs(plan, coordonnees):

    """
    Renvoit un dictionnaire avec les coordonnées de chaque point atteignable
    et les coordonnées du point précédent (qui ont permis d'attendre chaque point atteignable)

    Arguments:
        plan : list : le plan
        coordonnees : dict : les coordonnées du point de départ et d'arrivée

    Retour:
        dict : le dictionnaire des prédécesseurs

    Exemple : 
        predecesseurs(["X___OO__O___O", "__O__OOOO____", "OO_O__OO__O__", "_OO_O____OO_O", "__O_O__O_OOVO"], {"depart":(0, 0), "arrivee":(4, 11)})
            -> {
                'position': [(1, 0), (0, 1), (1, 1), (0, 2), (0, 3), 
                             (1, 3), (1, 4), (2, 4), (2, 5), (3, 5), 
                             (4, 5), (3, 6), (4, 6), (3, 7), (3, 8), 
                             (2, 8), (4, 8), (2, 9), (1, 9), (0, 9), 
                             (1, 10), (0, 10), (1, 11), (0, 11), (2, 11), 
                             (1, 12), (3, 11), (2, 12), (4, 11)], 
                'precedent': [(0, 0), (0, 0), (1, 0), (0, 1), (0, 2),
                             (0, 3), (1, 3), (1, 4), (2, 4), (2, 5), 
                             (3, 5), (3, 5), (4, 5), (3, 6), (3, 7), 
                             (3, 8), (3, 8), (2, 8), (2, 9), (1, 9),
                             (1, 9), (0, 9), (1, 10), (0, 10), (1, 11), 
                             (1, 11), (2, 11), (2, 11), (3, 11)]
                }
    """

    position = coordonnees["depart"] 
    arrivee = coordonnees["arrivee"] 

    plan_visites = [[False for j in plan[0]] for i in plan]
    file_a_visiter = collections.deque()

    plan_visites[position[0]][position[1]] = True
    file_a_visiter.append(position)  

    sortie_trouvee = False
    
    predecesseurs = {"position":[], "precedent":[]}

    while not sortie_trouvee:
        position = file_a_visiter.popleft()
       
        if position == arrivee:
            sortie_trouvee = True

        ajouter_voisins_predecesseur(plan, position, plan_visites, file_a_visiter, predecesseurs)
    
    return predecesseurs
                    

# ------------------------------------------------------------------------------------------------------------------------


def solution(predecesseurs, coordonnees):

    """
    Renvoit le chemin à parcourir pour résoudre le labyrinthe avec l'algorithme de Lee

    Arguments:
        predecesseurs : dict : dictionnaire des prédecesseurs
        coordonnees : dict : dictionnaires des coordonnées de départ et d'arrivée

    Retour:
        list : le chemin à parcourir

    Exemple : 
        predecesseurs = {
                'position': [(1, 0), (0, 1), (1, 1), (0, 2), (0, 3), 
                             (1, 3), (1, 4), (2, 4), (2, 5), (3, 5), 
                             (4, 5), (3, 6), (4, 6), (3, 7), (3, 8), 
                             (2, 8), (4, 8), (2, 9), (1, 9), (0, 9), 
                             (1, 10), (0, 10), (1, 11), (0, 11), (2, 11), 
                             (1, 12), (3, 11), (2, 12), (4, 11)], 
                'precedent': [(0, 0), (0, 0), (1, 0), (0, 1), (0, 2),
                             (0, 3), (1, 3), (1, 4), (2, 4), (2, 5), 
                             (3, 5), (3, 5), (4, 5), (3, 6), (3, 7), 
                             (3, 8), (3, 8), (2, 8), (2, 9), (1, 9),
                             (1, 9), (0, 9), (1, 10), (0, 10), (1, 11), 
                             (1, 11), (2, 11), (2, 11), (3, 11)]
                }
        solution(predecesseurs, {"depart":(0, 0), "arrivee":(4, 11)})
            -> [(4, 11), (3, 11), (2, 11), (1, 11), (1, 10), (1, 9), (2, 9), (2, 8), (3, 8), 
                (3, 7), (3, 6), (3, 5), (2, 5), (2, 4), (1, 4), (1, 3), (0, 3), (0, 2), (0, 1), (0, 0)]
    """

    chemin = [coordonnees["arrivee"]]

    while coordonnees["depart"] != coordonnees["arrivee"]:

        indice_precedent = predecesseurs["position"].index(coordonnees["arrivee"])
        coordonnees["arrivee"] = predecesseurs["precedent"][indice_precedent]

        chemin.append(coordonnees["arrivee"])

    return chemin


# ------------------------------------------------------------------------------------------------------------------------


def formater_positions(chemin):

    """
    Formate le chemin à parcourir

    Arguments:
        chemin : list : le chemin à parcourir

    Retour:
        str : le chemin formaté

    Exemple : 
        chemin = [(4, 11), (3, 11), (2, 11), (1, 11), (1, 10), (1, 9), (2, 9), (2, 8), (3, 8), 
        (3, 7), (3, 6), (3, 5), (2, 5), (2, 4), (1, 4), (1, 3), (0, 3), (0, 2), (0, 1), (0, 0)]
        
        formater_positions(chemin)
            -> "A1;B1;C1;D1;D2;E2;E3;F3;F4;G4;H4;I4;I3;J3;J2;K2;L2;L3;L4;L5"
    """
    
    positions = ""
    majuscules = string.ascii_uppercase

    chemin.reverse()

    for position in chemin:

        lettre = majuscules[position[1]]
        chiffre = str(position[0] + 1)

        positions = positions + lettre + chiffre + ";" 
    
    print(positions[0:len(positions) - 1])


# ------------------------------------------------------------------------------------------------------------------------


def main():

    """
    Programme principal

    Exemple : 
        main()
            > X___OO__O___O
            > __O__OOOO____
            > OO_O__OO__O__
            > _OO_O____OO_O
            > __O_O__O_OOVO

            -> A1;B1;C1;D1;D2;E2;E3;F3;F4;G4;H4;I4;I3;J3;J2;K2;L2;L3;L4;L5
    """

    plan = demander_plan()
    verifier_plan(plan)

    coordonnees = depart_arrivee(plan)

    if len(coordonnees) != 2:

        print("Aucune solution n'existe")
        sys.exit()

    precedents = predecesseurs(plan, coordonnees)
    chemin = solution(precedents, coordonnees)
    
    formater_positions(chemin)


# ------------------------------------------------------------------------------------------------------------------------
    

if __name__ == "__main__":
    main()