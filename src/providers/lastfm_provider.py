import requests
import json

from control.album import Album

class LastfmProvider:
    """docstring for LastfmProvider"""
    def __init__(self):
        self.endpoint = 'http://ws.audioscrobbler.com/2.0'
        self.api_key = '74f369c06f5d9597b9658a7a1cfd62d9'

    def search(self, music_scanner, album):
        payload = {'method': 'album.search', 'album': '{0}+{1}'.format(album.artist, album.title), 'api_key': self.api_key, 'format': 'json'}
        payload_str = "&".join("%s=%s" % (k,v) for k,v in payload.items())
        r = requests.get(self.endpoint, params=payload_str)
        response = json.loads(r.text)
        music_scanner.store_result(album, int(response['results']['opensearch:totalResults']) > 0)