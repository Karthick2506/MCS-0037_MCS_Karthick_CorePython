class interview:
    # STATE
    def __init__(self, name1, name2, round, mode):
        self.name1 = name1
        self.name2 = name2
        self.round = round
        self.mode = mode

    # BEHAVIOUR
    def get_inter_info(self):
        print("The Tablet info are:")
        print("Candidate Name:", self.name1,  "Interviewer:", self.name2,  "Round:", self.round, "Mode:", self.mode)


det = interview("Karthick", "Madhu Nettem", "Technical Round", "Virtual")
det.get_inter_info()