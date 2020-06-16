import sqlite3
connection = sqlite3.connect("util/SQLite_Python.db")
# By default auto-commit is set to true. You could set them to false using the connection object
cursor = connection.cursor()
cursor.execute("SELECT * FROM employee")
print("fetchall:")
result = cursor.fetchall()
for r in result:
    print(r)
cursor.execute("SELECT * FROM employee")
print("\nfetch one:")
res = cursor.fetchone()
print(res)

connection.close()