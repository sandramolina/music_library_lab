from models.artist import Artist
from models.album import Album
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

# artist1 = Artist("Madonna")
# artist_repository.save(artist1)

# artist1.change_name("Madonna Queen of Pop")

# artist_repository.update(artist1)

# artist2 = Artist("Cher")
# artist_repository.save(artist2)


# artist_repository.select_all()

#After adding the if statement to select(id) if we chose an id that does not exist. The program wont crash
#print(artist_repository.select(2))

# artist_repository.delete_all()

# artist_repository.delete(12)

# album1 = Album("The Immaculate Collection", "Pop", artist1)
# album_repository.save(album1)

# album_repository.select_all()

# album_repository.select(2)

# album_repository.delete_all()

# album_repository.delete(6)
#tests the update function
#album1.genre = "Rock Pop"
#album_repository.update(album1)

