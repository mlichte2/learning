import sqlite3

conn = sqlite3.connect('hw2_db.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fname = input('Enter file name: ')
if (len(fname) < 1):
    fname = 'mbox.txt'
fh = open(fname)

for line in fh:
    line = line.rstrip()
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    pieces = pieces[1].split('@')
    org = pieces[1]
    print(org)
    cur.execute('SELECT count FROM Counts WHERE org = ?', (org, ))
    row = cur.fetchone()

    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (? , 1)', (org,))
    else:
        cur.execute(
            'UPDATE Counts SET count = count + 1 WHERE org = ?', (org, ))
    conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(row[0], row[1])
