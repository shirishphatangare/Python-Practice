#Install the Pyodbc package if not existing
#Command Line: pip install pyodbc

import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=server_name;'
                      'Database=db_name;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM db_name.Table')

for row in cursor:
    print(row)