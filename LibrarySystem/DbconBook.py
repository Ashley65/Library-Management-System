import sqlite3
import os
import sys

# connect to the database and create a cursor object for the library database
conn = sqlite3.connect('books.db')
c = conn.cursor()
conn.PRAGMA.foreign_keys = 1
# create a table for the books database
c.execute('''CREATE TABLE IF NOT EXISTS books(
    serial_no INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(225) NOT NULL,
    author VARCHAR(225) NOT NULL,
    genre_ID INTEGER NOT NULL, FOREIGN KEY (genre_ID) references genre(genre_ID)
    )''')


# create a table for the issue database
c.execute('''CREATE TABLE IF NOT EXISTS issue(
    issue_no INTEGER PRIMARY KEY AUTOINCREMENT,
    serial_no INTEGER NOT NULL,
    issue_date DATE NOT NULL,
    student_name VARCHAR(225) NOT NULL,
    student_id VARCHAR(25) NOT NULL, 
    FOREIGN KEY (serial_no) REFERENCES books(serial_no))''')


# create a table for the genre database
c.execute('''CREATE TABLE IF NOT EXISTS genre(
    genre_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    genre_name VARCHAR(225) NOT NULL)''')

c.execute()

#

# commit the changes to the database
conn.commit()
