# Creating a class
class cricket:
    # STATE
    def __init__(self, batsize, batname, batprice):
        self.batsize = batsize
        self.batname = batname
        self.batprice = batprice
    # Behaviour
    def get_batinfo(self):
        print("The Bat Details are:")
        print("Bat Size:", self.batsize, "inch",  "Bat Name:", self.batname,  "bat price:", self.batprice)


bat = cricket(34, "MRF", 10000)
bat.get_batinfo()