import sqlite3
import os
from kivy.utils import platform
from supportFunction.Local_Database_System import get_user_path


def main():
    print("Let's Sign In System Begins");



def Creating_Auto_SignIn_System(options=0):
    try:
        if 0 <= options <= 1:
            pass
        else:
            return "Incorrect Input System"

        ''' Printing User Options'''
        file_path = get_user_path();
        print("Successfully Getting the file_path")

        database_path = os.path.join(file_path, "Temporary_Database.db")

        """ Creating a temporary database"""
        sqliteConnector = sqlite3.connect(database_path);
        cursor = sqliteConnector.cursor();
        print("Successfully Create Temporary Database")

        """ Creating a table with options as a variable """
        sql_creating_table_query = "CREATE TABLE IF NOT EXISTS Options(Options INT NO NULL DEFAULT 0) "
        cursor.execute(sql_creating_table_query)
        sqliteConnector.commit();
        print("Successfully Create Table")

        """ Checking the options input"""
        cursor.execute("""SELECT COUNT(*) FROM Options""")
        value = cursor.fetchone();
        print("Successfully Checking number the of database")

        if value[0] == 0:
            """ Inserting the value into the table"""
            cursor.execute("INSERT INTO Options(Options) VALUES (:Options)", {'Options': options});
            print("Successfully insert value into Table")
            sqliteConnector.commit();

            """ Updating The Options in the table"""
            cursor.execute("UPDATE Options SET Options = :Options", {'Options': options});

            print("Successfully Updating The Value System")

            sqliteConnector.commit();
        else:
            pass

        cursor.close();
    except sqlite3.Error as error:
        print(error)

    finally:
        if (sqliteConnector):
            sqliteConnector.close()


''' Deleting the database when the user log out and log in with different account'''


def Deleting_Auto_SignIn_System():
    try:
        file_path = get_user_path();
        print("Successfully Getting the file_path")

        if platform != "ios":
            for file in os.listdir(file_path):
                if file == "Temporary_Database.db":
                    os.remove("Temporary_Database.db")
                    print("Successfully Deleteing the database")
                else:
                    pass
        else:
            for file in os.listdir(file_path):
                if file == "Temporary_Database.db":
                    os.remove(os.path.join(file_path,"Temporary_Database.db"))
                    print("Successfully Deleteing the database")
                else:
                    pass

    except os.error as error:
        print(error)

def Checking_Auto_SignIn_System():

    file_path = get_user_path();
    print("Successfully Getting the file_path")
    for file in os.listdir(file_path):
        if file != "Temporary_Database.db":
            pass
        else:
            try:
                database_path = os.path.join(file_path, "Temporary_Database.db")
                sqliteConnector = sqlite3.connect(database_path);
                cursor = sqliteConnector.cursor();
                print("Successfully Connecting to the temporary database")

                ''' Creating a query to get the options value'''
                cursor.execute("""SELECT * FROM Options""");
                value = cursor.fetchone();
                print("Successfully Capturing the data")

                if value[0] == 1:
                    print("Auto Log In")
                    return True
                else:
                    print("Required Sign In")
                    return False

                cursor.close()

            except sqlite3.Error as error:
                print(error)
            finally:
                if (sqliteConnector):
                    sqliteConnector.close()


def Sign_In(username, password, path_to_your_database=None):
    try:
        file_path = get_user_path();
        print("Successfully Getting the file_path")

        database_path = os.path.join(file_path, "User_Database.db")

        ''' Connecting to the database '''
        sqliteConnection = sqlite3.connect(database_path);
        cursor = sqliteConnection.cursor();

        '''Checking if the username is in the database'''
        cursor.execute("""SELECT Username FROM User WHERE Username = :Username""", {'Username': username});
        username_checker = cursor.fetchone();
        print("Successfully Getting the Username")

        if username_checker is None:
            cursor.close()
            return "Not Existed"
        else:
            cursor.execute("""SELECT * FROM User WHERE Username = :Username and Password = :Password""",
                           {'Username': username, 'Password': password})
            value = cursor.fetchone();
        print("Successfully Checking Remember from user")

        if value is None:
            cursor.close()
            return "Either Password or Username is incorrect"

        sqliteConnection.commit();
        print("The Process is complete")
        cursor.close()

    except sqlite3.Error as error:
        print(error);
        return "Not Existed"

    finally:
        if (sqliteConnection):
            sqliteConnection.close();


if __name__ == "__main__":
    main()
