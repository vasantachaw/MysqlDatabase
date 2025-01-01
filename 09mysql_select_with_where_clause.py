#here all libraries import for mysql connections and operatons
import mysql.connector as mq
from mysql.connector import Error


class Database:
    def __init__(self, data_name=None):
        self.connection = None
        self.cursor = None
        self.data_name = data_name

    def connections(self):
        try:
            self.conn = mq.connect(
                host="localhost", user="root", password="", database=self.data_name
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

    def show_data(self, table_name=None):
        try:
            self.databases = None
            self.connections()
            if self.conn and self.cursor:
                self.query = f"select * from {table_name} " # where gender=='m' /age<20 / city!='kathmandu or <> '/
                #where age<=20 AND gender='M' AND city='Kathmandu'/
                #where age<=20 or gender='M'
                #where (age>=20 AND age<=30) or city='Kathmandu'/
                # where not age>=20 / age in (18,19,20) /age Not in (18,19,20)
                #where name between 'a' and 'c' /age betwen 18 and 21
                # where birth_date between "2001-01-01" and "2020 -01-01"
                # where name like 'r%' 
                
                self.cursor.execute(self.query)
                self.databases = self.cursor.fetchall()
                print(" Id     Name      Age      Phone     Gender   City")
                for data in self.databases:
                    print(
                        f" {data[0]}      {data[1]}    {data[2]}    {data[3]}    {data[4]}      {data[5]}"
                    )
                self.closes()
            else:
                print("Not show data !")
        except Error as e:
            print(f" Error : {e}")
            self.closes()


if __name__ == "__main__":
    data = Database("vasant")
    table_name = "employee"
    data.show_data(table_name)
