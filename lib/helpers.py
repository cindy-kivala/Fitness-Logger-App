from lib.db.models import User, Exercise, WorkoutSession, WorkoutSessionExercise
from lib.db import SessionLocal
from datetime import datetime
from lib.db.setup import CONN, CURSOR

def add_user():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    weight = float(input("Enter weight: "))

    session = SessionLocal()
    user = User.create(session, name, age, weight)
    session.close()
    print(f"User created: {user.name}, ID: {user.id}")

def view_users():
    session = SessionLocal()
    users = session.query(User).all()
    for u in users:
        print(f"ID: {u.id}, Name: {u.name}, Age: {u.age}, Weight: {u.weight}")
    session.close()

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

# def add_workout():
#     view_users()
#     user_id = int(input("Enter user ID for session: "))
#     activity = input("Enter activity: ")
#     duration = int(input("Enter duration (minutes): "))
#     calories = int(input("Enter calories burned: "))
#     date = input("Enter date (YYYY-MM-DD): ")

#      # Prompt for date, default to None to use DB's CURRENT_TIMESTAMP
#     date_input = input("Enter date (YYYY-MM-DD) [leave blank for today]: ").strip()
    
#     if date_input:
#     # Convert string to datetime object
#        date_obj = datetime.strptime(date_input, "%Y-%m-%d")
#     else:
#     # Use None to let DB default to CURRENT_TIMESTAMP
#        date_obj = None

#     session = SessionLocal()
#     workout = WorkoutSession.create(session, user_id, activity, duration, calories, date_obj)
#     print(f"Workout session created with ID: {session.id}")

# #attempt 1 prompt
#     while True:
#         add_more = input("Would you like to add an exercise to this workout session? (y/n): ").lower()
#         if add_more == 'y':
#             add_exercise_to_session(workout.id)  # pass session.id directly
#         else:
#             break

#     session.close()
#     #print(f"Workout session created with ID: {workout.id}")


def view_workouts():
    session = SessionLocal()
    workouts = session.query(WorkoutSession).all()
    for w in workouts:
        print(f"ID: {w.id}, User ID: {w.user_id}, Activity: {w.activity}, Duration: {w.duration} min, "
              f"Calories: {w.calories}, Date: {w.date}")
    session.close()

def add_exercise_to_session(session_id):
    # close_session = False
    # if not session:
    #     session = SessionLocal()
    #     close_session = True

    # if not session_id:
    #    view_workouts()
    #    session_id = int(input("Enter workout session ID: "))

    # workout = session.query(WorkoutSession).filter_by(id=session_id).first()
    # if not workout:
    #     print("Session not found.")
    #     if close_session:
    #         session.close()
    #     return
    
    view_exercises()
    exercise_id = int(input("Enter exercise ID: "))
    sets = int(input("Sets: "))
    reps = int(input("Reps: "))
    weight = float(input("Weight: "))

    session = SessionLocal()
    wse = WorkoutSessionExercise.add_to_session(session, session_id, exercise_id, sets, reps, weight)
    print(f"Added to session: {wse}")
    session.close()

    #  # Create WorkoutSessionExercise entry
    # wse = WorkoutSessionExercise(session_id=workout.id, exercise_id=exercise_id)

    # if hasattr(wse, 'sets'):
    #     wse.sets = sets
    # if hasattr(wse, 'reps'):
    #     wse.reps = reps
    # if hasattr(wse, 'weight'):
    #     wse.weight = weight

    # session.add(wse)
    # session.commit()
    
    #session.add_exercise(exercise_id, sets, reps, weight)
    print("Yay!!Exercise added to session.")
