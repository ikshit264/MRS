import requests

# Define the API URL with the movie ID
url = "https://api.themoviedb.org/3/movie/19995/images"

# Set the headers, including the authorization Bearer token
headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzMDg5YmE2YTk5ZWRjNTMzY2MyOTQ3Y2RlMTgwNTliZSIsIm5iZiI6MTcyOTMzNDAyNi40NzUwMTksInN1YiI6IjY3MTM4YTJmMGNiNjI1MmY5OTA4M2ZhMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.0secQdnywLRY0eksBo4XLbLJg8e41tRJnty1Te9LOZY"
}

# Make the GET request to fetch movie images
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # If successful, print the JSON response
    print(response.json())
else:
    # If not, print the status code and error message
    print(f"Error: {response.status_code}")
    print(response.json())  # Print the error details









# import pickle
# import pandas as pd

# '3089ba6a99edc533cc2947cde18059be'

# Load data
# movies = pickle.load(open('movie_list.pkl', 'rb'))
# similarity = pickle.load(open('similarity.pkl', 'rb'))

# # Convert dictionary to DataFrame
# df = pd.DataFrame(movies)

# # Inspect the DataFrame
# print(df.head())

# # Test: Accessing the movie title
# print(df['title'][0])  # This prints the first movie title

# # Fix: Find index for the movie 'Avatar' (case-insensitive)
# # Ensure that the comparison is case-insensitive
# avatar_index = df[df['title'].str.lower() == 'avatar'].index[0]
# print(f"Index of 'Avatar': {avatar_index}")

# id = df[df['title'].str.lower() == 'avatar']['id'].values