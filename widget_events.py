def on_search_changed(search_entry, listbox):
    listbox.invalidate_filter()

def filter_func(row, data, search_entry):
    query = search_entry.get_text().lower()
    return query in row.get_child().get_text().lower()
