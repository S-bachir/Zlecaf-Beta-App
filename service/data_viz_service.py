
from service.preprocess_service import PreprocessService
from service.fonction_service import FonctionService
from webservice.api_tweet import ApiTweet
from time_print import delay_print
import numpy as np
from wordcloud import WordCloud
from matplotlib import pyplot as plt
from PIL import Image
import datetime
from service.preprocess_service import PreprocessService

class DataVizService:
    
    def __init__(self):
        pass

    @staticmethod
    def plot_word_cloud(mot_clee, date) :
        #date = datetime.datetime.now()
        #today = "{}-{}-{}".format(date.year, date.month, date.day) # on recupère la date d'aujourd'hui   
        data = ApiTweet.get_tweet_date(key_word=mot_clee,from_date=date) # on recupere les tweets sous forme de dataframe
        if data is None :
            return None
        elif data is not None:
            
            data = PreprocessService.NLP_preprocess(data, mot_clee)  #on retire les stops_words
            top = FonctionService.top_words(data, 100) #top correspond à l'enssemble des mots les plus utilisées dans data
            masque = 'C:/Users/bachi/Zlecaf_Beta_App/image/R.png'
            
            mask_coloring = np.array(Image.open(str(masque)))
            
            # Définir le calque du nuage des mots
            wc = WordCloud(width=600,height=600,background_color="white", max_words=200,  mask = mask_coloring, max_font_size=300,collocations = False, random_state=42)
            plt.figure(figsize= (10,10))
            wc.generate_from_frequencies(top)
            plt.imshow(wc,interpolation="bilinear")
            plt.axis("off")
            plt.show()
            # Générer et afficher le nuage de mots
            

    @staticmethod
    def plot_word_cloud_pays(self, mot_clee, pays, date ,masque) :
        date = datetime.datetime.now()
        today = "{}-{}-{}".format(date.year, date.month, date.day) # on recupère la date d'aujourd'hui
        data = ApiTweet.get_tweet_date_place(key_word=mot_clee,from_date=date, to_date= today, country=pays) # on recupere les tweets sous forme de dataframe
        data = PreprocessService.remove_stopwords(data, mot_clee)  #on retire les stops_words
        top = FonctionService.top_words(data, 50) #top correspond à l'enssemble des mots les plus utilisées dans data

        mask_coloring = np.array(Image.open(str(masque)))
        
        # Définir le calque du nuage des mots
        wc = WordCloud(width=600,height=600,background_color="white", max_words=200,  mask = mask_coloring, max_font_size=300,collocations = False, random_state=42)

        # Générer et afficher le nuage de mots
        plt.figure(figsize= (10,10))
        wc.generate_from_frequencies(top)
        plt.imshow(wc,interpolation="bilinear")
        plt.axis("off")
        plt.show()

    @staticmethod
    def hist(dataframe):
        pass

 