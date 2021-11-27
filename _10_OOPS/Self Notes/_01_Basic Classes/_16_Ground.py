class ground:
    # STATE
    def __init__(self, game, timings, players):
        self.game = game
        self.timings = timings
        self.players = players

    # BEHAVIOUR
    def get_ground_info(self):
        print("The Ground info:")
        print("Game:",self.game,  "Timings Allowed:",self.timings, "Players Allowed:",self.players)


information = ground("Cricket", "10 AM", "15")
information.get_ground_info()