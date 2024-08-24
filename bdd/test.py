from service.article_service import ArticleService
from metier.article import Article


# articles = ArticleService.get_all_articles_from_db()

# for article in articles:
#     if "Princesse Tatie" in str(article.nom_article):
#         article.made_in_africa = 'True'
#         ArticleService.update_article_in_db(article)


# from service.compteur_service import CompteurService
# from metier.compteur import Compteur
# compteur_article = Compteur(1, "compteur_article", 0)
# compteur_site = Compteur(2, "compteur_site", 0)
# Compteur_utilisateur = Compteur(3, "compteur_utilisateur", 0)
# compteur_super_utilisateur = Compteur(4, "compteur_super_utilisateur", 0)
# compteur_pays = Compteur(5, "compteur_pays", 0)
#compteur_marque = Compteur(6, "compteur_marque", 0)
# CompteurService.add_compteur_to_db(compteur_article)
# CompteurService.add_compteur_to_db(compteur_site)
# CompteurService.add_compteur_to_db(Compteur_utilisateur)
# CompteurService.add_compteur_to_db(compteur_super_utilisateur)
# CompteurService.add_compteur_to_db(compteur_pays)
#CompteurService.add_compteur_to_db(compteur_marque)


# def cat_change(x):
#     indices = []
#     i = 0
#     while(i < len(x)):
#         if '/' in x[i:]:
#             indices.append(x[i:].index('/') + i)
#             i = indices[-1] + 1
#         else:
#              break
#     try:
#         x=x[:indices[1]]
#     except:
#         pass
#     return x

# articles = ArticleService.get_all_articles_from_db()

# for article in articles:
#     if article.pays_origine_article == "Cote d'ivoire": 
#         article.pays_origine_article = "Cote d'Ivoire"
#         ArticleService.update_article_in_db(article)
