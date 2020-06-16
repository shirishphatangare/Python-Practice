#Example1: Getting connected to the Database

#Installing SQLite
#1. Command Line: https://www.sqlite.org/download.html
#2. SQLite GUI: https://www.sqlitetutorial.net/download-install-sqlite/
#3. DB Browser SQLite another GUI to observe SQLite data on local system
#Default Database:https://www.sqlitetutorial.net/sqlite-sample-database/ (Ssample Database: chinook)
#SQLLite Understanding: https://www.sqlitetutorial.net/sqlite-sample-database/

#PIP for SQLLite (sqlite3): https://docs.python.org/3/library/sqlite3.html

import sqlite3

try:
    sqliteConnection = sqlite3.connect('util/SQLite_Python.db') # in SQLite we do not need separate DB. A file can serve as a DB
    cursor = sqliteConnection.cursor()
    print("Database created and Successfully Connected to SQLite")

    sqlite_select_Query = "select sqlite_version();"
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()
    print("SQLite Database Version is: ", record)
    cursor.close()
except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")