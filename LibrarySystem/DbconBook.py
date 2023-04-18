import sqlite3

# connect to the database and create a cursor object for the library database
conn = sqlite3.connect('books.db')
c = conn.cursor()

# create a table for the books
c.execute('''CREATE TABLE IF NOT EXISTS books(
    bookID INTEGER PRIMARY KEY AUTOINCREMENT,
    book_Title VARCHAR(225) NOT NULL,
    book_Author VARCHAR(225) NOT NULL,
    book_Genre VARCHAR(225) NOT NULL,
    book_status boolean NOT NULL DEFAULT 0,
    book_publishDate DATE NOT NULL
    )''')

c.execute('''CREATE TABLE IF NOT EXISTS issue(
    issueID INTEGER PRIMARY KEY AUTOINCREMENT,
    bookID INTEGER NOT NULL,
    studentID INTEGER NOT NULL,
    issueDate DATE NOT NULL,
    dueDate DATE NOT NULL,
    FOREIGN KEY (bookID) REFERENCES books(bookID),
    FOREIGN KEY (studentID) REFERENCES students(studentID)
    )''')
c.execute('''insert into books(book_Title,book_Author,book_Genre,book_publishDate) values('Game of Thrones','George R.R. Martin','Fiction','2011-08-16')''')
c.execute('''insert into books(book_Title,book_Author,book_Genre,book_publishDate) values('A Clash of Kings','George R.R. Martin','Fiction','1999-02-02')''')
c.execute('''insert into books(book_Title,book_Author,book_Genre,book_publishDate) values('A Storm of Swords','George R.R. Martin','Fiction','2000-08-08')''')
c.execute('''insert into books(book_Title,book_Author,book_Genre,book_publishDate) values('A Feast for Crows','George R.R. Martin','Fiction','2005-11-08')''')
c.execute('''insert into books(book_Title,book_Author,book_Genre,book_publishDate) values('A Dance with Dragons','George R.R. Martin','Fiction','2011-07-12')''')
c.execute('''insert into books(book_Title,book_Author,book_Genre,book_publishDate) values('The Winds of Winter','George R.R. Martin','Fiction','2016-12-20')''')

c.execute('''CREATE TABLE IF NOT EXISTS students(
    studentID INTEGER PRIMARY KEY AUTOINCREMENT,
    student_Name VARCHAR(225) NOT NULL,
    student_Class VARCHAR(225) NOT NULL,
    stuent_email VARCHAR(225) NOT NULL,
    student_password VARCHAR(225) NOT NULL,
    student_status boolean NOT NULL DEFAULT 0
    )''')

c.execute('''insert into students(student_Name,student_Class,stuent_email,student_password) values('John','12','john@jh','Game123')''')
c.execute('''insert into students(student_Name,student_Class,stuent_email,student_password) values('Jack','12','jack@jh','Game124')''')
c.execute('''insert into students(student_Name,student_Class,stuent_email,student_password) values('Jill','12','jill@jh','Game125')''')
c.execute('''insert into students(student_Name,student_Class,stuent_email,student_password) values('Jenny','12','jenny@jh','Game126')''')
c.execute('''insert into students(student_Name,student_Class,stuent_email,student_password) values('Jen','12','jen@jh','Game127')''')
c.execute('''insert into students(student_Name,student_Class,stuent_email,student_password) values('Jenny','12','jenny@jh','Game128')''')
c.execute('''insert into students(student_Name,student_Class,stuent_email,student_password) values('Jenny','12','jenny@jh','Game129')''')
c.execute('''insert into students(student_Name,student_Class,stuent_email,student_password) values('Jenny','12','jenny@jh','Game130')''')
c.execute('''insert into students(student_Name,student_Class,stuent_email,student_password) values('Jenny','12','jenny@jh','Game131')''')

c.execute('''CREATE TABLE IF NOT EXISTS return(
    returnID INTEGER PRIMARY KEY AUTOINCREMENT,
    issueID INTEGER NOT NULL,
    returnDate DATE NOT NULL,
    FOREIGN KEY (issueID) REFERENCES issue(issueID)
    )''')

