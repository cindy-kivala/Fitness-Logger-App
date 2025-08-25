
#our database initialization script
# 
import sqlite3
#from lib import CONN, CURSOR

CONN = sqlite3.connect('fitness.db')
CURSOR = CONN.cursor()

def create_tables():
# Create tables

    # Users table
    CURSOR.execute("""
       CREATE TABLE IF NOT EXISTS users (
          id INTEGER PRIMARY KEY,
          name TEXT NOT NULL,
          age INTEGER,
          weight REAL
        )
    """)

    # Exercises table
    CURSOR.execute("""
       CREATE TABLE IF NOT EXISTS exercises (
           id INTEGER PRIMARY KEY,
           name TEXT NOT NULL,
           muscle_group TEXT NOT NULL,
           equipment TEXT NOT NULL
        )
    """)

    # Workout Sessions table
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
    # Session Exercises table (many-to-many relationship)
    CURSOR.execute("""
       CREATE TABLE IF NOT EXISTS session_exercises (
           id INTEGER PRIMARY KEY,
           name TEXT NOT NULL,
           session_id INTEGER,
           exercise_id INTEGER,
           sets INTEGER,
           reps INTEGER,
           weight REAL,
           FOREIGN KEY (session_id) REFERENCES workout_sessions(id),
           FOREIGN KEY (exercise_id) REFERENCES exercises(id)
        )
    """)
    
    CONN.commit

# Drop tables if they exist
def drop_tables():
    CURSOR.execute("DROP TABLE IF EXISTS session_exercises")
    CURSOR.execute("DROP TABLE IF EXISTS workout_sessions")
    CURSOR.execute("DROP TABLE IF EXISTS exercises")
    CURSOR.execute("DROP TABLE IF EXISTS users")
    CONN.commit()

if __name__ == "__main__":
    drop_tables()
    create_tables()
    print("All tables created successfully!")
