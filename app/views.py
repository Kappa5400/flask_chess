from flask import Blueprint, g, current_app, jsonify, render_template
from .db import get_db
from .services import fetch_puzzle
from datetime import datetime





bp = Blueprint('main', __name__)

# views
@bp.route("/")
def index():
    return render_template("index.html", title="index")

@bp.route("/puzzle/<int:puzzle_id>")
def puzzle(puzzle_id):
    db = get_db()
    puzzle = cursor = db.execute("select * from puzzle where id = ? ", (puzzle_id,)).fetchone()
    #passing date type to template
    parsed_date = datetime.strptime(puzzle['date'], '%Y-%m-%d')
    return render_template("puzzle.html", title="puzzle", puzzle=puzzle, date=parsed_date)

