import requests
import json

from control.album import Album

class ItunesProvider:
    """docstring for ItunesProvider"""
    def __init__(self):
        self.endpoint = 'https://itunes.apple.com/search'

    def search(self, music_scanner, album):
        payload = {'entity': 'album', 'term': '{0}+{1}'.format(album.artist, album.title)}
        payload_str = "&".join("%s=%s" % (k,v) for k,v in payload.items())
        r = requests.get(self.endpoint, params=payload_str)
        response = json.loads(r.text)
        music_scanner.store_result(album, int(response['resultCount']) > 0)