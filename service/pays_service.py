from dao.pays_dao import PaysDao





class PaysService:

    def __init__(self):
        pass

    @staticmethod
    def get_pays_by_name(name):
        return PaysDao.find_pays_by_name(name)

    @staticmethod
    def add_pays_to_db(pays):
        return PaysDao.create(pays)


    @staticmethod
    def update_info_pays (pays):
        """
        :param pays: 
        :type pays:
        :return:
        :rtype:
        """
        return PaysDao.update(pays)

    @staticmethod
    def get_all_pays():
        return PaysDao.find_all_pays()

    @staticmethod
    def get_pays_dataframe():
        return PaysDao.dataframe()




