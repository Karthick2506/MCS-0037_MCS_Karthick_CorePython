class PG:
    # STATE
    def __init__(self, name, location, rent):
        self.name = name
        self.location = location
        self.rent = rent
    # BEHAVIOUR
    def get_pg_info(self):
        print("The Information is:")
        print("Name:", self.name,  "Location:", self.location,  "Rent:", self.rent)


info = PG("Karthick", "Marathahalli", 7000)
info.get_pg_info()

