class Album:
    def __init__(self, input_title, input_genre, artist, id=None):
        self.title = input_title
        self.genre = input_genre
        self.artist = artist
        self.id = id

class Artist:
    def __init__(self, input_artist_name, id=None):
        self.artist_name = input_artist_name
        self.id = id

    def change_name(self, new_name):
        self.artist_name = new_name

artist1 = Artist("Madonna")
album1 = Album("The Immaculate Collection", "Pop", artist1)
#album has a property which is an object, we need to access it using . 
print(album1.artist.artist_name)
