import sqlite3

# connect to the database and create a cursor object for the library database
conn = sqlite3.connect('books.db')
c = conn.cursor()
conn2 = sqlite3.connect('issue.db')
c2 = conn2.cursor()
conn3 = sqlite3.connect('genre.db')
c3 = conn3.cursor()

# create a table for the books database
c.execute('''CREATE TABLE IF NOT EXISTS books(
    serial_no INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(225) NOT NULL,
    author VARCHAR(225) NOT NULL,
    genre_ID INTEGER NOT NULL FOREIGN KEY REFERENCES genre(genre)
    )''')

# create a table for the issue database
c2.execute('''CREATE TABLE IF NOT EXISTS issue(
    serial_no INTEGER PRIMARY KEY AUTOINCREMENT,
    issue_date DATE NOT NULL,
    student_name VARCHAR(225) NOT NULL,
    student_id VARCHAR(225) NOT NULL)''')

# create a table for the genre database
c3.execute('''CREATE TABLE IF NOT EXISTS genre(
    genre_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    genre VARCHAR(225) NOT NULL)''')

# commit the changes to the database
conn.commit()
