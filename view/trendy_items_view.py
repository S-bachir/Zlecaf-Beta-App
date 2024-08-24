from PyInquirer import prompt, Separator

from view.abstract_vue import AbstractView
from PIL import Image
from service.article_service import ArticleService
from time_print import delay_print


class TrandyItemsView(AbstractView):

    def __init__(self):
        self.questions = [
                {
                    'type': 'list',
                    'name': 'choix_menu',
                    'message': 'retour:',
                    'choices': [
                        'Voir les categorie par pays',
                        Separator(),
                        'Retour au menu principal'
                    ]

                }
            ]

    def display_info(self):
        
        
        dataframe_articles = ArticleService.get_article_dataframe()
        #dataframe_articles[dataframe_articles.nb_avis_article >= 10].groupby(["pays_origine_article","categorie_article"])
        class_pays = dataframe_articles[['categorie_article','pays_origine_article']][dataframe_articles.nb_avis_article >= 10].value_counts(normalize=True)*100
        print(class_pays)# classes distributions
        
        

    def make_choice(self):

        reponse = prompt(self.questions)
        if reponse['choix_menu'] == 'Voir les categorie par pays':
            # from view.menu_principal_view import MenuPrincipalView
            # next_view =  MenuPrincipalView()
            from view.trandy_country_choice_view import TrandyCountryChoiceView
            next_view = TrandyCountryChoiceView()
            

        elif reponse['choix_menu'] == 'Retour au menu principal'  :
            from service.super_utilisateur_service import SuperUtilisateurService
            from view.menu_principal_view import MenuPrincipalView
            from view.super_menu_principal_view import SuperMenuPrincipalView
            try:
                AbstractView.session.user_name == SuperUtilisateurService.get_super_user_by_name(AbstractView.session.user_name)[0]
                next_view=SuperMenuPrincipalView()
            except:
                next_view = MenuPrincipalView()
        
        return next_view
