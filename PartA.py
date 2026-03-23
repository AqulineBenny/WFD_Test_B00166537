import random

class Artist:
    def __init__(self, name, DoB, country):
        self.name = name
        self.DoB = DoB
        self.country = country
        self.list_of_albums = []
        self.list_of_songs = []
    
    def display_info(self):
        print("Artist name is ", self.name)
        print("Date of Birth is ", self.DoB)
        print("Country is ", self.country)
        print("List of albums is ", self.list_of_albums)
        print("List of songs is ", self.list_of_songs)
    
    def add_album(self, album):
        self.list_of_albums.append(album)
    
    def add_song(self, song):
        self.list_of_songs.append(song)

class Song:
    def __init__(self, song_title, artist_name, year_of_release):
        self.song_title = song_title
        self.artist_name = artist_name
        self.year_of_release = year_of_release
    
    def display_info(self):
        print("Song title is ", self.song_title)
        print("Artist name is ", self.artist_name)
        print("Year of release is ", self.year_of_release)

class Album:
    def __init__(self, album_title, artist_name, year_of_release):
        self.album_title = album_title
        self.artist_name = artist_name
        self.year_of_release = year_of_release
        self.list_of_songs = []
    
    def display_info(self):
        print("Album title is ", self.album_title)
        print("Artist name is ", self.artist_name)
        print("Year of release is ", self.year_of_release)
        print("List of songs is ", self.list_of_songs)
    
    def add_song(self, title, release_year):
        new_song = Song(title, self.artist_name, release_year)
        self.list_of_songs.append(new_song)

class Playlist:
    def __init__(self, playlist_title):
        self.playlist_title = playlist_title
        self.list_of_songs = []
    
    def add_song(self, song):
        self.list_of_songs.append(song)
    
    def print_all_song(self):
        for song in self.list_of_songs:
            print(song.song_title)
    
    def sort_playlist(self, order='ASC'):
        if order == 'ASC':
            self.list_of_songs.sort(key=lambda x: x.song_title)
        elif order == 'DES':
            self.list_of_songs.sort(key=lambda x: x.song_title, reverse=True)
    
    def shuffle_playlist(self):
        random.shuffle(self.list_of_songs)

taylor = Artist("Taylor Swift", "December 13, 1989", "USA")

album1 = Album("Fearless", "Taylor Swift", 2008)

song1 = Song("Love Story", "Taylor Swift", 2008)
song2 = Song("You Belong With Me", "Taylor Swift", 2008)

taylor.add_song(song1)
taylor.add_song(song2)

album1.add_song("Fearless", 2008)
album1.add_song("Fifteen", 2008)

taylor.add_album(album1)

playlist1 = Playlist("Taylor Swift Favorites")

for song in album1.list_of_songs:
    playlist1.add_song(song)

print("All songs in playlist:")
playlist1.print_all_song()

print("\nSongs sorted ascending:")
playlist1.sort_playlist('ASC')
playlist1.print_all_song()

print("\nSongs shuffled:")
playlist1.shuffle_playlist()
playlist1.print_all_song()