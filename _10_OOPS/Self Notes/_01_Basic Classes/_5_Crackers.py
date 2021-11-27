class crackers:
    # STATE
    def __init__(self, name, orderid, brand):
        self.name = name
        self.orderid = orderid
        self.brand = brand
    # BEHAVIOUR
    def get_order_info(self):
        print("The order details are:")
        print("Name:", self.name, "orderid:", self.orderid, "Brand:", self.brand)


order = crackers("Karthick", 567856, "Standard")
order.get_order_info()