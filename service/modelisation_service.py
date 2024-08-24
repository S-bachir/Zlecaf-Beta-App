from os import name
import pickle
import pandas as pd
from service.preprocess_service import PreprocessService
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

class ModelisationService:
    
    def __init__(self):
        pass
    
    @staticmethod
    def SVMpredict_categorie_article(data):  
        with open('model_svm','rb') as f:
            model_svm = pickle.load(f)
        data_preprocess = PreprocessService.NLP_preprocess_racinisation(data)

        with open('tfv','rb') as f:
            tfv= pickle.load(f)
        data_preprocess = PreprocessService.NLP_preprocess_racinisation(data)

        model_svm_pred_0 = model_svm.predict(tfv.transform(data_preprocess))

        #transformation de la dataframe en vecteur tf-idf
        return model_svm_pred_0

    def SVMpredict_categorie_unit_article(name_article):
        with open('C:/Users/bachi/bureau/Untitled Folder/model_random_forest','rb') as f:
            model_rf = pickle.load(f)
        name = {'nom':['{}'.format(name_article)]}
        name_df= pd.DataFrame(name, columns=['nom'])
        name_df['nom']=PreprocessService.NLP_preprocess_racinisation(name_df['nom'])

        with open('C:/Users/bachi/Zlecaf_Beta_App/service/tfv','rb') as f:
            tfv= pickle.load(f)
        
        model_svm_pred_0 = model_rf.predict(tfv.transform(name_df['nom']))

        #transformation de la dataframe en vecteur tf-idf
        return model_svm_pred_0[0]
    