#Use the Dictionary to keep MySQL Connection arguments in Python

#Create mySQL Database:Create database Electronics;

import mysql.connector
from mysql.connector import Error

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
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Your connected to database: ", record)
except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

#Note:Some other connection arguments we can use to communicate with MySQL server from Python are:
#1.port: The TCP/IP port of the MySQL server. This value must be an integer. We can specify the different port number if MySQL server is listening to the different port. The default value for this port argument is 3306.
#2.use_unicode: Whether to use Unicode. The default value is True.
#3.charset: MySQL character set to use, character set variables relate to a client’s interaction with the server. There are almost 30 to 40 charset MySQL server supports. The default value of the charset argument is “utf8″.
#auto-commit: Whether to auto-commit transactions. If you want to manage transactions in MySQL from Python, you need to set this value to true or false. The default value is False, i.e. the changes are not committed to the database. You need to explicitly call a commit method to persist your changes in the database.
#get_warnings: To fetch warning, this is helpful to know the connection is established but with warnings. The default value is False.
#raise_on_warnings: Whether to raise an exception on warnings. The Default value is False.
#connection_timeout (connect_timeout*) : Timeout for the TCP and Unix socket connections. The connection terminates after this timeout expired.
#buffered: Whether cursor objects fetch the results immediately after executing queries. The default value is False.
#raw: Whether MySQL results are returned as-is, rather than converted to Python types. The default value is False. You can set it to true if you want a query result in python type.
#force_ipv6: When setting to True, uses IPv6 when an address resolves to both IPv4 and IPv6. By default, IPv4 used in such cases. The default value for this argument is false.
#pool_name: It is the Connection pool name that you are creating or using.
#pool_size: Connection pool size that you want to create. the default value is 5.
#pool_reset_session: Whether to reset session variables when the connection returned to the pool. the default is True.
#use_pure: Whether to use pure Python or C Extension. If use_pure=False then pure python module is used otherwise it connects MySQL using C extension. Moreover, if C Extension is not available, then My SQL Connector Python automatically fall back to the pure Python implementation.
#unix_socket: The location of the Unix socket file. These enable communication between two processes.
#auth_plugin: Authentication plugin to use. Added in 1.2.1.
#collation: MySQL collation to use. you can use the collation that you set while installing MySQL Server. The default value is utf8_generalW_chiich.
#sql_mode: Set the sql_mode session variable at connection time.