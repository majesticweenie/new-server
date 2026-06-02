from flask import Flask, jsonify 
import json
import os 

app = Flask(__name__)



def load_records():
    if os.path.exists("records.json"):
        with open("records.json", "r") as file: 
            return json.load(file)
    else:
        return []
    
def list_movies():
    movies = load_records()

    return jsonify(movies)


def get_movie(movie_id):
    movies = load_records()

    for movie in movies:
        if movie["id"] == movie_id:
            return movie
        
    return None

def get_summary():
    records = load_records()

    return jsonify({
        "status": "ok",
        "message": "server is running",
        "recordCount": len(records),
        "routes": ["/", "/tasks", "/tasks/<id>", "/status"]
    })

# Make an if statement and show "400" if status does not work. maybe for the @app.route section

@app.route("/")
def home():
    return jsonify([
        {"Status": "200"},
        {"Home": "Hello User, this Program is running!"}
    ])

@app.route("/movies")
def route_movies():
    return jsonify(load_records())
    

@app.route("/movies/<int:movie_id>")
def route_movie(movie_id):
    movie = get_movie(movie_id)
    
    if movie is None:
        return jsonify({
            "error": "movie not found",
            "id": movie_id
        }), 404
    
    return jsonify(movie)




@app.route("/summary")
def route_summary():
    return get_summary()








if __name__ == "__main__":
    app.run(port= 5000, debug= True)