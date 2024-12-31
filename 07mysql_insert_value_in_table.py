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

    def insert_data(
        self, ids=None, name=None, birth_date=None, phone=None, gender=None
    ):
        try:
            self.table_name = input("Enter table name : ")
            self.connections()
            if self.conn and self.cursor:
                self.query = f""" insert into {self.table_name}
                (id,name,birthday_date,phone,gender) values (%s,%s,%s,%s,%s)
                """
                self.data = [ids, name, birth_date, phone, gender]
                self.cursor.execute(self.query, self.data)
                self.conn.commit()
                print("Inserted Data in the table !")
                #print(ids, name, birth_date, phone, gender)
                self.closes()
            else:
                print("Not inserted data   !")
        except Error as e:
            print(f" Error : {e}")
            self.closes()


if __name__ == "__main__":
    db = Database("vasant")
    ids = int(input("Enter ID : "))
    name = input("Enter Name : ")
    birth_date = input("Enter Birth Date : ")
    phone = int(input("Enter Phone Number : "))
    gender = input("Enter Gender M/F : ")
    db.insert_data(ids, name, birth_date, phone, gender)
