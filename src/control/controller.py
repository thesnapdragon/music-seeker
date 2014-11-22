from control.file_scanner import FileScanner
from control.music_scanner import MusicScanner

class Controller:
    """docstring for Controller"""
    
    def __init__(self):
        self.file_scanner = FileScanner()
        self.music_scanner = MusicScanner()

    def scan_files(self, file_path):
        return self.file_scanner.get_albums(file_path)
