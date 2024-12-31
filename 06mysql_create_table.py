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

    def create_table(self):
        try:
            self.database_name = input("Enter table name : ")
            self.connections()
            if self.conn and self.cursor:
                self.query = f"""create table {self.database_name}
                (
                    id int,
                    name varchar(50),
                    birthday_date date,
                    phone int(10),
                    gender varchar(1)
                )
                """
                self.cursor.execute(self.query)
                print("Created table with constraints !")
            else:
                print("Not table   !")
        except Error as e:
            print(f" Error : {e}")
            self.closes()

if __name__ == "__main__":
    db = Database("vasant")
    db.create_table()
