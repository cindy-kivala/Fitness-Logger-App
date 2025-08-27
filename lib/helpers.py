from sqlalchemy.orm import sessionmaker
from lib.db.models import Base, User, Exercise, WorkoutSession, WorkoutSessionExercise
from lib.db import SessionLocal, engine
from datetime import datetime
from lib.db.setup import CONN, CURSOR
from lib.db.sessions import get_session


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

# USER HELPERS 
def list_users():
    session = SessionLocal()
    users = User.all(session)
    for u in users:
        print(f"ID: {u.id}, Name: {u.name}, Age: {u.age}, Weight: {u.weight}")
    session.close()

def handle_add_user():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    weight = float(input("Enter weight: "))
    session = SessionLocal()
    user = User.create(session, name, age, weight)
    print(f"User created: {user.name}, ID: {user.id}")
    session.close()

def handle_update_user():
    session = SessionLocal()
    list_users()
    user_id = int(input("Enter user ID to update: "))
    name = input("New name (leave blank to skip): ").strip()
    age_input = input("New age (leave blank to skip): ").strip()
    weight_input = input("New weight (leave blank to skip): ").strip()
    age = int(age_input) if age_input else None
    weight = float(weight_input) if weight_input else None
    session_user = session.query(User).filter_by(id=user_id).first()
    if not session_user:
        print("User not found!")
    else:
        if name: session_user.name = name
        if age: session_user.age = age
        if weight: session_user.weight = weight
        session.commit()
        print(f"Updated user {session_user.id}: {session_user.name}, {session_user.age}, {session_user.weight}")
    session.close()

def handle_delete_user():
    session = SessionLocal()
    list_users()
    user_id = int(input("Enter user ID to delete: "))
    session_user = session.query(User).filter_by(id=user_id).first()
    if not session_user:
        print("User not found!")
    else:
        sessions = session.query(WorkoutSession).filter_by(user_id=user_id).all()
        for s in sessions:
            session.delete(s)
        session.delete(session_user)
        session.commit()
        print(f"Deleted user {session_user.id}: {session_user.name}")
    session.close()

# EXERCISE HELPERS
def list_exercises():
    session = SessionLocal()
    exercises = Exercise.all(session)
    for e in exercises:
        print(f"ID: {e.id}, Name: {e.name}, Muscle: {e.muscle_group}, Equipment: {e.equipment}, Description: {e.description}")
    session.close()

def handle_add_exercise():
    name = input("Enter exercise name: ")
    muscle_group = input("Enter muscle group: ")
    equipment = input("Enter equipment: ")
    description = input("Enter brief description: ")
    session = SessionLocal()
    exercise = Exercise.create(session, name, description, muscle_group, equipment)
    print(f"Exercise created: {exercise.name}, ID: {exercise.id}")
    session.close()

def handle_update_exercise():
    session = SessionLocal()
    list_exercises()
    exercise_id = int(input("Enter exercise ID to update: "))
    name = input("New name (leave blank to skip): ").strip()
    muscle_group = input("New muscle group (leave blank to skip): ").strip()
    equipment = input("New equipment (leave blank to skip): ").strip()
    description = input("New description (leave blank to skip): ").strip()
    exercise = session.query(Exercise).filter_by(id=exercise_id).first()
    if not exercise:
        print("Exercise not found!")
    else:
        if name: exercise.name = name
        if muscle_group: exercise.muscle_group = muscle_group
        if equipment: exercise.equipment = equipment
        if description: exercise.description = description
        session.commit()
        print(f"Updated exercise {exercise.id}: {exercise.name}")
    session.close()

def handle_delete_exercise():
    session = SessionLocal()
    list_exercises()
    exercise_id = int(input("Enter exercise ID to delete: "))
    exercise = session.query(Exercise).filter_by(id=exercise_id).first()
    if not exercise:
        print("Exercise not found!")
    else:
        session.delete(exercise)
        session.commit()
        print(f"Deleted exercise {exercise.id}: {exercise.name}")
    session.close()

# WORKOUT HELPERS 
def list_workouts():
    session = SessionLocal()
    workouts = WorkoutSession.all(session)
    for w in workouts:
        print(f"ID: {w.id}, User ID: {w.user_id}, Activity: {w.activity}, Duration: {w.duration} min, Calories: {w.calories}, Date: {w.date}")
    session.close()

