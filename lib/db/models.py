from __init__ import CURSOR, CONN
# from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship

class User:
    def __init__(self,name, id=None):
        self.id = id
        self.name = name
    
    @classmethod
    def create_table(cls):
        CURSOR.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT
            )
        ''')
        CONN.commit()
    
    @classmethod
    def create(cls, name):
        CURSOR.execute("INSERT INTO users (name) VALUES (?)", (name,))
        CONN.commit()
        return cls(name, CURSOR.lastrowid)

class WorkoutSesssion:
    def __init__(self, user_id, activity, duration, calories, id=None):
        self.id = id
        self.user_id = user_id
        self.activity = activity
        self.duration = duration
        self.calories = calories
    
    @classmethod
    def create_table(cls):
        CURSOR.execute('''
            CREATE TABLE IF NOT EXISTS workout_sessions (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                activity TEXT,
                duration INTEGER,
                calories INTEGER,
                FOREIGN KEY(user_id) REFERENCES users(id)
            )
        ''')
        CONN.commit()
    
    @classmethod
    def create(cls, user_id, activity, duration, calories):
        CURSOR.execute("INSERT INTO workout_sessions(user_id, activity, duration, calories) VALUES (?, ?, ?, ?))", 
                       (user_id, activity, duration, calories))
        CONN.commit()
        return cls(user_id, activity, duration,calories, CURSOR.lastrowid)