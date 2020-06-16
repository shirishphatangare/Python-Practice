# Select limited rows from MySQL table using fetchmany and fetchone:Fetch Many example
#  fetch all the rows from a table is a time-consuming task if a table contains thousand of rows.
# If we fetch all rows we need more space and processing time to its advisable to use the
# fetchmany()  method of cursor class to fetch fewer rows.

#The syntax of the cursor’s fetchmany() : rows = cursor.fetchmany(size=1)
#This method fetches the next set of rows of a query result and returns a list of tuples.
# If no more rows are available, it returns an empty list.
#Cursor’s fetchmany() methods return the number of rows specified by size argument,
# defaults value of size argument is one. If the specified size is 5, then it returns Five rows.

#Note: If a table contains row lesser than specified size then fewer rows are returned.
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
    cursor = connection.cursor(buffered=True)
    cursor.execute(mySql_select_Query)
    fetching_size = 2
    records = cursor.fetchmany(fetching_size)
    print("Total number of rows is: ", cursor.rowcount)
    print("Printing ", fetching_size, " Laptop record using cursor.fetchmany")
    for row in records:
        print(row)
except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("connection is closed")