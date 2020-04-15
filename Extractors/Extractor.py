class Extractor(object):
    """
    A class used to represent a Extractor

    """

    @staticmethod
    def extract(self, text):
        """Extract specific information from data (text->str) usually by regex

        :param text: The data to read from
        :type text: str

        :returns: list of occurrences of the desired information
        :rtype: list

        :raise:
            NotImplementedError If the extract function not set in the extractor

        """

        raise NotImplementedError
