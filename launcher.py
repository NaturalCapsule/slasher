import gi
import widgets
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from get_apps_info import *
from widget_events import *

class Launcher(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.setupUI()
        self.boxes()
        self.adding_elements()

    def setupUI(self):
        self.set_default_size(300, 200)
        self.set_skip_taskbar_hint(True)
        self.set_skip_pager_hint(True)
        self.set_keep_above(True)
        self.set_decorated(False)
        self.set_resizable(False)    


    def boxes(self):
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)


        vbox.pack_start(widgets.search_entry, False, False, 0)

        vbox.pack_start(widgets.listbox, True, True, 0)

    def adding_elements(self):
        items = get_app_info()
        for name, exec_cmd, icon in items:
            label = Gtk.Label(label=name, xalign=0)
            widgets.listbox.add(label)

        widgets.listbox.set_filter_func(filter_func, None, widgets.search_entry)
        widgets.listbox.show_all()

win = Launcher()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
