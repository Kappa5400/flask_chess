CREATE TABLE IF NOT EXISTS puzzle(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    puzzle_id TEXT UNIQUE NOT NULL,
    pgn TEXT NOT NULL,
    answer TEXT NOT NULL,
    puzzle_rating INTEGER,
    date DATE
);