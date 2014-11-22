class Album:
    """docstring for Album"""
    @property
    def artist(self):
        return self._artist
    @artist.setter
    def artist(self, value):
        self._artist = value

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, value):
        self._title = value

    @property
    def file_path(self):
        return self._file_path
    @file_path.setter
    def file_path(self, value):
        self._file_path = value

    def __init__(self, artist = '', title = ''):
        self.artist = artist
        self.title = title

    def __hash__(self):
        return hash(self.artist) ^ hash(self.title)

    def __eq__(self, other):
        return other.artist == self.artist and other.title == self.title

    def __repr__(self):
        return '{0} - {1}'.format(self.artist, self.title)