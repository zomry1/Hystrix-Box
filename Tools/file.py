import filetype

# Need to install file type = pip install filetype
from Tools.file.getFileExtenstion import getFileExtension


def fileExtension(filename):
    extension = getFileExtension("Examples/CR2.CR2")
    if extension is None:
        print('Cannot guess file type!')
        return

    print(extension)
