from providers.deezer_provider import DeezerProvider
from providers.itunes_provider import ItunesProvider
from providers.lastfm_provider import LastfmProvider
from providers.spotify_provider import SpotifyProvider

class MusicScanner:
    """docstring for MusicScanner"""
    @property
    def album_available(self):
        return self._album_available
    @album_available.setter
    def album_available(self, value):
        self._album_available = value

    def __init__(self):
        self.album_available = {}
        self.music_services = []
        self.music_services.append(DeezerProvider())
        self.music_services.append(ItunesProvider())
        self.music_services.append(LastfmProvider())
        self.music_services.append(SpotifyProvider())

    def search(self, album):
        self.album_available[album] = []
        for service in self.music_services:
            service.search(self, album)

    def store_result(self, album, result):
        self.album_available[album].append(result)