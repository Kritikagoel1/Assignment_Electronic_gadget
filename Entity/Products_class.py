class Products:
    def __init__(self, product_id, product_name, description, price, quantity):

        self.Product_Id=product_id
        self.Product_Name=product_name
        self.Description=description
        self.Price=price
        self.InStock=quantity

    def get_product_details(self):
        print(" Product Id: %d" % self.Product_Id)
        print(" Product Name: %s" % self.Product_Name)
        print("Description: %s" % self.Description)
        print("Price: %.2f" % self.Price)
        print("In Stock:  %d" % self.InStock)

    def update_product_info(self, description=None, price=None, quantity=None):
        if description:
            self.Description=description
        if price:
            self.Price=price
        if quantity:
            self.InStock=quantity

        print("Products info updated successfully")

    def is_product_instock(self):
        if self.InStock>0:
            return self.InStock
        else:
            print("not in stock")
