


class FonctionService:


    def remove_punctuation(text):
        '''a function for removing punctuation'''
        # replacing the punctuations with space
        import re
        import string
        spaces = ""
        ponctuation = string.punctuation+"’"
        for i in ponctuation:
            spaces = spaces + " "
        return re.sub(' +', ' ', text.translate(str.maketrans(ponctuation, spaces, ''))).strip()

    def removeWordsContNB(text):
        import re
        """ Remove words containing numbers

        Parameters
        ----------
        text : str
            Any text

        Returns
        ------
        str
            A text cleaned
        """
        return re.sub(' +', ' ', re.sub(r'\w*\d\w*', '', text).strip())

    def find_somecharacters_in_text(text, characters):
        return characters in text

    def remove_single_letter(text):
        import re
        """ Remove single letters

        Parameters
        ----------
        text : str
            Any text

        Returns
        ------
        str
            A text cleaned
        """
        return re.sub(' +', ' ', re.sub(r'\b\w\b', '', text).strip())

    def remove_stopwords(text, stopword):
        '''a function for removing the stopword'''
        # removing the stop words and lowercasing the selected words
        text = [word.lower() for word in text.split() if word.lower() not in stopword]
        # joining the list of words with space separator
        return " ".join(text)

    def preprocessing_gen(doc):
        import gensim
        liste = gensim.utils.simple_preprocess(doc, deacc=True, min_len=3)
        a=""
        for i in liste:
            a+=" {}".format(i)
        return(a)

    def lemmatization(text):
        import spacy
        spacy_nlp = spacy.load('fr_core_news_md')
        text2=[]
        for token in spacy_nlp(u"{}".format(text)):
            text2.append(token.lemma_)
        return(" ".join(text2))


    
    def racinisation(text):
        from nltk.stem.snowball import FrenchStemmer
        stemmer = FrenchStemmer()
        text2=[]
        for token in text.split():
            text2.append(stemmer.stem(token))
        return(" ".join(text2))

    def top_words(donnees, compteur_1):
        import numpy as np
        from matplotlib import pyplot as plt
        words = []
        for i in donnees:
            c = i.split(" ")
            for k in c:
                if len(k) > 1:
                    words.append(k)

        # on va compter l'occurence de chaque mot
        compte_occurence_mot = {}.fromkeys(set(words), 0)
        for valeur in words:
            compte_occurence_mot[valeur] += 1

        len(compte_occurence_mot)  # il ya en tout 4390 mots différents

        mots = compte_occurence_mot.keys()
        occurence_mot = list(compte_occurence_mot.values())

        # 50 mots les plus utilisés

        def get_key(val):  # permet de retrouver une clée de compte à partir de sa valeur
            for key, value in compte_occurence_mot.items():
                if val == value:
                    return key

            return "There is no such Key"

        top_50 = {}
        """de la forme {"mot":"occurence",...}"""

        while compteur_1 > 0:
            c = max(occurence_mot)
            top_50[get_key(c)] = c
            occurence_mot.remove(c)
            compteur_1 -= 1
        occurence_mot = list(compte_occurence_mot.values())



        return top_50










