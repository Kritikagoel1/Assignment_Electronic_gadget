from datetime import datetime
from OrderDetails_Class import OrderDetail
from Entity.Products_class import Products
from Entity.Customer_class import Customer


class Orders:
    def __init__(self, order_id, customer: object, ostatus):
        self.OrderID = order_id
        self.Customer = customer
        self.OrderDate = datetime.now()
        self.TotalAmount = 0
        self.order_details = []
        self.OrderStatus=ostatus

    def calculate_total_amount(self):
        total_amount = 0
        for order_detail in self.order_details:
            total_amount += OrderDetail.calculate_subtotal()
        return total_amount

    def get_order_details(self):
        print("Order ID: %d" % self.OrderID)
        print("Order Date: %s " %self.order_details)
        print(" Customer name %s %s" % self.FirstName, self.LastName)
        print("Order Status %s" % self.OrderStatus)

    def update_order_status(self,ostatus=None):
        if ostatus is not None:
            self.OrderStatus=ostatus


    def CancelOrder(self):
        for order_detail in self.Products:
            order_detail.Product.StockQuantity += order_detail.Quantity

        self.Products = []
        self.TotalAmount = 0
        self.OrderStatus = "Cancelled"


