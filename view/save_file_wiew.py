from PyInquirer import prompt, Separator
from service.data_viz_service import DataVizService
from view.abstract_vue import AbstractView
from PIL import Image
from service.pays_service import PaysService
from time_print import delay_print
from view.menu_principal_view import MenuPrincipalView

class SaveFileView(AbstractView):

    def __init__(self):
        self.questions = [
            {
                'type': 'list',
                'name': 'sauvegarde',
                'message': 'Option de sauvegarde',
                'choices': [
                    "Enregistrer l'image",
                    Separator(),
                      "Revenir au menu principal"
                ]
            }
        ]

    def display_info(self):
        pass
    def make_choice(self):

        reponse = prompt(self.questions)
      
        if reponse["sauvegarde"] == "Enregistrer l'image":
            pass
        elif reponse["sauvegarde"] == "Revenir au menu principal":
            next_view= MenuPrincipalView()
        return next_view
