
#our database initialization script
# 
from lib import CONN, CURSOR

# Create tables
CURSOR.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)
""")

CURSOR.execute("""
CREATE TABLE IF NOT EXISTS exercises (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    muscle_group TEXT NOT NULL
)
""")

CURSOR.execute("""
CREATE TABLE IF NOT EXISTS workout_sessions (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    date TEXT NOT NULL,
    duration INTEGER NOT NULL,
    activity TEXT NOT NULL,
    calories INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
)
""")

CURSOR.execute("""
CREATE TABLE IF NOT EXISTS session_exercises (
    id INTEGER PRIMARY KEY,
    session_id INTEGER,
    exercise_id INTEGER,
    sets INTEGER,
    reps INTEGER,
    weight REAL,
    FOREIGN KEY (session_id) REFERENCES workout_sessions(id),
    FOREIGN KEY (exercise_id) REFERENCES exercises(id)
)
""")

CONN.commit()
print("All tables created successfully!")
