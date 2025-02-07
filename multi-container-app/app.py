import os
import psycopg2  # For PostgreSQL
import mysql.connector  # For MySQL
from flask import Flask

app = Flask(__name__)

# Choose the database type
DB_TYPE = os.getenv('DB_TYPE', 'postgresql')

def connect_db():
    if DB_TYPE == 'postgresql':
        return psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            host=os.getenv("DB_HOST", "db")  # Default to 'db'
        )
    elif DB_TYPE == 'mysql':
        return mysql.connector.connect(
            database=os.getenv("MYSQL_DATABASE"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            host=os.getenv("DB_HOST", "db")  # Default to 'db'
        )

@app.route("/")
def home():
    conn = connect_db()
    return "Connected to DB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)