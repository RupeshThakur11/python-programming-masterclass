#!/usr/bin/env python3

"""
Given the tuple below that represents the Imelda May album "More Mayhem", write
code to print the album details, followed by a listing of all the tracks in the album.

Indent the tracks by a single tab stop when printing them (remember that you can pass
more than one item to the print function, separating them with a comma).

imelda = "More Mayhem", "Imelda May", 2011, (
    (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))

print(imelda)
"""

imelda = "More Mayhem", "Imelda May", 2011, (
     (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))

album, artist, year, track_list = imelda
print("Album: {}".format(album))
print("Artist: {}".format(artist))
print("Year: {}".format(year))
print("Songs:")
for track in track_list:
    track_number, song = track
    print("\t {}. {}".format(track_number, song))
