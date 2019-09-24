class Songs:

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def singSong(self):
        for i in self.lyrics:
            print(i)

happy = Songs(["May god bless you, ", "Have a sunshine on you,", "Happy Birthday to you !"])
happy.singSong()