import sqlite3
import os
from supportFunction.Local_Database_System import get_user_path
import re


def main():
    print("Registering Process Begin")

def Sign_Up_Information(fullname, username, email, password):
    try:
        file_path = get_user_path();
        print("Successfully Getting the file_path")

        database_path = os.path.join(file_path, "User_Database.db")

        ''' Connecting to the database'''
        sqliteConnector = sqlite3.connect(database_path);
        cursor = sqliteConnector.cursor();
        print("Successfully Access to the database");

        print("Insert Data", username, email, password)
        ''' Storing All Information Into the local database'''
        sqlite_insert_query = """INSERT INTO User(Fullname,Username,Email,Password) VALUES (?,?,?,?)"""
        data_tuple = (fullname, username, email, password);
        cursor.execute(sqlite_insert_query, data_tuple);
        print("Successfully Insert Data")

        sqliteConnector.commit()
        cursor.close()
        print("Successfully Accomplished")

    except sqlite3.Error as error:
        print(error)

    finally:
        if (sqliteConnector):
            sqliteConnector.close()


def security_pass(pswrd):
    # + Length check:
    if len(pswrd) < 8:
        return 'Not enough letters'
    elif len(pswrd) > 21:
        return 'Too long'
    # + Case check for password: at least 1 uppper case letter:
    elif pswrd.islower():
        return 'Missing uppercase'
    # + Case check for password: at least 1 number:
    elif any(char.isdigit() for char in pswrd) == False:
        return 'Missing number'
    # + Case check for password: at least 1 special character:
    elif re.match("^[a-zA-Z0-9_]*$", pswrd):
        return 'Missing special character'

    return pswrd


def user_name_pass(username):
    # + Check user name length:
    if len(username) < 8:
        return 'Too short'

    # + Check if user name exist:
    elif check_duplicate_username(username) == True:
        return 'Already taken'

    # + Space check
    elif " " in username:
        return 'No space'

    return username


def check_duplicate_username(username):
    try:
        file_path = get_user_path();
        print("Successfully Getting the file_path")

        database_path = os.path.join(file_path, "User_Database.db")

        ''' Connecting to the database'''
        sqliteConnector = sqlite3.connect(database_path);
        cursor = sqliteConnector.cursor();
        print("Successfully Access to the database");

        cursor.execute("SELECT * FROM User WHERE Username = :Username", {'Username': username})
        value = cursor.fetchone()

        cursor.close()

    except sqlite3.Error as error:
        print(error)

    finally:
        if (sqliteConnector):
            sqliteConnector.close()
            if value is not None:
                return True
            else:
                return False




if __name__ == "__main__":
    main()
