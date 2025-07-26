from flask import Blueprint, g, current_app, jsonify, render_template
from .db import get_db
from .services import fetch_puzzle



bp = Blueprint('main', __name__)

# views
@bp.route("/")
def index():
    return render_template("index.html", title="index")

@bp.route("/puzzle")
def puzzle():
    return render_template("puzzle.html", title="puzzle")

