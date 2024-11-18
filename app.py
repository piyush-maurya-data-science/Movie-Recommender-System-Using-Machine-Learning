import streamlit as st
import pickle
import requests
import time


######################################
## to hit the api, requests library is required

## Function to fetch movie poster

def fetch_poster(movie_id):
    ## response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=273435ee8f82a2a4b2a6cfe47a91e98a'.format(movie_id))
    for _ in range(3): # Retry up to 3 times in case of failure
        try:
            response = requests.get(
                'https://api.themoviedb.org/3/movie/{}?api_key=273435ee8f82a2a4b2a6cfe47a91e98a'.format(movie_id), timeout=5)
            response.raise_for_status()
            data = response.json()

            # Check if 'poster_path' is available
            if data.get('poster_path'):
                return 'https://image.tmdb.org/t/p/w500/' + data['poster_path']
            else:
                return "https://via.placeholder.com/500"  # Placeholder if no poster path is available



        except requests.exceptions.RequestException as e:
            print(f'Error fetching poster: {e}. Retrying...')
            time.sleep(2) # Wait 2 seconds before retrying
    return "https://via.placeholder.com/500"  # Fallback placeholder if all retries fail


######################################
## recommend function

def recommend(movie):
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list_sorted = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list_sorted:
        #movie_id = i[0]
        tmdb_id = movies_list.iloc[i[0]]['movie_id']  # Ensure 'movie_id' column exists in movies.pkl
        recommended_movies.append(movies_list.iloc[i[0]].title)

        ## Fetch poster from API
        recommended_movies_posters.append(fetch_poster(tmdb_id))

    return recommended_movies, recommended_movies_posters





######################################
##import pickle files
movies_list = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movies = movies_list['title'].values

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Select a movie for recommendations:',
    movies
)

if st.button('Recommend'):

    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])