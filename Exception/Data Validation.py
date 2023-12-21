from Entity.Customer_class import  Customer
class InvalidDataException(Exception):
    pass

class Customer:
    def __init__(self, customer_id, first_name, last_name, email, phone, address):
        self.CustomerID = customer_id
        self.FirstName = first_name
        self.LastName = last_name
        self.Email = self.validate_email(email)
        self.Phone = phone
        self.Address = address
    def validate_email(self, email):
        if "@" not in email or "." not in email:
            raise InvalidDataException("Invalid email address format.")
        return email


try:
    customer_id = int(input("Enter Customer ID: "))
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone: ")
    address = input("Enter Address: ")


    customer = Customer(customer_id, first_name, last_name, email, phone, address)


    print("Customer created successfully!")

except InvalidDataException as e:
    print(f"Error: {e}")



