class SystemeComptes:

    """
    Cette classe représente un système de comptes
        - Chaque compte possède un pseudo (unique dans le système)
        - Un seul compte est connecté
        - Un Utilisateur ne peut que se connecter à un autre compte
        - L'Administrateur (compte unique) est le seul à pouvoir créer et supprimer des comptes
    """

    def __init__(self):

        """
        Constructeur de SystemeComptes

        Attributs : 
            self.comptes : set : ensemble des comptes (pseudo) du système
            self.pseudo_connecte : str : le compte actuellement connecté (par défaut l'Administrateur)

        Exemple : 
            système_compte = SystemeComptes()
        """

        self.comptes = {"Administrateur"}
        self.pseudo_connecte = self.recuperer_administrateur()
    

    # ------------------------------------------------------------------------------------------------------------------------------------------------


    def compte_existe(self, pseudo):

        """
        Vérifie si un compte existe dans le système

        Arguments:
            pseudo : str : pseudo à vérifier

        Retour:
            bool : True si le compte existe et False sinon

        Exemple : 
            compte_existe("Administrateur")
                -> True
        """

        return pseudo in self.comptes
    

    # ------------------------------------------------------------------------------------------------------------------------------------------------


    def recuperer_compte(self, pseudo):

        """
        Renvoit le pseudo si celui-ci existe et "" sinon

        Arguments:
            pseudo : str : pseudo à récupérer

        Retour:
            str : le pseudo

        Exemple : 
            recuperer_compte("compte_fictif")
                -> ""
        """

        if self.compte_existe(pseudo):
            return pseudo

        else:
            return ""

    
    # ------------------------------------------------------------------------------------------------------------------------------------------------


    def recuperer_administrateur(self):

        """
        Renvoit le pseudo de l'Administrateur du système

        Retour:
            str : le pseudo de l'administrateur

        Exemple : 
            recuperer_administrateur()
                -> "Administrateur"
        """

        return self.recuperer_compte("Administrateur")
    

    # ------------------------------------------------------------------------------------------------------------------------------------------------


    def utilisateur_connecte(self, pseudo):

        """
        Teste si un compte est connecté ou non

        Arguments:
            pseudo : str : le pseudo du compte à tester

        Retour:
            bool : True si le compte est connecté et False sinon

        Exemple : 
            utilisateur_connecte("Administrateur")
                -> True
        """

        return self.pseudo_connecte == pseudo
    

    # ------------------------------------------------------------------------------------------------------------------------------------------------


    def administrateur_connecte(self):

        """
        Teste si l'administrateur est connecté

        Retour:
            bool : True si l'administrateur est connecté et False sinon

        Exemple : 
            administrateur_connecte()
                -> True
        """

        administrateur = self.recuperer_administrateur()
        return self.utilisateur_connecte(administrateur)


    # ------------------------------------------------------------------------------------------------------------------------------------------------
    

    def ajouter_compte(self, pseudo):

        """
        L'Administrateur peut créer un compte s'il est connecté et que le compte n'existe pas

        Arguments:
            pseudo : str : le pseudo du compte à créer

        Exemple : 
            ajouter_compte("autre_compte")
        """

        administrateur = self.recuperer_administrateur()

        if not self.administrateur_connecte():
            print(f"Seul {administrateur} peut créer un compte")

        elif self.compte_existe(pseudo):
            print(f"Le compte {pseudo} existe deja donc ne peut pas être crée")

        else:
            self.comptes.add(pseudo)
            print(f"Le compte {pseudo} a été crée avec succès")
    

    # ------------------------------------------------------------------------------------------------------------------------------------------------


    def supprimer_compte(self, pseudo):

        """
        L'Administrateur peut supprimer un compte s'il est connecté et que le compte existe
        Cependant, le compte Administrateur ne peut pas être supprimé

        Arguments:
            pseudo : str : le pseudo du compte à supprimer

        Exemple : 
            supprimer_compte("autre_compte")
        """

        administrateur = self.recuperer_administrateur()

        if not self.administrateur_connecte():
            print(f"Seul {administrateur} peut supprimer un compte")

        elif not self.compte_existe(pseudo):
            print(f"Le compte {pseudo} n'existe pas donc ne peut pas être supprimé")

        elif pseudo == self.recuperer_administrateur():
            print(f"Le compte {administrateur} ne peut pas être supprimé") 
       
        else:
            self.comptes.remove(pseudo)
            print(f"Le compte {pseudo} a été supprimé avec succès")


    # ------------------------------------------------------------------------------------------------------------------------------------------------


    def connecter_compte(self, pseudo):

        """
        L'utilisateur peut se connecter à un autre compte si celui-ci existe 
        Cependant, un utilisateur ne peut pas se connecter à son propre compte

        Arguments:
            pseudo : str : le pseudo du compte sur lequel se connecter

        Exemple : 
            connecter_compte("autre_compte")
        """

        if not self.compte_existe(pseudo):
            print(f"Le compte {pseudo} n'existe pas, impossible de se connecter")

        elif self.utilisateur_connecte(pseudo):
            print(f"Le compte {pseudo} est déjà connecté")

        else:
            self.pseudo_connecte = pseudo
            print(f"Le compte {pseudo} est maintenant connecté")


    
