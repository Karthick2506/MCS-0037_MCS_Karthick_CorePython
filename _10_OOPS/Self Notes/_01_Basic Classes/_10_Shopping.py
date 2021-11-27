class shopping:
    # STATE
    def __init__(self, orderid, type, quantity, brand):
        self.orderid = orderid
        self.type = type
        self.quantity = quantity
        self.brand= brand
    # BEHAVIOUR
    def get_shirt_info(self):
        print("Your selected shirt details are:")
        print("Shirt orderid:", self.orderid, "Cloth Type:", self.type, "Quantity:", self.quantity, "Brand:", self.brand)


shirt = shopping(26785, "Cotton", 5, "Peter England")
shirt.get_shirt_info()