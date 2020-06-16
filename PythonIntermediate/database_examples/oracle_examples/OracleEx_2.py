# The pprint module provides a capability to “pretty-print” arbitrary Python data structures in a form which can be used as input to the interpreter.
# If the formatted structures include objects which are not fundamental Python types, the representation may not be loadable.

from pprint import pprint

import cx_Oracle
from database_examples.oracle_examples import config

connection = None
try:
    connection = cx_Oracle.connect(
        config.username,
        config.password,
        config.dsn,
        encoding=config.encoding)

    # define an arbitrary number of cursors using the cursor() method of the Connection object.
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM jobs')
    print("---------Display all data: Jobs Table ------------------")
   # pprint(cursor.fetchall())

    for row in cursor:  ## notice that this is plain English!
        print(row)
    #Creating another cursor
    column_data_types = cursor.execute('SELECT * FROM employees')
    print("---------Employee Table ------------------")
    print(column_data_types)
    print("---------Column Descriptions ------------------")
    pprint(cursor.description)

except cx_Oracle.Error as error:
    print(error)
finally:
    # release the connection
    if connection:
        connection.close()

#Note: Arguments required to connect MySQL from Python
#You need to know the following detail of the MySQL server to perform the connection from Python.
#Username –  i.e., the username that you use to work with MySQL Server. The default username for the MySQL database is a root
#Password – Password is given by the user at the time of installing the MySQL database. If you are using root then you won’t need the password.
#Host Name  – is the server name or Ip address on which MySQL is running. if you are running on localhost, then you can use localhost, or it’s IP, i.e. 127.0.0.0
#Database Name – Database name to which you want to connect.