c.execute('''insert into books(book_Title,book_Author,book_Genre,book_publishDate) values('Harry Potter and the Philosopher''s Stone','J.K. Rowling','Fantasy','1997-06-26')''')
c.execute('''insert into books(book_Title,book_Author,book_Genre,book_publishDate) values('Harry Potter and the Chamber of Secrets','J.K. Rowling','Fantasy','1998-07-02')''')
c.execute('''insert into books(book_Title,book_Author,book_Genre,book_publishDate) values('Harry Potter and the Prisoner of Azkaban','J.K. Rowling','Fantasy','1999-07-08')''')
c.execute('''insert into books(book_Title,book_Author,book_Genre,book_publishDate) values('Harry Potter and the Goblet of Fire','J.K. Rowling','Fantasy','2000-07-08')''')
c.execute('''insert into books(book_Title,book_Author,book_Genre,book_publishDate) values('Harry Potter and the Order of the Phoenix','J.K. Rowling','Fantasy','2003-06-21')''')
c.execute('''insert into books(book_Title,book_Author,book_Genre,book_publishDate) values('Harry Potter and the Half-Blood Prince','J.K. Rowling','Fantasy','2005-07-16')''')
c.execute('''insert into books(book_Title,book_Author,book_Genre,book_publishDate) values('Harry Potter and the Deathly Hallows','J.K. Rowling','Fantasy','2007-07-21')''')
c.execute('''insert into books(book_Title,book_Author,book_Genre,book_publishDate) values('The Hobbit','J.R.R. Tolkien','Fantasy','1937-09-21')''')
c.execute('''insert into books(book_Title,book_Author,book_Genre,book_publishDate) values('The Fellowship of the Ring','J.R.R. Tolkien','Fantasy','1954-07-29')''')
c.execute('''insert into books(book_Title,book_Author,book_Genre,book_publishDate) values('The Two Towers','J.R.R. Tolkien','Fantasy','1954-11-11')''')
c.execute('''insert into books(book_Title,book_Author,book_Genre,book_publishDate) values('The Return of the King','J.R.R. Tolkien','Fantasy','1955-10-20')''')
c.execute('''insert into books(book_Title,book_Author,book_Genre,book_publishDate) values('The Silmarillion','J.R.R. Tolkien','Fantasy','1977-09-15')''')



c.execute('''CREATE TABLE IF NOT EXISTS librarian(
    librarianID INTEGER PRIMARY KEY AUTOINCREMENT,
    librarian_Name VARCHAR(225) NOT NULL,
    librarian_email VARCHAR(225) NOT NULL,
    librarian_password VARCHAR(225) NOT NULL,
    librarian_status boolean NOT NULL DEFAULT 0
    )''')
c.execute('''insert into librarian(librarian_Name,librarian_email,librarian_password) values('admin','admin@test.ac.uk','password')''')
c.execute('''insert into librarian(librarian_Name,librarian_email,librarian_password) values('admin2','admin2@test.ac.uk','password')''')




c.execute('''CREATE TABLE IF NOT EXISTS bookAuthor(
    bookAuthorID INTEGER PRIMARY KEY AUTOINCREMENT,
    bookAuthor_Name VARCHAR(225) NOT NULL,
    bookAuthor_status boolean NOT NULL DEFAULT 0
    )''')



c.execute('''insert into bookAuthor(bookAuthor_Name) values('J.K. Rowling')''')
c.execute('''insert into bookAuthor(bookAuthor_Name) values('J.R.R. Tolkien')''')
c.execute('''insert into bookAuthor(bookAuthor_Name) values('George R.R. Martin')''')
c.execute('''insert into bookAuthor(bookAuthor_Name) values('Stephen King')''')
c.execute('''insert into bookAuthor(bookAuthor_Name) values('J.D. Salinger')''')


# commit the changes to the database
conn.commit()
