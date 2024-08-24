from PyInquirer import prompt, Separator

from view.abstract_vue import AbstractView
from PIL import Image
from service.article_service import ArticleService
from time_print import delay_print
from service.pays_service import PaysService

class TrandyCountryChoiceView(AbstractView):

    def __init__(self): 


        self.pays_objet = PaysService.get_all_pays()
        self.pays_nom = [objet_pays.nom_pays for objet_pays in self.pays_objet]
        # Création du menu
        choix_pays = self.pays_nom
        choix_pays.append(Separator())
        choix_pays.append("Retour au menu principal")

        self.questions = [
            {
                'type': 'list',
                'name': 'choix_menu',
                'message': "Menu : Veuillez choisir un pays",
                'choices': choix_pays
            }
        ]






    def display_info(self):
        
        from service.pays_service import PaysService
        # dataframe_articles = ArticleService.get_article_dataframe()
        # dataframe_articles[dataframe_articles.nb_avis_article >= 10].groupby(["pays_origine_article","categorie_article"])
        # class_pays = dataframe_articles[['categorie_article','pays_origine_article']].value_counts(normalize=True)*100
        # print(class_pays)# classes distributions
        dataframe_pays = PaysService.get_pays_dataframe()
        print(""" Informations interessante :
        Le pays qui a la plus forte croissance économique est :           {}  
                                                                avec {} pourcent de croissance annuelle (2020)
        Le pays qui a la part d'exportation relative la plus élevée est : {} 
        Le Pays qui a la part d'importation relative la plus élevée est : {}

        """.format(   [value for index, value in dataframe_pays[dataframe_pays.taux_croissance_pays == dataframe_pays["taux_croissance_pays"].max()]["nom_pays"].items()][0],
          dataframe_pays["taux_croissance_pays"].max(),
          [ value for index, value in dataframe_pays[dataframe_pays.part_exportation_intra_pays == dataframe_pays["part_exportation_intra_pays"].max()]["nom_pays"].items()][0],
          [ value for index, value in dataframe_pays[dataframe_pays.part_exportation_intra_pays == dataframe_pays["part_exportation_intra_pays"].min()]["nom_pays"].items()][0]))
        
        

    def make_choice(self):

        reponse = prompt(self.questions)
 
        if reponse['choix_menu'] == 'Retour au menu principal'  :
            from service.super_utilisateur_service import SuperUtilisateurService
            from view.menu_principal_view import MenuPrincipalView
            from view.super_menu_principal_view import SuperMenuPrincipalView
            try:
                AbstractView.session.user_name == SuperUtilisateurService.get_super_user_by_name(AbstractView.session.user_name)[0]
                next_view=SuperMenuPrincipalView()
            except:
                next_view = MenuPrincipalView()
        else :
            # from view.menu_principal_view import MenuPrincipalView
            # next_view =  MenuPrincipalView()
            index = self.pays_nom.index(reponse["choix_menu"])
            objet_pays = self.pays_objet[index]
            from view.trandy_items_country_view import TrandyItemsCountryView
            next_view=TrandyItemsCountryView(objet_pays)
            # dataframe_articles = ArticleService.get_article_dataframe()
            # dataframe_articles[dataframe_articles.nb_avis_article >= 10].groupby(["pays_origine_article","categorie_article"])
            # class_pays = dataframe_articles[['categorie_article','pays_origine_article']].value_counts(normalize=True)*100
            # print(class_pays)# classes distributions

            

        
        return next_view
