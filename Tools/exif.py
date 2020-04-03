'''
import os, time
from stat import *

stats = os.stat(("image.png"))
print(time.asctime(time.localtime(stats[ST_MTIME])))
'''
# Exif need to be installed and in path
# https://github.com/smarnach/pyexiftool/issues/26
import exiftool

file = "image.png"

with exiftool.ExifTool() as exif:
    print(exif.get_metadata(file))
