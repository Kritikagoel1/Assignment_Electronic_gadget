import mysql.connector as sql

class connect:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def connection(self):
        host=input("enter host: ")
        user=input("enter username: ")
        database=input("enter database name: ")
        password=input("enter password: ")

        try:
            self.conn=sql.connect(host=host,user=user,database=database,password=password)
            self.cursor=self.conn.cursor()
            if self.conn.is_connected:
                print("database is connected")

        except Exception as e:
            print(f"Unsuccessful Connection: {e}")
    def commit(self):
        try:
            self.conn.commit()
        except sql.error as e:
            print(f'error :{e}')

    def execute(self,query):
        try:
            self.cursor.execute(query)
        except sql.error as e:
            print(f'error :{e}')
