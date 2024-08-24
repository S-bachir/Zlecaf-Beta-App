import psycopg2

from dao.abstract_dao import AbstractDao
from dao.pool_connection import PoolConnection
from metier.site import Site
from service.compteur_service import CompteurService

class SiteDao(AbstractDao):

    @staticmethod
    def create(site):
        from service.site_service import SiteService
        if site.id_site == None:
            compteur_site = CompteurService.get_compteur_by_name("compteur_site")
            compteur_site.compte +=1
            site.id_site = compteur_site.compte
            CompteurService.update_compteur_in_db(compteur_site)
        elif site.id_article in SiteService.get_all_sites_id_from_db():
            compteur_site = CompteurService.get_compteur_by_name("compteur_site")
            compteur_site.compte +=1
            site.id_site = compteur_site.compte
            CompteurService.update_compteur_in_db(compteur_site)


        """
        Insère une ligne en base avec l'objet en paramètre.
        Retourne l'objet mise à jour avec son id de la base
        """

        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            # On envoie au serveur la requête SQL
            curseur.execute(
                "INSERT INTO site (id_site, nom_site, url_site, type_site, pays_hebergement_site )"
                " VALUES (%s, %s, %s, %s, %s);",
                (site.id_site, site.nom_site, site.url_site, site.type_site, site.pays_hebergement_site))

            # On enregistre la transaction en base
            connexion.commit()
        except psycopg2.Error as error:
            # la transaction est annulée
            connexion.rollback()
            raise error
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)

        return site

    @staticmethod
    def find_site_by_id(id_site):
        """
        Va chercher une élément de la base grâce à son id et retourne l'objet python associé
        """
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "SELECT *"
                "\n\t FROM site"
                "\n\t WHERE id_site= %s",
                (id_site,))
            resultat = curseur.fetchone()
            site = None

            # Si on a un résultat

            if resultat:
                site = Site(
                    id_site=resultat[0],
                    nom_site=resultat[1],
                    url_site=resultat[2],
                    type_site=resultat[3],
                    pays_hebergement_site = resultat[4])
                    

        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return site



    @staticmethod
    def find_site_by_name(name_site):
        """
        Va chercher une élément de la base grâce à son id et retourne l'objet python associé
        """
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "SELECT *"
                "\n\t FROM site"
                "\n\t WHERE nom_site= %s",
                (name_site,))
            resultat = curseur.fetchone()
            site = None

            # Si on a un résultat

            if resultat:
                site = Site(
                    id_site=resultat[0],
                    nom_site=resultat[1],
                    url_site=resultat[2],
                    type_site=resultat[3],
                    pays_hebergement_site = resultat[4])
                    

        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return site

    @staticmethod
    def find_all_sites():
        """
        Méthode permettant de chercher tous les pokémons présents dans une base de donnée

        :return: tous les pokémons d'une table sous forme de liste d'objets python associé
        :rtype: list
        """
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "SELECT *"
                "\n\t FROM site"
            )
            resultats = curseur.fetchall()
            sites = []
            for resultat in resultats:
                sites.append(
                    Site(
                    id_site=resultat[0],
                    nom_site=resultat[1],
                    url_site=resultat[2],
                    type_site=resultat[3],
                    pays_hebergement_site = resultat[4])
                )
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return sites

    @staticmethod
    def delete(site):
        """
        Supprime la ligne en base représentant l'objet en paramètre
        :return si une supression à eu lieu
        :rtype bool
        """
        deleted = False
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            # On envoie au serveur la requête SQL
            curseur.execute(
                "DELETE FROM site WHERE id_site=%s;",
                (site.id_site,))

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
    
