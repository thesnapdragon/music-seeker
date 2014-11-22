import requests
import json

from control.album import Album

class DeezerProvider:
    """docstring for DeezerProvider"""
    def __init__(self):
        self.endpoint = 'http://api.deezer.com/search/album'

    def search(self, album):
        payload = {'q': '{0}+{1}'.format(album.artist, album.title)}
        payload_str = "&".join("%s=%s" % (k,v) for k,v in payload.items())
        r = requests.get(self.endpoint, params=payload_str)
        response = json.loads(r.text)
        return int(len(response['data'])) > 0