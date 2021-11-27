class medical:
    # STATE
    def __init__(self, mname, mid, quantity, price):
        self.mname = mname
        self.mid = mid
        self.quantity = quantity
        self.price = price

    # BEHAVIOUR
    def get_tablet_info(self):
        print("The Tablet info are:")
        print("Medicine:", self.mname,  "Medicine id:", self.mid,  "Quantity", self.quantity, "Price:", self.price)


tablet = medical("Dolo", 650, 5, 40)
tablet.get_tablet_info()