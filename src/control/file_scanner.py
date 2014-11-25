import os
import fnmatch
import stagger

from control.album import Album

class FileScanner:
    """docstring for FileScanner"""

    def get_albums(self, path):
        albums = set()
        for dirpath, dirs, files in os.walk(path):
            for filename in fnmatch.filter(files, '*.mp3'):
                file_path = os.path.join(dirpath, filename)
                created_album = self.create_album(file_path)
                if created_album:
                    albums.add(created_album)
        return albums

    def create_album(self, file_path):
        album = Album()
        self.get_file_details(album, file_path)
        if not self.get_ID3_tags(album, file_path):
            return None
        return album

    def get_file_details(self, album, file_path):
        album.file_path = file_path

    def get_ID3_tags(self, album, file_path):
        try:
            album.artist = stagger.read_tag(file_path).artist
            album.title = stagger.read_tag(file_path).album
            if not album.artist or not album.title:
                return None
            return True
        except stagger.errors.NoTagError:
            return None