import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=860eb6b4588ed5b42b634fafac2575ee&language=en-US'.format(movie_id))
    
    data = requests.get()
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie_name):
    
    movie_index = movies[movies['title'] == movie_name].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    recommended_movies_poster = []
    for i in movie_list:
        movie_id = i[0]
     
        
        recommended_movies.append(movies.iloc[i[0]].title)
           #fetch poster from api
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies





movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'how would you like to be contacted?',
    movies['title'].values
)

import streamlit as st

# Page configuration (हमेशा सबसे ऊपर रखना है)
st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar input
with st.sidebar:
    st.title("🔍 Search")
    selected_movie = st.text_input("Enter movie name:")


st.header("🎞️ Movie Recommendation System")
recommendations = [
    ("Inception", "https://image.tmdb.org/t/p/w500/qmDpIHrmpJINaRKAfWQfftjCdyi.jpg"),
    ("Interstellar", "https://image.tmdb.org/t/p/w500/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg"),
    ("The Dark Knight", "https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg"),
    ("Tenet", "https://image.tmdb.org/t/p/w500/k68nPLbIST6NP96JmTxmZijEvCA.jpg"),
    ("Dunkirk", "https://image.tmdb.org/t/p/w500/ebSnODDg9lbsMIaWg2uAbjn7TO5.jpg"),
    ("Memento", "https://image.tmdb.org/t/p/w500/fQMSaP88cf1nz4qwuNEEFtazuDM.jpg"),
]


if selected_movie:
    st.subheader(f"Recommendations for: {selected_movie}")
    for i in range(0, len(recommendations), 3):
        cols = st.columns(3)  
        for j, col in enumerate(cols):
            if i + j < len(recommendations):
                title, poster_url = recommendations[i + j]
                with col:
                    st.image(poster_url, use_container_width=True)
                    st.caption(title)

else:
    st.write("👉 Please type a movie name in the sidebar to see recommendations.")

