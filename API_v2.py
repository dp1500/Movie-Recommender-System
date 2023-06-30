
from flask_restful import Resource, Api
from flask import jsonify
from flask import Flask
from flask_restful import Resource, Api

# from flask import request, flash,Blueprint
# from sqlalchemy import desc , select, join
import requests


from MOVIE_RECOMMENDER_SYSTEM import recommend_movie_for_api

app = Flask(__name__)
api = Api(app)

import pandas as pd
# import pickle
'''getting pre build model(similarity) and movie database in form of dictionary (movie_list)  this contains all the movies in dataset with thier ids, titles etc'''

# movies = pickle.load(open('movie_dict.pkl','rb'))
# similarity = pickle.load(open('similarity.pkl','rb'))

# print(type(movies))

# df = pd.DataFrame(movies)

""" for pickle versions"""
# print(df.iloc[2[0]].movie_id)
# print(movies['title'])
 
# def recommend_movie_for_api(movie):
#     # print(type(movies))
#     try:
#         index = df[df['title'] == movie].index[0]    # fetches the index of movie in dataset
#     except IndexError:
#         return None
#     distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
#     recommended_movies_list = []
#     for i in distances[1:8]:
        
#         movie_id = int(df.loc[i[0], 'movie_id'])
#         movie_name = df.loc[i[0], 'title']
        
#         recommended_movies_list.append({"id": movie_id, "name": movie_name})
#     return recommended_movies_list


class movie_prediction(Resource):
    def get(self,movie_name):
         
        movie_name = str(movie_name) 
        print(movie_name)

        recommended_movies = recommend_movie_for_api(movie_name)

        # print(recommended_movies)
        # recommend(movie_name)

        if recommended_movies:

            movies_data = []

            for movie in recommended_movies:
                movie_id = movie['id']
                print(movie_id)
                response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=e1a474f1f35cd80fdff65f0fdb76983b&language=en-US".format(movie_id))
                movie_data = response.json()
                movies_data.append(movie_data)
            # movies = recommended_movies[]
            if movies_data:
                final_response = {"Status": "0", "status_message": "", "movies": movies_data}
            else:
                final_response = {"Status": "2", "status_message": "error fetching movie from tmdb API call", "movies": []}
        else:
            final_response = {"Status": "1", "status_message": "movie not found in our database", "movies": []}
        return jsonify(final_response)


api.add_resource(movie_prediction, '/predicted_movies/<string:movie_name>')
    

movies_df = pd.read_csv('tmdb_5000_movies.csv')

class search_movie(Resource):
    def get(self, query):
        # use query parameter instead of request.args.get()
        search_string = query
        
        # search for movies containing search string in title
        matching_movies = movies_df[movies_df['original_title'].str.lower().str.contains(search_string.lower())]['title'].tolist()
        
        # return JSON response with matching movies
        return jsonify({'matching_movies': matching_movies})
    
# add resource to API with route and endpoint
api.add_resource(search_movie, '/search_movies/<string:query>')



if __name__ == '__main__': 
    app.run(debug=True)
