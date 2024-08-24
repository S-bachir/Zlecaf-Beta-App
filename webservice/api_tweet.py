import twint
import nest_asyncio
import pandas as pd
nest_asyncio.apply()  
import time


class  ApiTweet:
    def __init__(self) -> None:
        pass
    

    
    def get_tweet( key_word):
        c = twint.Config()
        c.Search = "{}".format(key_word)
        c.Limit = 1000
        #c.Geo = "13.513660,2.1098000,600km"  #recherche à 100 km de niamey (coordonné géo de niamey : 13.513660,2.1098000 )
                                     #                                               Addis  :  9.0249700,38.7468900
        #c.Store_json = True
        #c.Output = "tweeto.json"
        c.Pandas = True
        c.Hide_output= True

        twint.run.Search(c)
        data = pd.read_json('tweeto.json', lines=True)

        count_en = data[data.language=="en"]['tweet'].count()
        count_fr = data[data.language=="fr"]['tweet'].count()  


        return data

    def get_tweet_date(key_word, from_date):
        
        c = twint.Config()
        c.Search = "{}".format(key_word)
        c.Limit = 5000
        c.Since = "{}".format(from_date)
            
    
        #c.Geo = "13.513660,2.1098000,600km"  #recherche à 100 km de niamey (coordonné géo de niamey : 13.513660,2.1098000 )
                                     #                                               Addis  :  9.0249700,38.7468900
        #c.Store_json = True
        #c.Output = "data_1.json"
        c.Pandas = True
        c.Hide_output= True
        try:
            twint.run.Search(c)
            données = twint.storage.panda.Tweets_df
            data1 = données[données.language == 'fr']["tweet"]
            data2 = données[données.language == 'en']["tweet"]
            data = pd.concat([data1, data2])
            return data

        except:
            print("""format des dates incorrecte, 
                     essayez ce genre de format pour les dates : 2020–04–29
            """)
            time.sleep(5)
            a=None
            return a
        
        

    def get_tweet_date_place(key_word, from_date, to_date, country,perimetre):
        c = twint.Config()
        c.Search = "{}".format(key_word)
        c.Limit = 1000
        try:
            c.Since = "{}".format(from_date)
            c.Until = "{}".format(to_date)
        except:
            print("""format des dates incorrecte, 
                     essayez ce genre de format pour les dates : 2020–04–29
            """)
            time.sleep(4)
            pass

        coord_geo = country #faire une fonction qui retourne les coordonnées géo de la région
        c.Geo = "{},{}km".format(coord_geo,perimetre)  #recherche à 100 km de niamey (coordonné géo de niamey : 13.513660,2.1098000 )
                                     #                                               Addis  :  9.0249700,38.7468900
        c.Pandas = True
        c.Hide_output= True

        twint.run.Search(c)
        data = pd.read_json('date_place_1.json', lines=True)
        return data