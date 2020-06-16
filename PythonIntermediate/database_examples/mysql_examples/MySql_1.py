#download a free MySQL database at https://www.mysql.com/downloads/.

#-------------CONNECTING TO MYSQL USING PYTHON-----------------
#Before you can access MySQL databases using Python,
# you must install one (or more) of the following packages in a virtual environment:
import pip
#(1)MySQL-python: This package contains the MySQLdb module, which is written in C.
#   - It is one of the most commonly used Python packages for MySQL.
#   - Command Line: pip install MySQL-python
#(2)mysql-connector-python: This package contains the mysql.connector module, written entirely in Python.
#   -  Command Line: pip install mysql-connector-python
#(3)PyMySQL: This package contains the pymysql module, which is written entirely in Python.
#  - It is designed to be a drop-in replacement for the MySQL-python package.
#   -  Command Line: pip install pymysql

#Note: All three of these packages use Python's portable SQL database API.
# This means that if you switch from one module to another, you can reuse almost all of your existing code

#Documentation: https://dev.mysql.com/doc/connector-python/en/connector-python-connectargs.html
#-------------Steps to connect MySQL database in Python: MySQL Connector Python---------
#1.Install MySQL Connector or driver in Python using pip.
#2.Get the connection: Use the  mysql.connector.connect()  method of MySQL Connector Python with required parameters to connect MySQL.
#3.Get the cursor: Use the connection object returned by a  connect()  method to create a cursor object to perform Database Operations.
#4.The cursor.execute() to execute SQL queries from Python.
#5.Close the Cursor object using a cursor.close() and MySQL database connection using connection.close() after your work completes.
#6.Catch Exception if any that may occur during this process.

#------------Step 1:Install MySQL Driver-------------------
#1. Python needs a MySQL driver to access the MySQL database.
# - use the driver "MySQL Connector".
#Command to install: python -m pip mysql-connector-python
#Test MySQL Connector

#------------Step 2:Connect to the MySQL database-------------------
import mysql.connector
from mysql.connector import Error
#Start by creating a connection to the database.
#Check username in mySQL by using the command: select user()
#Step 1:Get the connect : use connect()
mydb = mysql.connector.connect(host="localhost",user="root",password="syntel123$",database='demo') # Need to install mysql
try:
    #Check if connection was successful
    if mydb.is_connected():
            db_Info = mydb.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = mydb.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print(type(record))
            print("You're connected to database: ", record)
except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (mydb.is_connected()):
        cursor.close()
        mydb.close()
        print("MySQL connection is closed")


#Note: Arguments required to connect MySQL from Python
#You need to know the following detail of the MySQL server to perform the connection from Python.
#Username –  i.e., the username that you use to work with MySQL Server. The default username for the MySQL database is a root
#Password – Password is given by the user at the time of installing the MySQL database. If you are using root then you won’t need the password.
#Host Name  – is the server name or Ip address on which MySQL is running. if you are running on localhost, then you can use localhost, or it’s IP, i.e. 127.0.0.0
#Database Name – Database name to which you want to connect.