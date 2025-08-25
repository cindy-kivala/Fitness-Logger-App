from .. import CURSOR, CONN #go up one level
# from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship

class User:
    def __init__(self,name,age=None, weight=None, id=None):
        self.id = id
        self.name = name
        self.age = age
        self.weight = weight
    
    @classmethod
    def create_table(cls):
        CURSOR.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER,
                weight REAL
            )
        ''')
        CONN.commit()
    
    @classmethod
    def create(cls, name, age=None, weight=None):
        sql = """
            INSERT INTO users (name, age, weight)
            VALUES (?, ?, ?)
        """
        CURSOR.execute("INSERT INTO users (name, age, weight) VALUES (?, ?, ?)", (name,age, weight))
        CONN.commit()
        return cls(name, age, weight, CURSOR.lastrowid)

class WorkoutSession:
    def __init__(self, user_id, activity, duration, calories, date, id=None):
        self.id = id
        self.user_id = user_id
        self.activity = activity
        self.duration = duration
        self.calories = calories
        self.date = date
    
    @classmethod
    def create_table(cls):
        CURSOR.execute('''
            CREATE TABLE IF NOT EXISTS workoutsessions (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                activity TEXT,
                duration INTEGER,
                calories INTEGER,
                date TEXT,
                FOREIGN KEY(user_id) REFERENCES users(id)
            )
        ''')
        CONN.commit()
    
    @classmethod
    def create(cls, user_id, activity, duration, calories, date):
        CURSOR.execute("INSERT INTO workoutsessions(user_id, activity, duration, calories, date) VALUES (?, ?, ?, ?, ?)", 
                       (user_id, activity, duration, calories, date))
        CONN.commit()
        return cls(user_id, activity, duration,calories,date, CURSOR.lastrowid)
    
    #add exercise method
    def add_exercise(self, exercise_id, sets, reps, weight):
        """
        Links an exercise to this workout session with sets, reps, and weight.
        """
        CURSOR.execute("""
            INSERT INTO session_exercises (session_id, exercise_id, sets, reps, weight)
            VALUES (?, ?, ?, ?, ?)
        """, (self.id, exercise_id, sets, reps, weight))
        CONN.commit()
    
#CONFRIRM IF WILL KEEP THIS CLASS OR JUST RETAIN CLASS GOAL
class Exercise:
    def __init__(self, name, muscle_group, equipment, id=None):
        self.id = id
        self.name = name
        self.muscle_group = muscle_group
        self.equipment = equipment
    
    @classmethod
    def create_table(cls):
        CURSOR.execute('''
            CREATE TABLE IF NOT EXISTS exercises (
                id INTEGER PRIMARY KEY,
                name TEXT,
                muscle_group TEXT,
                equipment TEXT
            )
        ''')
        CONN.commit()
    
    @classmethod
    def create(cls, name, muscle_group, equipment):
        CURSOR.execute("INSERT INTO exercises (name, muscle_group, equipment) VALUES (?, ?, ?)", 
                       (name, muscle_group, equipment))
        CONN.commit()
        return cls(name, muscle_group, equipment, CURSOR.lastrowid)
