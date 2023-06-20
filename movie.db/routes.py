from flask import jsonify, request
from moviedb import app, db
from moviedb.models import Movie

@app.route('/movies', methods=['POST'])
def add_movie():
    new_movie = Movie(
        title=request.json['title'], 
        director=request.json['director'], 
        genre=request.json['genre'],
        release_year=request.json['release_year'])
    db.session.add(new_movie)
    db.session.commit()
    return jsonify(new_movie)

@app.route('/movies', methods=['GET'])
def get_all_movies():
    movies = Movie.query.all()
    return jsonify([movie.to_dict() for movie in movies])

@app.route('/movies/<int:id>', methods=['GET'])
def get_movie(id):
    movie = Movie.query.get(id)
    return jsonify(movie.to_dict())

@app.route('/movies/<int:id>', methods=['PUT'])
def update_movie(id):
    movie = Movie.query.get(id)
    movie.title = request.json['title']
    movie.director = request.json['director']
    movie.genre = request.json['genre']
    movie.release_year = request.json['release_year']
    db.session.commit()
    return jsonify(movie.to_dict())

@app.route('/movies/<int:id>', methods=['DELETE'])
def delete_movie(id):
    movie = Movie.query.get(id)
    db.session.delete(movie)
    db.session.commit()
    return jsonify({'result': 'Movie deleted'})
