class Artist:
    def __init__(self, input_artist_name, id=None):
        self.artist_name = input_artist_name
        self.id = id

    def change_name(self, new_name):
        self.artist_name = new_name
        