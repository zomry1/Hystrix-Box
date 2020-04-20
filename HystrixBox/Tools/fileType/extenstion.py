class Extension(object):
    """A class used to represent a Extension

    :param extension: Extension name
    :type extension: str

    :param otherExtensions: Other possible extension names (if there are)
    :type otherExtensions: str

    :param mime:  MIME (Multipurpose Internet Mail Extensions)
    :type mime: str

    :param: description: Description on the extension
    :type: description: str

    """

    def __init__(self, extension, mime, description, otherExtensions=''):
        self.__extension = extension
        self._otherExtensions = otherExtensions
        self.__mime = mime
        self.__description = description

    @property
    def extension(self):
        return self.__extension

    @property
    def mime(self):
        return self.__mime

    @property
    def description(self):
        return self.__description

    # Check if the magic numbers are in the header
    def check(self, header):
        """Check if the correct magic numbers are in the file header

        :param header: Header of the file to be checked
        :type header: str

        :returns: Either the file is according to the magic numbers or not
        :rtype: bool

        :raise NotImplementedError: If the check function not set in the extension
        """
        raise NotImplementedError

    def __str__(self):
        return 'File extension: ' + self.__extension + '\nother extensions names: ' + self._otherExtensions + '\nMIME: ' + self.__mime + '\ndescription: ' + self.__description
