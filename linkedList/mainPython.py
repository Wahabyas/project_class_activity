class song_object:
    def __init__(self,Songname,NextSOng):
        self.Songname = Songname
        self.NextSOng = NextSOng
    def __str__ (self):
        return f"Songname: {self.Songname}\nNextSOng: {self.NextSOng}"