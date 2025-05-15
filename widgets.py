import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from widget_events import *

listbox = Gtk.ListBox()


search_entry = Gtk.SearchEntry()
search_entry.connect("search-changed", on_search_changed, listbox)

