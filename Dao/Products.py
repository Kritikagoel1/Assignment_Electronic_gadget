from Util.dbconnection import connect

class prod:
    def __init__(self):
        self.conn=connect()
        self.conn.connection()

    def product(self):
        stmt=self.conn.cursor
        create_str = ''' 
            CREATE TABLE IF NOT EXISTS products (
                product_id INT PRIMARY KEY,
                product_name VARCHAR(255),
                description text,
                price DECIMAL(10, 2),
                quantity INT
            )
        '''


        stmt.execute(create_str)
        self.conn.commit()
        print("created successfully")

        print("enter details to insert: ")

        product_id=int(input("enter product id:"))
        product_name=input("enter product nam:")
        description=input("enter description")
        price=float(input("enter price:"))
        quantity=int(input("enter quantity: "))

        stmt = self.conn.cursor
        insert_product = '''INSERT INTO products (product_id,product_name,description, price, quantity)
        VALUES (%s, %s, %s)'''
        data=(product_id,product_name,description, price, quantity)
        stmt.execute(insert_product,data)
        self.conn.commit()
        print("Product added successfully")


        prod_id=int(input("enter product id where you want to update:"))
        create_update='''update products set price=799.99 where product_id=%s'''
        stmt.execute(create_update,prod_id)
        self.conn.commit()
        print("updated successfully")


