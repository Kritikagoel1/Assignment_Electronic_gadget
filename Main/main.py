#dbconnection is imported through every class
class mainmodule():
    print("enter 1 for customer registration")
    print("enter 2 for products")
    print("enter 3 for Orders")
    print("enter 4 for Inventory")
    print("enter 5 for sales data")
    ch=input("enter choice")
    if ch=="1":
        try:
            from Dao.Customer_registration import cust
            c = cust()
            c.customer()
        except:
            print("Can't import customer ")

    elif ch=="2":
        try:
            from Dao.Products import prod
            p = prod()
            p.product()
        except:
            print("can't import products")

    elif ch=="3":
        try:
            from Dao.Order import Order
            o = Order()
            o.ord()
        except:
            print("can't import order")

    elif ch=="4":
        try:
            from Dao.Inventory import invent
            i = invent()
            i.inventory()
        except:
            print("can't import inventory")

    elif ch=="5":
        try:
            from Dao.sales_data import sales
            s = sales()
            s.salesdata()
        except:
            print("can't import sales")
    else:
        print("Invalid choice ")



