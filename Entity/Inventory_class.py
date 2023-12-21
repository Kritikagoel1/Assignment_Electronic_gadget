from datetime import datetime
from Entity.Products_class import Products
class Inventory:
    def __init__(self, inventory_id, product, quantity_in_stock, last_stock_update):
        self.InventoryID = inventory_id
        self.Product = product
        self.QuantityInStock = quantity_in_stock
        self.LastStockUpdate = last_stock_update

    def GetProduct(self):
        return self.Product

    def GetQuantityInStock(self):
        return self.QuantityInStock

    def AddToInventory(self, quantity):
        if quantity > 0:
            self.QuantityInStock += quantity
            self.LastStockUpdate = datetime.now()
            return True
        return False

    def RemoveFromInventory(self, quantity):
        if quantity > 0 and quantity <= self.QuantityInStock:
            self.QuantityInStock -= quantity
            self.LastStockUpdate = datetime.now()
            return True
        return False

    def UpdateStockQuantity(self, new_quantity):
        if new_quantity >= 0:
            self.QuantityInStock = new_quantity
            self.LastStockUpdate = datetime.now()
            return True
        return False

    def IsProductAvailable(self, quantity_to_check):
        return quantity_to_check <= self.QuantityInStock

    def GetInventoryValue(self):
        return self.QuantityInStock * self.Products.Price

    def ListLowStockProducts(self, threshold):
        if self.QuantityInStock < threshold:
            return f"{self.Products.Product_Name} is low in stock with quantity: {self.QuantityInStock}"

    def ListOutOfStockProducts(self):
        if self.QuantityInStock == 0:
            return f"{self.Products.Product_Name} is out of stock"

    def ListAllProducts(self):
        return f"Product: {self.Products.Product_Name}, Quantity: {self.QuantityInStock}"

invent=Inventory(
    inventory_id=int(input("enter inventory id: ")),
    product=input("enter product: "),
    quantity_in_stock=int(input("enter quantity in stock: ")),
    last_stock_update=input(" last stock updation date in yy-mm-dd format: ")

)

quantity_to_add = int(input("Enter quantity to add to inventory: "))
quantity_to_remove = int(input("Enter quantity to remove from inventory: "))
new_quantity = int(input("Enter new stock quantity: "))
quantity_to_check = int(input("Enter quantity to check availability: "))
threshold_value=int(input("enter threshold value:"))

invent.GetProduct()
invent.GetQuantityInStock()
invent.AddToInventory(quantity_to_add)
invent.RemoveFromInventory(quantity_to_remove)
invent.UpdateStockQuantity(new_quantity)
invent.IsProductAvailable(quantity_to_check)
invent.GetInventoryValue()
invent.ListLowStockProducts(threshold_value)
invent.ListOutOfStockProducts()
invent.ListAllProducts()