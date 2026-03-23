import unittest
from PartA import Artist, Song, Album, Playlist

class TestMusicClasses(unittest.TestCase):
    def setUp(self):
        self.artist1 = Artist("Taylor Swift", "December 13, 1989", "USA")
        self.artist2 = Artist("Ed Sheeran", "February 17, 1991", "UK")
        self.song1 = Song("Love Story", "Taylor Swift", 2008)
        self.song2 = Song("Shape of You", "Ed Sheeran", 2017)
        self.song3 = Song("Blank Space", "Taylor Swift", 2014)
        self.album1 = Album("Fearless", "Taylor Swift", 2008)
        self.playlist1 = Playlist("My Playlist")
    
    def test_artist_instance(self):
        self.assertTrue(isinstance(self.artist1, Artist))
    
    def test_song_instance(self):
        self.assertTrue(isinstance(self.song1, Song))
    
    def test_album_instance(self):
        self.assertTrue(isinstance(self.album1, Album))
    
    def test_playlist_instance(self):
        self.assertTrue(isinstance(self.playlist1, Playlist))
    
    def test_artist_not_instance_of_song(self):
        self.assertFalse(isinstance(self.artist1, Song))
    
    def test_song_not_instance_of_album(self):
        self.assertFalse(isinstance(self.song1, Album))
    
    def test_album_not_instance_of_song(self):
        self.assertFalse(isinstance(self.album1, Song))
    
    def test_song_not_instance_of_playlist(self):
        self.assertFalse(isinstance(self.song1, Playlist))
    
    def test_playlist_not_instance_of_album(self):
        self.assertFalse(isinstance(self.playlist1, Album))
    
    def test_album_not_instance_of_playlist(self):
        self.assertFalse(isinstance(self.album1, Playlist))
    
    def test_playlist_not_instance_of_artist(self):
        self.assertFalse(isinstance(self.playlist1, Artist))
    
    def test_identical_objects(self):
        song_copy = self.song1
        self.assertEqual(self.song1, song_copy)
    
    def test_unidentical_but_similar_objects(self):
        song_similar = Song("Love Story", "Taylor Swift", 2008)
        self.assertNotEqual(self.song1, song_similar)
    
    def test_artist_add_song(self):
        self.artist1.add_song(self.song1)
        self.assertIn(self.song1, self.artist1.list_of_songs)
    
    def test_artist_add_album(self):
        self.artist1.add_album(self.album1)
        self.assertIn(self.album1, self.artist1.list_of_albums)
    
    def test_album_add_song(self):
        self.album1.add_song("New Song", 2024)
        self.assertEqual(len(self.album1.list_of_songs), 1)
    
    def test_playlist_add_song(self):
        self.playlist1.add_song(self.song1)
        self.assertIn(self.song1, self.playlist1.list_of_songs)
    
    def test_sort_playlist_ascending(self):
        self.playlist1.add_song(self.song2)
        self.playlist1.add_song(self.song1)
        self.playlist1.sort_playlist('ASC')
        self.assertEqual(self.playlist1.list_of_songs[0].song_title, "Love Story")
    
    def test_sort_playlist_descending(self):
        self.playlist1.add_song(self.song1)
        self.playlist1.add_song(self.song2)
        self.playlist1.sort_playlist('DES')
        self.assertEqual(self.playlist1.list_of_songs[0].song_title, "Shape of You")
    
    def test_shuffle_playlist(self):
        self.playlist1.add_song(self.song1)
        self.playlist1.add_song(self.song2)
        self.playlist1.add_song(self.song3)
        original_order = [song.song_title for song in self.playlist1.list_of_songs]
        self.playlist1.shuffle_playlist()
        shuffled_order = [song.song_title for song in self.playlist1.list_of_songs]
        self.assertNotEqual(original_order, shuffled_order)

if __name__ == '__main__':
    unittest.main()