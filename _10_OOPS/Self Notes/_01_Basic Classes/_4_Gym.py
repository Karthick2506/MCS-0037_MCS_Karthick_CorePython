class gym:
    # STATE
    def __init__(self, name, intime, outtime, equipmentused):
        self.name = name
        self.intime = intime
        self.outtime = outtime
        self.equipmentused = equipmentused
    # BEHAVIOUR
    def get_info(self):
        print("The details are:")
        print("Name:", self.name,  "In time:", self.intime,  "Out time:", self.outtime,  "equipmentused:", self.equipmentused)


info = gym("Karthick", 4.00, 6.00, "Treadmill")
info.get_info()