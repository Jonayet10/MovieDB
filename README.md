# moviedb
This project involves creating a simple RESTful API for a movie database using Flask, a micro web framework in Python, and SQLite, a lightweight disk-based database. The API will allow users to perform various operations such as create, read, update, and delete (CRUD) operations on the movie data.


# Flask MovieDB API

This is a RESTful API built with Flask and SQLite for managing a simple movie database.

## Endpoints

- **POST /movies:** Add a new movie
- **GET /movies:** Get all movies
- **GET /movies/:id:** Get a specific movie
- **PUT /movies/:id:** Update a specific movie
- **DELETE /movies/:id:** Delete a specific movie

## Setup

1. Clone this repository.
2. Install the dependencies: `pip install -r requirements.txt`
3. Run the server: `python run.py`

## Sample Request


POST /movies
Content-Type: application/json

{
"title": "Interstellar",
"director": "Christopher Nolan",
"genre": "Sci-Fi",
"release_year": 2014
}


## Sample Response

{
"id": 1,
"title": "Interstellar",
"director": "Christopher Nolan",
"genre": "Sci-Fi",
"release_year": 2014
}
