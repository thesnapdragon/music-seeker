import requests
import json

from urllib.parse import quote

from control.album import Album

class SpotifyProvider:
    """docstring for SpotifyProvider"""
    def __init__(self):
        self.endpoint = 'https://api.spotify.com/v1/search'

    def search(self, music_scanner, album):
        payload = {'type': 'album', 'q': 'artist:{0}+album:{1}'.format(quote(album.artist), quote(album.title))}
        payload_str = "&".join("%s=%s" % (k,v) for k,v in payload.items())
        r = requests.get(self.endpoint, params=payload_str)
        response = json.loads(r.text)
        music_scanner.store_result(album, int(response['albums']['total']) > 0)