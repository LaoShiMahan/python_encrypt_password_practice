import bcrypt
import sqlite3

user_name = input("Username: ")
user_password = input("Password: ")
age = int(input("Age: "))

hashed_password = bcrypt.hashpw(user_password.encode("utf8"), bcrypt.gensalt())

print(hashed_password)

connection = sqlite3.connect("database.db")

print("Database connection successful")

connection.execute(
    """
        INSERT INTO EMPLOYEES
        (
            ID,
            USERNAME,
            PASSWORD,
            AGE
        )
        VALUES
        (
            0,
            ?,
            ?,
            ?
        )
    """,
    (
        user_name,
        hashed_password,
        age
    )
)

connection.commit()

print("Username and password INSERT INTO database successful")

connection.close()