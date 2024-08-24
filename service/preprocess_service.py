import pandas as pd
from matplotlib import pyplot as plt
from service.fonction_service import FonctionService





class PreprocessService:
    
    def __init__(self):
        pass
    
    @staticmethod
    def remove_stopwords(data, key_word):
        from nltk.corpus import stopwords
        

        stop_w = stopwords.words('french') + stopwords.words('english')
        stop_w += [key_word, 'https', 'amp']
        data = data.apply(FonctionService.remove_stopwords, stopword = stop_w)
        return data 
    
    @staticmethod
    def NLP_preprocess_racinisation(data):
        from nltk.corpus import stopwords
        stop_w = stopwords.words('french') + stopwords.words('english')
       
            
        
        data = data.apply(FonctionService.remove_single_letter)
        data = data.apply(FonctionService.remove_punctuation)
        data = data.apply(FonctionService.preprocessing_gen)
        data = data.apply(FonctionService.lemmatization)
        stop_w = stopwords.words('french') + stopwords.words('english') 
        data = data.apply(FonctionService.remove_stopwords, stopword = stop_w)
        data = data.apply(FonctionService.racinisation)

        return data
    
    @staticmethod
    def NLP_preprocess_lemmatisation(data, key_word):
        from nltk.corpus import stopwords
        import nltk
        nltk.download('stopwords')
            
        
        data = data.apply(FonctionService.remove_single_letter)
        data = data.apply(FonctionService.remove_punctuation)
        data = data.apply(FonctionService.preprocessing_gen)
        data = data.apply(FonctionService.lemmatization)
        stop_w = stopwords.words('french') + stopwords.words('english')
        stop_w += [key_word,'https', 'amp'] 
        data = data.apply(FonctionService.remove_stopwords, stopword = stop_w)

        return data
    

    @staticmethod
    def NLP_preprocess(data, key_word):
        from nltk.corpus import stopwords
        import nltk
        nltk.download('stopwords')
            
        
        data = data.apply(FonctionService.remove_single_letter)
        data = data.apply(FonctionService.remove_punctuation)
        data = data.apply(FonctionService.preprocessing_gen)
        stop_w = stopwords.words('french') + stopwords.words('english')
        stop_w += [key_word, 'https', 'amp'] 
        data = data.apply(FonctionService.remove_stopwords, stopword = stop_w)

        return data

    