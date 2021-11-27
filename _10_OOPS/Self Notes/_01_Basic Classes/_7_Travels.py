class travels:
    # STATE
    def __init__(self, name, pickuppoint, destination, amount):
        self.name = name
        self.pickuppoint = pickuppoint
        self.destination = destination
        self.amount = amount
    #BEHAVIOUR
    def get_ticket_info(self):
        print("The Travel details are:")
        print("name:",self.name,  "Pickup Point:", self.pickuppoint, "Destination:", self.destination, "Amount:", self.amount)


info = travels("Karthick", "Marathahalli", "Madurai", 1500)
info.get_ticket_info()