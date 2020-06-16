import sqlite3
connection = sqlite3.connect("util/SQLite_Python.db")
# By default auto-commit is set to true. You could set them to false using the connection object
cursor = connection.cursor()
# Inserting a list of tuples

staff_data = [("William", "Shakespeare", "m", "1961-10-25"),
              ("Frank", "Schiller", "m", "1955-08-17"),
              ("Jane", "Wall", "f", "1989-03-14")]

for p in staff_data:
    format_str = """INSERT INTO employee (staff_number, fname, lname, gender, birth_date)
    VALUES (NULL, "{first}", "{last}", "{gender}", "{birthdate}");"""

    sql_command = format_str.format(first=p[0], last=p[1], gender=p[2], birthdate=p[3])
    cursor.execute(sql_command)
#To save the data you have to commit
connection.commit()

connection.close()