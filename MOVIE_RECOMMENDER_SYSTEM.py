#!/usr/bin/env python
# coding: utf-8 

# In[2]:


import numpy as np
import pandas as pd


# In[3]:


credits = pd.read_csv('tmdb_5000_credits.csv')
movies = pd.read_csv('tmdb_5000_movies.csv')


# In[4]:


# movies.head(1)

#.head() returns first n rows of dataset


# In[5]:


movies = movies.merge(credits, on = 'title')


# In[6]:


# movies.head(1) #checking


# In[7]:


movies = movies[['movie_id','title','overview','genres','keywords','cast','crew']]


# In[8]:


# movies.info()


# In[9]:


# movies.head()


# In[10]:


# correcting the format of each  column
# taking care of missing value

movies.isnull().sum()        #gives num of missing entries of specific coulumn


# In[11]:


movies.dropna(inplace =True)
# drops rows (movies here) which have missing values 
# we dropped here cuz only three movies


# In[12]:


movies.duplicated().sum()
#checking if duplicated rows


# In[13]:


movies.iloc[0].genres


# In[14]:


# converting list of dictionnaries to just list of genres

import ast 
#list of dic for genres is in strings in dataset so we convert it to literal values present inside the list 

def convert(listt):
    l = []
    for x in ast.literal_eval(listt):
        l.append(x["name"])
    return l


#testing code
# print(convert(movies.iloc[0].genres))


# In[15]:


# apllying the code to dataset

movies['genres'] = movies['genres'].apply(convert)

# movies.head()  #checking 


# In[16]:


# apllying the same conversion for keywqords feature(column)

movies['keywords'] = movies['keywords'].apply(convert)

movies.head()


# In[17]:


# now we extract first 5 actors for the movie

def get_actors(text):
    L = []
    counter = 0
    for i in ast.literal_eval(text):
        if counter < 5:
            L.append(i['name'])
            counter+=1
        
        else:
            break
    return L

movies['cast'].apply(get_actors)  # checking


# In[18]:


# apllying this to whole dataset
movies['cast'] = movies['cast'].apply(get_actors)

movies.head()


# In[19]:


movies.iloc[0].cast


# In[20]:


# movies.head() 


# In[21]:


# now trying to get a director

def get_director(obj):
    dir = []
    for x in ast.literal_eval(obj):
        if x["job"] == "Director":
            dir.append(x["name"])
            break
    return dir


# In[22]:


movies['crew'].apply(get_director)


# In[23]:


movies['crew'] = movies['crew'].apply(get_director)


# In[24]:


# chhanging a line of overview to a list of words

movies['overview'] = movies['overview'].apply(lambda x:x.split())


# In[25]:


# now in our data set we may have names such as tom hardy and tom hanks.this may create errors so to avoid redundancy we collapse spaces
# tom hardy becomes TomHardy

def collapse(L):
    L1 = []
    for i in L:
        L1.append(i.replace(" ",""))
    return L1


# In[26]:


#apllying the collapse function to all required fetures 

movies['cast'] = movies['cast'].apply(collapse)
movies['crew'] = movies['crew'].apply(collapse)
movies['genres'] = movies['genres'].apply(collapse)
movies['keywords'] = movies['keywords'].apply(collapse)


# In[27]:


# movies.head(3)


# In[28]:


movies.iloc[0].genres     # checking collapse function


# In[29]:


# now we make an new column (feature) called tags by combining these other features

movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']


# In[30]:


movies.head(3)


# In[31]:


movies.iloc[0].tags    # tags becomes our main feature matrix which we will now use for our model 


# In[32]:




final_ds = movies.drop(columns=['overview','genres','keywords','cast','crew'])
# final_ds.head()


# In[33]:


# we make a new dataset

new = movies.drop(columns=['overview','genres','keywords','cast','crew'])


# In[34]:


# now we change lists of string of tags column into one long string (why we do this ill explain later)

new['tags'] = new['tags'].apply(lambda x: " ".join(x))


# In[35]:


new.iloc[0].tags


# In[36]:


# we also need to transform the text to lower case so model doesnt get confused??? (it is suggested to do so)

new['tags'] = new['tags'].apply(lambda x : x.lower())
new.iloc[0].tags


# In[37]:


