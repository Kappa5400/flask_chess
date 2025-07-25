from flask import Blueprint, jsonify
from app.db import query_db
from app.models import Puzzle


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