def handle_add_workout():
    list_users()
    user_id = int(input("Enter user ID for session: "))
    activity = input("Enter activity: ")
    duration = int(input("Enter duration (minutes): "))
    calories = int(input("Enter calories burned: "))
    date_input = input("Enter date (YYYY-MM-DD) [leave blank for today]: ").strip()
    date_obj = datetime.today() if not date_input else datetime.strptime(date_input, "%Y-%m-%d")
    session = SessionLocal()
    workout = WorkoutSession.create(session, user_id, activity, duration, calories, date_obj)
    print(f"Workout session added with ID: {workout.id}")
    # Prompt to add exercises
    while True:
        add_more = input("Add an exercise to this session? (y/n): ").lower()
        if add_more == 'y':
            handle_add_exercise_to_session(workout.id)
        else:
            break
    session.close()

def handle_update_workout():
    session = SessionLocal()
    list_workouts()
    session_id = int(input("Enter workout session ID to update: "))
    activity = input("New activity (leave blank to skip): ").strip()
    duration_input = input("New duration (leave blank to skip): ").strip()
    calories_input = input("New calories (leave blank to skip): ").strip()
    date_input = input("New date YYYY-MM-DD (leave blank to skip): ").strip()
    duration = int(duration_input) if duration_input else None
    calories = int(calories_input) if calories_input else None
    date = datetime.strptime(date_input, "%Y-%m-%d") if date_input else None
    workout = session.query(WorkoutSession).filter_by(id=session_id).first()
    if not workout:
        print("Workout session not found!")
    else:
        if activity: workout.activity = activity
        if duration: workout.duration = duration
        if calories: workout.calories = calories
        if date: workout.date = date
        session.commit()
        print(f"Updated workout session {workout.id}")
    session.close()

def handle_delete_workout():
    session = SessionLocal()
    list_workouts()
    session_id = int(input("Enter workout session ID to delete: "))
    workout = session.query(WorkoutSession).filter_by(id=session_id).first()
    if not workout:
        print("Workout session not found!")
    else:
        session.delete(workout)
        session.commit()
        print(f"Deleted workout session {workout.id}")
    session.close()

# WORKOUT SESSION EXERCISE HELPERS
def list_session_exercises():
    session = SessionLocal()
    wses = session.query(WorkoutSessionExercise).all()
    for wse in wses:
        print(f"ID: {wse.id}, Session ID: {wse.session_id}, Exercise ID: {wse.exercise_id}, Sets: {wse.sets}, Reps: {wse.reps}, Weight: {wse.weight}")
    session.close()

def handle_add_exercise_to_session(session_id=None):    
    """
    If session_id is passed, use it. Otherwise, ask user for it.
    """
    if session_id is None:
        session_id = int(input("Enter workout session ID: "))

    list_exercises()  # show all exercises
    exercise_id = int(input("Enter exercise ID: "))
    sets = int(input("Sets: "))
    reps = int(input("Reps: "))
    weight = float(input("Weight: "))

    session = get_session()
    wse = WorkoutSessionExercise.add_to_session(
        session, 
        session_id, 
        exercise_id, 
        sets, 
        reps, 
        weight
    )
    print(f"Added to session: {wse}")
    session.close()


def handle_update_session_exercise():
    session = SessionLocal()
    list_session_exercises()
    wse_id = int(input("Enter session exercise ID to update: "))
    sets_input = input("New sets (leave blank to skip): ").strip()
    reps_input = input("New reps (leave blank to skip): ").strip()
    weight_input = input("New weight (leave blank to skip): ").strip()
    sets = int(sets_input) if sets_input else None
    reps = int(reps_input) if reps_input else None
    weight = float(weight_input) if weight_input else None
    wse = session.query(WorkoutSessionExercise).filter_by(id=wse_id).first()
    if not wse:
        print("WorkoutSessionExercise not found!")
    else:
        if sets: wse.sets = sets
        if reps: wse.reps = reps
        if weight: wse.weight = weight
        session.commit()
        print(f"Updated workout session exercise {wse.id}")
    session.close()

def handle_delete_session_exercise():
    session = SessionLocal()
    list_session_exercises()
    wse_id = int(input("Enter session exercise ID to delete: "))
    wse = session.query(WorkoutSessionExercise).filter_by(id=wse_id).first()
    if not wse:
        print("WorkoutSessionExercise not found!")
    else:
        session.delete(wse)
        session.commit()
        print(f"Deleted workout session exercise {wse.id}")
    session.close()


