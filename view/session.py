
class Session:
    def __init__(self):
        """
        Définition des variables que l'on stocke en session
        Le syntaxe
        ref:type = valeur
        permet de donner le type des variables. Utile pour l'autocompletion.
        """
        self.id_dresseur = None
        self.id_utilisateur = None
        self.user_name = None
        self.pays_origine_user = None  # objet pays
        self.type_de_produit_commerce = None #objet categorie
        