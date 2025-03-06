import requests
import random

API_KEY = "your_api_key_here"  # Replace with your actual TMDB API key
GENRE_URL = f"https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}&language=en-US"
MOVIE_URL = "https://api.themoviedb.org/3/discover/movie"

def get_genre_id(genre_name):
    response = requests.get(GENRE_URL)
    if response.status_code == 200:
        genres = response.json()["genres"]
        for genre in genres:
            if genre["name"].lower() == genre_name.lower():
                return genre["id"]
    return None

def recommend_movie(genre_name):
    genre_id = get_genre_id(genre_name)
    if genre_id is None:
        print("Genre not found.")
        return

    params = {
        "api_key": API_KEY,
        "with_genres": genre_id
    }

    response = requests.get(MOVIE_URL, params=params)
    if response.status_code == 200:
        movies = response.json()["results"]
        if movies:
            movie = random.choice(movies)
            print(f"Recommended Movie: {movie['title']}")
            print(f"Overview: {movie['overview']}")
        else:
            print("No movies found for this genre.")
    else:
        print("Failed to fetch movie data.")

genre = input("Enter a movie genre: ")
recommend_movie(genre)