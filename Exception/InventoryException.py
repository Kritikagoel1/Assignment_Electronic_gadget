from datetime import datetime
from Entity.OrderDetails_Class import OrderDetail
class InsufficientStockException:
    pass

class Order:
    def __init__(self, order_id, customer, order_date):
        self.OrderID = order_id
        self.Customer = customer
        self.OrderDate = order_date
        self.Products = []  # List to store products in the order
        self.TotalAmount = 0
        self.OrderStatus = "Processing"

    def AddProduct(self, product, quantity):
        try:
            if product.StockQuantity >= quantity:
                order_detail = OrderDetail(len(self.Products) + 1, self, product, quantity)
                self.Products.append(order_detail)
                self.CalculateTotalAmount()
                product.StockQuantity -= quantity  # Update stock quantity
        except:
            raise InsufficientStockException(f"Insufficient stock for {product.ProductName}")


