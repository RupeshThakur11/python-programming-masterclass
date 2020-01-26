import os
import fnmatch
import id3reader_p3 as id3reader


# generators for finding files with a particular extension
def find_files(root, ext):
    for path, dirs, files in os.walk(root):
        for file in fnmatch.filter(files, "*.{}".format(ext)):
            # if you need the absolute path instead of relative, then use the below var in the join
            # abs_path = os.path.abspath(path)
            yield os.path.join(path, file)


scanned_files = find_files("music", "emp3")

# for f in scanned_files:
#     print(f)

error_list = []

for f in scanned_files:
    try:
        id3r = id3reader.Reader(f)
        print("Artist: {}, Album: {}, Track: {}, Song:{}".format(id3r.get_value('performer'), id3r.get_value('album'), id3r.get_value('track'), id3r.get_value('title')))
    except:
        error_list.append(f)

# display all errors
for i in error_list:
    print(i)
