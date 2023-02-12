import sqlite3

conn = sqlite3.connect('LoginSystem.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS LoginSystem(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(225) NOT NULL,
    password VARCHAR(225) NOT NULL,
    email VARCHAR(225) NOT NULL UNIQUE,
    phone VARCHAR(225) UNIQUE,
    address VARCHAR(225),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )''')

conn.commit()
