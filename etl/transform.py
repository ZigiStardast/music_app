from datetime import datetime

def transform_data(raw_data): # raw data je onaj all_data iz extract.py
    dim_artists = []
    dim_albums = []
    fact_tracks = []
    
    artist_ids_seen = set()
    album_ids_seen = set()
    
    date_id = int(datetime.today().strftime("%Y%m%d"))  # dim_date simulacija
    
    for entry in raw_data:
        artist_id = entry["artist_id"]
        artist_name = entry["artist_name"]
        tracks = entry["tracks"]
        
        if artist_id not in artist_ids_seen:
            dim_artists.append((artist_id, artist_name))
            artist_ids_seen.add(artist_id)
            
        for track in tracks:
            album_id = track["album"]["id"]
            album_title = track["album"]["title"]
            
            if album_id not in album_ids_seen:
                dim_albums.append((album_id, album_title))
                album_ids_seen.add(album_id)
            
            
            fact_tracks.append((
            track["id"],                # track_id
            track["title"],            # title
            track["link"],             # link
            track["duration"],         # duration
            artist_id,                 # artist_id (FK)
            album_id,                  # album_id (FK)
            date_id                  # date_id
        ))

    return dim_artists, dim_albums, fact_tracks