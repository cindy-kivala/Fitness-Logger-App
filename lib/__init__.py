import sqlite3
from .db.database import CURSOR, CONN

CONN = sqlite3.connect('fitness.db')
CURSOR = CONN.cursor()