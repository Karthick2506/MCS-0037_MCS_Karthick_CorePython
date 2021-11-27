class fruits:
    # STATE
    def __init__(self, fname1, quantity, price1, fname2, quantity2, price2):
        self.fname1 = fname1
        self.quantity1 = quantity
        self.price1 = price1
        self.fname2 = fname2
        self.quantity2 = quantity2
        self.price2 = price2

    # BEHAVIOUR
    def get_price_info(self):
        print("Fruit Price Details:")
        print("Fruit Name 1:", self.fname1, "Quantity 1:", self.quantity1, "price 1:", self.price1,
              "Fruit Name 2:", self.fname2, "Quantity 2:", self.quantity2, "Price 2:", self.price2)


fru = fruits("Apple", "2 kg", 200, "Banana", "1 Kg", 50)
fru.get_price_info()