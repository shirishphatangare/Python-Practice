# Fetch MySQL data using the column names instead of a column id

#To selected records from my MySQL table using a column name, we only need to change the cursor creation.
# Replace the standard cursor creation with the following code, and you are ready to fetch records from my MySQL table using a column name.
#cursor = connection.cursor(dictionary=True)
# This creates a cursor that returns rows as dictionaries so we can access using column name
# (here column name is the key of the dictionary)
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
    # MySQLCursorDict creates a cursor that returns rows as dictionaries
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Fetching each row using column name")
    for row in records:
        id = row["Id"]
        name = row["Name"]
        price = row["Price"]
        purchase_date = row["Purchase_date"]
        print(id, name, price, purchase_date)

except Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if (connection.is_connected()):
        connection.close()
        cursor.close()
        print("MySQL connection is closed")