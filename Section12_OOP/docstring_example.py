#!/usr/bin/env python3


class Song:
    """
    Class to represent a song

    Attributes:
        title (str): The title of the song
        artist (Artist): An artist object representing the songs creator.
        duration (int): The duration of the song in seconds.  May be zero
    """

    def __init__(self, title, artist, duration=0):
        """
        Song init method

        Args:
            title (str): Initialises the 'title' attribute
            artist (Artist): At Artist object representing the song's creator.
            duration (Optional[int]: Initial value for the 'duration' attribute.
                                     Will default to zero if not specified.
        """
        self.title = title
        self.artist = artist
        self.duration = duration


# to display info from docstrings
help(Song)  # all the things in the class
help(Song.__init__)  # only the docstring in the method
print(Song.__doc__)  # docstring of class
print(Song.__init__.__doc__)  # only the docstring in the method
