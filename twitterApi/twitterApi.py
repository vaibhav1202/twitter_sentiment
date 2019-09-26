
# coding: utf-8

# # Imports

# In[7]:


import pandas as pd
import numpy as np
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle
import os



# In[9]:


def preprocessing(combDf, isTraining=False):
    combDf["tweet"] = combDf["tweet"].str.lower()
#     combDf.sample(5)
    def remove_pat(s1, pat, nstr):
        return re.sub(pat, nstr, s1)
    combDf["new_tweet"] = np.vectorize(remove_pat)(combDf["tweet"], "@[\w]*", "")
    combDf["new_tweet"] = np.vectorize(remove_pat)(combDf["new_tweet"], "[^a-zA-Z_]+", " ")
    combDf["new_tweet"] = np.vectorize(remove_pat)(combDf["new_tweet"], r"\b[a-z]{1,1}\b", " ")
    if isTraining:
        combDf = combDf[combDf["label"].isin([0,1])]
    tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=1,ngram_range=(1,3),  max_features=100000, stop_words='english')
    print("-*-"*50)
    print(type(tfidf_vectorizer))    
    pkl_vect = "twitter_pickle_vect.pkl"
    if isTraining:
        bow = tfidf_vectorizer.fit_transform(combDf['new_tweet'])
        with open(pkl_vect, 'wb') as file:
            pickle.dump(tfidf_vectorizer, file)
    else:
        pkl_vect = os.path.join(os.path.abspath(os.path.dirname(__file__)), pkl_vect)            
        with open(pkl_vect, 'rb') as file:
            tfidf_vectorizer = pickle.load(file)
            print(type(tfidf_vectorizer))
            print("1"*100)
            print(combDf.head())
            bow = tfidf_vectorizer.transform(combDf['new_tweet'])
    return bow


# In[10]:


def training(combDf):
    bow = preprocessing(combDf, True)
    X = bow
    y = combDf["label"]
    model = MultinomialNB()
    model.fit(X, y)
    pkl_model = "twitter_pickle_model.pkl"
    with open(pkl_model, 'wb') as file:
        pickle.dump(model, file)


# In[11]:


def pred(ob):
    d1 = ob.to_dict()
    df = pd.DataFrame(d1, index=[0])
    print("="*50)
    print(df.head())
    bow = preprocessing(df, False)        
    print("*"*50)
    pkl_model = "./twitter_pickle_model.pkl"
    pkl_model = os.path.join(os.path.abspath(os.path.dirname(__file__)), pkl_model)
    with open(pkl_model, 'rb') as file:
        model = pickle.load(file)
    pred = model.predict(bow)
    return pred


# In[12]:


if __name__ == "__main__":
    combDf = pd.read_csv("train.csv")
    training(combDf)

