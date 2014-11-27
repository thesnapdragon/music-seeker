from control.file_scanner import FileScanner
from control.music_scanner import MusicScanner

class Controller:
    """docstring for Controller"""

    @property
    def music_scanner(self):
        return self._music_scanner
    @music_scanner.setter
    def music_scanner(self, value):
        pass

    @property
    def selected_folder(self):
        return self._selected_folder
    @selected_folder.setter
    def selected_folder(self, value):
        self._selected_folder = value

    @property
    def albums(self):
        return self._albums
    @albums.setter
    def albums(self, value):
        self._albums = value

    @property
    def albums_available(self):
        return self._albums_available
    @albums_available.setter
    def albums_available(self, value):
        self._albums_available = value
    
    def __init__(self, builder):
        self.builder = builder
        self.selected_folder = ''
        self.albums = []
        self.albums_available = {}
        self.file_scanner = FileScanner()
        self._music_scanner = MusicScanner()

    def scan_files(self, folder_path, callback):
        self.albums = self.file_scanner.get_albums(folder_path)
        callback()

    def search_albums(self, albums, callback, progressbar_callback = None):
        for i, album in enumerate(albums):
            if progressbar_callback:
                progressbar_callback(i / float(len(albums)))
            self.music_scanner.search(album)
        self.albums_available = self.music_scanner.albums_available
        callback()