from PyInquirer import prompt, Separator

from view.abstract_vue import AbstractView
from time_print import delay_print


class WelcomeView(AbstractView):

    def __init__(self):
        self.questions = [
            {
                'type': 'list',
                'name': 'choix_menu',
                'message': 'Menu',
                'choices': [
                    "Créer un compte",
                    "Se connecter",
                    "Invité",
                    Separator(),
                    "Quitter l'application"
                ]
            }
        ]

    def make_choice(self):
        reponse = prompt(self.questions)
        if reponse['choix_menu'] == 'Créer un compte':
            from view.create_account_view import CreateAccountView
            next_view = CreateAccountView()
        elif reponse["choix_menu"] == 'Se connecter':
            from view.sign_in_view import SignInView
            next_view = SignInView()
        elif reponse["choix_menu"] == 'Invité':
            from view.menu_principal_view import MenuPrincipalView
            next_view = MenuPrincipalView()
        else:
            next_view = None
        return next_view

    def display_info(self):
        print("Bienvenue dans la version Beta notre application dédiée aux échanges de la Zlecaf !")

        