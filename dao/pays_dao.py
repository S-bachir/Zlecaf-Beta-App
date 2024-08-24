import psycopg2

from dao.abstract_dao import AbstractDao
from dao.pool_connection import PoolConnection
from metier.pays import Pays
from service.compteur_service import CompteurService

class PaysDao(AbstractDao):

    @staticmethod
    def create(pays):

        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            # On envoie au serveur la requête SQL
            curseur.execute(
                "INSERT INTO pays ( nom_pays, PIB_pays, population_pays, taux_demographique_pays, taux_croissance_pays, inflation_pays, part_exportation_intra_pays, exportation_intra_pays)"
                " VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING nom_pays;",
                ( 	pays.nom_pays,
	                pays.PIB_pays,
	                pays.population_pays,
	                pays.taux_demographique_pays,
	                pays.taux_croissance_pays,
	                pays.inflation_pays,
	                pays.part_exportation_intra_pays,
	                pays.exportation_intra_pays))
            resultat = curseur.fetchone()[0]

            # On enregistre la transaction en base
            connexion.commit()
        except psycopg2.Error as error:
            # la transaction est annulée
            connexion.rollback()
            raise error
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)

        return resultat

    @staticmethod
    def update(pays):
        """Met à jour la ligne en base de donnée associé à l'objet métier en paramètre"""
        updated = False
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()

        try:
            curseur.execute(
                "UPDATE pays"
                "\n\tSET "
	            "\n\t PIB_pays = %s"
	            "\n\t population_pays = %s"
	            "\n\t taux_demographique_pays = %s"
	            "\n\t taux_croissance_pays = %s"
	            "\n\t inflation_pays = %s"
	            "\n\t part_exportation_intra_pays = %s"
	            "\n\t exportation_intra_pays = %s"
                "\n\t WHERE nom_pays=  %s",
                (pays.PIB_pays, 
                pays.population_pays, 
                pays.taux_demographique_pays, 
                pays.taux_croissance_pays, 
                pays.inflation_pays, 
                pays.part_exportation_intra_pays, 
                pays.exportation_intra_pays,
                pays.nom_pays ))

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
    def find_pays_by_name(name):
        """Va chercher une élément de la base grâce à son id et retourne l'objet python associé"""
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "SELECT *"
                "\n\t FROM pays "
                "\n\t WHERE nom_pays = %s",
                (name))
            resultat = curseur.fetchone()
            pays = None
            # Si on a un résultat

            if resultat:
                pays = Pays(
                    nom_pays = resultat[0],
                    PIB_pays = resultat[1], 
                    population_pays = resultat[2], 
                    taux_demographique_pays = resultat[3], 
                    taux_croissance_pays = resultat[4], 
                    inflation_pays = resultat[5], 
                    part_exportation_intra_pays = resultat[6], 
                    exportation_intra_pays = resultat[7]                  
                )

        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return pays


    @staticmethod
    def find_all_pays():
        """Retourne tous les éléments d'une table sous forme de liste d'objets python"""
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "SELECT *"
                "\n\t FROM pays"

            )
            resultats = curseur.fetchall()
            pays_liste = []
            for resultat in resultats:
                pays_liste.append(Pays(
                    nom_pays = resultat[0],
                    PIB_pays = resultat[1], 
                    population_pays = resultat[2], 
                    taux_demographique_pays = resultat[3], 
                    taux_croissance_pays = resultat[4], 
                    inflation_pays = resultat[5], 
                    part_exportation_intra_pays = resultat[6], 
                    exportation_intra_pays = resultat[7]      
                ))
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return pays_liste

    @staticmethod
    def dataframe():

        import pandas as pd
        connexion = PoolConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            # On envoie au serveur la requête SQL
            curseur.execute(
                "SELECT * FROM pays ;")
            
            dataframe = pd.read_sql_query('''SELECT * FROM pays ;''',connexion)
            # on verifie s'il y a eu des supressions
     
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
              
        return dataframe