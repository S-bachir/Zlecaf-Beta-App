from PyInquirer import prompt, Separator

from view.abstract_vue import AbstractView
from PIL import Image
from service.modelisation_service import ModelisationService
from time_print import delay_print
import time

class PredictCatView(AbstractView):

    def __init__(self):

        self.questions = [
                {
                    'type': 'input',
                    'name': 'cat_pred',
                    'message': "Pour quel article voulez vous connaitre la catégorie?  :",
                }
            ]
        

    def display_info(self):
        print("")
        

    def make_choice(self):
       
        reponse = prompt(self.questions)
        
        
        predict = ModelisationService.SVMpredict_categorie_unit_article(reponse["cat_pred"])
        print (""" 
        
        
        La catégorie prédite pour l'article {} est : 
                                    
                                
                                     {}
                                    
                                    
                                    """.format(reponse["cat_pred"],predict))
        time.sleep(10)
        from view.super_menu_principal_view import SuperMenuPrincipalView
        next_view = SuperMenuPrincipalView()

     

        return next_view
