import sqlite3

# This utility class acts as a custom database context manager to manage db connection object
# With context managers, DB connection is committed and closed automatically. We can also customize this behavior
class DatabaseConnection:

    def __init__(self, host: str):
        self.connection = None
        self.host = host

    def __enter__(self) -> sqlite3.Connection:
        self.connection = sqlite3.connect(self.host)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb): # __exit__ is called when there is an exception. We can use this function to handle connection or query errors gracefully
        if exc_type or exc_val or exc_tb: # These 3 params will have some values when error occurs
            self.connection.close() # Do not commit on error. DB may be inconsistent
        else:
            self.connection.commit()
            self.connection.close()
