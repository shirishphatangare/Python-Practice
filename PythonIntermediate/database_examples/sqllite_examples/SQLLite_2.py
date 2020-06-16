#Example1: Execute a SQLLite Script from Python

#Installing SQLLite
#1. Command Line: https://www.sqlite.org/download.html
#2. SQLLite GUI: https://www.sqlitetutorial.net/download-install-sqlite/
#Default Database:https://www.sqlitetutorial.net/sqlite-sample-database/ (Ssample Database: chinook)
#SQLLite Understanding: https://www.sqlitetutorial.net/sqlite-sample-database/

#PIP for SQLLite (sqlite3): https://docs.python.org/3/library/sqlite3.html

import sqlite3
try:
    sqliteConnection = sqlite3.connect('util/SQLite_Python.db')
    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")
    with open('util\SQLLiteScript.sql', 'r') as sqlite_file:
        sql_script = sqlite_file.read()
    cursor.executescript(sql_script)
    print("SQLite script executed successfully")
    cursor.close()
except sqlite3.Error as error:
    print("Error while executing sqlite script", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("sqlite connection is closed")