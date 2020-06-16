# Insert timestamp and DateTime into a MySQL table

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
    mySql_insert_query = """INSERT INTO Laptop (Id, Name, Price, Purchase_date) 
                                VALUES (%s, %s, %s, %s) """
    cursor = connection.cursor()
    current_Date = datetime.now()
    # convert date in the format you want
    formatted_date = current_Date.strftime('%Y-%m-%d %H:%M:%S')
    insert_tuple = (7, 'Acer Predator Triton', 2435, current_Date)
    #insert_tuple = (7, 'Acer Predator Triton', 2435, formatted_date)
    result = cursor.execute(mySql_insert_query, insert_tuple)
    connection.commit()
    print("Date Record inserted successfully")
except mysql.connector.Error as error:
    connection.rollback()
    print("Failed to insert into MySQL table {}".format(error))
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


#Note:  To fetch data use cursor.execute() to run a query.
#cursor.fetchall() to fetch all rows .
#cursor.fetchone() to fetch single row.
#cursor.fetchmany(SIZE) to fetch limited rows.