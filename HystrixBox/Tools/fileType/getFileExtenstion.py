from HystrixBox.Tools.fileType.extenstionDB import ALL_EXTENSIONS

HEADER_BYTES = 262


def get_header(filename):
    """Extract header from file

    :param filename: filename to be read
    :type filename: str

    :returns: Header of the file
    :rtype: bytearray
    """
    # Need to add checking for file with zero length
    try:
        with open(filename, 'rb') as file:
            return bytearray(file.read(HEADER_BYTES))
    except FileNotFoundError:
        print('Cant read the file')
        return None


def getFileExtension(filename):
    """Detect file extension

    :param filename: filename to be checked
    :type filename: str

    :returns: extension or None if not found
    :rtype: Extension
    """
    header = get_header(filename)
    if not header:
        return None

    for extension in ALL_EXTENSIONS:
        if extension.check(header):
            return extension
    return None
