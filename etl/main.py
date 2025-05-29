from extract import fetch_artists_and_tracks
from transform import transform_data
from load import load_to_db


if __name__ == "__main__":
    artist_names = ["guns and roses", "david bowie", "metallica", "lana del rey"]
    db_path = "../data/deezer.db"

    print("Data extraction...")
    raw_data = fetch_artists_and_tracks(artist_names)

    print("Data transformation...")
    dim_artists, dim_albums, fact_tracks = transform_data(raw_data)

    print("Loading Data into DB...")
    load_to_db(dim_artists, dim_albums, fact_tracks, db_path)

    print("ETL done.")