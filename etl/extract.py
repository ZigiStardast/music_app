import requests

def fetch_artists_and_tracks(artist_names):
    
    all_data = []
    
    for artist in artist_names:
        artist_search_url = f"https://api.deezer.com/search/artist?q={artist}"
        artist_response = requests.get(artist_search_url).json()
        
        if not artist_response['data']:
            print(f"No matches for {artist}")
            continue
        
        artist_info = artist_response['data'][0]
        artist_id = artist_info['id']
        artist_name = artist_info['name']
        artist_tracklist = requests.get(artist_info['tracklist']).json()['data']
        artist_picture_medium = artist_info["picture_medium"]
        
        all_data.append(
            {
                "artist_id": artist_id,
                "artist_name": artist_name,
                "picture": artist_picture_medium,
                "tracks": artist_tracklist
            }
        )
        
    return all_data
        
        
    