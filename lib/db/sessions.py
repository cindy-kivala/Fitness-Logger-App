import sqlite3

DB_NAME = "fitness.db"

def get_connection():
     """Return a database connection."""
     return sqlite3.connect(DB_NAME)

from sqlalchemy.orm import sessionmaker
from lib.db import engine

Session = sessionmaker(bind=engine)

def get_session():
    return Session()

# CREATE
def add_exercise_to_session(session_id, exercise_id, reps=None, sets=None, weight=None):
    """Insert an exercise into a workout session."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO session_exercises (session_id, exercise_id, reps, sets, weight)
        VALUES (?, ?, ?, ?, ?)
    """, (session_id, exercise_id, reps, sets, weight))

    conn.commit()
    conn.close()
    print("Exercise added to session successfully.")

# READ 
def view_session_exercises(session_id):
    """Fetch exercises for a given session."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT e.name, se.reps, se.sets, se.weight
        FROM session_exercises se
        JOIN exercises e ON e.id = se.exercise_id
        WHERE se.session_id = ?
    """, (session_id,))
    
    results = cursor.fetchall()
    conn.close()
    return results

# UPDATE 
def update_session_exercise(session_exercise_id, reps=None, sets=None, weight=None):
    """Update exercise details in a session."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE session_exercises
        SET reps = ?, sets = ?, weight = ?
        WHERE id = ?
    """, (reps, sets, weight, session_exercise_id))

    conn.commit()
    conn.close()
    print("Session exercise updated.")

# DELETE
def delete_session_exercise(session_exercise_id):
    """Remove exercise from a session."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM session_exercises WHERE id = ?", (session_exercise_id,))

    conn.commit()
    conn.close()
    print("Session exercise deleted.")