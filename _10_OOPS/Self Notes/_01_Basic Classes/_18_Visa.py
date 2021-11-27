class visa:
    # STATE
    def __init__(self, name, place, destination, type):
        self.name = name
        self.place = place
        self.destination = destination
        self.type = type

    # BEHAVIOUR
    def get_visa_info(self):
        print("Visa Details are:")
        print("Name:", self.name,  "From:", self.place,  "To:", self.destination, "Type:", self.type)


aa = visa("Karthick", "India", "Germany", "Tourist Visa")
aa.get_visa_info()