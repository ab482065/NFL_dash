import sqlite3
from sqlite3 import Error

def create_connection_and_table():
    conn = None;
    try:
        conn = sqlite3.connect('user_data.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users
                          (username TEXT PRIMARY KEY,
                           email TEXT NOT NULL,
                           password TEXT NOT NULL);''')
        conn.commit()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

