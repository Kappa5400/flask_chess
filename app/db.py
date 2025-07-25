import sqlite3
from flask import g, current_app

#db boilerplate
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(current_app.config['DATABASE'])
        g.db.row_factory = sqlite3.Row  # allows dict-like row access
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def init_db():
    db = get_db()
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf-8'))

def save_puzzle_db(puzzle):
    db = get_db()
    db.execute(
        """
         INSERT INTO puzzle (puzzle_id, pgn, answer, puzzle_rating, date)
        VALUES (?, ?, ?, ?, ?)
        """,
        (puzzle.puzzle_id, puzzle.pgn, puzzle.answer, puzzle.puzzle_rating, puzzle.date)
    )
    db.commit()

def delete_puzzle_id_11():
    result = query_db("SELECT 1 FROM puzzle WHERE id = 11", one=True)
    if result == None:
        print("There are only 10 puzzles in database.")
        return 0
    db = get_db()
    db.execute(
        """
        DELETE FROM puzzle WHERE id = 11 
        """
    )
    db.commit()
    print("11th puzzle dropped from db")
    return 1

def init_app(app):
    app.teardown_appcontext(close_db)