# this file is only a base model for sqlite3 only, in the other file 'mainDB.py' we are going to use sqlAlchemy, that's the one we are using for this project. #

import sqlite3

db = sqlite3.connect("books-collection.db", timeout=10)
cursor = db.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

cursor.execute("DELETE FROM books")

# SEED
cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
cursor.execute("INSERT INTO books VALUES(2, 'Eragon', 'Christopher Paolini', '8.5')")
cursor.execute("INSERT INTO books VALUES(3, 'Star Wars', 'George Lucas', '8.8')")
cursor.execute("INSERT INTO books VALUES(4, 'The Hobbit', 'J. R. R. Tolkien', '9.2')")
cursor.execute("INSERT INTO books VALUES(5, 'Game of Thrones', 'George R. R. Martin', '9.4')")
cursor.execute("INSERT INTO books VALUES(6, 'The Catcher in the Rye', 'J. D. Salinger', '8.7')")
cursor.execute("INSERT INTO books VALUES(7, '1984', 'George Orwell', '9.0')")
cursor.execute("INSERT INTO books VALUES(8, 'The Great Gatsby', 'F. Scott Fitzgerald', '8.9')")
cursor.execute("INSERT INTO books VALUES(9, 'Moby Dick', 'Herman Melville', '8.6')")
cursor.execute("INSERT INTO books VALUES(10, 'Pride and Prejudice', 'Jane Austen', '9.1')")

db.commit()
db.close()
