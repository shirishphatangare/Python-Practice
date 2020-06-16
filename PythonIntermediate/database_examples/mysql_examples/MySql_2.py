#Python MySQL Create Table
#Some Cursor Objects:
#1.Parse (optional): Not really required to be called because SQL statements are
# automatically parsed at the Execute stage. It can be used to validate statements before
# executing them. When an error is detected in such a statement, a DatabaseError exception
# is raised with a corresponding error message

#2.Execute: pass in  to be run directly against the database. Bind variables assigned through
# the parameters or keyword_parameters arguments can be specified as a dictionary, sequence,
# or a set of keyword arguments. If dictionary or keyword arguments are supplied then the
# values will be name-bound. If a sequence is given, the values will be resolved by their
# position. This method returns a list of variable objects if it is a query, and None when
# it's not.

#3.Fetch (optional)—Only used for queries (because DDL and DCL statements don't return results).
# On a cursor that didn't execute a query, these methods will raise an InterfaceError
# exception.
#3.1: fetchall() Fetches all remaining rows of the result set as a list of tuples. If no more rows are available, it returns an empty list.
#3.2:fetchmany([rows_no]) Fetches the next rows_no rows from the database. If the parameter
# isn't specified it fetches the arraysize number of rows. In situations where rows_no is
# greater than the number of fetched rows, it simply gets the remaining number of rows.
#3.3:fetchone() Fetches a single tuple from the database or none if no more rows are available.

#Create mySQL Database:Create database Electronics;

import mysql.connector
from mysql.connector import Error
from pprint import pprint
#The pprint module provides a capability to “pretty-print” arbitrary Python data structures
# in a form

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Electronics',
                                         user='root',
                                         password='syntel123$')

    mySql_Create_Table_Query = """CREATE TABLE Laptop ( 
                             Id int(11) NOT NULL,
                             Name varchar(250) NOT NULL,
                             Price float NOT NULL,
                             Purchase_date Date NOT NULL,
                             PRIMARY KEY (Id)) """

    #Cursor Creation
    cursor = connection.cursor()
    # cursors are iterators. These powerful Python structures let you iterate over sequences
    # in a natural way that fetches subsequent items on demand only. Costly database select
    # operations naturally fit into this idea because the data only gets fetched when needed.
    # Instead of creating or fetching the whole result set, you iterate until the desired
    # value is found or another condition fulfilled.
    #cursor.execute("DROP TABLE Laptop")
    result = cursor.execute(mySql_Create_Table_Query)
    print("Laptop Table created successfully: ",result)
    connection.commit() # If auto-commit is not set while creating a DB connection, we need to commit explicitly
    print("------------Details on the table columns: DESC Command------------")
    result = cursor.execute("Desc Laptop")

    ## it will print all the columns as 'tuples' in a list
    print(cursor.fetchall()) # try using result.fetchall()
    print("------------Details on the table columns:cursor.description------------")
    pprint(cursor.description)
    #Displays: column name, column type, display size, internal size, precision, scale and whether null is possible

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


# Other args for mysql.connector.connect()
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