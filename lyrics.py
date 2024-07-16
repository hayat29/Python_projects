# The code snippet is importing necessary modules for creating a GUI application using Tkinter library in Python.
import tkinter as tk
from tkinter import *
from lyrics_extractor import SongLyrics

# The code snippet `window = Tk()` creates a new window for the GUI application using the Tkinter library in Python.
window = Tk()
window.geometry('600x600')
window.title('LyricFlow')

# The lines `song = StringVar()` and `result = StringVar()` are creating two instances of the `StringVar` class from the Tkinter module in Python.
song = StringVar()
result = StringVar()

# The code snippet `head = Label(window, text="Enter the song you want Lyrics for", font=('Calibri 15'))` is creating a Label widget in the GUI application using Tkinter. This label will display the text "Enter the song you want Lyrics for" with a specified font style.
head = Label(window, text="Enter the song you want Lyrics for", font=('Calibri 15'))
head.pack(pady=20)

# The code `Entry(window, textvariable=song).pack()` is creating an Entry widget in the GUI
# application using Tkinter. This widget allows the user to input text, and the `textvariable=song`
# parameter is associating the text entered by the user with the `song` variable, which is an instance of the `StringVar` class. The `pack()` method is then used to display the Entry widget within the window.
Entry(window, textvariable=song).pack()


# The code `Message(window, textvariable=result, bg="light grey").pack(side=TOP, anchor=W, fill=BOTH,
# expand=1)` is creating a Message widget in the GUI application using Tkinter.
Message(window, textvariable=result, bg="light grey").pack(side=TOP, anchor=W, fill=BOTH, expand=1)

def get_lyrics():
    """
    The function `get_lyrics` retrieves the lyrics of a song using a specified API key and search engine
    ID.
    """
    song_name = song.get()
    api_key = "AIzaSyAcZ6KgA7pCIa_uf8-bYdWR85vx6-dWqDg"
    engine_id = "aa2313d6c88d1bf22"
    extract_lyrics = SongLyrics(api_key, engine_id)
    song_lyrics = extract_lyrics.get_lyrics(song_name)
    result.set(song_lyrics)

# The line `Button(window, text="GO", command=get_lyrics).pack()` is creating a Button widget in the
# GUI application using Tkinter.
Button(window, text="GO", command=get_lyrics).pack()

# `window.mainloop()` is a method call that starts the main event loop of the Tkinter GUI application.
# This method listens for events such as user input, mouse clicks, and other interactions within the
# GUI window. It keeps the GUI application running and responsive to user actions until the window is
# closed or the program is terminated.
window.mainloop()