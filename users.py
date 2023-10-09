# import sqlite3
# from sqlite3 import Error
from connection import DB

def create_connection_and_table():
    conn = None;
    try:
        
        conn =  DB() # get the database
        conn.connect() # connect to database
        # cursor = conn.cursor() # get the cursor
        conn.cursor.execute('''CREATE TABLE IF NOT EXISTS users2
                          (username TEXT PRIMARY KEY,
                           email TEXT NOT NULL,
                           password TEXT NOT NULL);''')
        # conn.commit()
    except Exception as e:
        print(e)
    finally:
        if conn:
            conn.close()
# def create_connection_and_table():
#     conn = None;
#     try:
#         conn = sqlite3.connect('user_data.db')
#         cursor = conn.cursor()
#         cursor.execute('''CREATE TABLE IF NOT EXISTS users
#                           (username TEXT PRIMARY KEY,
#                            email TEXT NOT NULL,
#                            password TEXT NOT NULL);''')
#         conn.commit()
#     except Error as e:
#         print(e)
#     finally:
#         if conn:
#             conn.close()

# Example usage:
if __name__ == "__main__":
    create_connection_and_table()