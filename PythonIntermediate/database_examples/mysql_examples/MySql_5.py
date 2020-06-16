#Python variables in a MySQL INSERT query

#Using a parameterized query we can pass python variables as a query parameter in which
# placeholders (%s) used for parameters.
# placeholders (?) can also be used for parameters.

#A parametrized query in Python is an operation which generates a prepared statement internally, then brings in your parameters and executes the SQL against the database.


import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

def insertVariblesIntoTable(id, name, price, purchase_date):
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
        cursor = connection.cursor()

        mySql_insert_query = """INSERT INTO Laptop (Id, Name, Price, Purchase_date) 
                                VALUES (%s, %s, %s, %s) """
        recordTuple = (id, name, price, purchase_date) # A Tuple
        cursor.execute(mySql_insert_query, recordTuple)
        #connection.commit()
        print("Record inserted successfully into Laptop table")
    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

insertVariblesIntoTable(2, 'Area 51M', 6999, '2019-04-14')
insertVariblesIntoTable(3, 'MacBook Pro', 2499, '2019-06-20')

