from flask import Blueprint, render_template, request, redirect, url_for
from DB.models.book_model import db, Book

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    all_books = Book.query.all()
    return render_template('index.html', all_books=all_books)

@routes.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        rating = request.form['rating']

        new_book = Book(title=title, author=author, rating=float(rating))

        db.session.add(new_book)
        db.session.commit()
        db.session.remove()

        return redirect(url_for('routes.home'))

    return render_template('add.html')

@routes.route("/edit/<int:book_id>", methods=['GET', 'POST'])
def edit(book_id):
    book = Book.query.get_or_404(book_id)
    
    if request.method == 'POST':
        book.title = request.form['title']
        book.author = request.form['author']
        book.rating = request.form['rating']
        db.session.commit()
        return redirect(url_for('routes.home'))

    return render_template('edit.html', book=book)

@routes.route("/delete/<int:book_id>")
def delete(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('routes.home'))