# MAYBE WE SHOULD ALSO PUNTUATION BUT HERE I DONT SEE MANY SO IGNORING FOR NOW BUT COULD BE USED TO OPTIMISE DATSET
# REMOVING PUNCTUATION SINCE WE NEED KEYWORDS LIKE BOND AND HARRY POTTER WHICH MODEL MAY RECOGANISE DIFFERENTLY IF ITS BOND AND BOND'S
# but it then just becomes bond and bonds?????
#definately helps in sum data rteduction tho??

import string

def remove_punctuation(s):
    s = ''.join([i for i in s if i not in frozenset(string.punctuation)])
    return s

new['tags'] = new['tags'].apply(remove_punctuation)


# In[38]:


new.iloc[5].tags


# ## MODEL SELECTION AND TRAINING

# ### The model we used for this particular problem is TEXT VECTORIZATION. HERE WE ARE USING BAG OF WORDS TECHNIQUE
# 
# #### In this we convert our text in tag coulmn into a vector of texts 

# In[39]:


# to counter same meaning words having diff speelings we will use nltk (natural language procsecing lib) 
# this will reduce love, loves, loving words into just love. this is called steming it will be coded on earlier cells


# In[41]:


# get_ipython().system('pip install nltk')


# In[42]:


import nltk


# In[43]:


from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()


# In[44]:


def stem(text):
    x = []
    
    for i in text.split():
        x.append(ps.stem(i))
    return " ".join(x)


# In[45]:


stem('in the 22nd century a paraplegic marine is dispatched to the moon pandora on a unique mission but becomes torn between following orders and protecting an alien civilization action adventure fantasy sciencefiction cultureclash future spacewar spacecolony society spacetravel futuristic romance space alien tribe alienplanet cgi marine soldier battle loveaffair antiwar powerrelations mindandsoul 3d samworthington zoesaldana sigourneyweaver stephenlang michellerodriguez jamescameron')


# In[46]:


new['tags'] = new['tags'].apply(stem)


# In[47]:


# since we r using bag of words we remove english stop words and keep a maximum features(words here) to 5000

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=5000,stop_words='english')


# In[48]:


# we store these text vector in vector

vectors = cv.fit_transform(new['tags']).toarray()


# In[49]:


vectors


# In[50]:


vectors[0]


# In[51]:


cv.get_feature_names_out()
# all words in root wordss


# #### NOW THAT WE HAVE MADE OUR VECTOR, WE COMPARE OUR MOVIES ON BASIS OF COSINE SIMILARITIES INSTEAD OF EUCLIDEAN DISTANCES. this is done pairwise(each movie is compared to every other movie on cosine similarity)

# In[52]:


from sklearn.metrics.pairwise import cosine_similarity
similarity = cosine_similarity(vectors)


# In[53]:


similarity[2]


# In[54]:


def recommend(movie):
    index = new[new['title'] == movie].index[0]    # fetches the index of movie in dataset
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    for i in distances[1:8]:
        print(new.iloc[i[0]].title)
# print("movie at location: ")
# # print(new.iloc[2662,1])
# print(new.loc[16, 'title'])

def recommend_movie_for_api(movie):
    try:
        index =None
        for i in range(len(new)):
            if new.iloc[i, 1].lower() == movie.lower():
                print(i)
                index = i
                break
        # index = new[new['title'] == movie].index[0]    # fetches the index of movie in dataset
    except IndexError:
        return None
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    recommended_movies_list = []
    for i in distances[1:8]:
        movie_id = int(new.loc[i[0], 'movie_id'])
        movie_name = new.loc[i[0], 'title']
        recommended_movies_list.append({"id": movie_id, "name": movie_name})
    print(recommended_movies_list)
    return recommended_movies_list
    
        


# In[63]:


# recommend('American Psycho') 

# recommend_movie_for_api('Dogtooth')


# In[56]:


# new.head()


# # In[57]:


# import pickle


# # In[58]:


# pickle.dump(new,open('movie_list.pkl','wb'))


# # In[59]:


# pickle.dump(similarity,open('similarity.pkl','wb'))


# # In[60]:


# new.head()


# # In[61]:


# new.to_dict()


# # In[61]:


# pickle.dump(new.to_dict(),open('movie_dict.pkl','wb'))


# # In[ ]:




