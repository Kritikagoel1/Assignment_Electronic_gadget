class IncompleteOrderException(Exception):
    pass

class OrderDetail:
    def __init__(self, order_detail_id, order, product, quantity):
        self.OrderDetailID = order_detail_id
        self.Order = order
        self.Product = self.validate_product(product)
        self.Quantity = quantity

    def validate_product(self, product):
        if product is None:
            raise IncompleteOrderException(f"Incomplete order detail (ID: {self.OrderDetailID}): Product reference is missing.")

        else:
            print("Order Complete of product:",product)
        return product


try:
    order_detail = OrderDetail(order_detail_id=1, order="123", product='SmartPhone', quantity=2)
except IncompleteOrderException as e:
    print(f"Exception: {e}")





