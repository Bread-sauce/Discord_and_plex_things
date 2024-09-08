import requests
import sys

# Configuration
radarr_4k_url = 'http://4k-radarr-url/api/v3'
radarr_4k_apikey = 'your_radarr_4k_api_key'
movie_library_name = 'Movies'  # The library you want to track

# Radarr function to search movie by title
def search_movie_in_radarr(movie_title):
    url = f"{radarr_4k_url}/movie/lookup?term={movie_title}"
    headers = {'X-Api-Key': radarr_4k_apikey}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error searching movie: {response.status_code}")
        return None

# Radarr function to add a movie to 4K Radarr
def add_movie_to_4k_radarr(movie_data):
    url = f"{radarr_4k_url}/movie"
    headers = {'X-Api-Key': radarr_4k_apikey}
    payload = {
        "tmdbId": movie_data['tmdbId'],  # Ensure the TMDB ID is passed
        "title": movie_data['title'],
        "year": movie_data['year'],
        "qualityProfileId": 5,  # Adjust according to your 4K profile ID in Radarr
        "rootFolderPath": "/movies",  # Update with your 4K folder path
        "monitored": True,
        "addOptions": {"searchForMovie": True}
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 201:
        print(f"Successfully added {movie_data['title']} to 4K Radarr")
    else:
        print(f"Error adding movie: {response.status_code}, {response.content}")

# Main function to process the data passed from Tautulli
def process_tautulli_data(movie_title, library_name):
    if library_name == movie_library_name:
        print(f"{movie_title} watched from the 'Movies' library. Adding to 4K Radarr.")
        movie_data = search_movie_in_radarr(movie_title)
        if movie_data:
            add_movie_to_4k_radarr(movie_data[0])
    else:
        print(f"Movie '{movie_title}' was not watched in the 'Movies' library.")

# Get the arguments passed from Tautulli
if __name__ == "__main__":
    # Tautulli passes these arguments when triggering the script
    movie_title = sys.argv[1]  # Movie title
    library_name = sys.argv[2]  # Library name (e.g., 'Movies')

    # Process the Tautulli data
    process_tautulli_data(movie_title, library_name)
