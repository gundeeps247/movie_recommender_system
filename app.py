import streamlit as st
import pickle
import pandas as pd
import requests #to access api


# def fetch_poster(movie_id):
#     response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=2e34127cca6bbd557b6725d783cc18f8&language=en-US'.format(movie_id))
#     data = response.json()
#     return "https://image.tmdb.org/t/p/w500" + data['poster_path']
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]  # here we replaced 'similarity[movie_index]' as we gave its value to 'distances'

    recommended_movies=[]
    recommended_movies_posters = []

    for i in movies_list:  # here i am getting a tuple everytime
        movie_id = i[0]

        recommended_movies.append(movies.iloc[i[0]].title)

        # fetch poster from api
        # recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,
        # recommended_movies_posters


# with open('movies.pkl', 'rb') as file:
#     movies_list = pickle.load(file)

movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
#loading similarity.pkl file
similarity=pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name =st.selectbox('Choose a movie',
                     movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)