import psycopg2

from dao.abstract_dao import AbstractDao
from dao.pool_connection import PoolConnection
from metier.article import Article
from service.compteur_service import CompteurService


class ArticleDao(AbstractDao):

    @staticmethod
    def create(article):
        """
        Méthode permettant d'ajouter un article dans notre base de données.

        :param article: l'objet python associé à un article à ajouter
        :type article: Article
        :return: l'objet python associé à un article
        :rtype: Article
        """
        from service.article_service import ArticleService
        if article.id_article == None:
            compteur_article = CompteurService.get_compteur_by_name("compteur_article")
            compteur_article.compte +=1
            article.id_article = compteur_article.compte
            CompteurService.update_compteur_in_db(compteur_article)
        elif article.id_article in ArticleService.get_all_articles_id_from_db():
            compteur_article = CompteurService.get_compteur_by_name("compteur_article")
            compteur_article.compte +=1
            article.id_article = compteur_article.compte
            CompteurService.update_compteur_in_db(compteur_article)

     


        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            # On envoie au serveur la requête SQL
            curseur.execute(
                "INSERT INTO article (id_article, nom_article, nb_avis_article,"
                "prix_article, made_in_africa, site_origine, note_article,"
                "categorie_article, pays_origine_article, date_article)"
                " VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s) RETURNING id_article;",
                (article.id_article,
                 article.nom_article,
                 article.nb_avis_article,
                 article.prix_article,
                 article.made_in_africa,
                 article.site_origine,
                 article.note_article,
                 article.categorie_article,
                 article.pays_origine_article,
                 article.date_article))
            # On récupère l'id généré
            article.id_article = curseur.fetchone()[0]

            # On enregistre la transaction en base
            connexion.commit()
        except psycopg2.Error as error:
            # la transaction est annulée
            connexion.rollback()
            raise error
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)

        return article

    @staticmethod
    def find_by_id(id):
        """
        Méthode permettant de chercher un article grâce à son id et retourne l'objet python associé

        :param id: l'identifiant du article recherché
        :type id: int
        :return: l'objet python associé à un article
        :rtype: Article
        """
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "SELECT *"
                "\n\t FROM article "
                "\n\t WHERE id_article= %s",
                (id,))
            resultat = curseur.fetchone()
            article = None
            # Si on a un résultat

            if resultat:
                article = Article(
                    id_article=resultat[0],
                    nom_article=resultat[1],
                    nb_avis_article=resultat[2],
                    prix_article=resultat[3],
                    made_in_africa=resultat[4],
                    site_origine=resultat[5],
                    note_article=resultat[6],
                    categorie_article=resultat[7],
                    pays_origine_article= resultat[8],
                    date_article = resultat[9])

        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return article

    @staticmethod
    def find_by_name(name):
        """
        Méthode permettant de chercher un article grâce à son nom et retourne l'objet python associé

        :param name: le nom du article recherché
        :type name: str
        :return: l'objet python associé à un article
        :rtype: Article
        """
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "SELECT *"
                "\n\t FROM article "
                "\n\t WHERE nom_article= %s",
                (name,))
            resultat = curseur.fetchone()
            article = None
            # Si on a un résultat

            if resultat:
                 article = Article(
                    id_article=resultat[0],
                    nom_article=resultat[1],
                    nb_avis_article=resultat[2],
                    prix_article=resultat[3],
                    made_in_africa=resultat[4],
                    site_origine=resultat[5],
                    note_article=resultat[6],
                    categorie_article=resultat[7],
                    pays_origine_article= resultat[8],
                    date_article = resultat[9])

        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return article

    @staticmethod
    def find_all():
        """
        Méthode permettant de chercher tous les articles présents dans une base de donnée

        :return: tous les articles d'une table sous forme de liste d'objets python associé
        :rtype: list
        """
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "SELECT *"
                "\n\t FROM article"
            )
            resultats = curseur.fetchall()
            articles = []
            for resultat in resultats:
                articles.append(
                    Article(
                    id_article=resultat[0],
                    nom_article=resultat[1],
                    nb_avis_article=resultat[2],
                    prix_article=resultat[3],
                    made_in_africa=resultat[4],
                    site_origine=resultat[5],
                    note_article=resultat[6],
                    categorie_article=resultat[7],
                    pays_origine_article=resultat[8],
                    date_article = resultat[9])
                )
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return articles

    @staticmethod
    def update(article):
        """
        Méthode permettant de mettre à jour les informations d'un article dans la base

        :param pokemon: l'objet python associé à un article à mettre à jour
        :type pokemon: Pokemon
        :return: une variable booléenne : True si le article est mis à jour, False sinon
        :rtype: bool
        """
        updated = False
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "UPDATE article"
                "\n\t SET "
                "\n\t nom_article = %s"
                "\n\t, nb_avis_article = %s"
                "\n\t, prix_article = %s"
                "\n\t, made_in_africa = %s"
                "\n\t, site_origine = %s"
                "\n\t, note_article = %s"
                "\n\t, categorie_article = %s"
                "\n\t, pays_origine_article=%s"
                "\n\t, date_article= %s"
                "\n\t WHERE id_article = %s",
                (article.nom_article,
                 article.nb_avis_article,
                 article.prix_article,
                 article.made_in_africa,
                 article.site_origine,
                 article.note_article,
                 article.categorie_article,
                 article.pays_origine_article,
                 article.date_article,
                 article.id_article))
            if curseur.rowcount > 0:
                updated = True

            # On enregistre la transaction en base
            connexion.commit()
        except psycopg2.Error as error:
            # la transaction est annulée
            connexion.rollback()
            raise error
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)

        return updated

    @staticmethod
    def delete(nom_article):
        """
        Méthode permettant de supprimer un article dans la base

        :param pokemon: l'objet python associé à un article à supprimer
        :type pokemon: Pokemon
        :return: une variable booléenne : True si le article est supprimer, False sinon
        :rtype: bool
        """
        deleted = False
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            # On envoie au serveur la requête SQL
            curseur.execute(
                "DELETE FROM article WHERE nom_article=%s;",
                (nom_article,))

            # on verifie s'il y a eu des supressions
            if curseur.rowcount > 0:
                deleted = True

            # On enregistre la transaction en base
            connexion.commit()
        except psycopg2.Error as error:
            # la transaction est annulée
            connexion.rollback()
            raise error
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)

        return deleted

    ###############################################################
    @staticmethod
    def dataframe():
        """
        Méthode permettant de supprimer un article dans la base

        :param pokemon: l'objet python associé à un article à supprimer
        :type pokemon: Pokemon
        :return: une variable booléenne : True si le article est supprimer, False sinon
        :rtype: bool
        """
        import pandas as pd
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            # On envoie au serveur la requête SQL
            curseur.execute(
                "SELECT * FROM article ;")
            
            dataframe = pd.read_sql_query('''SELECT * FROM article ;''',connexion)
            # on verifie s'il y a eu des supressions
     
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
              
        return dataframe

