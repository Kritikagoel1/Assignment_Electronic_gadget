class Customer:
    def __init__(self,customerid,firstname,lastname,email,phone,address):
        self.CustomerId=customerid
        self.FirstName=firstname
        self.LastName=lastname
        self.Email=email
        self.Phone=phone
        self.Address=address
        self.Orders=[]


    def get_customer_details(self):
        print("Customer Id: %d " % self.CustomerId)
        print("First Name:  %s" % self.FirstName)
        print("Last Name: %s" % self.LastName)
        print("Email : %s" % self.Email)
        print("Phone : %s" % self.Phone )
        print("Address : %s" % self.Address)
        print("Orders : %s " % self.Orders)

    def calculate_total_orders(self):
        return len(self.orders)

    def update_customer_info(self, email=None ,phone=None,address=None ):
        if email is not None:
            self.Email=email
        if phone is not None:
            self.Phone=phone
        if address is not None:
            self.Address=address
        print("customer info updated successfully")


cust=Customer(
    customerid=int(input("enter customer id: ")),
    firstname=input("enter first name: "),
    lastname=input("enter last name"),
    email=input("enter email:"),
    phone=input("enter phone number"),
    address=input("enter address")
)


cust.get_customer_details()
cust.calculate_total_orders()
cust.update_customer_info()
