import sqlite3
from practice.util.digital_library_database_connection import DatabaseConnection

LIBRARY_SQLLITE_DATA_FILE = "resources/sqllite_data.db"


def create_library_database():
    with DatabaseConnection(LIBRARY_SQLLITE_DATA_FILE) as connection:
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS books(name text primary key, author text ,read text)") # id integer row auto-incrementing is inserted automatically


def insert_record(record):
    with DatabaseConnection(LIBRARY_SQLLITE_DATA_FILE) as connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO books (name,author,read) VALUES (?, ?, ?)", (record['name'], record['author'],'0'))  #parameterized arguments as a tuple


def get_all_records():
    with DatabaseConnection(LIBRARY_SQLLITE_DATA_FILE) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM books")
        # cursor.fetchall() Returns a list of tuples
        # Covert List of tuples to list of dicts
        books = [ {'name':row[0],'author':row[1],'read':row[2]}  for row in cursor.fetchall() ]
    return books


def update_record(record_name):
    with DatabaseConnection(LIBRARY_SQLLITE_DATA_FILE) as connection:
        cursor = connection.cursor()
        cursor.execute("UPDATE books SET read = '1' WHERE name = ?", (record_name,)) #parameterized arguments as a tuple


def delete_record(record_name):
    with DatabaseConnection(LIBRARY_SQLLITE_DATA_FILE) as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM books WHERE name = ?", (record_name,)) #parameterized arguments as a tuple
