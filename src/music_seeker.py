#!/usr/bin/env python3

import os

from gi.repository import Gtk

from gui.window_handler import WindowHandler
from control.controller import Controller

def main():
    # import Glade
    builder = Gtk.Builder()
    working_dir = os.path.dirname(os.path.realpath(__file__))
    gui_path = os.path.join(working_dir, 'gui', 'music_seeker.glade')
    builder.add_from_file(gui_path)
    builder.connect_signals(WindowHandler(Controller()))

    window = builder.get_object("main_window")
    window.show_all()

    Gtk.main()

if __name__ == '__main__':
    main()