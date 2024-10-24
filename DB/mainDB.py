from flask import Flask
from models.book_model import db, Book
from seed import books_to_add 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        existing_books = db.session.query(Book).all()
        existing_ids = {book.id for book in existing_books}
        existing_titles = {book.title for book in existing_books}

        new_books = [book for book in books_to_add if book.id not in existing_ids and book.title not in existing_titles]

        db.session.add_all(new_books)
        db.session.commit()
    
    print('Finished seeding database.')
