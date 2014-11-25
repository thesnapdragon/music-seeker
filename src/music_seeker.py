#!/usr/bin/env python3

from gi.repository import Gtk

from gui.window_handler import WindowHandler
from control.controller import Controller

def main():
    # import Glade
    builder = Gtk.Builder()
    builder.add_from_file("gui/music_seeker.glade")
    builder.connect_signals(WindowHandler(Controller()))

    window = builder.get_object("main_window")
    window.show_all()

    Gtk.main()

if __name__ == '__main__':
    main()