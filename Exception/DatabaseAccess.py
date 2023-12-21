import mysql.connector as sql

class connect:
    def connection():
        host=input("enter host: ")
        user=input("enter username: ")
        database=input("enter database name: ")
        password=input("enter password: ")

        try:
            conn=sql.connect(host=host,user=user,database=database,password=password)
            if conn.is_connected:
                print("database is connected")

        except Exception as e:
            print(f"Unsucessfull Connection: {e}")

db=connect
db.connection()