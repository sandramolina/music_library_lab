from db.run_sql import run_sql
from repositories import artist_repository
from models.album import *

def save(album):
    sql = "INSERT INTO albums (title, genre, artist_id) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.genre, album.artist.id]
    results = run_sql(sql, values)
    
    id = results[0]['id']
    album.id = id 
    return album

def select_all():
    albums = []

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        artist = artist_repository.select(row['artist_id'])
        album = Album(row['title'], row['genre'], artist, row['id'])
        albums.append(album)
    return albums

def select(id):
    album = None;
    sql = "SELECT * FROM albums WHERE id=%s"
    values = [id]
    result = run_sql(sql, values)
    if result:
        result = result[0]
        artist = artist_repository.select(result['artist_id'])
        album = Album(result['title'], result['genre'], artist, result['id'])
    return album

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM albums WHERE id=%s"
    values = [id]
    run_sql(sql, values)

def update(album):
    sql = "UPDATE albums SET (title, genre, artist_id) = (%s, %s, %s) WHERE id = %s"
    values = [album.title, album.genre, album.artist.id, album.id]
    run_sql(sql, values)

#I run this code in Postico and it worked but not sure how to add this to the file. 
# def filter_artist_by_name(artist_name):
#     sql = "SELECT alb.title, alb.genre, art.artist_name from albums as alb INNER JOIN artists as art ON alb.artist_id = art.id WHERE art.artist_name = %s"
