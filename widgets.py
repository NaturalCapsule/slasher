import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from widget_events import *


def load_css_():
    css_provider = Gtk.CssProvider()
    with open (f'config/style.css', 'r') as f:
        css = f.read()
    css_provider.load_from_data(css.encode())

    Gtk.StyleContext.add_provider_for_screen(
        Gdk.Screen.get_default(),
        css_provider,
        Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
    )

listbox = Gtk.ListBox()
listbox.get_style_context().add_class('List-Apps')


search_entry = Gtk.SearchEntry()
search_entry.connect("search-changed", on_search_changed, listbox)
search_entry.get_style_context().add_class('Entry')
search_entry.set_placeholder_text('Search...')
# search_entry.set_icon_from_icon_name(Gtk.EntryIconPosition.PRIMARY, "view-app-grid-symbolic")
# search_entry.set_icon_from_icon_name(Gtk.EntryIconPosition.PRIMARY, "edit-clear-symbolic")
# search_entry.set_icon_from_icon_name(Gtk.EntryIconPosition.SECONDARY, "go-next-symbolic")


listbox.set_filter_func(filter_func, None, search_entry)


scrolled_window = Gtk.ScrolledWindow()
scrolled_window.get_style_context().add_class("Scroller")
scrolled_window.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
scrolled_window.set_min_content_height(300)
scrolled_window.set_max_content_height(500)
scrolled_window.set_propagate_natural_height(True)
scrolled_window.add(listbox)


load_css_()