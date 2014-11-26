from gi.repository import Gtk
from gi.overrides import GObject
import time #test only

from gui.background_worker import BackgroundWorker
from providers.deezer_provider import DeezerProvider
from providers.itunes_provider import ItunesProvider
from providers.lastfm_provider import LastfmProvider
from providers.spotify_provider import SpotifyProvider

class WindowHandler:
    """handling main window"""
    def __init__(self, controller, builder):
        self.controller = controller
        self.builder = builder
        self.deezer_provider = DeezerProvider()
        self.itunes_provider = ItunesProvider()
        self.lastfm_provider = LastfmProvider()
        self.spotify_provider = SpotifyProvider()

    def on_main_window_destroy(self, *args):
        """quits the application"""
        Gtk.main_quit(*args)

    # scan files tab

    #TODO
    def print_scan_status(self, result):
        tv = self.builder.get_object('scan_textview')
        button = self.builder.get_object('scan_button')
        num = len(self.controller.albums)
        tv.get_buffer().set_text('HELLO COMPLETE\nFound ' + str(num) + ' albums!')
        print(self.controller.albums)
        button.set_sensitive(True)

    def report_scan_progress(self, status):
        pb = self.builder.get_object('scan_progressbar')
        pb.set_fraction(status)

    #TODO
    def scan_delegate(self, worker):
        worker.report(0.1)
        self.controller.scan_files(self.controller.selected_folder)
        worker.report(0.2)
        for i in range(20, 101):
            time.sleep(0.05)
            worker.report(i * 0.01)

    def on_folder_chooser_selection_changed(self, folder_chooser):
        """changes current folder for music scan"""
        self.controller.selected_folder = folder_chooser.get_filename()

    def on_scan_button_clicked(self, button):
        button.set_sensitive(False)
        worker = BackgroundWorker(
            self.scan_delegate,
            self.print_scan_status,
            self.report_scan_progress)
        worker.start()

    def on_scan_next_button_clicked(self, button):
        self.builder.get_object('notebook').next_page()


    # search music tab

    def on_search_button_clicked(self, button):
        self.controller.search_albums(self.controller.albums)
        print(self.controller.albums_available)

    def on_search_next_button_clicked(self, button):
        self.builder.get_object('notebook').next_page()

    def on_deezer_checkbox_toggled(self, checkbox):
        if checkbox.get_active():
            self.controller.music_scanner.set_music_service(0, self.deezer_provider)
        else:
            self.controller.music_scanner.set_music_service(0, None)

    def on_itunes_checkbox_toggled(self, checkbox):
        if checkbox.get_active():
            self.controller.music_scanner.set_music_service(1, self.itunes_provider)
        else:
            self.controller.music_scanner.set_music_service(1, None)

    def on_lastfm_checkbox_toggled(self, checkbox):
        if checkbox.get_active():
            self.controller.music_scanner.set_music_service(2, self.lastfm_provider)
        else:
            self.controller.music_scanner.set_music_service(2, None)

    def on_spotify_checkbox_toggled(self, checkbox):
        if checkbox.get_active():
            self.controller.music_scanner.set_music_service(3, self.spotify_provider)
        else:
            self.controller.music_scanner.set_music_service(3, None)
