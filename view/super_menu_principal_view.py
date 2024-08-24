from PyInquirer import prompt, Separator

from view.abstract_vue import AbstractView

from time_print import delay_print


class SuperMenuPrincipalView(AbstractView):

    def __init__(self):
        self.questions = [
            {
                'type': 'list',
                'name': 'choix_menu',
                'message': 'Menu principal',
                'choices': [
                    "Afficher les produits tendance",
                    "Afficher les produits tendance par pays",                    
                    "Afficher quelques statistiques descriptives",
                    "Datavisualisations",
                    "Changer de pays d'origine",
                    Separator(),
                    "Prédire catégorie d'un article",
                    "Ajouter un nouveau site à la base",
                    Separator(),
                    "Se déconnecter"
                ]
            }
        ]

    def make_choice(self):
        reponse = prompt(self.questions)
        if reponse['choix_menu'] == "Afficher les produits tendance":
            from view.trandy_items_view import TrandyItemsView
            next_view = TrandyItemsView()

        elif reponse['choix_menu'] == "Afficher les produits tendance par pays":
            from view.trandy_country_choice_view import TrandyCountryChoiceView
            next_view = TrandyCountryChoiceView()


        elif reponse["choix_menu"] == "Afficher quelques statistiques descriptives":
            pass

        elif reponse["choix_menu"] == "Datavisualisations":
            from view.datavisualisation_view import DatavisualisationView
            next_view = DatavisualisationView()

        elif reponse["choix_menu"] == "Changer de pays d'origine":
            pass
        
        elif reponse["choix_menu"]=="Ajouter un nouveau site à la base":
            from view.ajout_site_view import AjoutSiteView
            next_view = AjoutSiteView()
            
        elif reponse["choix_menu"]=="Prédire catégorie d'un article":
            from view.predict_cat_view import PredictCatView
            next_view = PredictCatView()

        else:
            from view.welcome_view import WelcomeView
            next_view = WelcomeView()

        return next_view

    def display_info(self):
        print("\t**********************",
              "\n\t*   Menu Principal   *",
              "\n\t**********************\n")
       
        print('Bienvenue {}, content de vous savoir parmi nous!\n\n'.format(
                AbstractView.session.user_name))

      