class SystemeTaches:

    """
    Cette classe représente un système de tâches
        - Chaque tâche possède un nom, une description, 
          une liste de comptes associés (appartenant au système de comptes) et peut être complète ou non

        - On admet que plusieurs tâches ne peuvent pas avoir le même nom 
        - On admet également qu'une tâche est forcément associée à au moins un utilisateur

        - Un système de tâches est donc lié à un système de comptes
        - Un utilisateur peut lister et compléter les tâches auxquelles il est associé
        - L'Administrateur peut créer, supprimer, vider, lister et compléter toutes les
          tâches du système
    """

    def __init__(self, systeme_compte):

        """
        Constructeur de SystemeTaches

        Attributs : 
            self.taches : list : liste des tâches 
                Une tâche est un dictionnaire au format : {"nom":"value", "description":"value", "comptes_associes":[], "en_cours":True}
                    Le nom de la tâche est une chaine de caractères
                    La description de la tâche est une chaine de caractères
                    Les comptes associés sont une liste de chaines de caractères
                    La clé "en_cours" vaut True par défaut et tant que la tâche n'est pas complétée 

            self.systeme_compte : SystemCompte : le système de compte lié 

        Exemple : 
            système_compte = SystemeComptes()
            SystemeTaches(SystemeComptes)
        """

        self.taches = [] 
        self.systeme_compte = systeme_compte
    

    # ------------------------------------------------------------------------------------------------------------------------------------------------


    def recuperer_tache(self, nom):

        """
        Récupère une tâche (dictionnaire) à partir de son nom.
        Si la tâche n'est pas trouvée, on récupère le dictionnaire vide

        Arguments:
            nom : str : nom de la tâche

        Retour:
            dict : la tâche 

        Exemple : 
            recuperer_tache("tache_administration")
                -> {"nom":"tache_administration", "description":"tache administration", "comptes_associes"["Administrateur"], "en_cours":True}
        """

        tache_chercher = {}
        if len(self.taches):

            for tache in self.taches:
                nom_tache = tache["nom"]

                if nom_tache == nom:
                    tache_chercher = tache

        return tache_chercher
    

    # ------------------------------------------------------------------------------------------------------------------------------------------------


    def tache_existe(self, nom):

        """
        Vérifie si une tâche existe

        Arguments:
            nom : str : le nom de la tâche

        Retour:
            bool : True si la tâche existe et False sinon

        Exemple : 
            recuperer_tache("tache_administration")
                -> True
        """

        if self.recuperer_tache(nom):
            return True

        else:
            return False 


    # ------------------------------------------------------------------------------------------------------------------------------------------------


    def taches_associees_compte(self, pseudo):

        """
        Renvoit toutes les tâches auxquelles un compte est associé

        Arguments:
            pseudo : str : le pseudo du compte

        Retour:
            list : tâches auquelles le compte est associé

        Exemple : 
            taches_associees_compte("Administrateur)
                [{"nom":"tache_administration", "description":"tache administration", "comptes_associes"["Administrateur"], "en_cours":True}]
        """

        taches = []
        for tache in self.taches:
            if pseudo in tache["comptes_associes"]:
            
                taches.append(tache)

        return taches
    

    # ------------------------------------------------------------------------------------------------------------------------------------------------


    def ajouter_compte_tache(self, tache):

        """
        Méthode intermédiaire de ajouter_tache 
        Va ajouter un pseudo à la liste des comptes associés d'une tâche : (tache["comptes_associes"]) 

        Arguments:
            tache : dict : la tâche sur laquelle ajouter un compte

        Retour:
            dict : la tâche avec le compte ajouté

        Exemple : 
            tache = {"nom":"tache_administration", "description":"tache administration", "comptes_associes"["Administrateur"], "en_cours":True}
            ajouter_compte_tache(tache)
                > autre_compte
           
                -> {"nom":"tache_administration", "description":"tache administration", "comptes_associes"["Administrateur", "autre_compte"], "en_cours":True}
        """

        nom = tache["nom"]
        pseudo = input(f"veuillez saisir le pseudo à associer à la tâche {nom} : ")

        while not self.systeme_compte.compte_existe(pseudo):

            print(f"Le compte {pseudo} n'existe pas")
            pseudo = input(f"veuillez saisir le pseudo à associer à la tâche {nom} : ")

        tache["comptes_associes"].append(pseudo)
        return tache


    # ------------------------------------------------------------------------------------------------------------------------------------------------


    def afficher_taches(self, taches):

        """
        Méthode intermédiaire de lister_taches
        Va afficher toutes les caractéristiques de toutes les tâches d'une liste de tâches
        dans un format lisible pour l'être humain

        Arguments:
            taches : list : la chaine des tâches

        Exemple : 
            taches = [{"nom":"tache_administration", "description":"tache administration", "comptes_associes"["Administrateur"], "en_cours":True}]
            recuperer_caracteristiques(taches)
        """
        
        for tache in taches: 

            nom = tache["nom"]
            description = tache["description"]
            comptes_associes = tache["comptes_associes"]
            en_cours = tache["en_cours"]

            print(f"nom : {nom}, description : {description}, comptes_associes : {comptes_associes}, en_cours : {en_cours}")


    # ------------------------------------------------------------------------------------------------------------------------------------------------


    def ajouter_tache(self, nom, description):

        """
        L'administrateur peut créer une tâche (si celle-ci n'existe pas) et y associer un ou plusieurs comptes existants
        (une tâche doit être associée à au moins un compte). Celle-ci sera incomplète à la création : tache["en_cours"] = True

        Arguments:
            nom : str : le nom de la tâche
            description : str : la description de la tâche

        Exemple : 
            ajouter_tache("tache_administration", "tache administration")
        """

        if self.tache_existe(nom):
            print(f"La tâche {nom} existe déjà")

        elif not self.systeme_compte.administrateur_connecte():
            administrateur = self.systeme_compte.recuperer_administrateur()
            print(f"seul le compte {administrateur} peut créer des tâches")

        else:
            tache = {"nom":nom, "description":description, "comptes_associes":[], "en_cours":True}

            while not len(tache["comptes_associes"]):
                tache = self.ajouter_compte_tache(tache)
                
            nb_autres_utilisateurs = int(input("Combien d'autres utilisateurs voulez-vous ajouter ? "))

            for i in range(nb_autres_utilisateurs):
                tache = self.ajouter_compte_tache(tache)

            self.taches.append(tache)

    
    # ------------------------------------------------------------------------------------------------------------------------------------------------


    def retirer_tache(self, nom):

        """
        L'Administrateur peut supprimer une tâche existante s'il est connecté

        Arguments:
            nom : str : le nom de la tâche à supprimer

        Exemple : 
            retirer_tache("tache_administration")
        """

        tache = self.recuperer_tache(nom)
       
        if not self.tache_existe(nom):
            print(f"La tâche {nom} n'existe pas")

        elif not self.systeme_compte.administrateur_connecte():
            administrateur = self.systeme_compte.recuperer_administrateur()
            print(f"Seul {administrateur} peut supprimer une tâche")

        else:
            print(f"La tâche {nom} a été correctement supprimée")
            self.taches.remove(tache)

    
    # ------------------------------------------------------------------------------------------------------------------------------------------------


    def completer_tache(self, nom):

        """
        L'utilisateur peut déclarer une tâche existante comme complète s'il y'est associée
        Cependant, l'Administrateur peut déclarer comme complète n'importe quelle tâche existante

        Arguments:
            nom : str : le nom de la tâche à compléter

        Exemple : 
            completer_tache("tache_administration")
        """

        tache = self.recuperer_tache(nom)

        if not self.tache_existe(nom):
            print(f"La tâche {nom} n'existe pas")

        else:
            pseudo_connecte = self.systeme_compte.pseudo_connecte
            administrateur = self.systeme_compte.recuperer_administrateur()

            if pseudo_connecte == administrateur or pseudo_connecte in tache["comptes_associes"]:
                tache["en_cours"] = False

            else:
                print(f"Seul le compte {administrateur} ou un compte lié à la tâche {nom} peut compléter celle-ci")
    

    # ------------------------------------------------------------------------------------------------------------------------------------------------


    def lister_taches(self):

        """
        L'utilisateur peut afficher toutes les tâches auxquelles il est associé (sauf si il n'est associé à aucune tâche)
        Cependant, l'administrateur peut afficher toutes les tâches existantes (sauf si aucune n'existe)

        Exemple : 
            lister_taches()
        """

        if self.systeme_compte.administrateur_connecte():

            if not self.taches:
                print("aucune tâche n'existe dans le système")

            else:
                self.afficher_taches(self.taches)

        else:

            pseudo_connecte = self.systeme_compte.pseudo_connecte
            taches_a_afficher = self.taches_associees_compte(pseudo_connecte)

            if not taches_a_afficher:
                print(f"Le compte {pseudo_connecte} n'est associé à aucune tache")

            else:
                self.afficher_taches(taches_a_afficher)
    

    # ------------------------------------------------------------------------------------------------------------------------------------------------


    def vider_taches(self):

        """
        L'Administrateur peut vider la liste des tâches s'il est connecté

        Exemple : 
            vider_taches()
        """

        if self.systeme_compte.administrateur_connecte():

            self.taches = []
            print("La liste des tâches à été vidée avec succès")

        else:

            administrateur = self.systeme_compte.recuperer_administrateur()
            print(f"Seul {administrateur} peut vider la liste des tâches")
    

