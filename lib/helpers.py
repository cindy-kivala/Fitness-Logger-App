from lib.db.models import User, Exercise, WorkoutSession

def add_user():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    weight = float(input("Enter weight: "))
    user = User.create(name, age, weight)
    print(f"User created: {user.name}, ID: {user.id}")

def view_users():
    users = User.all()
    for u in users:
        print(f"ID: {u.id}, Name: {u.name}, Age: {u.age}, Weight: {u.weight}")


def add_exercise():
    name = input("Enter exercise name: ")
    muscle = input("Enter muscle group: ")
    equipment = input("Enter equipment: ")
    exercise = Exercise.create(name, muscle, equipment)
    print(f"Exercise created: {exercise.name}, ID: {exercise.id}")

def view_exercises():
    exercises = Exercise.all()
    for e in exercises:
        print(f"ID: {e.id}, Name: {e.name}, Muscle: {e.muscle_group}, Equipment: {e.equipment}")

def add_workout():
    view_users()
    user_id = int(input("Enter user ID for session: "))
    activity = input("Enter activity: ")
    duration = int(input("Enter duration (minutes): "))
    calories = int(input("Enter calories burned: "))
    date = input("Enter date (YYYY-MM-DD): ")
    session = WorkoutSession.create(user_id, activity, duration, calories, date)
    print(f"Workout session created with ID: {session.id}")

#attempt 1 prompt
    while True:
        add_more = input("Would you like to add an exercise to this workout session? (y/n): ").lower()
        if add_more == 'y':
            add_exercise_to_session(session.id)  # pass session.id directly
        else:
            break

def view_workouts():
    sessions = WorkoutSession.all()
    for s in sessions:
        print(f"ID: {s.id}, User ID: {s.user_id}, Activity: {s.activity}, Duration: {s.duration} min, Calories: {s.calories}, Date: {s.date}")

def add_exercise_to_session(session_id=None):
    if not session_id:
       view_workouts()
       session_id = int(input("Enter workout session ID: "))
    session = WorkoutSession.find_by_id(session_id)
    if not session:
        print("Session not found.")
        return
    
    view_exercises()
    exercise_id = int(input("Enter exercise ID: "))
    sets = int(input("Sets: "))
    reps = int(input("Reps: "))
    weight = float(input("Weight: "))
    
    session.add_exercise(exercise_id, sets, reps, weight)
    print("Yay!!Exercise added to session.")
