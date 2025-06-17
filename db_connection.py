# db.py
import mysql.connector as ms

def connection_to_database():
    try:
        conn = ms.connect(
            host="localhost",
            user="root",
            password="sql123",
            database="Library"
        )
        cursor = conn.cursor()
        return conn, cursor
    except Exception as e:
        print("Error connecting to database:", e)
        return None, None
