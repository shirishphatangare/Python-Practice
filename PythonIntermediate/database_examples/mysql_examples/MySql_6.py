# Insert multiple rows into the MySQL table using the cursor’s executemany()

# using the prepared statement (parameterized query) to insert multiple rows into a table.
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
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
    records_to_insert = [(4, 'HP Pavilion Power', 1999, '2019-01-11'),
                         (5, 'MSI WS75 9TL-496', 5799, '2019-02-27'),
                         (6, 'Microsoft Surface', 2330, '2019-07-23')] # List of Tuples

    #cursors are iterators. These powerful Python structures let you iterate over sequences
    # in a natural way that fetches subsequent items on demand only. Costly database select
    # operations naturally fit into this idea because the data only gets fetched when needed.
    # Instead of creating or fetching the whole result set, you iterate until the desired
    # value is found or another condition fulfilled.
    cursor.executemany(mySql_insert_query, records_to_insert)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Laptop table")
except mysql.connector.Error as error:
    print("Failed to insert record into MySQL table {}".format(error))
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")