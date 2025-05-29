from etl.extract import fetch_artists_and_tracks
from etl.transform import transform_data
from etl.load import load_to_db


if __name__ == "__main__":
    artist_names = ["guns and roses", "david bowie", "metallica", "lana del rey"]

    print("Data extraction...")
    raw_data = fetch_artists_and_tracks(artist_names)

    print("Data transformation...")
    dim_artists, dim_albums, dim_genres, fact_tracks = transform_data(raw_data)

    print("Loading Data into DB...")
    load_to_db(dim_artists, dim_albums, dim_genres, fact_tracks)

    print("ETL done.")