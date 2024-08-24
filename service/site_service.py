
from dao.site_dao import SiteDao


class SiteService:

    def __init__(self):
        pass

    @staticmethod
    def add_site_in_db(site):
        return SiteDao.create(site)

    @staticmethod
    def get_site(site):
        return SiteDao.find_site_by_name(site)

    @staticmethod
    def get_all_sitess_from_db():
        return SiteDao.find_all_sites()

    @staticmethod
    def get_all_sites_id_from_db():
        """
        Récupère un certain nombre d'article en base
        :return: une liste de article
        :rtype: list of Article
        """
        sites = SiteDao.find_all()
        liste_id = [site.id_article for site in sites]
        return liste_id

    @staticmethod
    def delete_site_from_db(site):
        return SiteDao.delete(site)
