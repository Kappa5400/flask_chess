from app.db import get_db


#puzzle model

class Puzzle():
    def __init__(self, puzzle_id, pgn, answer, puzzle_rating, date):
        self.puzzle_id = puzzle_id
        self.pgn = pgn
        self.answer = answer
        self.puzzle_rating = puzzle_rating
        self.date = date


