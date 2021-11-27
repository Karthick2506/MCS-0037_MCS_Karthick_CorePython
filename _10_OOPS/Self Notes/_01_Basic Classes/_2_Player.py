class player:
    # STATE
    def __init__(self, name, runs, boundaries):
        self.name = name
        self.runs = runs
        self.boundaries = boundaries
    # Behaviour
    def get_playerinfo(self):
        print("The Player Details are:")
        print("Player:", self.name,  "Runs Scored:", self.runs,  "Boundaries:", self.boundaries)


details = player("Sachin", 130, 12)
details.get_playerinfo()