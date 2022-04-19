from models.artist import Artist
import repositories.artist_repository as artist_repository

artist1 = Artist("Madonna")
artist_repository.save(artist1)

artist_repository.select_all()

artist_repository.select(3)