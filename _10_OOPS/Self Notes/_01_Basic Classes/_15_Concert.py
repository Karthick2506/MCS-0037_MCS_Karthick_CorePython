class concert:
    # STATE
    def __init__(self, venue, singer, language):
        self.venue = venue
        self.singer = singer
        self.language = language

    # BEHAVIOUR
    def get_info(self):
        print("The Concert Details are:")
        print("Concert Venue:",self.venue,  "Singer:",self.singer, "Language:",self.language)


detailss = concert("Madurai", "Yuvan Shankar Raja", "Tamil")
detailss.get_info()