import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from widget_events import *

listbox = Gtk.ListBox()


search_entry = Gtk.SearchEntry()
search_entry.connect("search-changed", on_search_changed, listbox)

listbox.set_filter_func(filter_func, None, search_entry)
# listbox.connect("key-press-event", lambda w, e, listbox = listbox: on_key_press_(w, e, listbox))


scrolled_window = Gtk.ScrolledWindow()
scrolled_window.get_style_context().add_class("Scroll-Window")
scrolled_window.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
scrolled_window.set_min_content_height(300)
scrolled_window.set_max_content_height(500)
scrolled_window.set_propagate_natural_height(True)
scrolled_window.add(listbox)