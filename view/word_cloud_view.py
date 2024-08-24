from service.super_utilisateur_service import SuperUtilisateurService
from time import time
from PyInquirer import prompt, Separator
from service.data_viz_service import DataVizService
from view.abstract_vue import AbstractView
from PIL import Image
from service.pays_service import PaysService
from time_print import delay_print
from view.save_file_wiew import SaveFileView

class WordCloudView(AbstractView):

    def __init__(self):
        self.questions_key_word = [
                {
                    'type': 'input',
                    'name': 'Mot_clé',
                    'message': "Pour quel élément voulez-vous connaitre l'engagement textuel?  :",
                }
            ]
        self.questions_country = [
                {
                    'type': 'input',
                    'name': 'Pays',
                    'message': "Dans quel pays souhaitez vous axer la recherche?:",
                }
            ]
        self.questions_date = [
                {
                    'type': 'input',
                    'name': 'Dates',
                    'message': """
A quand doit remonter la recherche?  :
        date de la forme 2021–01–29)  
                       ->""",
                }
            ]


    def display_info(self):
        print("""        
                     Quelles sont les termes les plus retrouvés quand on évoque la Zlecaf?  

                                """)
        #DataVizService.plot_word_cloud('Zlecaf', '2018-01-01')

    def make_choice(self):

        reponse_key_word = prompt(self.questions_key_word)
        reponse_country = prompt(self.questions_country)
        reponse_date= prompt(self.questions_date)
        liste_nom_pays = [pays.nom_pays for pays in PaysService.get_all_pays()]
        #if reponse_country['Pays'].capitalize() in liste_nom_pays:
        #    pass
       
        wc = DataVizService.plot_word_cloud(reponse_key_word['Mot_clé'], reponse_date['Dates'])
        if wc is None:
            from view.datavisualisation_view import DatavisualisationView
            return DatavisualisationView() 
        else:
            wc
            time.sleep(5)
            from view.menu_principal_view import MenuPrincipalView
            from view.super_menu_principal_view import SuperMenuPrincipalView
            try:
                AbstractView.session.user_name == SuperUtilisateurService.get_super_user_by_name(AbstractView.session.user_name)[0]
                next_view=SuperMenuPrincipalView()
            except:
                next_view = MenuPrincipalView()

            return next_view

        
