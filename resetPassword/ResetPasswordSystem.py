import sqlite3
import os
from supportFunction.Local_Database_System import get_user_path


def main():
    print("Let's the change password process begin")


def reset_user_password(email, password):
    ''' Change or Update User Password'''
    try:
        file_path = get_user_path();
        print("Successfully Getting the file_path")

        database_path = os.path.join(file_path, "User_Database.db")

        sqlite3Connector = sqlite3.connect(database_path)

        cursor = sqlite3Connector.cursor()
        print("Successfully connect to the database")

        cursor.execute("UPDATE User SET Password = :Password WHERE Email = :Email",
                       {'Password': password, 'Email': email})
        sqlite3Connector.commit()
        print("Successfully update the user password")

        cursor.close()
        sqlite3Connector.close()

    except sqlite3.Error as error:
        print(error)
    finally:
        if (sqlite3Connector):
            sqlite3Connector.close()

def checking_password_database(password, email):
    try:
        file_path = get_user_path();
        print("Successfully Getting the file_path")

        database_path = os.path.join(file_path, "User_Database.db")

        sqlite3Connector = sqlite3.connect(database_path)

        cursor = sqlite3Connector.cursor()
        print("Successfully connect to the database")

        cursor.execute("SELECT * FROM User WHERE Email = :Email AND Password = :Password",
                       {'Password': password, 'Email': email})

        value = cursor.fetchone();
        print("Successfully update the user password")



        cursor.close()
    except sqlite3.Error as error:
        print(error)
    finally:
        if (sqlite3Connector):
            sqlite3Connector.close()
            if value is None:
                return True
            else:
                return False

if __name__ == "__main__":
    main()
