from moviedb import db

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    director = db.Column(db.String(50), nullable=False)
    genre = db.Column(db.String(20), nullable=False)
    release_year = db.Column(db.Integer, nullable=False)
