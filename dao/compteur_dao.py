import psycopg2

from dao.abstract_dao import AbstractDao
from dao.pool_connection import PoolConnection
from metier.compteur import Compteur


class CompteurDao(AbstractDao):

    @staticmethod
    def create(compteur):
        """
        Méthode permettant d'ajouter un compteur dans notre base de données.

        :param compteur: l'objet python associé à un compteur à ajouter
        :type compteur: Compteur
        :return: l'objet python associé à un compteur
        :rtype: Compteur
        """

        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            # On envoie au serveur la requête SQL
            curseur.execute(
                "INSERT INTO compteur (id_compteur, nom_compteur, compte)"
                " VALUES (%s, %s, %s) RETURNING id_compteur",
                (compteur.id_compteur,
                 compteur.nom_compteur,
                 compteur.compte))
            # On récupère l'id généré
            compteur.id_article = curseur.fetchone()[0]

            # On enregistre la transaction en base
            connexion.commit()
        except psycopg2.Error as error:
            # la transaction est annulée
            connexion.rollback()
            raise error
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)

        return compteur

    @staticmethod
    def find_by_id(id):
        """
        Méthode permettant de chercher un compteur grâce à son id et retourne l'objet python associé

        :param id: l'identifiant du compteur recherché
        :type id: int
        :return: l'objet python associé à un compteur
        :rtype: Compteur
        """
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "SELECT *"
                "\n\t FROM compteur "
                "\n\t WHERE id_compteur= %s",
                (id,))
            resultat = curseur.fetchone()
            compteur = None
            # Si on a un résultat

            if resultat:
                compteur = Compteur(
                    id_compteur=resultat[0],
                    nom_compteur=resultat[1],
                    compte=resultat[2])

        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return compteur

    @staticmethod
    def find_by_name(name):
        """
        Méthode permettant de chercher un compteur grâce à son nom et retourne l'objet python associé

        :param name: le nom du compteur recherché
        :type name: str
        :return: l'objet python associé à un compteur
        :rtype: Compteur
        """
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "SELECT *"
                "\n\t FROM compteur "
                "\n\t WHERE nom_compteur= %s",
                (name,))
            resultat = curseur.fetchone()
            compteur = None
            # Si on a un résultat

            if resultat:
                compteur = Compteur(
                    id_compteur=resultat[0],
                    nom_compteur=resultat[1],
                    compte=resultat[2])

        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return compteur

    @staticmethod
    def find_all():
        """
        Méthode permettant de chercher tous les compteurs présents dans une base de donnée

        :return: tous les compteurs d'une table sous forme de liste d'objets python associé
        :rtype: list
        """
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "SELECT *"
                "\n\t FROM compteur"
            )
            resultats = curseur.fetchall()
            compteurs = []
            for resultat in resultats:
                compteurs.append(
                    compteur = Compteur(
                    id_compteur=resultat[0],
                    nom_compteur=resultat[1],
                    compte=resultat[2])
                )
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return compteurs

    @staticmethod
    def update(compteur):
        """
        Méthode permettant de mettre à jour les informations d'un compteur dans la base

        :param compteur: l'objet python associé à un compteur à mettre à jour
        :type compteur: Compteur
        :return: une variable booléenne : True si le compteur est mis à jour, False sinon
        :rtype: bool
        """
        updated = False
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "UPDATE compteur"
                "\n\t SET "
                "\n\t nom_compteur = %s"
                "\n\t, compte = %s"
                "\n\t WHERE id_compteur = %s",
                (compteur.nom_compteur,
                 compteur.compte,
                 compteur.id_compteur))
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
    def delete(nom_compteur):
        """
        Méthode permettant de supprimer un compteur dans la base

        :param pokemon: l'objet python associé à un compteur à supprimer
        :type pokemon: Compteur
        :return: une variable booléenne : True si le compteur est supprimer, False sinon
        :rtype: bool
        """
        deleted = False
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            # On envoie au serveur la requête SQL
            curseur.execute(
                "DELETE FROM compteur WHERE nom_compteur=%s;",
                (nom_compteur,))

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
