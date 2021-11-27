class theatre:
    # STATE
    def __init__(self, mname, showtime, persons):
        self.mname = mname
        self.showtime = showtime
        self.persons = persons

    # BEHAVIOUR
    def get_show_info(self):
        print("The Movie information:")
        print("Movie Name:", self.mname, "showtime:", self.showtime, "No. of. Persons:", self.persons)


show = theatre("Master", 6, 10)
show.get_show_info()
