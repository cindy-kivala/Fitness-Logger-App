#from lib.db.models import User, Exercise, WorkoutSession
import sys
from lib.helpers import User, Exercise, WorkoutSession, WorkoutSessionExercise
from lib.helpers import add_user, view_users, view_exercises, view_workouts, add_exercise, add_workout

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