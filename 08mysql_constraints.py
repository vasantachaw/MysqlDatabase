import mysql.connector as mq
from mysql.connector import Error


class Database:
    def __init__(self,db_name=None):
        self.connection = None
        self.cursor = None
        self.db_name=db_name

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
                    id int not null unique,
                    name varchar(50) not null,
                    age int not null check(age>=18),
                    phone int(10) not null unique,
                    gender varchar(1) not null,
                    city varchar(15) not null default 'Kathmandu'
                )
                """
                self.cursor.execute(self.query)
                print("Created table !")
                self.closes()
            else:
                print("Not table   !")
        except Error as e:
            print(f" Error : {e}")
            self.closes()

    

    def insert_data(
        self, ids=None, name=None, age=None, phone=None, gender=None,city=None):
        try:
            self.table_name = input("Enter table name : ")
            self.connections()
            if self.conn and self.cursor:
                self.query = f""" insert into {self.table_name}
                (id,name,age,phone,gender) values (%s,%s,%s,%s,%s)
                """
                self.data = [ids, name, age, phone, gender]
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

if __name__=="__main__":
    db=Database("vasant")
    ids = int(input("Enter Uniuqe ID : "))
    name = input("Enter Name : ")
    age = input("Enter Age >=18   : ")
    phone = int(input("Enter Unique Phone Number : "))
    gender = input("Enter Gender M/F : ")
    # city=deafult / optional city row
    db.insert_data(ids, name, age, phone, gender)
