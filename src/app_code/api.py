from flask import Blueprint, jsonify
from src.app_code.db import query_db
from .db import get_db

api_bp = Blueprint('api', __name__, url_prefix='/api' )

@api_bp.route("/puzzles")
def get_puzzle_all():
    rows = query_db("select * from puzzle")
    puzzles = [dict(row) for row in rows]
    return jsonify(puzzles)

@api_bp.route('/puzzle/<id>')
def get_puzzle(id):
    row = query_db("select * from puzzle where id = ?", [id], one=True )
    if row:
        return jsonify(dict(row))
    else:
        return jsonify({"error": "Puzzle not found"}), 404

@api_bp.route('/puzzle/<int:offset>')
def puzzle_offset(offset):
    offset = int(offset)
    if offset >= 10 or offset < 0:
        return jsonify({"Error": "Offset our of range"}), 404

    db = get_db()
    puzzle = db.execute(
        "SELECT * FROM puzzle ORDER BY date ASC LIMIT 1 OFFSET ?",
        (offset,)
    ).fetchone()

    if puzzle is None:
        return jsonify({"Error": "No puzzle found"}), 404

    return jsonify(dict(puzzle))