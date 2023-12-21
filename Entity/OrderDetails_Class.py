class OrderDetail:
    def __init__(self, order_detail_id, order, product, quantity):
        self.OrderDetailID = order_detail_id
        self.Order = order
        self.Product = product
        self.Quantity = quantity

    def calculate_Subtotal(self):
        return self.Quantity * self.Product.Price

    def getOrderDetailInfo(self):
        return (
            f"Order Detail ID: {self.OrderDetailID}\n"
            f"Product: {self.Product.ProductName}\n"
            f"Quantity: {self.Quantity}\n"
            f"Subtotal: {self.CalculateSubtotal():.2f}"
        )

    def UpdateQuantity(self, new_quantity):
        self.Products.InStock += self.Quantity - new_quantity
        self.Quantity = new_quantity

    def AddDiscount(self, discount_amount):
        self.Products.InStock += self.Quantity
        self.Quantity = max(0, self.Quantity - discount_amount)

