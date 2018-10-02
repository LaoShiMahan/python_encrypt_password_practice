import sqlite3

connection = sqlite3.connect("database.db")

print("Database connection successful")

connection.execute(
    """
        CREATE TABLE EMPLOYEES
        (
            ID        INT   PRIMARY KEY  NOT NULL,
            USERNAME  TEXT               NOT NULL,
            PASSWORD  TEXT               NOT NULL,
            AGE       INT                NOT NULL
        )
    """
)

print("Table creation successful")

connection.close()