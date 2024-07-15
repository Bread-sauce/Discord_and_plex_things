import requests

# Your Radarr API key and URL
radarr_url = 'http://192.168.1.2:7878'
api_key = 'api_key_here'

def get_movies():
    """Retrieve list of all movies from Radarr."""
    url = f"{radarr_url}/api/v3/movie"
    params = {'apikey': api_key}
    response = requests.get(url, params=params)
    response.raise_for_status()  # This will raise an error for HTTP error codes
    return response.json()

def get_codec(movie):
    """Retrieve the codec of the movie."""
    if 'movieFile' in movie and 'mediaInfo' in movie['movieFile']:
        media_info = movie['movieFile']['mediaInfo']
        print(f"Debug: media_info for {movie['title']}: {media_info}")  # Debug print statement
        if isinstance(media_info, dict) and 'videoCodec' in media_info:
            return media_info['videoCodec']
    return None

def get_tags():
    """Retrieve the list of tags from Radarr."""
    url = f"{radarr_url}/api/v3/tag"
    params = {'apikey': api_key}
    response = requests.get(url, params=params)
    response.raise_for_status()  # This will raise an error for HTTP error codes
    return response.json()

def get_tag_id(tags, tag_name):
    """Get the ID of the tag with the given name. Create the tag if it doesn't exist."""
    for tag in tags:
        if tag['label'] == tag_name:
            return tag['id']
    
    # Tag not found, create it
    url = f"{radarr_url}/api/v3/tag"
    headers = {'Content-Type': 'application/json'}
    params = {'apikey': api_key}
    payload = {'label': tag_name}
    response = requests.post(url, json=payload, headers=headers, params=params)
    response.raise_for_status()  # This will raise an error for HTTP error codes
    return response.json()['id']

def add_tag(movie_id, tag_id):
    """Add a tag to a movie using the /movie/editor endpoint."""
    url = f"{radarr_url}/api/v3/movie/editor"
    headers = {'Content-Type': 'application/json'}
    params = {'apikey': api_key}
    payload = {
        "movieIds": [movie_id],
        "tags": [tag_id],
        "applyTags": "add"
    }
    response = requests.put(url, json=payload, headers=headers, params=params)
    response.raise_for_status()  # This will raise an error for HTTP error codes
    return response.json()

def main():
    movies = get_movies()
    tags = get_tags()
    for movie in movies:
        codec = get_codec(movie)
        if codec:
            tag_name = codec.lower()
            try:
                tag_id = get_tag_id(tags, tag_name)
                add_tag(movie['id'], tag_id)
                print(f"Added tag '{tag_name}' to movie '{movie['title']}'")
            except requests.exceptions.HTTPError as err:
                print(f"Failed to add tag '{tag_name}' to movie '{movie['title']}': {err}")

if __name__ == "__main__":
    main()
