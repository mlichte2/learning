# relational dbs

# database - contains many tables
# relation (or table) - contains tuples and attributes
# tuple (or row) - a set of fields that generally represents an "object" like a person or a music track
# attribute (also column or field) - one of possibly many elements of data corresponding to the object represented by the row

# schema contains the metadata and info about the contents

# using the db

# sqlite is built into python

# commands used

# SELECT * FROM Users ORDER BY email
# SELECT * FROM Users ORDER BY name
# SELECT * FROM Users
# SELECT * FROM Users WHERE email='kf@umich.edu'
# UPDATE Users SET name='Charles' WHERE email='kf@umich.edu'
# DELETE FROM Users WHERE email="mike@umich.edu"
# INSERT INTO Users (name, email) VALUES ('Kristin', 'kf@umich.edu')

# CREATE TABLE Users (
# 	name  VARCHAR(128),
# 	email VARCHAR(128)
# )

# worked example

import sqlite3
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('''
            CREATE TABLE Counts (email TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1):
    fname = 'mbox.txt'
fh = open(fname)

for line in fh:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE email = ?', (email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts (email, count) VALUES (?, 1)', (email,))
    else:
        cur.execute(
            'UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))
    conn.commit()

sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