# ------------------------------------------------------------------------------------------------------------------------------------------------

    
def main():

    """
    Le programme principal qui représente le système de commandes
    On peut utiliser n'importe quelle fonctionnalité des systèmes de comptes/taches
    Deux autres commandes permettent d'afficher la liste des commandes (afficher-commandes) et quitter le programme (end)
    """

    sc = SystemeComptes()
    systeme_taches = SystemeTaches(sc)

    commande = " "
    prompt = systeme_taches.systeme_compte.pseudo_connecte
    print(f"{prompt}> Bienvenue : ")

    affichage_commandes = f"{prompt}> veuillez saisir une commande entre\n" + \
             "- ajouter\n" + \
             "- retirer\n" + \
             "- completer\n" + \
             "- liste\n" + \
             "- vider\n" + \
             "- ajouter-compte\n" + \
             "- supprimer-compte\n" + \
             "- connecter\n" + \
             "- afficher-commandes\n" + \
             "- end\n"

    print(affichage_commandes)
             
    while commande != "end":

        prompt = systeme_taches.systeme_compte.pseudo_connecte
        commande = input(f"{prompt}>")

        if (commande == "ajouter"):

            nom = input("saisissez le nom de la tache : ")
            description = input("saisissez la description de la tache : ")
            systeme_taches.ajouter_tache(nom, description)

        elif (commande == "retirer"):

            nom = input("saisissez le nom de la tache : ")
            systeme_taches.retirer_tache(nom)

        elif (commande == "completer"):

            nom = input("saisissez le nom de la tache : ")
            systeme_taches.completer_tache(nom)

        elif (commande == "liste"):

            systeme_taches.lister_taches()

        elif (commande == "vider"):

            systeme_taches.vider_taches()

        elif (commande == "ajouter-compte"):

            pseudo = input("saisissez un pseudo : ")
            systeme_taches.systeme_compte.ajouter_compte(pseudo)

        elif (commande == "supprimer-compte"):

            pseudo = input("saisissez un pseudo : ")
            systeme_taches.systeme_compte.supprimer_compte(pseudo)

        elif (commande == "connecter"):

            pseudo = input("saisissez un pseudo : ")
            systeme_taches.systeme_compte.connecter_compte(pseudo)

        elif (commande == "afficher-commandes"):

            print(affichage_commandes)

        elif (commande != "end"):
            
            print("La commande n'existe pas")


    print("Merci de votre utilisation ! ")


# ------------------------------------------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()