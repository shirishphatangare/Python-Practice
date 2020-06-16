#Example2: Inserting the Data

#Parameterized queries are an important feature of essentially all database interfaces
# This type of query serves to improve the efficiency of queries that are repeated several
# times.

import sqlite3
try:
    sqliteConnection = sqlite3.connect('util/SQLite_Python.db')
    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")
    product_sql = "INSERT INTO products (name, price) VALUES (?, ?)"
    cursor.execute(product_sql, ('Introduction to Combinatorics', 7.99))
    cursor.execute(product_sql,('A Guide to Writing Short Stories', 17.99))
    cursor.execute(product_sql,  ('Data Structures and Algorithms', 11.99))
    cursor.execute(product_sql,  ('Advanced Set Theory', 16.99))
    print("Insertion Successfull")
    cursor.execute("SELECT id, name, price FROM products")
    formatted_result = [f"{id:<5}{name:<35}{price:>5}" for id, name, price in cursor.fetchall()]
    id, product, price = "Id", "Product", "Price"
    print('\n'.join([f"{id:<5}{product:<35}{price:>5}"] + formatted_result))
    cursor.close()
except sqlite3.Error as error:
    print("Error while executing sqlite script", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("sqlite connection is closed")