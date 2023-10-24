from dotenv import load_dotenv
from urllib.parse import urlparse
import psycopg2
import os

# Load environment variables from .env file
load_dotenv()

class DB:
    def __init__(self, db_url = os.environ['DATABASE_URL']):
        print({'db_url': db_url})
        self.db_url = db_url
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(self.db_url)
            self.cursor = self.connection.cursor()
            return True
        except Exception as e:
            print(f"Error connecting to the database: {e}")
            return False

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            
    
    def getConnection(self):
        conn = DB()
        conn.connect()
        conn.connection.autocommit=True
        return conn

# Example usage:
if __name__ == "__main__":
    # Replace this with your PostgreSQL connection URL
    db_url = os.environ['DATABASE_URL']

    # Create an instance of the DatabaseWrapper class
    db_wrapper = DB(db_url)

    # Attempt to connect to the database
    if db_wrapper.connect():
        # Now you can access the connection and cursor as public members
        print("Connected to the database!")
        # Example query
        db_wrapper.cursor.execute("SELECT * FROM users")
        result = db_wrapper.cursor.fetchall()
        print(result)
        # Close the cursor and connection when done
        db_wrapper.close()
