import pickle
import pandas as pd
import streamlit as st
import gzip


def load_compressed_pickle(filename, compression_type='gzip'):
    if compression_type == 'gzip':
        with gzip.open(filename, 'rb') as f:
            return pickle.load(f)
    else:
        raise ValueError(f"Unsupported compression type: {compression_type}")
    
# Recommendation function using the DataFrame
def recommend(movie):
    # Find the index of the selected movie
    index = movies[movies['title'] == movie].index[0]
    
    # Get the sorted list of similarity distances
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    
    # Prepare lists to hold recommended movie names and similarity scores
    recommended_movie_names = []
    similarity_scores = []
    
    # Loop through the top 10 recommendations (excluding the first one, which is the selected movie)
    for i in distances[1:11]:  # Start from 1 to skip the selected movie itself
        similarity_scores.append(i[1])  # Append similarity score
        recommended_movie_names.append(movies.iloc[i[0]]['title'])  # Fetch title

    return recommended_movie_names, similarity_scores

# Streamlit application
st.header('Movie Recommender System')

# Load the DataFrame and similarity matrix
movies = pd.DataFrame(pickle.load(open('movie_list.pkl', 'rb')))
similarity = load_compressed_pickle('similarity_compressed.pkl.gz', 'gzip')

# Display dropdown with movie titles
movie_list = movies['title'].values  # Extract titles from DataFrame
selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

# Function to color-code the similarity score
def color_similarity(score):
    if score > 0.30:
        return 'rgba(0, 225, 0, 0.6)'  # Green with 0.6 opacity (high similarity)
    elif 0.20 <= score <= 0.30:
        return 'rgba(0, 0, 255, 0.6)'  # Blue with 0.6 opacity (medium similarity)
    else:
        return 'rgba(255, 0, 0, 0.8)'  # Red with 0.8 opacity (low similarity)

# Add color legend
st.markdown("""
    <div style='display: flex; justify-content: space-between; margin-bottom: 15px;'>
        <span style='color: rgba(0, 225, 0, 0.6);'>■ High Recomendation </span>
        <span style='color: rgba(0, 0, 255, 0.6);'>■ Medium Recomendation </span>
        <span style='color: rgba(255, 0, 0, 0.8);'>■ Low Recomendation </span>
    </div>
""", unsafe_allow_html=True)

# Display recommendations on button click
if st.button('Show Recommendation'):
    recommended_movie_names, similarity_scores = recommend(selected_movie)
    
    # Display the movie names and their similarity scores with color-coding
    for movie, score in zip(recommended_movie_names, similarity_scores):
        color = color_similarity(score)  # Get color based on similarity
        st.markdown(f"<span style='color:{color}'>{movie}</span>", unsafe_allow_html=True)
