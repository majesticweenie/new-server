from flask import Flask, jsonify 
import json
import os 

app = Flask(__name__)

filename = "records.json"

def load_records(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file: 
            return json.load(file)
    else:
        return []
    
def list_movies():
    movies = load_records(filename)

    return jsonify(movies)


def get_movie(movie_id):
    movies = load_records(filename)

    for movie in movies:
        if movie["id"] == movie_id:
            return movie
        
        return None

def get_summary():
    return jsonify([
        {"Status": "200"}
    ])

# Make an if statement and show "400" if status does not work. maybe for the @app.route section









if __name__ == "__main__":
    app.run(port= 5000, debug= True)