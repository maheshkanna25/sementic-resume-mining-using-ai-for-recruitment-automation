import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mahesh@2530",  # ⚠️ change this
        database="resume_ai"
    )