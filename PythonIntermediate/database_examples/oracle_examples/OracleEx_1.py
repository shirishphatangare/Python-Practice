#Documentation: https://www.oracletutorial.com/python-oracle/connecting-to-oracle-database-in-python/
#Examples and API: https://developer.oracle.com/dsl/prez-python-queries.html

#-------------CONNECTING TO Oracle USING PYTHON-----------------
#Before you can access databases using Python, you must install the following packages in a virtual environment:
#(1)cx_Oracle:
#   - It is a Python extension module that enables access to Oracle Database.
#   - It conforms to the Python database API 2.0 and Support for Python 2 and 3.
#   - Support for Oracle Client 11.2, 12, 18 and 19. Allows easy upgrades and connectivity to different Oracle Database versions.
#   - Command Line: pip install cx_Oracle
#
#You can connect to Oracle Database using cx_Oracle in two ways:
# (1)standalone : useful when the application has a single user session to the Oracle database
# (2) pooled connections: critical for performance when the application often connects and disconnects from the database.

#-------------Steps to connect database in Python: cx_Oracle Python---------
#1.Install Connector in Python using pip.
#2.Use the connect() of Connector Python with required parameters.
#3.Use the connection object to create a cursor object to perform Database Operations.
#4.The cursor.execute() to execute SQL queries from Python.
#5.Close the Cursor object using a cursor.close() and database connection using connection.close() after your work completes.
#6.Catch Exception if any that may occur during this process.

#------------Step 1:Install Driver-------------------
#1. pip install cx_Oracle
#2. Retrieve the connection information by locating your tnsnames.ora file on your computer.
# Look for Hostname,port number and service name

#------------Step 2:Connect to the database-------------------
#create a standalone connection, you use the cx_Oracle.connect() method or cx_Oracle.Connection().
import cx_Oracle
from database_examples.oracle_examples import config

connection = None
try:
    connection = cx_Oracle.connect(
        config.username,
        config.password,
        config.dsn,
        encoding=config.encoding)

    # show the version of the Oracle Database
    print(connection.version)
except cx_Oracle.Error as error:
    print(error)
finally:
    # release the connection
    if connection:
        connection.close()

#Note: Arguments required to connect Oracle from Python
#You need to know the following detail of the Oracle server to perform the connection from Python.
#Username –  i.e., the username that you use to work with Oracle Server. The default username for the Oracle database is a root
#Password – Password is given by the user at the time of installing the MySQL database. If you are using root then you won’t need the password.
#Host Name  – is the server name or Ip address on which Oracle is running. if you are running on localhost, then you can use localhost, or it’s IP, i.e. 127.0.0.0
#Database Name – Database name to which you want to connect.