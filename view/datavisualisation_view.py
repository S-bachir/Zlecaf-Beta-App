from service.utilisateur_service import UtilisateurService
from service.super_utilisateur_service import SuperUtilisateurService
from view.session import Session
from PyInquirer import prompt, Separator

from view.abstract_vue import AbstractView

from PIL import Image

from time_print import delay_print


class DatavisualisationView(AbstractView):

    def __init__(self):
        self.questions = [
                {
                    'type': 'list',
                    'name': 'choix_menu',
                    'message': 'retour:',
                    'choices': [
                        'WordCloud',
                        'Cartographie',
                        'Boxplot',
                        'autres',
                        Separator(),
                        'Retour au menu principal'
                    ]

                }
            ]


    def display_info(self):
        pass

    def make_choice(self):

        reponse = prompt(self.questions)
        if reponse['choix_menu'] == 'WordCloud':
           

            from view.word_cloud_view import WordCloudView
            next_view = WordCloudView()

        else:
            from view.menu_principal_view import MenuPrincipalView
            from view.super_menu_principal_view import SuperMenuPrincipalView
            try:
                AbstractView.session.user_name == SuperUtilisateurService.get_super_user_by_name(AbstractView.session.user_name)[0]
                next_view=SuperMenuPrincipalView()
            except:
                next_view = MenuPrincipalView()

        return next_view
