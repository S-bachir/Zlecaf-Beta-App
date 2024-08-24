from PyInquirer import prompt, Separator

from view.abstract_vue import AbstractView
from PIL import Image
from service.site_service import SiteService
import time
from metier.site import Site

class AjoutSiteView(AbstractView):

    def __init__(self):

        self.questions_nom = [
                {
                    'type': 'input',
                    'name': 'nom_site',
                    'message': "Quel est le nom du site? :",
                }
            ]
        self.questions_url = [
                {
                    'type': 'input',
                    'name': 'url_site',
                    'message': "quel est le lien url du site? :",
                }
            ]
        self.questions_type = [
                {
                    'type': 'list',
                    'name': 'type_site',
                    'message': "De quel type de site s'agit-t-il?:",
                    'choices': [
                        'Site de E-commerce',
                        'Site public',
                        'Site privé',
                        "Site d'une Organisation International",
                        'Site de type DataCenter',
                    ]

                }
            ]
        
        self.questions_pays = [
                {
                    'type': 'input',
                    'name': 'pays_site',
                    'message': "Quel pays heberge ce site?:",
                }
            ]

    def display_info(self):
        print("")
        

    def make_choice(self):
       
        reponse_nom = prompt(self.questions_nom)
        reponse_url = prompt(self.questions_url)
        reponse_type = prompt(self.questions_type)
        reponse_pays = prompt(self.questions_pays)
        
        site = Site(id_site=None, nom_site=reponse_nom['nom_site'], url_site=reponse_url['url_site'], type_site=reponse_type['type_site'], pays_hebergement_site=reponse_pays['pays_site'] )
        
        SiteService.add_site_in_db(site)
        print('le site {} a été ajouté à la base de données'.format(reponse_nom['nom_site']))
        time.sleep(5)
        
        from view.super_menu_principal_view import SuperMenuPrincipalView
        next_view = SuperMenuPrincipalView()


     

        return next_view
