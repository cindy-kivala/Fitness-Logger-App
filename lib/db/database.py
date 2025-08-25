import sqlite3

CONN = sqlite3.connect('fitness.db')
CURSOR = CONN.cursor()