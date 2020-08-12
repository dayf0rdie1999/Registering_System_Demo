import sqlite3
from kivy.utils import platform
import os


def main():
    print("Let's create the database begins")



def get_user_path():

    if platform != 'ios':
        root = os.getcwd()
        return root
    elif platform == 'ios':
        root = os.path.expanduser('~')
        return os.path.join(root, "Library")

def Create_Local_Database():

    try:
        file_path = get_user_path();
        print("Successfully Getting the file_path")

        database_path = os.path.join(file_path, "User_Database.db")

        sqliteConnector = sqlite3.connect(database_path)
        cursor = sqliteConnector.cursor()
        print("Successfully Connecting or creating to the database")

        cursor.execute("""CREATE TABLE IF NOT EXISTS User(Fullname TEXT NOT NULL,Username TEXT NOT NULL, Password TEXT NOT NULL, Email TEXT NOT NULL)""")
        sqliteConnector.commit()
        print("Successfully creating table in local database")

        cursor.close()
    except sqlite3.Error as error:
        print(error)
    finally:
        if (sqliteConnector):
            sqliteConnector.close()


if __name__ == "__main__":
    main()
