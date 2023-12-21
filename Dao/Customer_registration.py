from Util.dbconnection import connect

class cust:
    def __init__(self):
        self.conn=connect()
        self.conn.connection()

    def customer(self):

        stmt= self.conn.cursor
        create_str='''create table  if not exists customer(
        customer_id int,
        first_name varchar(50),
        last_name varchar(50),
        phone varchar(50),
        email varchar(50),
        address varchar(50)
        )'''

        stmt.execute(create_str)
        self.conn.commit()
        print("created successfully")

        print("enter details to insert: ")

        stmt=self.conn.cursor
        customer_id=int(input("enter customer id "))
        first_name=(input("enter first name "))
        last_name=(input("enter last name"))
        phone=(input("enter phone no "))
        email=(input("enter email"))
        address=(input("enter address"))


        create_insert=''' insert into customer(customer_id, first_name,last_name,phone,email,address) values(%s,%s,%s,%s,%s,%s)'''
        data=(customer_id, first_name,last_name,phone,email,address)
        stmt.execute(create_insert,data)
        self.conn.commit()
        print("inserted successfully")


