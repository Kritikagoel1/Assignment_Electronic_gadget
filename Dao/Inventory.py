from Util.dbconnection import connect

class invent:
    def __init__(self):
        self.conn=connect()
        self.conn.connection()

    def inventory(self):
        stmt=self.conn.cursor
        create_str = ''' 
            CREATE TABLE IF NOT EXISTS inventory (
            inventory_id INT PRIMARY KEY,
            product_id INT,
            quantity_in_stock INT NOT NULL,
            FOREIGN KEY (product_id) REFERENCES products(product_id)
            )'''
        stmt.execute(create_str)
        self.conn.commit()
        print("created successfully")

        print("For updation")
        prod_id=int(input("enter id to update: "))
        stmt = self.conn.cursor()
        update_str = '''UPDATE inventory SET quantity_in_stock = %s WHERE product_id = %s'''
        stmt.execute(update_str,prod_id)
        self.conn.commit()
        print("Quantity updated successfully")

        print("selection from inventory")
        stmt=self.conn.cursor
        select_str='''select * from inventory'''
        stmt.execute(select_str)
        data=stmt.fetchall()
        for p in data:
            print(p)
        self.conn.commit()
        print("selected successfully")


