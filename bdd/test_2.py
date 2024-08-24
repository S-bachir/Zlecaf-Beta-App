from service.super_utilisateur_service import SuperUtilisateurService
from service.modelisation_service import ModelisationService
from hashlib import sha1


mdp_hash = sha1('bachir'.encode()).hexdigest()
SuperUtilisateurService.add_super_user_in_db('bach',mdp_hash)

#ModelisationService.SVMpredict_categorie_unit_article('sprit 100ml')