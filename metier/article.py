

class Article:
    NOM_BASE_DE_DONNEE = "article"

    def __init__(self, nom_article, id_article, nb_avis_article, prix_article, made_in_africa,
                 site_origine, note_article, categorie_article, pays_origine_article, date_article):

        self.nom_article = nom_article
        self.id_article = id_article
        self.nb_avis_article = nb_avis_article
        self.prix_article = prix_article
        self.made_in_africa = made_in_africa
        self.site_origine = site_origine
        self.note_article = note_article
        self.categorie_article = categorie_article
        self.pays_origine_article = pays_origine_article
        self.date_article = date_article


  
