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

@bp.route("/daily")
def daily_puzzle():
    db = get_db()
    puzzle = db.execute("select * from puzzle order by date desc limit 1 ").fetchone()
    #passing date type to template
    parsed_date = datetime.strptime(puzzle['date'], '%Y-%m-%d')
    return render_template("puzzle.html", title="Daily Puzzle",
                           puzzle=puzzle, date=parsed_date)

@bp.route('/puzzle/<int:offset>')
def puzzle_offset(offset):
    offset = int(offset)
    if offset >= 10 or offset < 0:
        return jsonify({"Error": "Offset our of range"}), 404

    db = get_db()
    puzzle = db.execute(
        "SELECT * FROM puzzle ORDER BY date ASC LIMIT 1 OFFSET ?",
        (offset,)
    ).fetchone()
    date = datetime.strptime(puzzle['date'],'%Y-%m-%d')

    if puzzle is None:
        return jsonify({"Error": "No puzzle found"}), 404

    return render_template("puzzle.html", title="puzzle", puzzle=puzzle, date=date)

@bp.route("/about")
def about():
    return render_template("about.html", title="about")