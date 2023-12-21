from Util.dbconnection import connect


class Order:
    def __init__(self):
        self.conn = connect()
        self.conn.connection()

    def select_ord(self):
        stmt = self.conn.cursor

        # Select all rows from the 'products' table
        create_select = '''SELECT * FROM orders'''
        stmt.execute(create_select)
        data = stmt.fetchall()
        for p in data:
            print(p)

        print("Selected successfully")

        print("total orders: ")
        total_orders = '''
        SELECT
            products.product_id,
            products.product_name,
            SUM(products.quantity * products.price) AS total_order_amount
        FROM
            products
        JOIN
            orders ON orders.product_id = products.product_id
        GROUP BY
            products.product_id, products.product_name
        '''
        stmt.execute(total_orders)
        data = stmt.fetchall()
        for p in data:
            print(p)

        print('Displayed successfully')




