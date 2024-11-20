import streamlit as st
import pandas as pd

# Dummy Data for Movies and Similarity
movies = pd.DataFrame({
    'title': ['Avatar', 'Spectre', 'Dark Knight', 'Spiderman 3', 'Tangled', 'Man of Steel'],
    'movie_id': [101, 102, 103, 104, 105, 106]
})

similarity = [
    [1, 0.8, 0.2, 0.1, 0.5, 0.3],
    [0.8, 1, 0.3, 0.4, 0.6, 0.2],
    [0.2, 0.3, 1, 0.7, 0.1, 0.4],
    [0.1, 0.4, 0.7, 1, 0.5, 0.6],
    [0.5, 0.6, 0.1, 0.5, 1, 0.8],
    [0.3, 0.2, 0.4, 0.6, 0.8, 1],
]

# Function to fetch dummy posters
def fetch_poster(movie_id):
    return f"https://via.placeholder.com/150?text=Movie+{movie_id}"

# Function to recommend movies
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # Dummy recommendations
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters

# Streamlit App
st.header('Movie Recommender System')

# Dropdown for movie selection
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

# Display Recommendations
if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)  # Updated for modern Streamlit
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
