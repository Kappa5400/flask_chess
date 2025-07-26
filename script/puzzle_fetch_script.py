from logging import exception

from app import create_app
from app.models import Puzzle
from app.db import query_db, save_puzzle_db, delete_puzzle_id_11
from app.services import fetch_puzzle
import sys

app = create_app()
with app.app_context():
    try:
        new_puzzle = fetch_puzzle()
        if new_puzzle is None:
            raise ValueError("fetch_puzzle() returned None")

        result = query_db("SELECT 1 FROM puzzle WHERE puzzle_id = ?", [new_puzzle.puzzle_id], one=True)

        if result is None:
            save_puzzle_db(new_puzzle)
            print("Inserted puzzle into DB.")
            try:
                delete_puzzle_id_11()
                sys.exit(0)
            except Exception as e:
                print(f"Error deleting 11th puzzle, {e}")
                sys.exit(4)

        else:
            print("Puzzle already exists, duplicate.")
            sys.exit(3)

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(2)
