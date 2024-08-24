import twint
import nest_asyncio
import pandas as pd
from matplotlib import pyplot as plt
nest_asyncio.apply()
from Preprocessing import Fonction
from nltk.corpus import stopwords
import spacy
spacy_nlp = spacy.load('fr_core_news_md')
from wordcloud import WordCloud
import numpy as np  
from PIL import Image
import nltk


class TweeterSearchService:
    def __init__(self) -> None:
        pass
    

    def plot_word_cloud(self, top) :
    
        mask_coloring = np.array(Image.open(str('R.png')))

        # Définir le calque du nuage des mots
        wc = WordCloud(width=600,height=600,background_color="white", max_words=200,  mask = mask_coloring, max_font_size=300,collocations = False, random_state=42)

        # Générer et afficher le nuage de mots
        plt.figure(figsize= (10,10))
        wc.generate_from_frequencies(top)
        plt.imshow(wc,interpolation="bilinear")
        plt.axis("off")
        plt.show()

    def preprocess(self, key_word):
        c = twint.Config()
        c.Search = "{}".format(key_word)
        c.Limit = 1000
        #c.Geo = "13.513660,2.1098000,600km"  #recherche à 100 km de niamey (coordonné géo de niamey : 13.513660,2.1098000 )
                                     #                                               Addis  :  9.0249700,38.7468900
        c.Store_json = True
        c.Output = "moringa_demo_1.json"

        twint.run.Search(c)
        data = pd.read_json('moringa_demo_1.json', lines=True)

        count_en = data[data.language=="en"]['tweet'].count()
        count_fr = data[data.language=="fr"]['tweet'].count()
        del data['id']
        del data['conversation_id']
        del data['user_id']
        del data['source']
        del data['user_rt_id']
        del data['user_rt']
        del data['retweet_id']
        del data['thumbnail']
        del data['translate']
        del data['trans_src']
        del data['trans_dest']
        del data['reply_to']    

        stop_w = stopwords.words('french') + stopwords.words('english') 
        stop_w.append(key_word)
        data["tweet"] = data["tweet"].apply(Fonction.remove_stopwords, stopword = stop_w)
        nltk.download('stopwords')

        top_words_no_sw_fr = Fonction.top_words(data[data.language == "fr"].tweet, 100)

        top_words_no_sw_en = Fonction.top_words(data[data.language == "en"].tweet, 100)

        top_words_no_sw = dict(top_words_no_sw_fr)
        top_words_no_sw.update(top_words_no_sw_en)
        data["tweet"] = data["tweet"].apply(Fonction.remove_single_letter)
        data["tweet"] = data["tweet"].apply(Fonction.remove_punctuation)

        sortie = [top_words_no_sw_en, top_words_no_sw_fr, top_words_no_sw]
        return sortie

