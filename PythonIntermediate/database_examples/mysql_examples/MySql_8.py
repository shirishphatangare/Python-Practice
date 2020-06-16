# SELECT Query example to fetch rows from MySQL table.
#Use fetchall(), fetchmany() and fetchone()  methods of a cursor class to fetch limited rows from a table.

import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from datetime import datetime
try:
    connection_config_dict = {
        'user': 'root',
        'password': 'syntel123$',
        'host': 'localhost',
        'database': 'Electronics',
        'raise_on_warnings': True,
        'use_pure': False,
        'autocommit': True,
        'pool_size': 5
    }
    connection = mysql.connector.connect(**connection_config_dict)
    sql_select_Query = "select * from Laptop"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall() # Cursor is an iterator. Instead of fetching all the rows we can also iterate over cursor to fetch records untill a specific condition meets
    print("Total number of rows in Laptop is: ", cursor.rowcount)
    print("\nPrinting each laptop record")
    for row in records:
        print("Id = ", row[0], )
        print("Name = ", row[1])
        print("Price  = ", row[2])
        print("Purchase date  = ", row[3], "\n")
except Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if (connection.is_connected()):
        connection.close()
        cursor.close()
        print("MySQL connection is closed")