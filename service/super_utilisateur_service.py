from dao.super_utilisateur_dao import SuperUtilisateurDao


class SuperUtilisateurService:

    def __init__(self):
        pass

    @staticmethod
    def add_super_user_in_db(pseudo, mdp):
        return SuperUtilisateurDao.create(pseudo, mdp)

    @staticmethod
    def get_super_user_by_name(pseudo):
        return SuperUtilisateurDao.find_by_name(pseudo)

    @staticmethod
    def update_info_super_user(pseudo, mdp):
        return SuperUtilisateurDao.update(pseudo, mdp)

    @staticmethod
    def get_all_super_user():
        return SuperUtilisateurDao.find_all_pseudo()


