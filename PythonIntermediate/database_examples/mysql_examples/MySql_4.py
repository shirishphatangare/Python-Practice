#Python example to insert a single row/record into MySQL table

import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
try:
    #Putting in the configuration details in a dictionary
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
    if connection.is_connected():
        mySql_insert_query = """INSERT INTO Laptop (Id, Name, Price, Purchase_date) 
                                   VALUES 
                                   (10, 'Lenovo ThinkPad P71', 659, '2019-08-14') """

        cursor = connection.cursor()
       # cursor.execute("Delete from Laptop")
        cursor.execute(mySql_insert_query)
        #connection.commit()
        print(cursor.rowcount, "Record inserted successfully into Laptop table")
        cursor.close()
except mysql.connector.Error as error:
    print("Failed to insert record into Laptop table {}".format(error))
finally:
    if (connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")

#Notes:
#Python makes extensive use of the exception model and the DB API defines several standard
# exceptions that could be very helpful in debugging problems in the application.
# Below are the standard exceptions with a short description of the types of causes:
#1.Warning—Data was truncated during inserts, etc.
#2.Error—Base class for all of the exceptions mentioned here except for Warning
#3.InterfaceError—The database interface failed rather than the database itself
#4.DatabaseError—Strictly a database problem
#5.DataError—Problems with the result data: division by zero, value out of range, etc.
#6.OperationalError—Database error independent of the programmer: connection loss, memory
# allocation error, transaction processing error, etc.
#7.IntegrityError—Database relational integrity has been affected, e.g. foreign key
# constraint fails
#8.InternalError—Database has run into an internal error, e.g. invalid cursor, transaction
# out of synchronization
#9.ProgrammingError—Table not found, syntax error in SQL statement, wrong number of
# parameters specified etc.
#10. NotSupportedError—A non-existent part of API has been called