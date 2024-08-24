
from pandas.io.sql import read_sql_query
from dao.article_dao import ArticleDao


class ArticleService:

    def __init__(self):
        pass

    @staticmethod
    def get_article_from_db_by_id(id_article):
        """
        Récupère un article grâce à son nom
        :param id_article:
        :type id_article:
        :return:
        :rtype:
        """
        return ArticleDao.find_by_id(id_article)

    @staticmethod
    def get_article_by_name(name_article):
        return ArticleDao.find_by_name(name_article)

    @staticmethod
    def get_info_article_by_id(id_article):
        return ("""Le nom de l'article:                  {}
                 Son prix :                           {}  
                 son pays d'origine :                 {}
                 made in africa :                     {}
                 catégorie de l'article:              {}
  
        
        """.format(
            ArticleDao.find_by_id(id_article).nom_article,
            ArticleDao.find_by_id(id_article).prix_article,
            ArticleDao.find_by_id(id_article).pays_origine_article,
            ArticleDao.find_by_id(id_article).made_in_africa,
            ArticleDao.find_by_id(id_article).categorie_article,
        ))

    @staticmethod
    def get_all_articles_from_db():
        """
        Récupère un certain nombre d'article en base
        :return: une liste de article
        :rtype: list of Article
        """
        return ArticleDao.find_all()

    @staticmethod
    def get_all_articles_id_from_db():
        """
        Récupère un certain nombre d'article en base
        :return: une liste de article
        :rtype: list of Article
        """
        articles = ArticleDao.find_all()
        liste_id = [article.id_article for article in articles ]
        return liste_id

    @staticmethod
    def get_all_articles_name_from_db():
        """
        Récupère un certain nombre d'article en base
        :return: une liste de article
        :rtype: list of Article
        """
        articles = ArticleDao.find_all()
        liste_nom = [article.nom_article for article in articles ]
        return liste_nom

    @staticmethod
    def add_article_to_db(article):
        """

        :param article:
        :type article:
        :return:
        :rtype:
        """

        return ArticleDao.create(article)

    @staticmethod
    def update_article_in_db(article):
        """

        :param article:
        :type article:
        :return:
        :rtype:
        """
        return ArticleDao.update(article)

    @staticmethod
    def delete_article_from_db_with_name(article_name):
        return ArticleDao.delete(article_name)

    @staticmethod
    def get_article_dataframe():
        return ArticleDao.dataframe()

   

    


