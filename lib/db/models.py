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