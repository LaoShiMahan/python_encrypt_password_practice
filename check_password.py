import bcrypt
import sqlite3

connection = sqlite3.connect("database.db")

print("Database connection successful")

data = connection.execute(
    """
        SELECT
            ID,
            USERNAME,
            PASSWORD,
            AGE
        FROM EMPLOYEES
    """
)

for row in data:
    print("      ID  =  ", row[0])
    print("USERNAME  =  ", row[1])
    print("PASSWORD  =  ", row[2])
    print("     AGE  =  ", row[3])
    print("\n")

    hashed_password = row[2]
    print(hashed_password)

    user_password = input(f"Please enter the password for username {row[1]}: ")
    
    validate_password = bcrypt.hashpw(user_password.encode("utf8"), hashed_password) == hashed_password
    print(validate_password)

print("Database SELECT successful")

connection.close()