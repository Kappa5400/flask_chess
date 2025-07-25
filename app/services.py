
import requests
from datetime import datetime
from .models import Puzzle

def fetch_puzzle():
    try:
        raw = requests.get("https://lichess.org/api/puzzle/daily")
        if raw.status_code != 200:
            raise requests.RequestException(f"Bad status: {raw.status_code}")
        response = raw.json()
        game = response["game"]
        puzzle = response["puzzle"]

        puzzle_id = puzzle["id"]
        pgn = game["pgn"]
        answer = ",".join(puzzle["solution"])
        puzzle_rating = puzzle['rating']
        date = datetime.utcnow().isoformat()

        return Puzzle(puzzle_id, pgn, answer, puzzle_rating, date)


    except (requests.RequestException, KeyError)  as e:
        print(f"Error fetching puzzle: {e}")
        return None