class bike:
    # STATE
    def __init__(self, company, model, price, insuranceamt):
        self.company = company
        self.model = model
        self.price = price
        self.insuranceamt= insuranceamt
    # BEHAVIOUR
    def get_bike_info(self):
        print("The bike details are:")
        print("Bike:", self.company, "Model:", self.model, "Price:", self.price, "Insurance Amount:", self.insuranceamt)


information = bike("Yamaha", "Gixer SF", 100000, 5000)
information.get_bike_info()