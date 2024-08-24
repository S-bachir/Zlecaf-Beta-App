from PyInquirer import prompt, Separator

from view.abstract_vue import AbstractView
from PIL import Image
from service.article_service import ArticleService
import time
from service.pays_service import PaysService

class TrandyItemsCountryView(AbstractView):

    def __init__(self, country): 

        self.country = country
        # self.pays_objet = PaysService.get_all_pays()
        # self.pays_nom = [objet_pays.nom_pays for objet_pays in self.pays_objet]
        # # Création du menu
        # choix_pays = self.pays_nom
        # choix_pays.append(Separator())
        # choix_pays.append("Retour au menu principal")

        self.questions = [
            {
                'type': 'list',
                'name': 'choix_menu',
                'message': "Menu : Veuillez choisir un pays",
                'choices': ["Revenir au choix du pays",
                            Separator(),
                            "Retour au menu principal"]
            }
        ]






    def display_info(self):
        country = self.country 
        from service.article_service import ArticleService
        dataframe_articles = ArticleService.get_article_dataframe()

        if  country.nom_pays in dataframe_articles["pays_origine_article"].unique():
            class_pays = dataframe_articles[dataframe_articles['pays_origine_article']==country.nom_pays][["categorie_article","nb_avis_article"]]
            class_pays = class_pays[class_pays.nb_avis_article >= 5]["categorie_article"].value_counts(normalize=True)*100
            print("les catégorie d'article qui ont le plus de succès sont :")
            time.sleep(3)
            
            print(class_pays)# classes distributions
            dataframe_pays = PaysService.get_pays_dataframe()

            time.sleep(3)
            habitant = [value for index, value in dataframe_pays[dataframe_pays.nom_pays == country.nom_pays ]["population_pays"].items()][0]
            habitant=int(habitant)
            habitant=str(habitant)
            print(""" 
            
            
            
            Quelques Informations sur le pays, {}:
            Le population est de :      {} {} {} habitants  
                                        pour un PIB de {} milliard de dollars (US)
                                        et un taux de croissance de {}

            """.format(  country.nom_pays,
            int(habitant[:-6]),
            int(habitant[-6:-3]),
            int(habitant[-3:]),
            [value for index, value in dataframe_pays[dataframe_pays.nom_pays == country.nom_pays ]["pib_pays"].items()][0],
            [value for index, value in dataframe_pays[dataframe_pays.nom_pays == country.nom_pays ]["taux_croissance_pays"].items()][0]))
        else:
            print("""
            
            Ce Pays n'existe pour l'instant pas dans la base
            
            
            """)    
        

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
            from view.trandy_country_choice_view import TrandyCountryChoiceView
            next_view = TrandyCountryChoiceView()
            # dataframe_articles = ArticleService.get_article_dataframe()
            # dataframe_articles[dataframe_articles.nb_avis_article >= 10].groupby(["pays_origine_article","categorie_article"])
            # class_pays = dataframe_articles[['categorie_article','pays_origine_article']].value_counts(normalize=True)*100
            # print(class_pays)# classes distributions

            

        
        return next_view
