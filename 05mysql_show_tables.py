import mysql.connector as mq
from mysql.connector import Error


class Database:
    def __init__(self, db_name=None):
        self.connection = None
        self.cursor = None
        self.db_name = db_name

    def connections(self):
        try:
            self.conn = mq.connect(
                host="localhost", user="root", password="", database=self.db_name
            )
            if self.conn.is_connected():
                self.cursor = self.conn.cursor()
                print("Connected !")
                print()
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
            self.databases = None
            self.connections()
            if self.conn and self.cursor:
                self.query = f"show tables"
                self.cursor.execute(self.query)
                self.databases = self.cursor.fetchall()
                for i, db in enumerate(self.databases):
                    print(f" {i+1}. Name tables : {db[0]}")
                self.closes()
            else:
                print("Not show tables !")
        except Error as e:
            print(f" Error : {e}")
            self.closes()


if __name__=="__main__":
    db = Database("vasant")
    db.use_database()
