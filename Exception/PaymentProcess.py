class PaymentFailedException(Exception):
    pass

class Order:
    def __init__(self, order_id, customer, order_date,total_amount):
        self.OrderID = order_id
        self.Customer = customer
        self.OrderDate = order_date
        self.Products = []  # List to store products in the order
        self.TotalAmount = total_amount
        self.OrderStatus = "Processing"

    def ProcessPayment(self):
        try:
            amount=self.TotalAmount
            entered_amount=float(input("enter amount you want to pay"))
            if(entered_amount == amount):
                print("Payment processed successfully.")
            else:
              raise PaymentFailedException("Payment failed. Transaction declined.")

        except PaymentFailedException as e:

            print(f"Error processing payment: {e}")


try:
    order = Order(order_id=1, customer="John Doe", order_date="2023-01-01",total_amount=1000.0)
    order.ProcessPayment()
except PaymentFailedException as e:
    print(f"Exception: {e}")