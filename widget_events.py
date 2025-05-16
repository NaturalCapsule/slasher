import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gtk, GLib, GdkPixbuf, Gdk
import shlex
import subprocess
import os

def on_search_changed(search_entry, listbox):
    listbox.invalidate_filter()

def filter_func(row, data, search_entry):
    if not row:
        return False

    event_box = row.get_child()
    if not event_box:
        return False

    hbox = event_box.get_child()
    if not hbox:
        return False

    label = None
    for child in hbox.get_children():
        if isinstance(child, Gtk.Label):
            label = child
            break

    if not label:
        return False

    query = search_entry.get_text().lower()
    return query in label.get_text().lower()



def create_submenu_item(label_text, icon_path=None, use_theme_icon=False):
    box = Gtk.EventBox()
    box.set_above_child(False)
    
    hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox.set_border_width(8)
    
    if icon_path:
        if use_theme_icon:
            try:
                pixbuf = Gtk.IconTheme.get_default().load_icon(icon_path, 32, 0)
                scaled_pixbuf = pixbuf.scale_simple(20, 20, GdkPixbuf.InterpType.BILINEAR)
                icon = Gtk.Image.new_from_pixbuf(scaled_pixbuf)
                icon.get_style_context().add_class('App-Images')

            except GLib.Error:
                icon = Gtk.Image.new_from_icon_name(icon_path, Gtk.IconSize.SMALL_TOOLBAR)
                icon.get_style_context().add_class('App-Images')
                
        hbox.pack_start(icon, False, False, 2)
        
    label = Gtk.Label(label=label_text)

    label.get_style_context().add_class('App-Names')
    label.set_xalign(0)
    hbox.pack_start(label, True, True, 2)
    
    box.add(hbox)
    
    
    return box


def run_selected_program(row, exec_cmd):
    event_box = row.get_child()
    box = event_box.get_child()

    try:
        label = box.get_children()[1]
        app_name = label.get_text()
    except IndexError:
        label = box.get_children()[0]
        app_name = label.get_text()

    print(f"Launching {app_name}...")
    launch_app(widget = None, exec=exec_cmd)
    exit(0)

# def on_key_press_(widget, event, listbox, exec_):
def on_key_press_(widget, event):
    key = Gdk.keyval_name(event.keyval)
    if key == "Return":
        selected_row = widget.get_selected_row()
        if selected_row:
            exec_cmd = selected_row.get_child().exec_cmd
            run_selected_program(selected_row, exec_cmd)
        return True


def launch_app(widget, exec):
    if exec == 'kitty' or exec =='htop' or exec == 'yazi' or exec == 'vim' or exec == 'nvim':
        subprocess.Popen(["kitty", "-e", "sh", "-c", exec])
    else:
        cmd = shlex.split(exec)
        subprocess.Popen(cmd, start_new_session = True, cwd = os.path.expanduser("~"))
    exit(0)


def on_key_press(widget, event):
    key = Gdk.keyval_name(event.keyval)
    if key == "Escape":
        # exit(0)
        Gtk.main_quit()
        return True
    return False