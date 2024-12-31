import mysql.connector as mq
from mysql.connector import Error


class Database:
    def __init__(self,db_name=None):
        self.connection = None
        self.cursor = None
        self.db_name=db_name

    def connections(self):
        try:
            self.conn = mq.connect(host="localhost", user="root", password="",database=self.db_name)
            if self.conn.is_connected():
                self.cursor = self.conn.cursor()
                print("Connected !")
            else:
                print("Not Connected !")
        except Error as e:
            print(f"Error : {e}")
        # finally:
        #     if self.conn and self.conn.is_connected():
        #         self.conn.close()
        #         print("Connection closed.")

    def closes(self):
        if self.conn.is_connected():
            self.conn.close()
            print("Connection closed !")

    def use_database(self):
        try:
            self.database_name = input("Enter use database name : ")
            self.connections()
            if self.conn and self.cursor:
                self.query = f"use  {self.database_name}"
                self.cursor.execute(self.query)
                print("used database !")
                self.closes()
            else:
                print("Not used Database !")
        except Error as e:
            print(f" Error : {e}")
            self.closes()


if __name__=="__main__":
    db = Database("vasant")
    db.use_database()
