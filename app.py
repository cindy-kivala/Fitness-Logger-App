from lib.db.models import User, Exercise, WorkoutSession
import sys

def main_menu():
    print("\n=== FITNESS LOGGER ===")
    print("1. Add User")
    print("2. View Users")
    print("3. Add Exercise")
    print("4. View Exercises")
    print("5. Add Workout Session")
    print("6. View Workout Sessions")
    print("7. Exit")
    choice = input("Choose an option: ")
    return choice

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

def view_workouts():
    sessions = WorkoutSession.all()
    for s in sessions:
        print(f"ID: {s.id}, User ID: {s.user_id}, Activity: {s.activity}, Duration: {s.duration} min, Calories: {s.calories}, Date: {s.date}")

def run():
    while True:
        choice = main_menu()
        if choice == "1":
            add_user()
        elif choice == "2":
            view_users()
        elif choice == "3":
            add_exercise()
        elif choice == "4":
            view_exercises()
        elif choice == "5":
            add_workout()
        elif choice == "6":
            view_workouts()
        elif choice == "7":
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    run()