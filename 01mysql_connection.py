import mysql.connector as mq
from mysql.connector import Error

#libraries
class Database:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connections(self):
        try:
            self.connection = mq.connect(host="localhost", user="root", password="")
            if self.connection.is_connected():
                print("Connected !")
            else:
                print("Not Connected !")
                self.cursor = self.connection.cursor()
        except Error as e:
            print(f"Error : {e}")
        finally:
            if self.connection and self.connection.is_connected():
                self.connection.close()
                print("Connection closed.")

    def closes(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Connection closed !")


if __name__=="__main__":
    db = Database()
    db.connections()
    db.closes()
