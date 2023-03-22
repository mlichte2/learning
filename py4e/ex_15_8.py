# previously did one-many data model

# MANY TO MANY data model

# Course <- Member -> User
# --------------------------
# id      user_id     id
# title   course_id   name
#                     email

# so member has two foreign keys which connects it to course and user
# member does not have a primary key

# CREATE TABLE User (
# 	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
# 	name TEXT,
# 	email TEXT
# );

# CREATE TABLE Course (
# 	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
# 	title TEXT
# );

# CREATE TABLE Member (
# 	user_id INTEGER,
# 	course_id INTEGER,
# 	role INTEGER,
# 	PRIMARY KEY (user_id, course_id)
# );

# INSERT INTO User (name, email) VALUES ('Jane', 'jane@tsugi.org');
# INSERT INTO User (name, email) VALUES ('Ed', 'ed@tsugi.org');
# INSERT INTO User (name, email) VALUES ('Sue', 'sue@tsugi.org');

# INSERT INTO Course (title) VALUES ('Python');
# INSERT INTO Course (title) VALUES ('SQL');
# INSERT INTO Course (title) VALUES ('PHP');

# INSERT INTO Member (user_id, course_id, role) VALUES (1,1,1);
# INSERT INTO Member (user_id, course_id, role) VALUES (2,1,0);
# INSERT INTO Member (user_id, course_id, role) VALUES (3,1,0);

# INSERT INTO Member (user_id, course_id, role) VALUES (1,2,0);
# INSERT INTO Member (user_id, course_id, role) VALUES (2,2,1);

# INSERT INTO Member (user_id, course_id, role) VALUES (2,3,1);
# INSERT INTO Member (user_id, course_id, role) VALUES (3,3,0);

# SELECT User.name, Member.role, Course.title
# FROM User JOIN Member JOIN Course
# on Member.user_id = User.id AND Member.course_id = Course.id
# ORDER BY Course.title, Member.role DESC, User.name

# returns
# Ed	1	PHP
# Sue	0	PHP
# Jane	1	Python
# Ed	0	Python
# Sue	0	Python
# Ed	1	SQL
# Jane	0	SQL

import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# Do some setup

cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Course (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE
);

CREATE TABLE Member (
    user_id INTEGER,
    course_id INTEGER,
    role INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'roster_data.json'

str_data = open(fname).read()
json_data = json.loads(str_data)


for line in json_data:
    name = line[0]
    title = line[1]
    role = line[2]

    cur.execute('INSERT OR IGNORE INTO User (name) VALUES (?)', (name,))

    cur.execute('SELECT id FROM User WHERE name = ?', (name,))
    user_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)', (title,))

    cur.execute('SELECT id FROM Course WHERE title = ?', (title,))
    course_id = cur.fetchone()[0]

    cur.execute(
        'INSERT OR REPLACE INTO Member (user_id, course_id, role) VALUES (?,?,?)', (user_id, course_id, role))

    conn.commit()

cur.execute('SELECT User.name, Course.title, Member.role FROM User JOIN Course JOIN Member ON Member.user_id = User.id AND Member.course_id = Course.id')
student_list = cur.fetchall()
for student in student_list:
    print(*student)
