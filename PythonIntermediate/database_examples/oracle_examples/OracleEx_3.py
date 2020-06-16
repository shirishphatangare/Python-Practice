#Example: Working with Bind variables
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
    named_params = {'dept_id': 50, 'sal': 1000}
    query1 = cursor.execute('SELECT * FROM employees WHERE department_id=:dept_id AND salary>:sal', named_params)
    #Another way to pass in values to a bind variable
    query2 = cursor.execute('SELECT * FROM employees WHERE department_id=:dept_id AND salary>:sal', dept_id=50,
                            sal=1000)
    #Printing bind variabkes
    print(cursor.bindnames())
    #Passing by position is similar but you need to be careful about naming
    r1 = cursor.execute('SELECT * FROM locations WHERE country_id=:1 AND city=:2', ('US', 'Seattle'))
    print(len(cursor.fetchall()))

except cx_Oracle.Error as error:
    print(error)
finally:
    # release the connection
    if connection:
        connection.close()

