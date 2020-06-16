# Select limited rows from MySQL table using fetchmany and fetchone: fetchone example
# fetchone(): retrieve the next row of a query result set.
# This method returns a single record or None if no more rows are available.
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
    mySql_select_Query = "select * from laptop"
    #Buffered cursor: Helps you buffer the results from the result set
    cursor = connection.cursor(buffered=True)
    cursor.execute(mySql_select_Query)
    record = cursor.fetchone()
    print(record)
except Error as error:
    print("Error while connecting to MySQL", error)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")