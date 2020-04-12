import time

from Tools.file.extenstionDB import ALL_EXTENSIONS

HEADER_BYTES = 262


def get_header(filePath):
    # Need to add checking for file with zero length
    try:
        with open(filePath, 'rb') as file:
            return bytearray(file.read(HEADER_BYTES))
    except FileNotFoundError:
        print('Cant read the file')
        return None


def getFileExtension(filePath):
    header = get_header(filePath)
    if not header:
        return None

    for extension in ALL_EXTENSIONS:
        if extension.check(header):
            return extension
    return None
