from gi.repository import Gtk
from gi.overrides import GObject

from providers.deezer_provider import DeezerProvider
from providers.itunes_provider import ItunesProvider
from providers.lastfm_provider import LastfmProvider
from providers.spotify_provider import SpotifyProvider
from misc.future import Future
from control.statistics import Statistics

class WindowHandler:
    """handling main window"""
    def __init__(self, builder):
        self.builder = builder
        self.deezer_provider = DeezerProvider()
        self.itunes_provider = ItunesProvider()
        self.lastfm_provider = LastfmProvider()
        self.spotify_provider = SpotifyProvider()

    def set_controller(self, controller):
        self.controller = controller

    def on_main_window_destroy(self, *args):
        """quits the application"""
        Gtk.main_quit(*args)

    ## paging functions

    def on_home_button_clicked(self, button):
        self.builder.get_object('outer_notebook').set_current_page(0)

    def on_home_scan_button_clicked(self, button):
        self.builder.get_object('outer_notebook').set_current_page(1)
        self.builder.get_object('notebook').set_current_page(0)

    def on_home_search_button_clicked(self, button):
        self.builder.get_object('outer_notebook').set_current_page(2)

    def on_next_button_clicked(self, button):
        self.builder.get_object('notebook').next_page()

    ## simple keyword search page

    def on_k_search_button_clicked(self, button):
        pass

    def on_k_itunes_checkbox_toggled(self, button):
        pass

    def on_k_lastfm_checkbox_toggled(self, button):
        pass

    def on_k_spotify_checkbox_toggled(self, button):
        pass

    def on_k_deezer_checkbox_toggled(self, button):
        pass

    # complex coverage scan page
    # scan files tab

    def on_folder_chooser_selection_changed(self, folder_chooser):
        """changes current folder for music scan"""
        self.controller.selected_folder = folder_chooser.get_filename()

    def on_scan_button_clicked(self, button):
        Future(self.controller.scan_files, self.controller.selected_folder, self.on_scan_future_finish)
        self.builder.get_object('scan_spinner').start()

    def on_scan_future_finish(self):
        self.builder.get_object('scan_spinner').stop()
        albums_results = self.builder.get_object('albums_results')
        albums_results.clear()
        for album in self.controller.albums:
            albums_results.append([album.artist, album.title])

    # search music tab

    def on_search_button_clicked(self, button):
        Future(self.controller.search_albums, self.controller.albums, self.on_search_future_finish, self.set_progressbar)
        self.builder.get_object('search_spinner').start()

    def on_search_future_finish(self):
        self.set_progressbar(1)
        self.builder.get_object('search_spinner').stop()
        albums_available_results = self.builder.get_object('albums_available_results')
        albums_available_results.clear()
        for album in zip(self.controller.albums_available.keys(), self.controller.albums_available.values()):
            albums_available_results.append([album[0].artist, album[0].title, album[1][0], album[1][1], album[1][2], album[1][3]])
        Future(Statistics, self.controller.albums_available, self.on_statistics_future_finish)

    def set_progressbar(self, value):
        search_progressbar = self.builder.get_object('search_progressbar')
        search_progressbar.set_fraction(value)

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

    # statistics

    def on_statistics_future_finish(self, data):
        for service in ['deezer', 'itunes', 'lastfm', 'spotify']:
            self.builder.get_object('{0}_statistics'.format(service)).set_text('{0} album found ({1} %)'.format(data[service]['count'], data[service]['percent']))
        self.builder.get_object('bestbuy').set_text(data['best_buy'])
