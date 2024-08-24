from service.article_service import ArticleService
from metier.article import Article

import json
import pandas as pd
from matplotlib import pyplot as plt


#REFLECHIR A LA GESTION DES CLEE POUR LES DIFFERENT IDENTIFIANTS

supermarcher_ci_1 = pd.read_json("supermarcher_ug_08-06.json")
supermarcher_ci_2 = pd.read_json("supermarcher_ug_08-07.json")
supermarcher_ci_3 = pd.read_json("supermarcher_ug_08-09.json")
supermarcher_ci_4 = pd.read_json("supermarcher_ug_08-10.json")
supermarcher_ci_5 = pd.read_json("supermarcher_ug_08-11.json")
supermarcher_ci_6 = pd.read_json("supermarcher_ug_08-12.json")
supermarcher_ci_7 = pd.read_json("supermarcher_ug_08-13.json")
supermarcher_ci_8 = pd.read_json("supermarcher_ug_08-14.json")
supermarcher_ci_9 = pd.read_json("supermarcher_ug_08-15.json")


supermarcher_ci_2["date"]='2021-08-07'
supermarcher_ci_3["date"]='2021-08-09'
supermarcher_ci_4["date"]='2021-08-10'
supermarcher_ci_5["date"]='2021-08-11'
supermarcher_ci_6["date"]='2021-08-12'
supermarcher_ci_7["date"]='2021-08-13'
supermarcher_ci_8["date"]='2021-08-14'
supermarcher_ci_9["date"]='2021-08-15'






init_articles= pd.concat([supermarcher_ci_9, supermarcher_ci_2, supermarcher_ci_3, supermarcher_ci_4, supermarcher_ci_5, supermarcher_ci_6, supermarcher_ci_7, supermarcher_ci_8])


def transfo_int(x):
    try:
        x=float(x)
    except:
        x=0
    return(x)

init_articles["Nb_avis"] = init_articles["Nb_avis"].apply(transfo_int)
init_articles["prix"] = init_articles["prix"].apply(transfo_int)


init_articles["Nb_avis"]=init_articles["Nb_avis"].fillna(0)                 # on remplace les valeurs manquante pour les avis par 0 avis
init_articles["note"]=init_articles["note"].fillna(init_articles["note"].mean()) #  on remplace les valeurs manquante pour les note par la moyenne pour ne pas biaiser les calculs d'analyse


liste_nom = [ nom for nom in init_articles['Nom']]
liste_avis = [ avis for avis in init_articles['Nb_avis']]
liste_prix = [ prix for prix in init_articles['prix']]
liste_note = [ note for note in init_articles['note']]
liste_cat = [ cat for cat in init_articles['categorie']]
liste_site = [ site for site in init_articles['site origine']]
liste_pays = [ pays for pays in init_articles['pays']]
liste_made = [ 'False' for i in init_articles['Nom']]
liste_date = [date for date in init_articles['date']]



for i in range (len(liste_nom)):
    article=Article(nom_article=liste_nom[i], id_article=None, nb_avis_article=liste_avis[i], prix_article=liste_prix[i], made_in_africa=liste_made[i],
    site_origine=liste_site[i], note_article=liste_note[i],categorie_article=liste_cat[i], pays_origine_article=liste_pays[i], date_article=liste_date[i])
    ArticleService.add_article_to_db(article)