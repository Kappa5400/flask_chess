from logging import exception
from flask import Flask, g
import requests
import sqlite3
import time

app = Flask(__name__)

DATABASE ='database.db'

#db boilerplate
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


#puzzle model

class puzzle():
    def __init__(self):

        puzzle_id = "0"
        pgn = ""
        answer = ""
        puzzle_rating = '0'
        date = time.now()



    def get_data(self):
        try:
            raw = requests.get("https://lichess.org/api/puzzle/daily")
            response = raw.json()
            game = raw["game"]
            puzzle = raw["puzzle"]

            puzzle_id = puzzle["id"]
            pgn = game["pgn"]
            answer = puzzle["solution"]
            puzzle_rating = puzzle['rating']
            date = time.now()
            self.post_puzzle()

        except exception as e:
            print(f"Error: {e}")

    def post_puzzle(self):
        db = get_db()
        db.execute("INSERT INTO puzzle (puzzle_id, pgn, answer, puzzle_rating,date) VALUES(?,?,?,?, ?)",
                  (self.puzzle_id, self.pgn, self.answer, self.puzzle_rating, self.date)
                   )
        db.commit()

# views
@app.route("/")
def hello_world():
    return "<p>Hiya</p>"



