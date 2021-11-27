class songs:
    # STATE
    def __init__(self, sname, singer, music, language):
        self.sname = sname
        self.singer = singer
        self.music = music
        self.language = language

    # BEHAVIOUR
    def get_song_info(self):
        print("The song info are:")
        print("Song Name:",self.sname,  "Singer:",self.singer,  "Music By:",self.music, "Language:",self.language)


songg = songs("Nee_Marilyn_Manroe", "Benny Dayal", "A.R. Rahman", "Tamil")
songg.get_song_info()