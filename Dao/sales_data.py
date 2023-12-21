from Util.dbconnection import connect

class sales:
    def __init__(self):
        self.conn=connect()
        self.conn.connection()
    def salesdata(self):
        date_param = input("Enter the date (YYYY-MM-DD): ")

        stmt = self.conn.cursor
        select_str = '''
            SELECT
                orders.order_id,
                customer.customer_id,
                customer.first_name,
                customer.last_name,
                products.product_id,
                products.product_name,
                orders.order_date,
                orders.Order_status,
                products.quantity * products.price AS total_amount
            FROM
                orders
            JOIN
                customer ON orders.customer_id = customer.customer_id
            JOIN
                products ON orders.product_id = products.product_id
            WHERE
                DATE_FORMAT(orders.order_date, '%Y-%m-%d') = %s
        '''

        stmt.execute(select_str,(date_param,))
        data = stmt.fetchall()
        print("Number of rows fetched:", len(data))
        for p in data:
            print(p)
        self.conn.commit()
        print("sales data displayed")

