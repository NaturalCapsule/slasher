import gi
import widgets
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from get_apps_info import *
from widget_events import *


class Slasher(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.apps = {}
        self.setupUI()
        self.boxes()
        self.adding_elements()

    def setupUI(self):
        self.set_skip_taskbar_hint(True)
        self.set_skip_pager_hint(True)
        self.set_keep_above(True)
        self.set_decorated(False)
        self.set_resizable(False)
        self.get_style_context().add_class('Window')
        self.connect("key-press-event", on_key_press)

    def boxes(self):
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)
        vbox.pack_start(widgets.search_entry, False, False, 0)
        vbox.pack_start(widgets.scrolled_window, False, False, 0)

    def adding_elements(self):
        items = get_app_info()
        for name, exec_cmd, icon in items:
            item = create_submenu_item(name, icon, True)
            item.exec_cmd = exec_cmd
            item.connect("button-press-event", lambda w, e, cmd=exec_cmd: launch_app(w, cmd))

            widgets.listbox.add(item)
        widgets.listbox.connect("key-press-event", on_key_press_)



slasher = Slasher()
slasher.connect("destroy", Gtk.main_quit)
slasher.show_all()
Gtk.main()
