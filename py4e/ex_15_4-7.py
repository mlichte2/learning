# designing a data model

# think about what is most essential for the app?
# in this case its tracks

# 1st build the track table by figuring out what parts of the data are attributes of tracks
# 2nd add whats not part of a track (artists, albums, genre) -- whats connected?

# primary key -> a unique number (so an album_id -- foreign key -- that the track can use to map the track to the album)
# logical key -> might be used in a WHERE clause

# time to get it now -- going to use JOIN Operation

# SELECT Album.title, Artist.name from Album JOIN Artist on Album.artist_id = Artist.id


# SELECT Track.title, Album.title from Track JOIN Album on Track.album_id = Album.id

# # returns
# # Black Dog	IV
# # Stairway	IV
# # About to Rock	Who Made Who
# # Who Made Who	Who Made Who

# SELECT Track.title, Artist.name, album.title, Genre.name
# FROM Track JOIN Genre JOIN Album JOIN Artist
# on Track.genre_id = Genre.id and track.album_id = Album.id and album.artist_id = artist.id

# returns
# Black Dog	Led Zepplin	IV	rock
# Stairway	Led Zepplin	IV	rock
# About to Rock	AC/DC	Who Made Who	metal
# Who Made Who	AC/DC	Who Made Who	metal

import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('trackdb-hw.sqlite')
cur = conn.cursor()

# make some fresh tables using executescript()
cur.executescript("""

DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;


CREATE TABLE Artist (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Genre (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Album (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id INTEGER,
    title TEXT UNIQUE
);

CREATE TABLE Track (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id INTEGER,
    genre_id INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);

""")

fname = input('Enter file name: ')
if (len(fname) < 1):
    fname = 'Library.xml'


def lookup(d, key):
    found = False
    for child in d:
        if found:
            return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None


stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print('Dict count:', len(all))
for entry in all:
    if (lookup(entry, 'Track ID') is None):
        continue
    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')
    genre = lookup(entry, 'Genre')

    if name is None or artist is None or album is None or genre is None:
        continue

    print(name, artist, album, count, rating, length, genre)

    # or ignore basically says if the artist is already there dont add a new one
    cur.execute('''
    INSERT OR IGNORE INTO Artist (name) VALUES (?) 
    ''', (artist, ))

    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''
    INSERT OR IGNORE INTO Genre (name) VALUES (?)
    ''', (genre, ))

    cur.execute('SELECT id FROM Genre WHERE name = ?', (genre, ))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', (album, artist_id))

    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, len, rating, count, genre_id) 
        VALUES ( ?, ?, ?, ?, ?, ? )''',
                (name, album_id, length, rating, count, genre_id))

    conn.commit()
