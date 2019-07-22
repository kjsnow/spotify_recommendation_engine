from tkinter import *
from tkinter import ttk
from spotify_object_classes import SpotifyObject

def search_spotify(*args):
    try:
        result.search_term = search.get()
        result.type = search_type.get().lower()
        result.execute_search()

        # # Display Name...
        # ttk.Label(mainframe, textvariable=result._name).grid(column=2, row=2, sticky=(W, E))
        result_name.set(result._name)
        result_followers.set(result._followers)

    except ValueError:
        pass

root = Tk()
root.title("Spotify Search")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

search = StringVar()
result = SpotifyObject()
result_name = StringVar()
result_followers = StringVar()

search_type = StringVar()

# Dictionary with options
choices = { 'Artist', 'Track', 'Album'}
#search_type.set('Artist'.lower()) # set the default option

search_entry = ttk.Entry(mainframe, width=7, textvariable=search)
search_entry.grid(column=2, row=1, sticky=(W, E))

popupMenu = ttk.OptionMenu(mainframe, search_type, *choices)
popupMenu.grid(column=3, row=1, sticky=W)

ttk.Label(mainframe, textvariable=result_name).grid(column=2, row=2, sticky=(W, E))
ttk.Label(mainframe, textvariable=result_followers).grid(column=2, row=3, sticky=(W, E))
ttk.Button(mainframe, text="Search", command=search_spotify).grid(column=3, row=3, sticky=W)

#ttk.Label(mainframe, text="search").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="Artist name: ").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="Followers: ").grid(column=1, row=3, sticky=E)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

search_entry.focus()
root.bind('<Return>', search_spotify)

root.mainloop()