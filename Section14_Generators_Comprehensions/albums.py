import os
import fnmatch


# generator for finding albums
def find_albums(root, artist_name):
    caps_name = artist_name.upper()
    for path, dirs, files in os.walk(root):
        # case sensitive
        # for artist in fnmatch.filter(dirs, artist_name):
        # case permissive
        # for artist in fnmatch.filter((d.upper() for d in dirs), caps_name):
        # case doesn't matter
        for artist in (d for d in dirs if fnmatch.fnmatch(d.upper(), caps_name)):
            subdir = os.path.join(path, artist)
            for album_path, albums, _ in os.walk(subdir):
                for album in albums:
                    yield os.path.join(album_path, album), album


# generator for finding songs
def find_song(albums):
    for album in albums:
        # we want the path, not the album name
        for song in os.listdir(album[0]):
            yield song


# album_list = find_albums("music", "Aerosmith")
album_list = find_albums("music", "black*")
song_list = find_song(album_list)

# for a in album_list:
#     print(a)

for b in song_list:
    print(b)
