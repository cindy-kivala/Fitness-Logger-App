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
    
    @classmethod
    def all(cls):
        CURSOR.execute("SELECT * FROM users")
        rows = CURSOR.fetchall()
        return [cls(row[1], row[2], row[3], row[0]) for row in rows]
    
    #find by id
    @classmethod
    def find_by_id(cls, user_id):
        CURSOR.execute("SELECT * FROM user WHERE id=?", (user_id,))
        row = CURSOR.fetchone()
        if row:
            return cls(row[1], row[2], row[3], row[0])
        return None
    
    #update
    def update(self, name=None, age=None, weight=None):
        self.name = name if name is not None else self.name
        self.age = age if age is not None else self.age
        self.weight = weight if weight is not None else self.weight
        CURSOR.execute(
            "UPDATE users SET name = ?, age = ?, weight = ? WHERE id = ?",
            (self.name, self.age, self.weight, self.id)
        )
        CONN.commit()

    #delete
    def delete(self):
        CURSOR.execute("DELETE FROM users WHERE id = ?", (self.id,))
        CONN.commit()

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

    @classmethod
    def all(cls):
        CURSOR.execute("SELECT * FROM workoutsessions")
        rows = CURSOR.fetchall()
        return [cls(row[1], row[2], row[3], row[4], row[5], row[0]) for row in rows]
     
    #our "filter"
    @classmethod
    def find_by_id(cls, session_id):
        CURSOR.execute("SELECT * FROM workoutsessions WHERE id = ?", (session_id,))
        row = CURSOR.fetchone()
        if row:
            return cls(row[1], row[2], row[3], row[4], row[5], row[0])
        return None

    #update
    def update(self, activity=None, duration=None, calories=None, date=None):
        #comprehension
        self.activity = activity if activity is not None else self.activity
        self.duration = duration if duration is not None else self.duration
        self.calories = calories if calories is not None else self.calories
        self.date = date if date is not None else self.date
        CURSOR.execute(
            "UPDATE workoutsessions SET activity = ?, duration = ?, calories = ?, date = ? WHERE id = ?",
            (self.activity, self.duration, self.calories, self.date, self.id)
        )
        CONN.commit()

    def delete(self):
        CURSOR.execute("DELETE FROM workoutsessions WHERE id = ?", (self.id,))
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
    
    #basic crud
    @classmethod
    def all(cls):
        CURSOR.execute("SELECT * FROM exercises")
        rows = CURSOR.fetchall()
        return [cls(row[1], row[2], row[3], row[0]) for row in rows]

    @classmethod
    def find_by_id(cls, exercise_id):
        CURSOR.execute("SELECT * FROM exercises WHERE id = ?", (exercise_id,))
        row = CURSOR.fetchone()
        if row:
            return cls(row[1], row[2], row[3], row[0])
        return None

    def update(self, name=None, muscle_group=None, equipment=None):
        self.name = name if name is not None else self.name
        self.muscle_group = muscle_group if muscle_group is not None else self.muscle_group
        self.equipment = equipment if equipment is not None else self.equipment
        CURSOR.execute(
            "UPDATE exercises SET name = ?, muscle_group = ?, equipment = ? WHERE id = ?",
            (self.name, self.muscle_group, self.equipment, self.id)
        )
        CONN.commit()

    def delete(self):
        CURSOR.execute("DELETE FROM exercises WHERE id = ?", (self.id,))
        CONN.commit()
