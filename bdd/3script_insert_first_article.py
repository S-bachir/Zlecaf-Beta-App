from service.article_service import ArticleService
from metier.article import Article

import json
import pandas as pd
from matplotlib import pyplot as plt

supermarcher_ci = pd.read_json("supermarcher_ci.json")
supermarcher_sn = pd.read_json("supermarcher_sn.json")
supermarcher_tn = pd.read_json("supermarcher_tn.json")
supermarcher_dz = pd.read_json("supermarcher_dz.json")
supermarcher_ng = pd.read_json("supermarcher_ng.json")
supermarcher_ma = pd.read_json("supermarcher_ma.json")
supermarcher_ke = pd.read_json("supermarcher_ke.json")
supermarcher_ug = pd.read_json("supermarcher_ug.json")

init_articles= pd.concat([supermarcher_ci, supermarcher_sn, supermarcher_ma, supermarcher_tn, supermarcher_dz, supermarcher_ng, supermarcher_ke, supermarcher_ug])


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
liste_date= [ '2021-08-01' for nom in init_articles['Nom']]



for i in range (len(liste_nom)):
    article=Article(nom_article=liste_nom[i], id_article=i, nb_avis_article=liste_avis[i], prix_article=liste_prix[i], made_in_africa=liste_made[i],
    site_origine=liste_site[i], note_article=liste_note[i],categorie_article=liste_cat[i], pays_origine_article=liste_pays[i], date_article=liste_date[i])
    ArticleService.add_article_to_db(article)