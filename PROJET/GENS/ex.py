class Livreur:
    def __init__(self, nom="", zone_de_livraison="", nombre_de_livraisons=0, note=0.0):
        self.__nom = nom
        self.__zone_de_livraison = zone_de_livraison
        self.__nombre_de_livraisons = nombre_de_livraisons
        self.__note = note
        self.__liste_de_commandes = []
    def get__nom(self):
        return self.__nom
    def set_nom(self, nom):
        self.__nom = nom
    def get__zone_de_livraison (self):
        return self.__zone_de_livraison 
    def set_nom(self, zone_de_livraison ):
        self.__zone_de_livraison  = zone_de_livraison 
    def get__nombre_de_livraisons (self):
        return self.__nombre_de_livraisons 
    def set__nombre_de_livraisons (self, nombre_de_livraisons ):
        self.__nombre_de_livraisons  = nombre_de_livraisons 
    def get__note(self):
        return self.__note
    def set_note(self, note):
        self.__note= note
    
    def ajouter_commande(self, commande):
        self.__liste_de_commandes.append(commande)

    def retirer_commande(self, commande):
        self.__liste_de_commandes.remove(commande)

    def afficher_liste_de_commandes(self):
        for commande in self.__liste_de_commandes:
            print(commande)

class Client:
    def __init__(self, nom="", adresse=""):
        self.__nom = nom
        self.__adresse = adresse
        self.__liste_de_commandes = []

    def get__nom(self):
        return self.__nom
    def set_nom(self, nom):
        self.__nom = nom
    def get__adresse(self):
        return self.__adresse
    def set_adresse(self, adresse):
        self.__adresse= adresse

    def ajouter_commande(self, commande):
        self.__liste_de_commandes.append(commande)

    def retirer_commande(self, commande):
        self.__liste_de_commandes.remove(commande)

    def afficher_liste_de_commandes(self):
        for commande in self.__liste_de_commandes:
            print(commande)

class Command(Livreur):
    def __init__(self, nom_du_client="", adresse_du_client="", nom_du_livreur="", adresse_du_livreur="", etat="en cours de préparation", note=0.0):
        super().__init__ (self,nom_du_livreur, ) 
        self.__nom_du_client = nom_du_client
        self.__adresse_du_client = adresse_du_client
        self.__adresse_du_livreur = adresse_du_livreur
        self.__etat = etat
        self.__note= note
        self.liste_prix = []
    def get__nom_du_client(self):
        return self.__nom_du_client
    def set_nom_du_client(self, nom_du_client):
        self.__nom_du_client = nom_du_client
    def get__adresse_du_client(self):
        return self.__adresse_du_client
    def set__adresse_du_client(self, adresse_du_client):
        self.__adresse_du_client=adresse_du_client
    def get__adresse_du_livreur(self):
        return self.__adresse_du_livreur
    def set__adresse_du_livreur(self, adresse_du_livreur):
        self.__adresse_du_livreur =adresse_du_livreur
    def get__etat(self):
        return self.__etat
    def set_etat(self, etat):
        self.__etat = etat
    def get__note(self):
        return self.__note
    def set_note(self, note):
        self.__note = note

    def changer_etat(self,nouvel_etat):
        self.etat = nouvel_etat

    def donner_note(self, note):
        self.note = note
        
    def ajouter_prix(self, prix):
        self.liste_prix.append(prix)
        
    def get_total(self):
        return sum(self.liste_prix)
class Menu:
    def afficher_options(self):
        print("1. Passer une commande")
        print("2. Afficher la liste des commandes")
        print("3. Afficher les livreurs disponibles")
        print("4. Quitter l'application")
        choix = input("Que souhaitez-vous faire ? ")
        if choix == "1":
            self.passer_commande()
        elif choix == "2":
            self.afficher_liste_des_commandes()
        elif choix == "3":
            self.afficher_livreurs_disponibles()
        elif choix == "4":
            print("Au revoir !")
        else:
            print("Choix invalide, veuillez ressayer.")
            self.afficher_options()

    def passer_commande(self):
        nom_du_client = input("Entrez votre nom : ")
        adresse_du_client = input("Entrez votre adresse : ")
        print("Voici la liste des livreurs disponibles :")
        self.afficher_livreurs_disponibles()
        nom_du_livreur = input("Entrez le nom du livreur choisi : ")
        adresse_du_livreur = input("Entrez l'adresse du livreur choisi : ")
        commande = input("entrer la commande")
        commande = Command(nom_du_client, adresse_du_client, nom_du_livreur, adresse_du_livreur)
        choix = ""
        while choix != "1":
            choix = input("Entrez le nom d'un produit (ou 1 pour terminer la commande) : ")
            if choix != "1":
                prix = float(input("Entrez le prix du produit : "))
                commande.ajouter_prix(prix)
        print("La commande a été passée avec succès !")
        total = commande.get_total()
        print(f"Le prix total de la commande est de {total} dh.")
        self.liste_de_commandes.append(commande)
        
    