from sqlalchemy.orm import Session
from lib.db.models import User, Exercise, WorkoutSession, WorkoutSessionExercise
from lib.db import SessionLocal
from datetime import datetime
from lib.db.setup import CONN, CURSOR

Base.metadata.create_all(engine)
session = Session(engine)

def list_users():
    users = User.all(session)
    for u in users:
        print(u)

def add_user():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    weight = float(input("Enter weight: "))

    session = SessionLocal()
    user = User.create(session, name, age, weight)
    session.close()
    print(f"User created: {user.name}, ID: {user.id}")

def update_user():
    list_users()
    user_id = int(input("Enter user ID to update: "))
    name = input("New name (leave blank to skip): ").strip()
    age = input("New age (leave blank to skip): ").strip()
    weight = input("New weight (leave blank to skip): ").strip()
    update_user(session, user_id, 
                name=name or None, 
                age=int(age) if age else None, 
                weight=float(weight) if weight else None)
    
def delete_user():
    list_users()
    user_id = int(input("Enter user ID to delete: "))
    delete_user(session, user_id)

def view_users():
    session = SessionLocal()
    users = session.query(User).all()
    for u in users:
        print(f"ID: {u.id}, Name: {u.name}, Age: {u.age}, Weight: {u.weight}")
    session.close()

#EXERCISES

def add_exercise():
    name = input("Enter exercise name: ")
    muscle = input("Enter muscle group: ")
    equipment = input("Enter equipment: ")
    description = input("Enter brief description: ")

    session = SessionLocal()
    exercise = Exercise.create(session, name, muscle, equipment, description)
    session.close()
    print(f"Exercise created: {exercise.name}, ID: {exercise.id}")
    session.close()

def view_exercises():
    session = SessionLocal()
    #exercises = session.query(Exercise).all()
    for e in Exercise.all(session):
        print(f"ID: {e.id}, Name: {e.name}, Muscle: {e.muscle_group}, Equipment: {e.equipment},Description: {e.description}")
    session.close()

def add_workout():
    # List all users
    CURSOR.execute("SELECT id, name, age, weight FROM users")
    users = CURSOR.fetchall()
    for u in users:
        print(f"ID: {u[0]}, Name: {u[1]}, Age: {u[2]}, Weight: {u[3]}")

    # Get user input
    user_id = int(input("Enter user ID for session: "))
    activity = input("Enter activity: ")
    duration = int(input("Enter duration (minutes): "))
    calories = int(input("Enter calories burned: "))
    
    date_input = input("Enter date (YYYY-MM-DD) [leave blank for today]: ")
    if date_input.strip() == "":
        date_obj = datetime.today()
    else:
        date_obj = datetime.strptime(date_input, "%Y-%m-%d")
    
    # Insert into workout_sessions
    CURSOR.execute(
        """
        INSERT INTO workout_sessions (user_id, date, duration, activity, calories)
        VALUES (?, ?, ?, ?, ?)
        """,
        (user_id, date_obj.strftime("%Y-%m-%d"), duration, activity, calories)
    )
    CONN.commit()
    print("Workout session added successfully!")

    # Get the ID of the session we just added
    session_id = CURSOR.lastrowid
    print(f"Yay!!Workout session added successfully with ID: {session_id}!")

    # Prompt to add exercises to this session
    while True:
        add_more = input("Would you like to add an exercise to this workout session? (y/n): ").lower()
        if add_more == 'y':
            add_exercise_to_session(session_id)  # Pass session_id to your function
        else:
            break

def view_workouts():
    session = SessionLocal()
    workouts = session.query(WorkoutSession).all()
    for w in workouts:
        print(f"ID: {w.id}, User ID: {w.user_id}, Activity: {w.activity}, Duration: {w.duration} min, "
              f"Calories: {w.calories}, Date: {w.date}")
    session.close()

def add_exercise_to_session(session_id):
   
    view_exercises()
    exercise_id = int(input("Enter exercise ID: "))
    sets = int(input("Sets: "))
    reps = int(input("Reps: "))
    weight = float(input("Weight: "))

    session = SessionLocal()
    wse = WorkoutSessionExercise.add_to_session(
        session, 
        session_id, 
        exercise_id, 
        sets, 
        reps, 
        weight)
    print(f"Added to session: {wse}")
    session.close()


    print("Yay!!Exercise added to session.")
