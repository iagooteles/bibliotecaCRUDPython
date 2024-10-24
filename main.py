from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from DB.models.book_model import db
from routes import routes 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(routes)

if __name__ == "__main__":
    app.run(debug=True)
