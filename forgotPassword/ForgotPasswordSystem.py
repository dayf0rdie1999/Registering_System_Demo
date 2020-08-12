import sqlite3
import os
from supportFunction.Local_Database_System import get_user_path


def main():
    print("Let's check the email process begin")


def Checking_Email_Database(email):
    'Checking The Email Database'
    try:
        file_path = get_user_path();
        print("Successfully Getting the file_path")

        database_path = os.path.join(file_path, "User_Database.db")

        sqlite3Connector = sqlite3.connect(database_path);
        cursor = sqlite3Connector.cursor()
        print("Successfully connecting to the database")

        cursor.execute("SELECT Email FROM User WHERE Email = :Email", {'Email':email})
        value = cursor.fetchone()

        if value is None:
            return False
        else:
            Email = value[0]
            return Email

        cursor.close()

    except sqlite3.Error as error:
        print(error)

    finally:
        if (sqlite3Connector):
            sqlite3Connector.close()


if __name__ == "__main__":
    main()