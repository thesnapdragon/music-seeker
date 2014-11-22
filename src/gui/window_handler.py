from gi.repository import Gtk

class WindowHandler:
    """handling main window"""
    def __init__(self, controller):
        self.controller = controller

    def on_delete_window(self, *args):
        """quits the application"""
        Gtk.main_quit(*args)
