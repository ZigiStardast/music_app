import sqlite3
from datetime import datetime, timedelta


def load_to_db(dim_artists, dim_albums, fact_tracks, db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    
    # dim_artist
    cur.execute("""
                CREATE TABLE IF NOT EXISTS dim_artist (
                    id INTEGER PRIMERY KEY,
                    name TEXT
                )
                """)
    
    # dim_album
    cur.execute("""
                CREATE TABLE IF NOT EXISTS dim_album (
                    id INTEGER PRIMARY KEY,
                    title TEXT
                )
                """)
    
    # fact_tracks
    cur.execute("""
                CREATE TABLE IF NOT EXISTS fact_tracks (
                    id INTEGER PRIMARY KEY,
                    title TEXT,
                    link TEXT,
                    duration INTEGER,
                    artist_id INTEGER,
                    album_id INTEGER,
                    date_id INTEGER,
                    FOREIGN KEY (artist_id) REFERENCES dim_artist(id),
                    FOREIGN KEY (album_id) REFERENCES dim_album(id)
                )
                """)
    
    
    # insert
    cur.executemany("INSERT OR IGNORE INTO dim_artist (id, name) VALUES (?, ?)", dim_artists)
    cur.executemany("INSERT INTO IGNORE INTO dim_album (id, title) VALUES (?, ?)", dim_albums)
    
    cur.executemany("""
                    INSERT OR REPLACE INTO fact_tracks
                    (id, title, link, duration, artist_id, album_id, date_id)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    """, fact_tracks)
    
    dates = generate_dates()
    
    cur.executemany("""
        INSERT OR IGNORE INTO dim_date (date_id, full_date, day, month, year, weekday_name)
        VALUES (?, ?, ?, ?, ?, ?)
    """, dates)
    
    
    conn.commit()
    conn.close()
    
    
def generate_dates():
    start_date = datetime(2025, 5, 20)
    dates = []
    for i in range(365 * 5):  # 5 godina
        date = start_date + timedelta(days=i)
        date_id = int(date.strftime("%Y%m%d"))
        dates.append((date_id, date.date(), date.day, date.month, date.year, date.strftime("%A")))

    return dates