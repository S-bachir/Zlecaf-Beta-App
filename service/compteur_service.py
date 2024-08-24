
from dao.compteur_dao import CompteurDao


class CompteurService:

    def __init__(self):
        pass

    @staticmethod
    def get_compteur_from_db_by_id(id_compteur):
        """
        Récupère un compteur grâce à son nom
        :param id_compteur:
        :type id_compteur:
        :return:
        :rtype:
        """
        return CompteurDao.find_by_id(id_compteur)

    @staticmethod
    def get_compteur_by_name(name_compteur):
        return CompteurDao.find_by_name(name_compteur)



    @staticmethod
    def get_all_compteurs_from_db():
        """
        Récupère un certain nombre d'article en base
        :return: une liste de article
        :rtype: list of Article
        """
        return CompteurDao.find_all()



    @staticmethod
    def add_compteur_to_db(compteur):
        """

        :param article:
        :type article:
        :return:
        :rtype:
        """

        return CompteurDao.create(compteur)

    @staticmethod
    def update_compteur_in_db(compteur):
        """

        :param article:
        :type article:
        :return:
        :rtype:
        """
        return CompteurDao.update(compteur)

    @staticmethod
    def delete_compteur_from_db_with_name(compteur_name):
        return CompteurDao.delete(compteur_name)


