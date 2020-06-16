# Stored Procedure
#Sample Stored Procedure:
#
"""
    DELIMITER $$
    CREATE PROCEDURE SP_GetLaptops_1()
    BEGIN
        SELECT Name,price,purchase_date
        FROM Laptop;
    END$$
    DELIMITER ;
show procedure status like 'SP%';
"""


#


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
    cursor = connection.cursor()
    cursor.callproc('SP_GetLaptops')
    # print out the result
    for result in cursor.stored_results():
        print(result.fetchall())

except Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if (connection.is_connected()):
        connection.close()
        cursor.close()
        print("MySQL connection is closed")