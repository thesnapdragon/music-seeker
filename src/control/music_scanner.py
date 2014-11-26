class MusicScanner:
    """docstring for MusicScanner"""
    @property
    def albums_available(self):
        return self._albums_available
    @albums_available.setter
    def albums_available(self, value):
        self._albums_available = value

    def __init__(self):
        self.albums_available = {}
        self.music_services = [None, None, None, None]

    def set_music_service(self, idx, service):
        self.music_services[idx] = service

    def search(self, album):
        self.albums_available[album] = []
        for service in [service for service in self.music_services if service is not None]:
            service.search(self, album)

    def store_result(self, album, result):
        self.albums_available[album].append(result)