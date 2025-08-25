from lib.db.models import User, Exercise, WorkoutSession
from lib.db.database import CONN, CURSOR
#AVOID MODULE CONFLICT
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))


def seed_data():
    #drop tables if they exist BUT CURRENTLY THEY DONT
    
    #recreate tables
    User.create_table()
    Exercise.create_table()
    WorkoutSession.create_table()
    #Goal.create_table()

    #seed users
    pepper = User.create("Pepper", age=24, weight=65)
    nicky = User.create("Nicky", age=22, weight=55)
    #for more data, try faker library

    #seed exercises
    squat = Exercise.create("Squat", "Legs", "Bodyweight")
    plank = Exercise.create("Plank", "Core", "Bodyweight")  
    deadlift = Exercise.create("Deadlift", "Back", "Barbell")
    bench_press = Exercise.create("Bench Press", "Chest", "Barbell")
    #Which of these is the better way?
    # squat = Exercise.create("Squat","legs", sets=3, reps=15, calories_burned=50)
    # plank = Exercise.create("Plank", "core",sets=3, reps=15, calories_burned=50)
    # pushup = Exercise.create("Push-up","core",sets=3, reps=15, calories_burned=50)
    #add more exercises
    #I FEEL LIKE THERE SHOULD BE A WAY TO DEFINE THESE NUMBERS: KGS, GRAMS AND MINUTES

    # seed workout sessions
    session1 = WorkoutSession.create(user_id=pepper.id, date="2025-08-25", duration=45, activity="Strength Training", calories=300)
    session2 = WorkoutSession.create(user_id=nicky.id, date="2025-08-26", duration=30, activity="Strength Training", calories=500)

    # link exercises to sessions (if many-to-many)
    session1.add_exercise(squat.id, sets=3, reps=15, weight=0)
    session2.add_exercise(deadlift.id, sets=4, reps=12, weight=60)
    session1.add_exercise(bench_press, sets=2, reps=5, weight=0)

if __name__ == "__main__":
    seed_data()

