import sys
from lib.db.models import User, Exercise, WorkoutSession, WorkoutSessionExercise
from lib.helpers import (
    handle_add_user, list_users, handle_update_user, handle_delete_user,
    handle_add_exercise, list_exercises, handle_update_exercise, handle_delete_exercise,
    handle_add_workout, list_workouts, handle_update_workout, handle_delete_workout,
    handle_add_exercise_to_session, list_session_exercises,
    handle_update_session_exercise, handle_delete_session_exercise
)


def main_menu():
    print("\n=== FITNESS LOGGER ===")
    print("1. Add User")
    print("2. View Users")
    print("3. Update User")
    print("4. Delete User")
    print("5. Add Exercise")
    print("6. View Exercises")
    print("7. Update Exercise")
    print("8. Delete Exercise")
    print("9. Add Workout Session")
    print("10. View Workout Sessions")
    print("11. Update Workout")
    print("12. Delete Workout")
    print("13. Add Exercise to Session")
    print("14. View Session Exercise")
    print("15. Update Session Exercise")
    print("16. Delete Session Exercise")
    print("17. Exit")
    choice = input("Choose an option: ")
    return choice


def run():
    while True:
        choice = main_menu()
        if choice == "1":
            handle_add_user()
        elif choice == "2":
            list_users()
        elif choice == "3":
            handle_update_user()
        elif choice == "4":
            handle_delete_user()
        elif choice == "5":
            handle_add_exercise()
        elif choice == "6":
            list_exercises()
        elif choice == "7":
            handle_update_exercise()
        elif choice == "8":
            handle_delete_exercise()
        elif choice == "9":
            handle_add_workout()
        elif choice == "10":
            list_workouts()
        elif choice == "11":
            handle_update_workout()
        elif choice == "12":
            handle_delete_workout()
        elif choice == "13":
            handle_add_exercise_to_session()
        elif choice == "14":
            list_session_exercises()
        elif choice == "15":
            handle_update_session_exercise()
        elif choice == "16":
            handle_delete_session_exercise()
        
        elif choice == "17":
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    run()